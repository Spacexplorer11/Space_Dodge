// Utility: simple UUID v4
function generateUUID() {
  return ([1e7]+-1e3+-4e3+-8e3+-1e11)
    .replace(/[018]/g, c =>
      (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
}

window.addEventListener("DOMContentLoaded", () => {
  const page = window.location.pathname.split("/").pop();

  // Only hydrate & start SSE from the real pages
  if (page === "contributors.html" || page === "stats.html") {
    const stored = localStorage.getItem("lastGithubPayload");
    if (stored) {
      try {
        updateContributorsUI(JSON.parse(stored));
      } catch (e) {
        console.error("Could not parse stored payload:", e);
      }
    }
    setupSSE();
  }

  highlightActiveMenu();
  isMobile();
});

function setupSSE() {
  // Persist deviceId in localStorage instead of a cookie
  let deviceId = localStorage.getItem("DEVICE_ID");
  if (!deviceId) {
    deviceId = generateUUID();
    localStorage.setItem("DEVICE_ID", deviceId);
    console.log("Generated DEVICE_ID:", deviceId);
  }

  // Attach it as a query-param so your Worker can read it
  const url = new URL("https://github-backend.spacexplorer11.workers.dev/sse");
  url.searchParams.set("device_id", deviceId);

  const sse = new EventSource(url.toString());
  sse.onopen = () => console.log("SSE opened");
  sse.onerror = err => console.error("SSE error:", err);

  sse.onmessage = e => {
    let payload;
    try {
      payload = JSON.parse(e.data);
    } catch {
      console.warn("Non-JSON event:", e.data);
      return;
    }
    localStorage.setItem("lastGithubPayload", e.data);
    updateContributorsUI(payload);
  };
}

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

async function updateContributorsUI(data) {
  // 1) use the same key your Worker is emitting
  const commitCount = data.commit_count;
  const contributors = data.contributors;

  // 2) update the count display
  const commitDisplay = document.getElementById("commit-count");
  if (commitDisplay) {
    commitDisplay.textContent = commitCount;
  }

  // 3) bail if no container
  const container = document.getElementById("contributors");
  if (!container) return;

  // 4) clear out old rows so we never double‐append
  container.innerHTML = "";

  // 5) the rest of your logic is unchanged
  const validContributors = (contributors || []).filter(c =>
    (c.contributions ?? c.total) != null &&
    (c.login || c.author?.login)
  );

  const totalContribs = validContributors.reduce(
    (sum, c) => sum + (c.contributions ?? c.total), 0
  );

  let withPct = validContributors.map(c => {
    const contribs = c.contributions ?? c.total;
    const pct = totalContribs > 0
      ? Math.round((contribs/totalContribs)*1000)/10
      : 0;
    return { ...c, percent: isNaN(pct) ? 0 : pct };
  });

  // adjust to exactly 100%
  let sumPct = withPct.reduce((s, c) => s + c.percent, 0);
  const diff = Math.round((100 - sumPct)*10)/10;
  if (diff !== 0 && withPct.length) {
    withPct.sort((a,b) => b.percent - a.percent)[0].percent += diff;
  }

  // render
  withPct.forEach(c => {
    const login    = c.login || c.author?.login;
    const avatar   = c.avatar_url || c.author?.avatar_url;
    const profile  = c.html_url   || c.author?.html_url;
    const contribs = c.contributions ?? c.total;
    if (!login||!avatar||!profile||contribs==null) return;

    const div = document.createElement("div");
    div.className = "contributor";
    div.innerHTML = `
      <img src="${avatar}" alt="${login}" width="32" height="32"
           style="border-radius:50%;margin-right:8px">
      <a href="${profile}" target="_blank" style="margin-right:6px">
        ${login}
      </a>
      <span>${c.percent}%</span>
    `;
    container.appendChild(div);
  });

  // hide loading, show container
  document.getElementById("loading-message").style.display = "none";
  container.style.display = "block";
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
