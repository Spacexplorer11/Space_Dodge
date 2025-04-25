let lastValidTimestamp = null;
let pollingInterval = 10000; // default
let intervalId;
let lastContributorsJSON = null; // global to track previous data

// Particle.js initialization and dynamic adjustment based on screen size
function setupParticles() {
    const screen_size = window.innerWidth * window.innerHeight;

    console.log("Setting up particles..."); // Add this line
    particlesJS("particles-js", {
        "particles": {
            "number": {
                "value": Math.max(50, screen_size * 0.00002),
                "density": {
                    "enable": true,
                    "value_area": 800
                }
            },
            "color": {"value": "#ffffff"},
            "shape": {
                "type": "circle",
                "stroke": {
                    "width": 0,
                    "color": "#000000"
                },
                "polygon": {"nb_sides": 5},
                "image": {
                    "src": "img/github.svg",
                    "width": 100,
                    "height": 100
                }
            },
            "opacity": {
                "value": 0.5,
                "random": false,
                "anim": {
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.1,
                    "sync": false
                }
            },
            "size": {
                "value": 3,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 2,
                    "size_min": 0.1,
                    "sync": false
                }
            },
            "line_linked": {
                "enable": true,
                "distance": 150,
                "color": "#ffffff",
                "opacity": 0.4,
                "width": 1
            },
            "move": {
                "enable": true,
                "speed": 6,
                "direction": "none",
                "random": false,
                "straight": false,
                "out_mode": "out",
                "bounce": false,
                "attract": {
                    "enable": false,
                    "rotateX": 600,
                    "rotateY": 1200
                }
            }
        },
        "interactivity": {
            "detect_on": "window",
            "events": {
                "onhover": {
                    "enable": true,
                    "mode": "grab"
                },
                "onclick": {
                    "enable": true,
                    "mode": "push"
                },
                "resize": true
            },
            "modes": {
                "grab": {
                    "distance": 121.80465781011475,
                    "line_linked": {"opacity": 1}
                },
                "bubble": {
                    "distance": 400,
                    "size": 40,
                    "duration": 2,
                    "opacity": 8,
                    "speed": 3
                },
                "repulse": {
                    "distance": 32.481242082697264,
                    "duration": 0.4
                },
                "push": {"particles_nb": 4},
                "remove": {"particles_nb": 2}
            }
        },
        "retina_detect": true
    });
}

window.onload = function () {
    setupParticles();

    window.addEventListener("resize", () => {
        if (window.pJSDom && window.pJSDom.length > 0) {
            window.pJSDom[0].pJS.fn.vendors.destroypJS();
            window.pJSDom = [];
        }

        setupParticles();
    });
};

function getDeviceInfo() {
    const ua = navigator.userAgent;

    if (/android/i.test(ua)) return "Android";
    if (/iPad|iPhone|iPod/.test(ua) && !window.MSStream) return "iOS";
    if (/Macintosh/.test(ua)) return "macOS";
    if (/Windows/.test(ua)) return "Windows";
    if (/Linux/.test(ua)) return "Linux";

    return "Unknown OS";
}

// Determines mobile/desktop layout styling
function isMobile() {
    if (window.innerWidth <= 600 || Mobile.includes(getDeviceInfo())) {
        document.body.classList.add("mobile");
        console.log("Mobile detected");
    } else {
        document.body.classList.remove("mobile");
    }
}

// Array of desktop and mobile OS types
const Desktop = [
    "Windows",
    "macOS",
    "Linux"
]
const Mobile = [
    "Android",
    "iOS"
]

// Navigates to game instructions or error page based on device
async function startGame() {
    const device = getDeviceInfo();
    if (Desktop.includes(device)) {
        window.location.href = "instructions.html";
    } else if (Mobile.includes(device)) {
        window.location.href = "mobile_error.html";
    } else {
        alert("Your OS is not supported.");
        window.location.href = "mobile_error.html";
    }
}

// Returns to the start page
function backToStart() {
    window.location.href = "index.html";
}

