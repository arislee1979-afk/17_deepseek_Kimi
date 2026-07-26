// DeepSeek Research Portal - Interactive Script
document.addEventListener('DOMContentLoaded', () => {
  // Tab Switching in Dashboard
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.getAttribute('data-tab');
      
      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));
      
      btn.classList.add('active');
      const content = document.getElementById(targetTab);
      if (content) {
        content.classList.add('active');
      }
    });
  });

  // Table Responsive Wrappers
  const tables = document.querySelectorAll('.markdown-body table');
  tables.forEach(table => {
    if (!table.parentElement.classList.contains('table-wrapper')) {
      const wrapper = document.createElement('div');
      wrapper.className = 'table-wrapper';
      table.parentNode.insertBefore(wrapper, table);
      wrapper.appendChild(table);
    }
  });

  // Active Sidebar Link on Scroll
  const headers = document.querySelectorAll('.markdown-body h1, .markdown-body h2, .markdown-body h3');
  const sidebarLinks = document.querySelectorAll('.sidebar-link');
  
  if (headers.length > 0 && sidebarLinks.length > 0) {
    window.addEventListener('scroll', () => {
      let current = '';
      headers.forEach(header => {
        const headerTop = header.offsetTop;
        if (pageYOffset >= headerTop - 150) {
          current = header.getAttribute('id');
        }
      });

      sidebarLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
          link.classList.add('active');
        }
      });
    });
  }

  // Smooth scroll for anchors
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId && targetId !== '#') {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });
});
