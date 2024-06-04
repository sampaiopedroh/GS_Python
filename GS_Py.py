# Define o tamanho do rio
largura_rio = int(input('Diga a largura do rio:\n-> '))
comprimento_rio = int(input('Diga o comprimento do rio:\n-> '))

# Cria uma lista representando o rio (água limpa)
rio = [['.' for _ in range(largura_rio)] for _ in range(comprimento_rio)]

# Define a posição inicial do óleo
pos_x = largura_rio // 2  # Meio da largura
pos_y = comprimento_rio // 2  # Meio do comprimento

# Lista para armazenar as posições do óleo
posicoes_oleo = [(pos_x, pos_y)]

# Define a taxa de dispersão (opcional)
taxa_dispersao = float('Diga a taxa de dispersão:\n-> ')


# Função para atualizar as posições do óleo
def espalhar_oleo(rio, posicoes_oleo):
    novas_posicoes = []
    for pos_x, pos_y in posicoes_oleo:
        # Verifica se as posições adjacentes são água limpa
        if pos_y + 1 < comprimento_rio and rio[pos_y + 1][pos_x] == '.':
            rio[pos_y + 1][pos_x] = '#'
            novas_posicoes.append((pos_x, pos_y + 1))
        if pos_y - 1 >= 0 and rio[pos_y - 1][pos_x] == '.':
            rio[pos_y - 1][pos_x] = '#'
            novas_posicoes.append((pos_x, pos_y - 1))
        if pos_x + 1 < largura_rio and rio[pos_y][pos_x + 1] == '.':
            rio[pos_y][pos_x + 1] = '#'
            novas_posicoes.append((pos_x + 1, pos_y))
        if pos_x - 1 >= 0 and rio[pos_y][pos_x - 1] == '.':
            rio[pos_y][pos_x - 1] = '#'
            novas_posicoes.append((pos_x - 1, pos_y))
    return novas_posicoes


# Loop principal da simulação
tempo = 0
while tempo < 8:  # Simula por 10 unidades de tempo
    # Espalha o óleo
    posicoes_oleo = espalhar_oleo(rio, posicoes_oleo)

    # Aplicar dispersão (opcional)
    # ... (implementar código para reduzir a quantidade de óleo)

    # Imprime o estado do rio
    print(f"Tempo: {tempo}")
    for linha in rio:
        print(''.join(linha))
    print()

    tempo += 1