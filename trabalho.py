# A primeira coluna ("matricula") é composta por números inteiros, onde cada número representa um indivíduo. Assim, repetições nessa coluna indicam que o estudante fez mais de uma vez a mesma matéria.
# Atenção: R-nota indica REPROVAÇÃO POR NOTA e R-freq REPROVAÇÃO POR FALTA. Se houver outro "status" para representar reprovação, este dever ser trocado para o rótulo adequado (R-nota ou R-freq). Frequências < 75 causam reprovação por falta; Médias abaixo de 50 causam reprovação por nota.
# Analise o dataset do referido arquivo para responder as seguintes perguntas:

import pandas as pd
import sys

# Recebe o arquivo csv do primeiro argumento da chamada do programa
nome_arquivo = sys.argv[1]
df = pd.read_csv(nome_arquivo)

# Função para atualizar o status de Reprovado
def atualizar_status(row):
    if row['status'] == 'Reprovado':
        if row['frequencia'] < 75:
            return 'R-freq'
        elif row['nota'] < 50:
            return 'R-nota'
    return row['status']

# Aplicar a função à coluna 'status'
df['status'] = df.apply(atualizar_status, axis=1)

# Desconsidera alunos que obtiveram aprovação por equivalência
df = df[df['tipo'] != 'EQUIVALENCIA']

### 1. Qual é a média de nota dos aprovados (no período total e por ano)?

# Considera desempenho total mesmo que o aluno tenha cursado duas vezes no mesmo ano
media_total = df[(df['status'] == 'Aprovado')]['nota'].mean()
media_por_periodo = df[(df['status'] == 'Aprovado')][['ano', 'nota']].groupby(by='ano').mean().round(2)
print(f'1. Média da nota dos aprovados: {media_total:.2f}\n')
print(f'   Média da nota dos aprovados por ano: ')
print(media_por_periodo)

### 2. Qual é a média de nota dos reprovados por nota (período total e ano)?

# Filtra diretamente pelos alunos reprovados por nota
# Desempenho total mesmo que o aluno tenha cursado duas vezes no mesmo ano

media_r_nota_total = df[df['status'] == 'R-nota']['nota'].mean()
media_r_nota_periodo = df[df['status'] == 'R-nota'][['ano', 'nota']].groupby(by='ano').mean().round(2)
print(f'\n2. Média da nota dos reprovados por nota: {media_r_nota_total:.2f}\n')
print(f'   Média da nota dos reprovados por nota por ano: ')
print(media_r_nota_periodo)

### 3. Qual é a média de frequência dos reprovados por nota (período total e por ano)?

# Filtra diretamente pelos alunos reprovados por frequência
# Desempenho total mesmo que o aluno tenha cursado duas vezes no mesmo ano

media_r_freq = df[df['status'] == 'R-freq']['frequencia'].mean()
media_r_freq_periodo = df[df['status'] == 'R-freq'][['ano', 'frequencia']].groupby(by='ano').mean().round(2)
print(f'\n3. Média da nota dos reprovados por frequência: {media_r_freq:.2f}\n')
print(f'   Média da nota dos reprovados por frequência por ano: ')
print(media_r_freq_periodo)

### 4. Qual a porcentagem de evasões (total e anual)?

# Ordena o DataFrame pela coluna 'ano' em ordem decrescente para cada aluno e
# mantém apenas o registro mais recente (maior ano) para cada aluno 
# pois a evasão aparece em todas as vezes que o aluno cursou a matéria
df_evad = df.sort_values(by=['matricula', 'ano'], ascending=[True, False]).drop_duplicates(subset='matricula', keep='first')
total_alunos = len(df_evad['matricula'])
num_evasoes_total = len(df_evad[df_evad['situacaoDiscente'] == 'Evasão'])
porcentagem_evasoes_total = (num_evasoes_total / total_alunos) * 100