async function fetchRepoStats() {
    try {
        if (document.getElementById("contributors").innerHTML === "") {
              document.getElementById("loading-message").style.display = "block";
              document.getElementById("contributors").style.display = "none";
        }
        const tokenRes = await fetch("https://proxy.spacexplorer11.hackclub.app/get-token");
        const {token, timestamp} = await tokenRes.json();

        const response = await fetch(`https://proxy.spacexplorer11.hackclub.app/stats?token=${token}&timestamp=${timestamp}`);
        if (response.ok) {
            lastValidTimestamp = Date.now();
             // ✅ Clear the notice if it was shown previously
              const notice = document.getElementById("rate-limit-notice");
              if (notice) {
                notice.textContent = "";
              }
        }

        const data = await response.json();

        // Extract the commit count and contributors from the JSON
        const commitCount = data.commit_count;
        const contributors = data.contributors;

        // Check if the commit count element exists before updating
        const commitDisplay = document.getElementById("commit-count");
        if (commitDisplay) {
            commitDisplay.textContent = commitCount;
        } else {
            console.warn("commit-count element not found.");
        }

        // Check if the contributor container exists before updating
        const contributorContainer = document.getElementById("contributors");
        if (contributorContainer) {
            let validContributors = contributors.filter(c =>
                (c.contributions ?? c.total) != null &&
                (c.login || c.author?.login)
            );

            // Now recalculate commit count just from valid contributors
            const validCommitCount = validContributors.reduce((sum, c) =>
                sum + (c.contributions ?? c.total), 0
            );

            let contributorsWithPercent = validContributors
                .map(c => {
                    const contribs = c.contributions ?? c.total;
                    const percent = validCommitCount > 0
                        ? Math.round((contribs / validCommitCount) * 1000) / 10
                        : 0;
                    return {
                        ...c,
                        percent: isNaN(percent) ? 0 : percent
                    };
                });

            // Adjust to make sure total = 100%
            let totalPercent = contributorsWithPercent.reduce((sum, c) => sum + c.percent, 0);
            const diff = Math.round((100 - totalPercent) * 10) / 10;

            if (diff !== 0) {
                const largestContributor = contributorsWithPercent.reduce((max, c) =>
                    c.percent > max.percent ? c : max, contributorsWithPercent[0]
                );

                largestContributor.percent += diff;

                // Ensure the percentages are recalculated and valid
                contributorsWithPercent = contributorsWithPercent
                    .filter(c =>
                        (c.contributions ?? c.total) &&
                        (c.login || c.author?.login) &&
                        (c.avatar_url || c.author?.avatar_url) &&
                        (c.html_url || c.author?.html_url)
                    )
                    .map(c => ({
                        login: c.login || c.author?.login,
                        html_url: c.html_url || c.author?.html_url,
                        avatar_url: c.avatar_url || c.author?.avatar_url,
                        contributions: c.contributions ?? c.total,
                        percent: c.percent
                    }));
            }

            // Compare contributorsWithPercent JSON to lastContributorsJSON to avoid flashing
            const contributorsWithPercentJSON = JSON.stringify(contributorsWithPercent);
            if (contributorsWithPercentJSON === lastContributorsJSON) {
                console.log("No change in data — skipping update.");
                document.getElementById("loading-message").style.display = "none";
                document.getElementById("contributors").style.display = "block";
                return;
            }
            lastContributorsJSON = contributorsWithPercentJSON; // cache the new value

            contributorsWithPercent.forEach(c => {
                const login = c.login || c.author?.login;
                const avatar = c.avatar_url || c.author?.avatar_url;
                const profile = c.html_url || c.author?.html_url;
                const contributions = c.contributions ?? c.total;

                if (login && avatar && profile && contributions != null && !isNaN(c.percent)) {
                    const div = document.createElement("div");
                    div.className = "contributor";

                    const img = document.createElement("img");
                    img.src = avatar;
                    img.alt = login;
                    img.width = 32;
                    img.height = 32;
                    img.style.borderRadius = "50%";
                    img.style.marginRight = "8px";

                    const name = document.createElement("a");
                    name.href = profile;
                    name.textContent = login;
                    name.style.marginRight = "6px";
                    name.target = "_blank";

                    const perc = document.createElement("span");
                    perc.textContent = `${c.percent}%`;

                    div.appendChild(img);
                    div.appendChild(name);
                    div.appendChild(perc);
                    document.getElementById("loading-message").style.display = "none";
                    document.getElementById("contributors").style.display = "block";
                    contributorContainer.appendChild(div);
                }
            });
        }
    else
        {
            console.warn("contributors element not found.");
        }
    }
    catch (error) {
        if (lastValidTimestamp) {
            displayRateLimitNotice(lastValidTimestamp); // ✅ Show fallback
            return; // ⛔ Don’t clear anything
        }
        const loading_message = document.getElementById("loading-message");
        loading_message.style.display = "none";
        console.error("Failed to fetch GitHub stats:", error);
            }
}

