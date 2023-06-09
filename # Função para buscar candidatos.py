# Função para buscar candidatos de acordo com os critérios digitados pelo usuário
def buscar_candidatos(resultados, criterios):
    candidatos_encontrados = []
    for resultado in resultados:
        notas = resultado.split('_')[1:]  # Ignora o "eX" no início do resultado
        notas_int = [int(nota[1:]) for nota in notas]  # Converte as notas para inteiros, ignorando o primeiro caractere "t", "p" ou "s"
        if all(nota >= criterio for nota, criterio in zip(notas_int, criterios)):
            candidatos_encontrados.append(resultado)
    return candidatos_encontrados

# Lista de resultados dos candidatos
resultados = ['e5_t10_p8_s9', 'e7_t9_p4_s5', 'e3_t8_p9_s7', 'e6_t7_p6_s8', 'e4_t5_p9_s6', 'e8_t6_p7_s9', 'e9_t4_p3_s5', 'e2_t2_p5_s6', 'e10_t10_p10_s10', 'e1_t1_p1_s2']

# Leitura dos critérios digitados pelo usuário com validação
notas_minimas = input("Digite as notas mínimas desejadas para (e t p s): ").split()

# Verifica se foram fornecidas 4 notas
if len(notas_minimas) != 4:
    print("Erro: É necessário fornecer 4 notas mínimas.")
    exit()

# Validação das notas mínimas para garantir que estejam dentro do intervalo válido
for nota in notas_minimas:
    if not nota.isdigit() or int(nota) < 0 or int(nota) > 10:
        print("Erro: As notas mínimas devem ser valores numéricos entre 0 e 10.")
        exit()

# Conversão das notas mínimas para inteiros
criterios = list(map(int, notas_minimas))

# Busca dos candidatos de acordo com os critérios
candidatos_encontrados = buscar_candidatos(resultados, criterios)

# Exibição dos candidatos encontrados
if len(candidatos_encontrados) > 0:
    print("Candidatos encontrados:")
    for candidato in candidatos_encontrados:
        print(candidato)
else:
    print("Nenhum candidato encontrado com as notas mínimas especificadas.")
 
