

// a funcao splice ela altera o array, ela pode remover elementos ou substituir elementos 

//remover um elemento a partir da posicao 2 do indice de memoria

let numeros = [1,2,3,4,5]

numeros.splice(2,1) // no indice de memoria 2, remova 1 item

console.log("Resultado Remoção" ,numeros)

let numeros2 = [1,2,3,4,5]

numeros.splice(2,1,500 )

console.log("Resultado Sub Array", numeros2);