'use strict';

function diceRolls() {

    while (true) {

        let num_dice = (Math.floor(Math.random()*6)+1);
        document.querySelector('#dice').innerHTML += `<li>${num_dice}</li>`;
        if (num_dice===6){
            break;
        }

    }
}

diceRolls()