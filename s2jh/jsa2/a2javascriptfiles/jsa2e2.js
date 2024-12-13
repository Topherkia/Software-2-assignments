  'use strict';

  let participants = prompt("How many participants in your game?");
  let array = []
  for(let i = 0; i < participants;i++){
    array.push((prompt("Enter players name")))
  }
  array.sort()

  document.querySelector('#parties').innerHTML = array