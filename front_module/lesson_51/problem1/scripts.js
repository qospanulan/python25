const elemNumber1 = document.getElementById("number1");
const elemNumber2 = document.getElementById("number2");

const elemResult = document.getElementById("result");

const elemBtn1 = document.getElementById("btn1");

function btnClickHandler(event) {
  console.log(event);
  var number1 = parseInt(elemNumber1.textContent);
  var number2 = parseInt(elemNumber2.textContent);

  elemResult.textContent = number1 + number2;
}

elemBtn1.addEventListener("click", btnClickHandler);
