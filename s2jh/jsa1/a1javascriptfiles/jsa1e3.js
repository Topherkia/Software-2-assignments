'use strict';
let sums=0;
let product=1;
for(let i=1; i<=3; i++){
    let number=prompt('insert integer number '+ i);
    sums=parseInt(sums)+parseInt(number);
    product=product*number;
}
document.querySelector('#sum').innerHTML =('sum: '+ sums);
document.querySelector('#prod').innerHTML =('product: '+ product);
document.querySelector('#aver').innerHTML =('average: '+ sums/3);
