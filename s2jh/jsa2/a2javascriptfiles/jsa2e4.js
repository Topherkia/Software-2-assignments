'use strict';
let array = [];
while(true){
  let number = parseInt(prompt("Insert a number, type 0 to end"));
  if (number===0){
      break;
  }
  array.push(number);
}
array.sort();
array.reverse();
console.log(array);