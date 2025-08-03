document.addEventListener("DOMContentLoaded", function () {
  // ✅ Lenis
  const lenis = new Lenis({
    duration: 1.2,
    easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)) // easeOutExpo
  });

  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  // ✅ Anchor scroll with Lenis
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        lenis.scrollTo(target);
      }
    });
  });

  // ✅ Swiper
  new Swiper('.mySwiper', {
    loop: true,
    autoplay: { delay: 3000 },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });

  // ✅ Barba Page Transitions (Optional)
  barba.init({
    transitions: [{
      name: 'fade',
      leave(data) {
        return gsap.to(data.current.container, {
          opacity: 0,
          duration: 0.5
        });
      },
      enter(data) {
        return gsap.from(data.next.container, {
          opacity: 0,
          duration: 0.5
        });
      }
    }]
  });
});
