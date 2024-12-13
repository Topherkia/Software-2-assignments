'use strict';

function groupPicker(insart){
    let rand=Math.floor(Math.random()*3);
    if (rand===0){
        return(insart+'! you are Gryffindor');
    }
    else if (rand===1){
        return(insart+'! you are Slytherin');
    }
    else if (rand===2){
        return(insart+'! you are Hufflepuff');
    }
    else if (rand===3){
        return(insart+'! you are Ravenclaw');;
    }
}

const jacky=prompt('insert your name new kid: ');
document.querySelector('#pottah').innerHTML=(groupPicker(jacky));

