/**
* Template Name: Selecao - v4.0.0
* Template URL: https://bootstrapmade.com/selecao-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Use-cases slider
   */
  new Swiper('.use-cases-slider', {
    speed: 600,
    loop: false,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: '3',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
});


  document.addEventListener('aos:in:countUp', ({ detail }) => {
    /**
      * Extracted from
      * https://www.i-visionblog.com/2014/11/jquery-animated-number-counter-from-zero-to-value-jquery-animation.html
    */
    $('.count').each(function () {
      $(this).prop('Counter',0).animate({
          Counter: $(this).text()
      }, {
          duration: 1500,
          easing: 'swing',
          step: function (now) {
              $(this).text(Math.ceil(now));
          }
      });
    });
  });

  /**
   * Generic list search
   *
   * This will filter the elements of a list with ID <prefix>List using the value entered via an
   * input with name <prefix>SearchInput. For example, to filter boards that are contained in a
   * <div id="boardList">...</div>, place an
   * <input name="boardSearchInput" type="text" placeholder="Search..">
   */
  $(document).ready(function(){
    $("input[name*='SearchInput']").on("keyup", function(e) {
      var target = $(e.target);
      var prefix = target.attr("name").split("SearchInput")[0];
      var searchValue = target.val().toLowerCase();
      if (prefix == "driver") {
        var list = $(".list-group-item");
        if (searchValue == "") {
            $(".collapse").collapse("hide");
        }
        else {
            $(".collapse").collapse("show");
        }
      }
      else {
        var list = $("#" + prefix + "List *").not(".exclude");
      }

      list.filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(searchValue) > -1)
      })
    });
  });

  /**
   * Create a new 'script' element which sources Twitter widgets script
   */
  function loadTwitterScript() {
    let script = document.createElement('script');
    let timeline = $("#twitter-timeline");
    let cb = () => {
      // When the script is loaded we bind to the widget rendering event to display it
      twttr.events.bind("rendered", (event) => {
          timeline.addClass("rendered");
      });
    }

    script.src = "https://platform.twitter.com/widgets.js"
    script.onload = cb;
    document.head.append(script);
  }

  /**
   * We need to wait until we know the user accepts using third party cookies
   */
  $(window).on("cookiesAccepted", () => {
    loadTwitterScript();
  });

})()
