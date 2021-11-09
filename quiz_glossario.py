from random import choice, shuffle

MAX_DEFS = 5

def importa_dados():
    with open('dados_glossario.txt', 'r') as arq:
        dados = arq.readlines()
    return dados

def gera_glossario(dados):
    glossario = {}
    linhas = map(str.strip, dados)
    for linha in linhas:
        if len(linha) == 0:
            pass
        elif len(linha) == 1:
            letra = linha[0]
            glossario[letra] = {}
        else:
            termo, definicao = map(str.strip, linha.split(':'))
            glossario[letra].update({termo: definicao})
    return glossario


def obtem_proximo_termo(glossario, letras_populadas):
    
    letra = choice(letras_populadas)
    mapa_termos_letra = tuple(enumerate(glossario[letra].keys()))
    id_termo = choice(range(len(mapa_termos_letra)))
    termo = mapa_termos_letra[id_termo][1]
    definicao = glossario[letra][termo]

    return letra, termo, definicao

def randomiza_lista(glossario):
    lista_unica_termos = \
        [(termo, glossario[letra][termo]) \
            for letra in [letra for letra in glossario] \
                for termo in glossario[letra]]

    shuffle(lista_unica_termos)

    return lista_unica_termos


dados = importa_dados()
glossario = gera_glossario(dados)
lista_termos_aleatorios = randomiza_lista(glossario)
definicoes_vistas = 0
definicoes_total = len(lista_termos_aleatorios)

for termo, definicao in lista_termos_aleatorios:
    # obtem proxima definicao
    letra = termo[0].upper()

    print(f'                                        {definicoes_vistas}/{definicoes_total}')
    print(f'--\n:: {letra} ::\n\n* * {termo} * *\n')

    wait = input('\nEnter para mostrar a definição..')
    print(f'\n>>>\n\t{definicao}')

    definicoes_vistas += 1
    
    op = input('\n\n? (0 p/ encerrar)')
    if op == '0':
        break
    
