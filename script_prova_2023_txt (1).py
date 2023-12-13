import pandas as pd


file_name = 'python-scriping/prova-2013.txt'
# Abrir o arquivo de TEXTO
with open(file_name, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

# Inicializar variáveis para armazenar as questões
questoes = []
questao_atual = None

# Loop pelas linhas do arquivo
for linha in linhas:
    linha = linha.strip()

    # Verificar se é uma linha de questão
    if linha.startswith("QUESTÃO"):
        if questao_atual:
            questoes.append(questao_atual)
        questao_atual = {"QUESTÃO": linha}
    else:
        if questao_atual:
            questao_atual["TEXTO"] = questao_atual.get("TEXTO", "") + linha

# Adicione a última questão à lista
if questao_atual:
    questoes.append(questao_atual)

# Converter a lista de questões em um DataFrame do pandas
df = pd.DataFrame(questoes)

# Salvar o DataFrame em um arquivo Excel
df.to_excel('questoestxt.xlsx', index=False)
