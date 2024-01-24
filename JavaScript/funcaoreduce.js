let numeros = [1,2,3,4,5]

// funcao reduce ira somar todos os elementos do array resultando em um unico valor

let somatotal = numeros.reduce(function(x,y){
    return x+y
});

console.log('Soma dos elementos', somatotal)