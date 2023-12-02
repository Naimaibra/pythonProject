


document.addEventListener("DOMContentLoaded", function() {
  // DOM is ready, now you can manipulate the elements

  // Use const for variables that won't be reassigned
  const triggerElement = document.getElementById("trigger");
  const targetImage = document.getElementById("target");

  // Add mouseover and mouseout event listeners to the trigger element
  triggerElement.addEventListener("mouseover", function() {
    // Change the source of the image when the mouse is over
    targetImage.src = 'Image/image1-large.jpeg';
  });

  triggerElement.addEventListener("mouseout", function() {
    // Change the source of the image back to the original when the mouse is out
    targetImage.src = 'Image/image2-medium.jpeg';
  });
});

