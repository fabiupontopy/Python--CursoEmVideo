palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON',
            'CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
            'MERCADO','PROGRAMADOR','FUTURO')
for c in palavras:
    print(f'\nA vogal da palavra "{c}" é: ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(f'{letra.lower()} ',end='')