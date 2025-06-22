const btnElem = document.getElementById("btn1");
const resultElem = document.getElementById("result");
const inputElem1 = document.getElementById("number1");
const inputElem2 = document.getElementById("number2");

function btnClickHandler() {
  number1 = parseInt(inputElem1.value);
  number2 = parseInt(inputElem2.value);

  resultElem.textContent = number1 + number2;
}

btnElem.addEventListener("click", btnClickHandler);
