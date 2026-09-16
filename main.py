#Cyber Pulse Tech

startups = {
    "nome":"Cyber Pulse Tech",
    "segmento":"Segurança da Informação",
    "ano_adesao":2026
}
soluções_ativas = ["Fire Wall IA","Scan de Vulerabilidades"]
print("STARTUP===", startups["nome"],"===")
print("Projeto em andamento",soluções_ativas[0])

#Bancadas de Trabalho

bancadas = [
    ["Bancada N1 ocupada","Bancada N2 Livre"],
    ["Bancada S1 Ocupada","Bancada S2 Livre"]
]
print("bancada N1:",bancadas[0][0])
print("bancada N2:",bancadas[0][1])
print("bancada S1:",bancadas[1][0])
print("bancada S2:",bancadas[1][1])

# Leitura dos custos em nuvem
with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_dados_1 = arquivo.readline()
    linha_dados_2 = arquivo.readline()
    linha_dados_3 = arquivo.readline()
    linha_dados_4 = arquivo.readline()

    print(cabecalho, end="")
    print(linha_dados_1, end="")
    print(linha_dados_2, end="")
    print(linha_dados_3, end="")
    print(linha_dados_4, end="")

# Consolidação da infraestrutura Cloud
nome_startup = startups["nome"]
bancada_alocada = bancadas[0][0].replace(" ocupada", "")

recurso_1, valor_1 = linha_dados_1.strip().split(",")
recurso_2, valor_2 = linha_dados_2.strip().split(",")
recurso_3, valor_3 = linha_dados_3.strip().split(",")
recurso_4, valor_4 = linha_dados_4.strip().split(",")

valor_1 = float(valor_1)
valor_2 = float(valor_2)
valor_3 = float(valor_3)
valor_4 = float(valor_4)
total = valor_1 + valor_2 + valor_3 + valor_4

print("\n===== PAINEL FINAL =====")
print(f"Nome da startup: {nome_startup}")
print(f"Bancada alocada: {bancada_alocada}")
print(f"Total da infraestrutura Cloud: R$ {total:.2f}")