document.addEventListener("DOMContentLoaded", function() {
  // DOM is ready, now you can manipulate the elements

  // Use const for variables that won't be reassigned
  const searchForm = document.getElementById("searchForm");
  const resultsContainer = document.getElementById("results");

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
          // Display search results on the web page
          displaySearchResults(data);
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
    }
  });

  // Function to display search results on the web page
  function displaySearchResults(results) {
    // Clear previous search results
    resultsContainer.innerHTML = "";

    // Loop through the results and create articles for each series
    results.forEach(tvShow => {
      const tvShowElement = document.createElement("article");
      tvShowElement.classList.add("tv-show");

      // Display series name in <h2> element
      const nameElement = document.createElement("h2");
      nameElement.textContent = tvShow.show.name;
      tvShowElement.appendChild(nameElement);

      // Display link to details in <a> element
      const urlElement = document.createElement("a");
      urlElement.href = tvShow.show.url;
      urlElement.textContent = "Details";
      urlElement.target = "_blank";
      tvShowElement.appendChild(urlElement);

      // Display medium image with <img src="" alt="">
      const imageElement = document.createElement("img");
      imageElement.src = tvShow.show.image ? tvShow.show.image.medium : "https://via.placeholder.com/210x295?text=Not%20Found";
      imageElement.alt = tvShow.show.name;
      tvShowElement.appendChild(imageElement);

      // Display summary in <div> element
      const summaryElement = document.createElement("div");
      summaryElement.innerHTML = tvShow.show.summary || "No summary available.";
      tvShowElement.appendChild(summaryElement);

      // Append the TV show element to the results container
      resultsContainer.appendChild(tvShowElement);
    });
  }
});