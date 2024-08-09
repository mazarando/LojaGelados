print('Bem-vindo(a) a Loja de Gelados da Millenna Mazaro')
print('-' * 20 + 'Cardápio'+ '-' *20)
print('-'*48)
print('---|  Tamanho  |  Cupuaçu (CP) |  Açaí (AC) |---')
print('---|     P     |    R$  9.00   |  R$ 11.00  |---')
print('---|     M     |    R$ 14.00   |  R$ 16.00  |---')
print('---|     G     |    R$ 18.00   |  R$ 20.00  |---')
print('-'*48)

total_pedido = 0 #acumulador

while True:
    sabor = input('Escolha o sabor (CP para Cupuaçu ou AC para Açai): ').upper()

    if sabor not in ['CP', 'AC']:
        print('Sabor Inválido. Tente novamente.')
        continue

    tamanho = input('Escolha o tamanho (P, M ou G): ').upper() #Caso o usuario escreva em minusculo

    if tamanho not in ['P', 'M', 'G']: #implementei caso o usuario não escolha uma das opções
        print('Tamanho Inválido. Tente novamente.')
        continue

    if sabor == 'CP': # Cupuaçu
        if tamanho == 'P' or tamanho == 'p':
            preco = 9
        elif tamanho == 'M' or tamanho == 'm':
            preco = 14
        else:
            preço = 18
    else: # Açai
        if tamanho == 'P' or tamanho == 'p':
            preco = 11
        elif tamanho =='M' or tamanho == 'm':
            preco = 16
        else:
            preco = 20

    total_pedido += preco #soma do total + preço
    deseja = input('Deseja mais alguma coisa? (sim ou não): ').upper() #Caso o cliente queira pedir mais uma vez
    if deseja == 'NÃO' or deseja == 'NAO':
        print(f'O total do seu pedido ficou: R$ {total_pedido}.\nObrigada por comprar com a gente! :)') #finalizando o pedido
        break