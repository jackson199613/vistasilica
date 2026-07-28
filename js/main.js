/* Vistachem Silica — shared interactions */
(function () {
  "use strict";

  // ---- Mobile nav toggle ----
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      header.classList.toggle("nav-open");
      var open = header.classList.contains("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // ---- Dropdown menus (hover on desktop, click on mobile) ----
  var dropItems = document.querySelectorAll(".nav__links > li.has-mega");
  dropItems.forEach(function (li) {
    var link = li.querySelector("a");
    // desktop hover
    li.addEventListener("mouseenter", function () {
      if (window.innerWidth > 860) li.classList.add("is-open");
    });
    li.addEventListener("mouseleave", function () {
      if (window.innerWidth > 860) li.classList.remove("is-open");
    });
    // mobile / keyboard click
    link.addEventListener("click", function (e) {
      if (window.innerWidth <= 860) {
        e.preventDefault();
        li.classList.toggle("is-open");
      }
    });
  });

  // ---- FAQ accordion ----
  document.querySelectorAll(".faq-q").forEach(function (q) {
    q.addEventListener("click", function () {
      var item = q.closest(".faq-item");
      var answer = item.querySelector(".faq-a");
      var isOpen = item.classList.toggle("is-open");
      answer.style.maxHeight = isOpen ? answer.scrollHeight + "px" : null;
      q.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  });

  // ---- Back to top ----
  var topBtn = document.querySelector(".floater--top");
  if (topBtn) {
    topBtn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // ---- Form demo submit (no backend on static host) ----
  document.querySelectorAll("form[data-demo]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = form.querySelector('input[type="checkbox"][required]');
      if (ok && !ok.checked) { ok.focus(); return; }
      var note = form.querySelector(".form-result");
      if (note) {
        note.hidden = false;
        note.scrollIntoView({ behavior: "smooth", block: "center" });
      }
      form.reset();
    });
  });

  // ---- Scroll reveal ----
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll("[data-reveal]").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll("[data-reveal]").forEach(function (el) { el.classList.add("in"); });
  }
})();
