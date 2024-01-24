# funcao filter filtra elementos de ums estrutura de dados

listamista = [1,"joao","Pedro",53]

def busca(x):
    return x == "joao"

print(list(filter(busca,listamista)))

print(list(filter(lambda x:x=="Pedro",listamista)))