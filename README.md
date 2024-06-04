# GS_Python - Simulador de Derramamento de Óleo em um Rio
Este programa simula a propagação de um derramamento de óleo em um rio, usando uma representação textual. Você pode modificar os parâmetros para explorar diferentes cenários.

-> Instruções de Uso:
- Executar o código: Salve o código em um arquivo chamado sim_oleo.py (ou qualquer nome desejado) e execute-o em um interpretador Python.
- Observar a simulação: O programa irá imprimir a visualização do rio a cada passo, mostrando a dispersão do óleo.
- Modificar os parâmetros: Altere as variáveis no início do código para personalizar a simulação:
  - largura_rio: Largura do rio (em unidades).
  - comprimento_rio: Comprimento do rio (em unidades).
  - pos_x: Posição horizontal inicial do óleo (em unidades).
  - pos_y: Posição vertical inicial do óleo (em unidades).
  - taxa_dispersao: A taxa de dispersão do óleo (entre 0 e 1, sendo 0.1 equivalente a 10% de dispersão a cada passo).

-> Requisitos:
- Python: O código foi escrito em Python. Certifique-se de ter o Python instalado em seu sistema.

-> Dependências:
- Nenhuma dependência adicional é necessária.

-> Detalhes do Projeto:
- Representação do Rio: O rio é representado por uma lista de listas (matriz) onde cada elemento é um caractere:
- "." representa a água limpa.
- "#" representa o óleo.
- Propagação do Óleo: A cada iteração, o óleo se espalha para as posições adjacentes (acima, abaixo, esquerda, direita) que ainda estiverem limpas.
- Taxa de Dispersão: O parâmetro taxa_dispersao controla a quantidade de óleo que desaparece a cada passo, simulando a dispersão natural do óleo.
- Visualização: O programa imprime a matriz do rio no console, mostrando a propagação do óleo.

-> Aprimoramentos Possíveis:
- Correnteza: Simular a influência da correnteza na propagação do óleo.
- Visualização Gráfica: Criar uma visualização gráfica mais interessante usando bibliotecas como Matplotlib.
- Interação do Usuário: Adicionar a possibilidade do usuário interagir com o programa, definindo parâmetros durante a execução.
- Fatores Ambientais: Incluir outros fatores como vento, ondas e margens do rio.
