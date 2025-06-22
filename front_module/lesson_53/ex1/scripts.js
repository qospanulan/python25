const postsElem = document.getElementById("posts");

const posts = [
  {
    postId: 1,
    postTitle: "Test post!",
    postContent: "Blah-blah-blah!",
  },
  {
    postId: 2,
    postTitle: "AI is not the future, it is the present!",
    postContent: "Blah-blah-blah!",
  },
];

for (i = 0; i < posts.length; i++) {
  const postElem = document.createElement("div");
  postElem.className = "post";

  const postId = posts[i].postId;
  const postTitle = posts[i].postTitle;
  const postContent = posts[i].postContent;

  postElem.innerHTML = `
    <h4>${postId}. ${postTitle}</h4>
    <p>${postContent}</p>
  `;

  console.log(postElem);

  postsElem.appendChild(postElem);
}
