'use strict'
let dice_sum=0;
let dice_num = prompt('how many dices should I roll?');
for(let i=0; i<dice_num; i++){
    let dice=Math.floor(Math.random()*6);
    dice+=1;
    dice_sum+=dice;
}

document.querySelector('#roll-dice').innerHTML=dice_sum