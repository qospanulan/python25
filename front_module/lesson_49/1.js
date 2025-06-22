a = [1, 3, 5, "Hello"];

console.log("Before:", a);

a.unshift(12);
a.push(99); // .append()
console.log("After 1:", a);
x = a.pop();
console.log("After 2:", a);
console.log("Removed:", x);
