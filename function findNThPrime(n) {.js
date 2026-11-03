function findNThPrime(n) {
    var ana = [2, 3,5,7,9,11,13];
    var x = 15;
    while (ana.length < n) {
        x += 2
        var add = true;
        for (let i = 0; i < ana.length; i++) {
            if( x%ana[i] == 0){
                add = false;
                break
            } 
            
            }
            if(add){
                ana.push(x)
          }
          
  
  
  
  
  
  
  console.log(ana)
}
return ana[n-1]
  }
  console.log(findNThPrime(19));