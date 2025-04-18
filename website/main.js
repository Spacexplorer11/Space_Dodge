// Ensure Stats.js is loaded via script tag in HTML, or import it if using a module system
// Example (HTML): <script src="https://cdnjs.cloudflare.com/ajax/libs/stats.js/r17/Stats.min.js"></script>
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

function isMobile() {
    if (window.innerWidth <= 600 || Mobile.includes(getDeviceInfo())) {
        document.body.classList.add("mobile");
        console.log("Mobile detected");
    } else {
        document.body.classList.remove("mobile");
    }
}

const Desktop = [
    "Windows",
    "macOS",
    "Linux"
]
const Mobile = [
    "Android",
    "iOS"
]

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

function backToStart() {
    window.location.href = "index.html";
}

// Function to open anchor links in a new tab
document.querySelectorAll('a').forEach(link => {
    link.setAttribute('target', '_blank');
});