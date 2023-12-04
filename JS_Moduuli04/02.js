
document.addEventListener("DOMContentLoaded", function() {

  const searchForm = document.getElementById("searchForm");

  // Add submit event listener to the form
  searchForm.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the value entered in the input field
    const query = document.getElementById("query").value;

    // Check if the query is not empty
    if (query.trim() !== "") {
      // Send a request to the TVMaze API
      fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
        .then(response => {
          if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          // Print the search result to the console
          console.log(data);
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
    }
  });
});