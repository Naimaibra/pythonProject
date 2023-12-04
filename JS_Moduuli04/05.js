

document.addEventListener("DOMContentLoaded", function() {
  // Send a request to the chucknorris.io API
  fetch("https://api.chucknorris.io/jokes/random")
    .then(response => {
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      // Print the Chuck Norris joke to the console
      console.log(data.value);
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });
});
