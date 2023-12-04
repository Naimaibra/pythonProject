document.addEventListener("DOMContentLoaded", function() {
  const searchForm = document.querySelector("#searchForm");
  const searchTermInput = document.querySelector("#searchTerm");
  const jokesContainer = document.querySelector("#jokesContainer");

  searchForm.addEventListener("submit", function(event) {
    event.preventDefault();
    const searchTerm = searchTermInput.value;

    if (searchTerm.trim() !== "") {
      fetch(`https://api.chucknorris.io/jokes/search?query=${searchTerm}`)
        .then(response => {
          if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          displayJokes(data.result);
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
    }
  });

  function displayJokes(jokes) {
    jokesContainer.innerHTML = ""; // Clear previous jokes

    jokes.forEach(joke => {
      const article = document.createElement("article");
      const p = document.createElement("p");
      p.textContent = joke.value;
      article.appendChild(p);
      jokesContainer.appendChild(article);
    });
  }
});