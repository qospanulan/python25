// list with len N. You must find sum and difference of min and max elems.

// function getSum(x, y) {
//   return x + y;
// }

// function getDifference(x, y) {
//   return x - y;
// }

// [4, 1, 7, 99, 54];
// current_max = 99
function getMax(arr) {
  var current_max = arr[0];

  for (i = 1; i < arr.length; i++) {
    if (arr[i] > current_max) {
      current_max = arr[i];
    }
  }

  return current_max;
}

function getMin(arr) {
  var current_min = arr[0];

  for (i = 1; i < arr.length; i++) {
    if (arr[i] < current_min) {
      current_min = arr[i];
    }
  }

  return current_min;
}

function getResultFromMinMax(func, a) {
  return func(getMax(a), getMin(a));
}

a = [4, 2, 7, 99, 54];
res = getResultFromMinMax((x, y) => x + y, a);
console.log("result:", res);

res = getResultFromMinMax((x, y) => x - y, a);
console.log("result:", res);
