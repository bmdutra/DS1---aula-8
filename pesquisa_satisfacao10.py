# Pesquisa de Satisfação — Empresa TudoWeb
# ======================================================

qtde_excelente = 0
qtde_ruim = 0
total_entrevistados = 10  # Definido pela empresa

print("=" * 10)
print("      PESQUISA DE SATISFAÇÃO — ATENDIMENTO")
print("         Empresa TudoWeb")
print("=" * 10)
print("Opções de avaliação:")
print("   1 → EXCELENTE")
print("   2 → BOM")
print("   3 → RUIM")
print("=" * 10)

# Laço de repetição 
for entrevistado in range(1, total_entrevistados + 1):
    print(f"\n--- Entrevistado {entrevistado} de {total_entrevistados} ---")
    
    # Coleta de dados
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    # Validação da opinião
    while True:
        opiniao = input(f"{nome}, qual sua avaliação do atendimento? (1/2/3): ")
        if opiniao in ["1", "2", "3"]:
            opiniao = int(opiniao)
            break
        print("Opção inválida! Digite 1, 2 ou 3.")
    
    # Classificação com estrutura de decisão
    if opiniao == 1:
        avaliacao = "EXCELENTE"
        qtde_excelente += 1
    elif opiniao == 2:
        avaliacao = "BOM"
    elif opiniao == 3:
        avaliacao = "RUIM"
        qtde_ruim += 1
    
    print(f"Obrigado(a), {nome}! Sua avaliação foi: {avaliacao}")

# Exibição dos resultados finais
print("\n" + "=" * 10)
print("          RESULTADO FINAL DA PESQUISA")
print("=" * 10)
print(f"Total de entrevistados: {total_entrevistados}")
print(f"a) Quantidade de respostas EXCELENTE: {qtde_excelente}")
print(f"b) Quantidade de respostas RUIM: {qtde_ruim}")
print("=" * 10)