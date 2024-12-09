def verificar_numero(numero):
    # Verifica se o número é par ou ímpar
    par = numero % 2 == 0  # Retorna True se for par, False se for ímpar
    
    # Verifica se o número está no intervalo de 10 a 50
    dentro_intervalo = 10 <= numero <= 50  # Retorna True se estiver no intervalo, False caso contrário
    
    # Retorna as avaliações
    return par, dentro_intervalo

# Exemplo de uso
numero = int(input("Digite um número: "))
eh_par, no_intervalo = verificar_numero(numero)

print(f"O número é {'par' if eh_par else 'ímpar'}.")
print(f"O número está {'dentro' if no_intervalo else 'fora'} do intervalo de 10 a 50.")
