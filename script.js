document.addEventListener('DOMContentLoaded', () => {

  // ─── THEME TOGGLE ───
  const body = document.body;
  const toggle = document.getElementById('themeToggle');
  if (localStorage.getItem('theme') === 'light') body.classList.add('light-mode');
  toggle.addEventListener('click', () => {
    body.classList.toggle('light-mode');
    localStorage.setItem('theme', body.classList.contains('light-mode') ? 'light' : 'dark');
    toggle.textContent = body.classList.contains('light-mode') ? '🌙 Dark' : '☀️ Light';
  });
  toggle.textContent = body.classList.contains('light-mode') ? '🌙 Dark' : '☀️ Light';

  // ─── CUSTOM CURSOR ───
  const dot = document.querySelector('.cursor-dot');
  const ring = document.querySelector('.cursor-ring');
  let mx = 0, my = 0, dx = 0, dy = 0, rx = 0, ry = 0;
  document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });
  (function animateCursor() {
    dx += (mx - dx) * 0.25;
    dy += (my - dy) * 0.25;
    rx += (mx - rx) * 0.1;
    ry += (my - ry) * 0.1;
    dot.style.left = dx + 'px';
    dot.style.top = dy + 'px';
    ring.style.left = rx + 'px';
    ring.style.top = ry + 'px';
    requestAnimationFrame(animateCursor);
  })();

  // ─── NAV SCROLL ───
  const nav = document.querySelector('nav');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 80);
  });

  // ─── HAMBURGER ───
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
  navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));

  // ─── TYPED SUBTITLE ───
  const roles = ['Developer', 'Designer', 'Problem Solver'];
  const typedEl = document.getElementById('typed');
  let ri = 0, ci = 0, deleting = false;
  function typeLoop() {
    const word = roles[ri];
    if (!deleting) {
      typedEl.textContent = word.substring(0, ci + 1);
      ci++;
      if (ci === word.length) { deleting = true; setTimeout(typeLoop, 1800); return; }
      setTimeout(typeLoop, 100);
    } else {
      typedEl.textContent = word.substring(0, ci - 1);
      ci--;
      if (ci === 0) { deleting = false; ri = (ri + 1) % roles.length; setTimeout(typeLoop, 400); return; }
      setTimeout(typeLoop, 50);
    }
  }
  typeLoop();

  // ─── HERO PARALLAX ───
  const heroName = document.querySelector('.hero-name');
  const heroSub = document.querySelector('.hero-subtitle');
  document.addEventListener('mousemove', e => {
    const cx = (e.clientX / window.innerWidth - 0.5) * 2;
    const cy = (e.clientY / window.innerHeight - 0.5) * 2;
    heroName.style.transform = `translate(${cx * 12}px, ${cy * 8}px)`;
    heroSub.style.transform = `translate(${cx * -8}px, ${cy * -5}px)`;
  });

  // ─── SCROLL REVEAL ───
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); } });
  }, { threshold: 0.15 });
  reveals.forEach(el => observer.observe(el));

  // ─── STAT COUNTERS ───
  const statEls = document.querySelectorAll('.stat-number');
  const statObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.target);
        const suffix = el.dataset.suffix || '';
        let current = 0;
        const step = Math.max(1, Math.floor(target / 40));
        const timer = setInterval(() => {
          current += step;
          if (current >= target) { current = target; clearInterval(timer); }
          el.textContent = current + suffix;
        }, 30);
        statObs.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  statEls.forEach(el => statObs.observe(el));

  // ─── ACTIVE NAV LINK ───
  const sections = document.querySelectorAll('section[id]');
  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(s => {
      if (window.scrollY >= s.offsetTop - 200) current = s.id;
    });
    document.querySelectorAll('.nav-links a').forEach(a => {
      a.classList.toggle('active', a.getAttribute('href') === '#' + current);
    });
  });

  // ─── SMOOTH SCROLL ───
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      const target = document.querySelector(a.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
  });

  // ─── RANDOM SKILL TAG ROTATION ───
  document.querySelectorAll('.skill-tag').forEach(tag => {
    tag.style.transform = `rotate(${(Math.random() - 0.5) * 8}deg)`;
  });
});
