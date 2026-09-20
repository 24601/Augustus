(function () {
  var root = document.documentElement;
  var reduce = false;

  try {
    reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (err) {
    reduce = false;
  }

  if (reduce) {
    root.classList.add("motion-off");
    return;
  }

  var played = false;
  try {
    played = window.sessionStorage.getItem("augustus-hero-once") === "1";
  } catch (err) {
    played = false;
  }

  if (played) {
    root.classList.add("hero-done");
    return;
  }

  root.classList.add("hero-play");
  try {
    window.sessionStorage.setItem("augustus-hero-once", "1");
  } catch (err) {
    /* ignore quota / private mode */
  }
})();
