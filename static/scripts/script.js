// Adapted from https://levelup.gitconnected.com/overcoming-css-not-calculating-auto-height-for-transitions-f98a7e062f07
window.addEventListener("DOMContentLoaded", () => (function(d, w) {
  console.log(d, w)

    // Grab all targets to be resized
    var calcTargets = d.getElementsByClassName("resize-container");
    
    // Make sure the variable --calc-height on body is set to auto
    d.body.style.setProperty("--calc-height", "auto");

    // Set the current width of the element to the calculated auto width
    function resize() {
      for (var target of calcTargets) {
        var width = target.firstElementChild.offsetWidth + "px";
        if (target.style.getPropertyValue("--calc-width") !== width) {
          target.style.setProperty("--calc-width", width);
        }
      }
    }
    
    w.addEventListener("resize", resize, false);
    w.addEventListener("load", resize, false);
  })(document, window)
)