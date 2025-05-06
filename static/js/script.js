// script.js

document.addEventListener('DOMContentLoaded', function() {
    // --- Mantener el estado de los collapses en el sidebar ---
    const collapseElements = document.querySelectorAll('#sidebar .collapse');

    collapseElements.forEach(collapseEl => {
        collapseEl.addEventListener('show.bs.collapse', function() {
            localStorage.setItem('sidebar-collapse-' + this.id, 'show');
        });

        collapseEl.addEventListener('hide.bs.collapse', function() {
            localStorage.removeItem('sidebar-collapse-' + this.id);
        });

        const storedState = localStorage.getItem('sidebar-collapse-' + collapseEl.id);
        if (storedState === 'show') {
            new bootstrap.Collapse(collapseEl, { show: true });
        }
    });

    // --- Resaltar el enlace activo en el sidebar ---
    const sidebarLinks = document.querySelectorAll('#sidebar .nav-link');

    sidebarLinks.forEach(link => {
        link.addEventListener('click', function() {
            sidebarLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // --- Opcional: Cerrar el sidebar en dispositivos pequeños al hacer clic en un enlace ---
    const sidebar = document.getElementById('sidebar');
    const sidebarToggler = document.querySelector('.navbar-toggler'); // Si tienes un toggler en la navbar

    sidebarLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth < 768 && sidebar.classList.contains('show')) {
                const bsCollapse = new bootstrap.Collapse(sidebar);
                bsCollapse.hide();
                if (sidebarToggler) {
                    sidebarToggler.classList.add('collapsed');
                    sidebarToggler.setAttribute('aria-expanded', false);
                }
            }
        });
    });
});