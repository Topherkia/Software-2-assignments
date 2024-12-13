'use strict';

let array = []
  for(let i = 1; i <= 6;i++){
    array.push((prompt(`Enter dog ${i}'s name`)))
  }

  array.sort()
  array.reverse()

  for (let i = 0;i < 6;i++){
    document.querySelector('#dogs').innerHTML += `<li>${array[i]}</li>`
  }