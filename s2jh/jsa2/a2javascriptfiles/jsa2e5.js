'use strict';

let set =[]

while (true){
  let number = parseInt(prompt('Insert a number'));
  if (number in set){
    alert('already exists')
    break;
  }
  set.push(number)


}
set.sort();

console.log(set)