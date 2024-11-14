'''
Projeto Locadora de Veiculos
'''

def exibir_portfolio():
    '''Função que exibe os carros que a locadora possui'''
    print("Lista de Carros")
    for carro in carros_disponiveis:
        print(f"ID: {carro['id']} | Marca: {carro['marca']} | Modelo: {carro['modelo']} | Preço: R${carro['preco']:.2f} \n")

def alugar_carro():
    '''Função que reserva e calcula o aluguel do carro de acordo com os dias informados'''
    exibir_carros_disponiveis()
    try:
        id_selecionado = int(input("Digite o ID do carro que deseja selecionar: "))
    except ValueError:
        print("Erro: ID inválido. Por favor, insira um número.")
        return

    carro_selecionado = None
    for carro in carros_disponiveis:
        if carro['id'] == id_selecionado:
            carro_selecionado = carro
            break
    
    if carro_selecionado:
        print(f"Carro selecionado: {carro_selecionado['marca']} {carro_selecionado['modelo']}")
        try:
            quantidade_dias_alugados = int(input('Digite a quantidade de dias que deseja alugar: '))
            if quantidade_dias_alugados <= 0:
                print("A quantidade de dias deve ser maior que zero.")
                return
        except ValueError:
            print("Erro: número de dias inválido. Por favor, insira um número.")
            return

        valor_final = carro_selecionado['preco'] * quantidade_dias_alugados
        print(f'O valor final do aluguel é de R${valor_final:.2f}')
        
        carros_alugados.append(carro_selecionado)
        carros_disponiveis.remove(carro_selecionado)
    else:
        print("ID não encontrado! Tente novamente.")

def devolver_carro():
    '''Função que devolve um carro à locadora'''
    exibir_carros_alugados()
    try:
        id_selecionado = int(input("Digite o ID do carro que deseja devolver: "))
    except ValueError:
        print("Erro: ID inválido. Por favor, insira um número.")
        return

    carro_selecionado = None
    for carro in carros_alugados:
        if carro['id'] == id_selecionado:
            carro_selecionado = carro
            break
    
    if carro_selecionado:
        carros_alugados.remove(carro_selecionado)
        carros_disponiveis.append(carro_selecionado)
        print(f"Carro {carro_selecionado['marca']} {carro_selecionado['modelo']} devolvido com sucesso.")
    else:
        print("ID não encontrado! Tente novamente.")

def exibir_carros_disponiveis():
    '''Função que exibe os carros disponíveis para locação'''
    print("Lista de Carros Disponíveis")
    if not carros_disponiveis:
        print("Nenhum carro disponível no momento.")
    else:
        for carro in carros_disponiveis:
            print(f"ID: {carro['id']} | Marca: {carro['marca']} | Modelo: {carro['modelo']} | Preço: R${carro['preco']:.2f} \n")

def exibir_carros_alugados():
    '''Função que exibe os carros alugados'''
    print("Lista de Carros Alugados")
    if not carros_alugados:
        print("Nenhum carro alugado no momento.")
    else:
        for carro in carros_alugados:
            print(f"ID: {carro['id']} | Marca: {carro['marca']} | Modelo: {carro['modelo']} | Preço: R${carro['preco']:.2f} \n")

# Listas iniciais de carros disponíveis e alugados
carros_disponiveis = [
    {'id': 0, 'marca': 'Toyota', 'modelo': 'Corolla', 'preco': 120},
    {'id': 1, 'marca': 'Fiat', 'modelo': 'Fastback', 'preco': 180},
    {'id': 2, 'marca': 'Honda', 'modelo': 'Civic', 'preco': 230},
    {'id': 3, 'marca': 'Ford', 'modelo': 'Mustang', 'preco': 550},
    {'id': 4, 'marca': 'BMW', 'modelo': 'X1', 'preco': 380},
    {'id': 5, 'marca': 'Mercedes', 'modelo': 'Classe C', 'preco': 350}
]
carros_alugados = []

# Loop principal do menu
while True:
    print(''' 
        BEM-VINDO À LOCADORA DE CARROS
        Selecione uma opção:
        0 - Mostrar o portfólio  |  1 - Alugar um carro  |  2 - Devolver um carro  |  3 - Sair
    ''')

    try:
        opcao_menu = int(input('Escolha uma opção: '))
    except ValueError:
        print("Erro: opção inválida. Por favor, insira um número.")
        continue

    if opcao_menu == 0:
        exibir_portfolio()
    elif opcao_menu == 1:
        alugar_carro()
    elif opcao_menu == 2:
        devolver_carro()
    elif opcao_menu == 3:
        print("Saindo do sistema. Obrigado por usar a locadora!")
        break
    else:
        print('Opção inválida! Por favor, selecione uma opção válida.')
