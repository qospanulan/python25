const usersElem = document.getElementById("users");

async function loadData() {
  response = await fetch("https://reqres.in/api/users", {
    method: "GET",
    headers: {
      "x-api-key": "reqres-free-v1",
    },
  }).then((response) => response.json());

  users = response.data;

  for (i = 0; i < users.length; i++) {
    const userElem = document.createElement("div");
    userElem.className = "user";
    userData = users[i];

    userElem.innerHTML = `
    <h4>UserID: ${userData.id}</h4>
    <ul>
      <li>First Name: ${userData.first_name}</li>
      <li>Last Name: ${userData.last_name}</li>
      <li>Email: ${userData.email}</li>
    </ul>
  `;

    usersElem.appendChild(userElem);
  }
}

document.addEventListener("DOMContentLoaded", loadData);
