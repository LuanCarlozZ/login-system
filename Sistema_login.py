
# Sistema simples de login com menu

# Sistema simples de login com menu

while True:
    print('\n=== MENU ===')
    print('1 - Login')
    print('2 - Sair')

    opcao = input('Escolha uma opção: ').strip()

    if opcao == '1':
        usuario = ''
        senha = ''
        tentativas = 0
        limite = 3

        while tentativas < limite:
            usuario = input('Digite o usuário: ').strip().lower()
            senha = input('Digite a senha: ').strip().lower()

            if usuario == 'admin' and senha == '2345':
                break

            if usuario != 'admin':
                print('❌ Usuário não encontrado!')
            elif senha != '2345':
                print('❌ Senha incorreta!')

            tentativas += 1
            restantes = limite - tentativas

            if restantes > 0:
                print(f'🔁 Tentativas restantes: {restantes}')

        if usuario == 'admin' and senha == '2345':
            print('✅ Acesso liberado!')
        else:
            print('🔒 Acesso bloqueado!')

        break

    elif opcao == '2':
        print('Saindo do programa...')
        break

    else:
        print('⚠️ Opção inválida!')