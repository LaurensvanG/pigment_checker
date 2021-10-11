// Wait for content to be loaded
window.addEventListener("DOMContentLoaded", () => ((d, w) => {

    // Flyout menu items
    // Adapted from https://levelup.gitconnected.com/overcoming-css-not-calculating-auto-height-for-transitions-f98a7e062f07
    
    // Grab all targets to be resized
    let calcTargets = d.getElementsByClassName("resize-container");
    
    // Make sure the variable --calc-height on body is set to auto
    d.body.style.setProperty("--calc-height", "auto");

    // Set the current width of the element to the calculated auto width
    function resize() {
      for (let target of calcTargets) {
        let width = target.firstElementChild.offsetWidth + "px";
        if (target.style.getPropertyValue("--calc-width") !== width) {
          target.style.setProperty("--calc-width", width);
        }
      }
    }
    
    w.addEventListener("resize", resize, false);
    w.addEventListener("load", resize, false);


    // Get all pigments that act as modals
    const modals = d.getElementsByClassName("pigment-container");

    // Get the <span> element that closes the modal
    const span = document.getElementsByClassName("close")[0];

    // When the user clicks on the pigment, open the modal
    for (let modal of modals) {
      modal.onclick = function() {
        modal.classList.add("modal");
  
        // Disable hover effects
        modal.classList.remove("pigment-hover");
  
        // Change appearance of the card inside the modal
        modal.firstElementChild.classList.add("container", "card");
        modal.firstElementChild.classList.remove("ellipsis-manufacturer")
      }
    }

    // When the user clicks on <span> (x), close the modal
    // span.onclick = function() {
    //   modal.style.display = "none";
    // }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      for (let modal of modals) {
        if (event.target == modal) {
          modal.classList.remove("modal");
          modal.classList.add("pigment-hover");
          modal.firstElementChild.classList.remove("container", "card");
          modal.firstElementChild.classList.add("ellipsis-manufacturer");
        } 
      }
    }

  })(document, window)
)