'use strict';

function diceRolls(sides) {
    while (true) {
        let dice = Math.floor(Math.random()*sides+1);
        document.querySelector('#dice2').innerHTML += `<li>${dice}</li>`;
        if(dice===sides){
            break;
        }
    }
}
let side=prompt('Insert the amount of dice sides');
diceRolls(parseInt(side));