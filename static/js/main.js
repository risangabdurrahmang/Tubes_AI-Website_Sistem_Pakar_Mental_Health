(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  };

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach((e) => e.addEventListener(type, listener));
      } else {
        selectEl.addEventListener(type, listener);
      }
    }
  };

  /**
   * Easy on scroll event listener
   */
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select("#navbar .scrollto", true);
  const navbarlinksActive = () => {
    let position = window.scrollY + 200;
    navbarlinks.forEach((navbarlink) => {
      if (!navbarlink.hash) return;
      let section = select(navbarlink.hash);
      if (!section) return;
      if (position >= section.offsetTop && position <= section.offsetTop + section.offsetHeight) {
        navbarlink.classList.add("active");
      } else {
        navbarlink.classList.remove("active");
      }
    });
  };
  window.addEventListener("load", navbarlinksActive);
  onscroll(document, navbarlinksActive);

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let elementPos = select(el).offsetTop;
    window.scrollTo({
      top: elementPos,
      behavior: "smooth",
    });
  };

  /**
   * Back to top button
   */
  let backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add("active");
      } else {
        backtotop.classList.remove("active");
      }
    };
    window.addEventListener("load", toggleBacktotop);
    onscroll(document, toggleBacktotop);
  }

  /**
   * Mobile nav toggle
   */
  on("click", ".mobile-nav-toggle", function (e) {
    select("body").classList.toggle("mobile-nav-active");
    this.classList.toggle("bi-list");
    this.classList.toggle("bi-x");
  });

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on(
    "click",
    ".scrollto",
    function (e) {
      if (select(this.hash)) {
        e.preventDefault();

        let body = select("body");
        if (body.classList.contains("mobile-nav-active")) {
          body.classList.remove("mobile-nav-active");
          let navbarToggle = select(".mobile-nav-toggle");
          navbarToggle.classList.toggle("bi-list");
          navbarToggle.classList.toggle("bi-x");
        }
        scrollto(this.hash);
      }
    },
    true
  );

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener("load", () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash);
      }
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener("load", () => {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  });
})();

/**
 * Slide Bar
 */
let rangeInput = document.querySelectorAll(".range-input input");
let rangeValue = document.querySelectorAll(".range-input .value div");
window.addEventListener("load", function () {
  rangeValue.innerHTML = "<div> &nbsp;<i class='bi bi-emoji-smile'></i></div>";
});
for (let x = 0; x < rangeInput.length; x++) {
  let start = parseInt(rangeInput[x].min);
  let end = parseInt(rangeInput[x].max);
  let step = parseInt(rangeInput[x].step);
  rangeValue[x].innerHTML = "<div> &nbsp;<i class='bi bi-emoji-smile'></i></div>";
  rangeInput[x].oninput = function () {
    let data_input = parseInt(this.value);
    if (data_input == 0) {
      rangeValue[x].innerHTML = "<div> &nbsp;<i class='bi bi-emoji-smile'></i></div>";
      console.log(data_input);
    }
    if (data_input == 1) {
      rangeValue[x].innerHTML = "<div> &nbsp;<i class='bi bi-emoji-frown'></i></div>";
      console.log(data_input);
    }
  };
  // for (let i = start; i <= end; i += step) {
  //   let data_input = parseInt(rangeInput[x].value);
  //   if (data_input == 0) {
  //     rangeValue[x].innerHTML += "<div>" + i + "&nbsp;<i class='bi bi-emoji-smile'></i></div>";
  //     // rangeInput[x].value = i;
  //   }
  //   if (data_input == 1) {
  //     rangeValue[x].innerHTML += "<div>" + i + "&nbsp;<i class='bi bi-emoji-frown'></i></div>";
  //     // rangeInput[x].value = i;
  //   }
  // }

  rangeInput[x].addEventListener("input", function () {
    let top = (parseFloat(rangeInput[x].value) / step) * -40;
    rangeValue[x].style.marginTop = top + "px";
  });
}
