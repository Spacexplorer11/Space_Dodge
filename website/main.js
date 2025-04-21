let lastValidTimestamp = null;

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
function startGame() {
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
    const response = await fetch("http://37.27.51.34:3004/stats");
    if (response.ok) {
        lastValidTimestamp = Date.now(); // ✅ save successful fetch timestamp
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
            contributorContainer.innerHTML = ""; // Clear existing content

            // Calculate and round percentages
            const contributorsWithPercent = contributors.map(c => ({
                ...c,
                percent: Math.round((c.contributions / commitCount) * 1000) / 10 // 1 decimal
            }));

            // Adjust to make sure total = 100%
            let totalPercent = contributorsWithPercent.reduce((sum, c) => sum + c.percent, 0);
            const diff = Math.round((100 - totalPercent) * 10) / 10;

            if (diff !== 0) {
                const maxIndex = contributorsWithPercent.reduce((maxIdx, c, i, arr) =>
                    c.percent > arr[maxIdx].percent ? i : maxIdx
                , 0);
                contributorsWithPercent[maxIndex].percent += diff;
            }

            contributorsWithPercent.forEach(user => {
                const div = document.createElement("div");
                div.className = "contributor";

                const img = document.createElement("img");
                img.src = user.avatar_url;
                img.alt = user.login;
                img.width = 32;
                img.height = 32;
                img.style.borderRadius = "50%";
                img.style.marginRight = "8px";

                const name = document.createElement("a");
                name.href = user.html_url;
                name.textContent = user.login;
                name.style.marginRight = "6px";
                name.target = "_blank";

                const perc = document.createElement("span");
                perc.textContent = `${user.percent}%`;

                const contributions = document.createElement("p");
                contributions.textContent = ` ${user.contributions}`;

                div.appendChild(img);
                div.appendChild(name);
                div.appendChild(perc);

                contributorContainer.appendChild(div);
            });
        } else {
            console.warn("contributors element not found.");
        }
    } catch(error) {
        if (lastValidTimestamp) {
            displayRateLimitNotice(lastValidTimestamp); // ✅ show fallback message
        }
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

// Initial fetch and polling every 10 seconds
console.log(fetchRepoStats());
console.log("Fetching GitHub stats...");
// Poll every 10 seconds
setInterval(fetchRepoStats, 10000);

// Ensures all anchor links open in a new tab
document.querySelectorAll('a').forEach(link => {
    link.setAttribute('target', '_blank');
});