'use strict'
let shudy=confirm('should I calculate the square root?');
if (shudy){
    let fr_num=prompt('insert number for me to calculate the square root');
    if (fr_num>=0){
        document.querySelector('#beetroot').innerHTML='the square root is: '+Math.sqrt(parseInt(fr_num))
    }
    else if (fr_num<0){
        document.querySelector('#beetroot').innerHTML='The square root of a negative number is not defined'
    }
}