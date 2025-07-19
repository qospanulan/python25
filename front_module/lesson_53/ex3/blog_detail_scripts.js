const blogsElem = document.getElementById("blog");

async function loadData() {
  response = await fetch("http://localhost:8000/blog/", {
    method: "GET",
  }).then((response) => response.json());

  blogs = response;

  for (i = 0; i < blogs.length; i++) {
    const blogElem = document.createElement("div");
    blogElem.className = "blog";
    blogData = blogs[i];

    blogElem.innerHTML = `
    <p><a href="http://localhost:8000/blog/${blogData.id}/" >${blogData.name}</a></p>
  `;

    blogsElem.appendChild(blogElem);
  }
}

document.addEventListener("DOMContentLoaded", loadData);
