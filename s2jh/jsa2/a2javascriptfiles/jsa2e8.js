'use strict';

let stringArray = [ 'Johnny', 'DeeDee', 'Joey', 'Marky'];
let space = '';

function concat (arrayX){
    for (let i = 0; i < arrayX.length; i++){
        space += arrayX[i]
        document.querySelector('#concat').innerHTML = space;
    }
}

concat(stringArray)