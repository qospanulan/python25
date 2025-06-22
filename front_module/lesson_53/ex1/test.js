const users = await fetch("https://reqres.in/api/users", {
  method: "GET",
  headers: {
    "x-api-key": "reqres-free-v1",
  },
}).then((response) => response.json());

console.log(users);