# Agrupa por ano e conta o número de alunos que evadiram em cada ano
evasoes_por_ano = df_evad[df_evad['situacaoDiscente'] == 'Evasão'].groupby('ano').size()
total_alunos_por_ano = df_evad.groupby('ano').size()
porcentagem_evasao_por_ano = ((evasoes_por_ano / total_alunos_por_ano) * 100).round(2)
porcentagem_evasao_por_ano.fillna(0, inplace=True)

# Exibir em formato de tabela com porcentagem
df_porcentagem_evasao = pd.DataFrame(porcentagem_evasao_por_ano, columns=['Porcentagem de Evasão'])
df_4 = df_porcentagem_evasao.applymap(lambda x: f'{x:.2f}%')
print(f'\n4. Porcentagem de evasão: {porcentagem_evasoes_total:.2f}%\n')
print(f'   Porcentagem de evasão por ano: ')
print(df_4)

### 5. Como os anos de pandemia impactaram no rendimento dos estudantes em relação aos anos anteriores, 
### considerando o rendimento dos aprovados, a taxa de cancelamento e as reprovações? Considere como 
### anos de pandemia os anos de 2020 e 2021.

# DataFrame dos anos de pandemia e dos anos anteriores
dados_pandemia = df[df['ano'].isin([2020, 2021])]
dados_anteriores = df[~df['ano'].isin([2020, 2021, 2022])]

#Função genérica para cálculo de estatísticas
def calcular_estatisticas(dados, nomeIndex):
    total_alunos = len(dados)
    aprovados = len(dados[dados['status'] == 'Aprovado'])
    reprovados = len(dados[dados['status'].str.startswith('R-')])
    cancelamentos = len(dados[dados['status'] == 'Cancelado'])

    # Calcular taxas de aprovação, reprovação e cancelamento
    taxa_aprovacao = (aprovados / total_alunos) * 100
    taxa_reprovacao = (reprovados / total_alunos) * 100
    taxa_cancelamento = (cancelamentos / total_alunos) * 100

    data =  {
        'Total de Alunos': total_alunos,
        'Aprovados': aprovados,
        'Reprovados': reprovados,
        'Cancelamentos': cancelamentos,
        'Taxa de Aprovação': f"{taxa_aprovacao:.2f}%",
        'Taxa de Reprovação': f"{taxa_reprovacao:.2f}%",
        'Taxa de Cancelamento': f"{taxa_cancelamento:.2f}%"
    }

    df_estatisticas = pd.DataFrame(data, index=nomeIndex)

    return df_estatisticas

df_pandemia = calcular_estatisticas(dados_pandemia, ['Pandemia'])
df_anteriores = calcular_estatisticas(dados_anteriores,['Anos Anteriores'])
df_5 = pd.concat([df_pandemia, df_anteriores])

# Exibir o DataFrame de comparação em formato de tabela
print('\n5. Comparação de Rendimento entre Pandemia e Anos Anteriores:')
print(df_5)

### 6. Compare a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores.

# Dados do período híbrido de 2022
dados_hibrido_2022 = df[(df['ano'] == 2022) & (df['periodo'] == '1')]
df_hibrido_2022 = calcular_estatisticas(dados_hibrido_2022, ['Volta às Aulas Híbrida (2022/1)'])
df_6 = pd.concat([df_5, df_hibrido_2022])
print('\n6. Comparação a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores: ')
print(df_6)

### 7. Compare a volta às aulas presencial (2022 período 2) com a volta híbrida do item anterior. 

# Dados do período presencial de 2022
dados_presencial_2022 = df[(df['ano'] == 2022) & (df['periodo'] == '2')]

# Fazendo as contas apenas para formalizar, porém como todos os alunos ainda estão apenas matrículados, não há como comparar desempenho algum
df_presencial_2022 = calcular_estatisticas(dados_presencial_2022, ['Volta às Aulas Presencial (2022/2)'])
df_7 = pd.concat([df_hibrido_2022, df_presencial_2022])
print('\n7. Comparação entre a volta às aulas presencial (2022 período 2) com a volta híbrida:')
print(df_7)