function displayRateLimitNotice(timestamp) {
  const notice = document.getElementById("rate-limit-notice");
  const date = new Date(timestamp);

  const locale = navigator.language || "en-GB"; // use British or user's local style
  const formatted = date.toLocaleString(locale, {
    timeZone: "UTC",
    hour: "2-digit",
    minute: "2-digit",
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour12: false
  });

  if (notice) {
    notice.textContent = `Note: This data is from ${formatted} UTC due to temporary API limits.`;
  }
}

// Ensures all anchor links open in a new tab
document.querySelectorAll('a').forEach(link => {
    link.setAttribute('target', '_blank');
});

// Sends a report to the server with the specified type
async function sendSecureReport(type) {
  const tokenRes = await fetch(`https://proxy.spacexplorer11.hackclub.app/get-secure-token/${type}`);
  const { token } = await tokenRes.json();

  await fetch("https://proxy.spacexplorer11.hackclub.app/proxy-discord", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token })
  });
}

// === 🍔 Hamburger Menu (Main.js) ===

// Toggle menu state
function toggleMenu() {
    const menu = document.getElementById("hamburger-menu");
    const containers = document.querySelectorAll(".container");

    menu.classList.toggle("active");

    containers.forEach(container => {
        container.classList.toggle("active_menu"); // Match the CSS class
    });
}

// Set active marker based on current page
function highlightActiveMenu() {
  const links = document.querySelectorAll(".hamburger-menu a");
  const currentPage = window.location.pathname.split("/").pop();

  links.forEach(link => {
    const page = link.getAttribute("href");
    if (page === currentPage) {
      link.classList.add("active-link");
    } else {
      link.classList.remove("active-link");
    }
  });
}

// Simple fetch function which returns boolean, used for checking if stats are available
async function areStatsAvailable() {
  try {
    const tokenRes = await fetch("https://proxy.spacexplorer11.hackclub.app/get-token");
    const { token, timestamp } = await tokenRes.json();

    const statsRes = await fetch(`https://proxy.spacexplorer11.hackclub.app/stats?token=${token}&timestamp=${timestamp}`);
    return statsRes.ok;
  } catch (err) {
    console.error("Stats availability check failed:", err);
    return false;
  }
}

// Report Fingerprint
async function reportFingerprint() {
  const metadata = {
    ua: navigator.userAgent,
    screen: `${screen.width}x${screen.height}`,
    platform: navigator.platform,
    timestamp: Math.floor(Date.now() / 10000) * 10  // round to 10s
  };

// This data is automatically deleted after 5 minutes on the server
  try {
    await fetch("https://proxy.spacexplorer11.hackclub.app/log-fingerprint", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(metadata)
    });
  } catch (err) {
    console.warn("Could not send fingerprint:", err);
  }
}

// Automatic function to adjust the polling interval based on active users
async function startPolling() {
  try {
    const res = await fetch("https://proxy.spacexplorer11.hackclub.app/active-users");
    const { active } = await res.json();

    // Adjust polling interval based on load
    if ((active * 360) > 5000 ) {
      pollingInterval = Math.max(10000, Math.round((active * 360) / 5000) * 1000);
    }

    console.log(`🛰️ Adjusted polling interval to ${pollingInterval}ms for ${active} users`);

    // Get current UTC seconds
    const now = new Date();
    const seconds = now.getUTCSeconds();
    const msUntilNextTick = (10 - (seconds % 10)) * 1000;

    console.log(`🕒 Waiting ${msUntilNextTick}ms to sync with UTC tick...`);

    // Delay until next UTC 10s mark
    setTimeout(() => {
      fetchRepoStats(); // initial call
      intervalId = setInterval(fetchRepoStats, pollingInterval);
    }, msUntilNextTick);
  } catch (err) {
    console.warn("Could not fetch active user count:", err);
  }
}

// Run this on load
window.addEventListener("DOMContentLoaded", () => {
  highlightActiveMenu();
  isMobile();
  startPolling();
});
