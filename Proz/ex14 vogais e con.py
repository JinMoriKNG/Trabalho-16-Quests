print('-'*10, 'VOGAIS E CONSOANTES', '-'*10)

letra = input('Digite uma letra para verificação: ').strip().upper()

if letra in 'AEIOU':
    print('Essa letra é uma VOGAL.')
else:
    print('Essa letra é uma CONSOANTE')
