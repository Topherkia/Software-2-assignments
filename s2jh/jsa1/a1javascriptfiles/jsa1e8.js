'use strict'

function leapChecker(year){
    if (year%4===0 && (year%100)!==0){
       return true
    }
    else if (year%100===0){
        if (year%400===0){
            return true
        }
        else{
            return false
        }
    }
    else{
        return false
    }
}

const fyr= prompt('insert the first year: ')
const lyr= prompt('insert the last year: ')
 if (isNaN(fyr) || isNaN(lyr) || fyr > lyr) {
            alert("Please enter valid years.");
        }
 const leapYearList = document.getElementById("leap-years");
        leapYearList.innerHTML = '';
let leap_yrs=[];
for(let i=fyr; i<=lyr; i++){
    if (leapChecker(i)===true){
        const listItem = document.createElement('li');
        listItem.textContent = i;
        leapYearList.appendChild(listItem);
    }
}