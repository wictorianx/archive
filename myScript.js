function sequence(number){
    let length = 0;
    while (number !== 1){
        if (number === 0){
            break}
        else if (number%2 === 0){
            number = number/2}
        else{
            number = number*3+1
        length += 1}}
    return(length+1)}
let biggest = 0;
let answer = 0;
for (let i =0; i < 1000000; i++){
    let chain = sequence(i);
    if (chain > biggest){
        biggest = chain;
        answer = i}};
alert(answer);
console.log(answer);

    
