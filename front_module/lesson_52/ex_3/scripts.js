const btnElem = document.getElementById("btn1");
const squareElem = document.getElementById("square");

function btnClickHandler() {
  // if (squareElem.style.backgroundColor === "red") {
  //   squareElem.style.backgroundColor = "black";
  // } else {
  //   squareElem.style.backgroundColor = "red";
  // }

  squareElem.style.backgroundColor =
    squareElem.style.backgroundColor === "black" ? "red" : "black";
}

btnElem.addEventListener("click", btnClickHandler);

// при нажатии менять цвет с красного на черный, с черного на красный

// a = "x is greater than 12" if x>12 else "x is less than 12"
