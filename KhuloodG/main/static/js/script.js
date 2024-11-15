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

let sortByName = true; 

function toggleSortMode() {
    if (sortByName) {
        sortProjectsByName();
        document.getElementById('sortLabel').textContent = "Sort by Date";
    } else {
        sortProjectsByDate();
        document.getElementById('sortLabel').textContent = "Sort by Name";
    }
    sortByName = !sortByName; // Toggle the flag
}

// Search function
function searchProjects() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const projects = document.querySelectorAll('.project-card');

    projects.forEach(project => {
        const name = project.querySelector('h3').textContent.toLowerCase();
        if (name.includes(input)) {
            project.style.display = '';
        } else {
            project.style.display = 'none';
        }
    });
}

// Sort projects by name function
function sortProjectsByName() {
    const projectGrid = document.getElementById('projectGrid');
    const projects = Array.from(projectGrid.children);

    projects.sort((a, b) => {
        const nameA = a.getAttribute('data-name').toLowerCase();
        const nameB = b.getAttribute('data-name').toLowerCase();
        return nameA.localeCompare(nameB);
    });

    projects.forEach(project => projectGrid.appendChild(project));
}

// Sort projects by date function
function sortProjectsByDate() {
    const projectGrid = document.getElementById('projectGrid');
    const projects = Array.from(projectGrid.children);

    projects.sort((a, b) => {
        const dateA = new Date(a.getAttribute('data-date'));
        const dateB = new Date(b.getAttribute('data-date'));
        return dateB - dateA;
    });

    projects.forEach(project => projectGrid.appendChild(project));
}

// Filter projects by category function
function filterProjects() {
    const category = prompt("Enter a category to filter by (e.g., 'Blog', 'Real Estate')");
    const projects = document.querySelectorAll('.project-card');

    projects.forEach(project => {
        if (project.getAttribute('data-name').toLowerCase() === category.toLowerCase()) {
            project.style.display = '';
        } else {
            project.style.display = 'none';
        }
    });
}

// Toggle icon color function
function toggleIconColor(element) {
    const toolbarItems = document.querySelectorAll('.toolbar-item');
    toolbarItems.forEach(item => item.classList.remove('active'));
    
    element.classList.add('active');
}
