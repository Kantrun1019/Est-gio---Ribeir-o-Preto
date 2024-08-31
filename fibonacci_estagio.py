# 1 - Crie um programa que mostre a sequencia de Fibonacci, leia um número e reporte a mensagem se esse número está na sequencia ou não

# - Criando a sequencia de Fibonacci:
#Os primeiros três termos sempre são os mesmos, logo serão definidos nas variaveis t1 (termo 1) e t2 (termo 2) e t3 (termo 3)
t1 = 0 
t2 = 1
t3 = 1
# Criamos uma lista para inserir os termos para Fibonacci e apontar em qual posição estará o número escolhido
fibo = [t1, t2]
n = int(input('Digite o número que deseja encontrar na sequencia de Fibonacci: ')) #entrada para o número que queremos verificar
while t3 != n: #Laço para determinar quantos itens iremos adicionar a nossa lista antes de mostrar o resultado.
    t3 = t1 + t2
    fibo.append(t3)
    t1 = t2
    t2 = t3
    if t3 == n:
        print(f'O número {n} pertence a sequencia de fibonacci e é o {fibo.index(t3)+1}º termo dessa seqûencia.')
        print(f'Essa é a sequência correta até o seu número: {fibo}')
        break
    elif n < 1:
        print(f'Os números 1 e 0 são os três primeiros termos de Fibonacci: {fibo}')
        break
    elif t3 > n:
        print(f'O número {n} não pertence a sequencia de Fibonacci')
        print(f'Essa é a sequência correta até o seu número: {fibo}')
        break
print('Fim do Programa!')
