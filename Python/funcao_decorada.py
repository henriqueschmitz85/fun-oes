## funcoes decoradoras potencializam ou modificam a logica de outra funcao ou metodo
# uma funcao decoradora e quando utilizamos o @ em cima de uma funcao

#exemplo

#@decoradora - decora potencializa a funcao oi com os recursos dela
# def oi():
#  print('oi')

## criar uma funcao decoradora

def master(msg):
    def imprime():
        print("essa e a funcao decoradora")
    msg()
    return imprime

#criar uma funcao que vai receber a decoradora
@master
def chama_funcao():
    print("esta esta chamando a funcao real")


##chamndo a funcao

chama_funcao()
