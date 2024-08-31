# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
frase = str(input('Digite o que desejar: ')).upper().strip()
if 'A' in frase:
    print(f'A letra A está dentro do seu texto e ela foi digitada {frase.count('A')} vezes ')
else:
    print('A letra A não foi digitada em seu texto')
print('Fim do programa!')
