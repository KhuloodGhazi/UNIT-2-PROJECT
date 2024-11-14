document.addEventListener("DOMContentLoaded", function () {
    // ScrollReveal animations
    ScrollReveal().reveal('.nav-links li', { delay: 200, origin: 'left', distance: '50px' });
    ScrollReveal().reveal('.social-icons a', { delay: 200, origin: 'right', distance: '50px' });
    ScrollReveal().reveal('#intro h1', { delay: 300, origin: 'bottom', distance: '30px' });
    ScrollReveal().reveal('#intro h2', { delay: 500, origin: 'bottom', distance: '30px' });

    // Set active state on scroll
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-links a");

    window.addEventListener("scroll", () => {
        let current = "";
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= sectionTop - sectionHeight / 3) {
                current = section.getAttribute("id");
            }
        });

        navLinks.forEach(link => {
            link.classList.remove("active");
            if (link.getAttribute("href").includes(current)) {
                link.classList.add("active");
            }
        });
    });
});
