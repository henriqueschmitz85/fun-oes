def saudacao(**kwargs):
    print(kwargs)
#chamar a funcao
saudacao(manha='bom dia', tarde='boa tarde',noite = 'Boa Noite')

def saudacoes_dia(**kwargs):
    for turno,saudacao in kwargs.items():
        print(f'Durante a {turno} dizemos {saudacao}')

saudacoes_dia(manha='bom dia',tarde='boa tarde')



