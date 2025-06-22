const mainContainer = document.getElementById("main");
const createTextBtn = document.getElementById("btn1");

function btnClickHandler() {
  console.log("Button clicked!");
  mainContainer.innerHTML = "<p>Ha-ha-ha!</p>";
}

createTextBtn.addEventListener("click", btnClickHandler);
// document.addEventListener("click", btnClickHandler);
