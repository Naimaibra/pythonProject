document.addEventListener("DOMContentLoaded", function() {
  // DOM is ready, now you can manipulate the elements

  // Array of data for articles
  const picArray = [
    {
      title: "Article 1",
      medium_image: "image1.jpg",
      caption: "Caption for Image 1",
      description: "Description for Article 1"
    },
    {
      title: "Article 2",
      medium_image: "image2.jpg",
      caption: "Caption for Image 2",
      description: "Description for Article 2"
    },
    // Add more items as needed
  ];

  // Use const for variables that won't be reassigned
  const sectionElement = document.getElementById("articleSection");

  // Loop through the picArray and create articles
  for (let i = 0; i < picArray.length; i++) {
    const articleElement = document.createElement("article");
    articleElement.classList.add("card");

    articleElement.innerHTML = `
      <h2>${picArray[i].title}</h2>
      <figure>
        <img src="${picArray[i].medium_image}" alt="${picArray[i].title}">
        <figcaption>${picArray[i].caption}</figcaption>
      </figure>
      <p>${picArray[i].description}</p>
    `;

    // Append the article to the section
    sectionElement.appendChild(articleElement);
  }
});
