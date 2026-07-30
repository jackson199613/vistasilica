/* Vistachem — Apple-style motion
   Scroll-reveal with staggered, decelerating entrance.
   Honors prefers-reduced-motion. Uses IntersectionObserver. */
(function () {
  'use strict';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Auto-tag common content blocks for reveal (only if author didn't opt out)
  var selectors = [
    '.sol-card', '.feature', '.card', '.case-card', '.wp-card',
    '.doc-card', '.step', '.pain', '.section-title', '.section-lead',
    '.metric', '.stat'
  ];
  var nodes = [];
  selectors.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      if (!el.hasAttribute('data-reveal') && !el.closest('.hero')) {
        el.setAttribute('data-reveal', '');
        nodes.push(el);
      }
    });
  });

  if (reduce || !('IntersectionObserver' in window)) {
    nodes.forEach(function (el) { el.classList.add('is-in'); });
    return;
  }

  // Stagger siblings that reveal together for a natural cascade
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      var parent = el.parentElement;
      var siblings = parent ? [].slice.call(parent.querySelectorAll('[data-reveal]')) : [el];
      var idx = Math.max(0, siblings.indexOf(el));
      el.style.transitionDelay = Math.min(idx * 70, 350) + 'ms';
      el.classList.add('is-in');
      io.unobserve(el);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

  nodes.forEach(function (el) { io.observe(el); });
})();
