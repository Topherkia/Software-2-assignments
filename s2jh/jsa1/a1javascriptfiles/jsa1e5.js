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
const yr=prompt('insert year: ')
if (leapChecker(yr)){
    alert('leap year')
}
else {
    alert('not a leap year')
}