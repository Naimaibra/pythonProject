

document.addEventListener("DOMContentLoaded", function() {

  const sectionElement = document.getElementById("articleSection");
  const modal = document.getElementById("imageModal");
  const modalImage = document.getElementById("modalImage");
  const closeModalButton = document.getElementById("closeModal");

  // Array of data for articles
  const picArray = [
    {
      title: "Article 1",
      medium_image: "Image/image1medium.jpeg",
      large_image: "image1-large.jpeg",
      caption: "Caption for Image 1",
      description: "Description for Article 1"
    },
    {
      title: "Article 2",
      medium_image: "Image/image2_medium.jpg",
      large_image: "Image/image2-large.jpg",
      caption: "Caption for Image 2",
      description: "Description for Article 2"
    },
    // Add more items as needed
  ];

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

    // Add click event listener to open the modal
    articleElement.addEventListener("click", function() {
      modalImage.src = picArray[i].large_image;
      modal.showModal();
    });

    // Append the article to the section
    sectionElement.appendChild(articleElement);
  }

  // Add click event listener to close the modal
  closeModalButton.addEventListener("click", function() {
    modal.close();
  });
});