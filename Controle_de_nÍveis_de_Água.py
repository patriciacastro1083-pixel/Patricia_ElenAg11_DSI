# Controle de Níveis de Água

print("Controle de Níveis de Água")

from colorama import Fore, Style

# Lista de níveis de água
nivel_água = [1, 2, 3, 4, 5]

# Função que define a cor e a mensagem

def verificar_nivel(nivel):
    if nivel == 1:
     print(Fore.RED + "Nivel 1 Muito baixo (crítico)")
    elif nivel == 2:
        print(Fore.YELLOW + "Nivel 2 Baixo")
    elif nivel == 3:
        print(Fore.GREEN + "Nivel 3 Médio")
    elif nivel == 4:
        print(Fore.CYAN + "Nivel 4 Alto")
    elif nivel == 5:
        print(Fore.BLUE + "Nivel 5 Muito alto (alerta)")

    # Exibe todos os níveis de água

for nivel in nivel_água:
    verificar_nivel(nivel)

# Restaura a cor padrão
print(Style.RESET_ALL)
