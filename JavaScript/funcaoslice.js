// a funcao slice ela retorna uma copia da parte de um array para outro array (subarray)

// ele ira copiar a parte de um array da posicao 1 a 4 e colocar em outro array

let carros = ["gol","Fusca","Ford KA","Sandero","Uno"]

let garagem = carros.slice(1,4);// começa no 1 e termina no 3

console.log("Carros na Garagem",garagem)