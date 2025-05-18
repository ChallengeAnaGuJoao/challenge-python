pacientes = []
consultas = []
paciente_logado = None

# ------------------- FUNÇÕES DE PACIENTE -------------------

def cadastrar_paciente():
    print("\n[CADASTRO DE PACIENTE]")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    for paciente in pacientes:
        if paciente['email'] == email:
            print("Email já cadastrado!")
            return

    pacientes.append({
        'nome': nome,
        'email': email,
        'senha': senha
    })
    print("Paciente cadastrado com sucesso!")

def login():
    global paciente_logado
    print("\n[LOGIN]")
    email = input("Email: ")
    senha = input("Senha: ")

    for paciente in pacientes:
        if paciente['email'] == email and paciente['senha'] == senha:
            paciente_logado = paciente
            print(f"Login bem-sucedido! Bem-vindo(a), {paciente['nome']}.")
            return
    print("Email ou senha inválidos!")

def logout():
    global paciente_logado
    paciente_logado = None
    print("Logout realizado com sucesso.")

def listar_pacientes():
    print("\n[LISTA DE PACIENTES] - APENAS PARA PROVA DE CONCEITO - NAO FAZ SENTIDO NO NEGOCIO")
    for p in pacientes:
        print(f"- {p['nome']} ({p['email']})")

# ------------------- FUNÇÕES DE CONSULTA -------------------

def agendar_consulta():
    if not paciente_logado:
        print("Você precisa estar logado para agendar uma consulta.")
        return

    print("\n[AGENDAR CONSULTA]")
    data = input("Data (dd/mm/aaaa): ")
    hora = input("Hora (hh:mm): ")
    descricao = input("Descrição: ")

    consultas.append({
        'email': paciente_logado['email'],
        'data': data,
        'hora': hora,
        'descricao': descricao
    })
    print("Consulta agendada com sucesso!")

def listar_consultas_paciente():
    if not paciente_logado:
        print("Você precisa estar logado para ver suas consultas.")
        return

    print(f"\n[CONSULTAS DE {paciente_logado['nome']}]")
    consultas_paciente = [c for c in consultas if c['email'] == paciente_logado['email']]
    
    if not consultas_paciente:
        print("Nenhuma consulta encontrada.")
        return

    for c in consultas_paciente:
        print(f"- {c['data']} às {c['hora']}: {c['descricao']}")

def listar_todas_consultas():
    print("\n[TODAS AS CONSULTAS - APENAS PARA PROVA DE CONCEITO - NAO FAZ SENTIDO NO NEGOCIO]")
    for c in consultas:
        print(f"- {c['data']} {c['hora']} | {c['descricao']} (Paciente: {c['email']})")

# ------------------- MENU -------------------

def exibir_menu():
    print("\n" + "="*50)
    print(" SISTEMA DE CONSULTAS MÉDICAS ".center(50, "="))
    print("="*50)
    print("1. Cadastrar Paciente")
    print("2. Login")
    print("3. Logout")
    print("4. Listar Pacientes")
    print("5. Agendar Consulta")
    print("6. Ver Minhas Consultas")
    print("7. Ver Todas as Consultas")
    print("0. Sair")

def menu_principal():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            cadastrar_paciente()
        elif opcao == 2:
            login()
        elif opcao == 3:
            logout()
        elif opcao == 4:
            listar_pacientes()
        elif opcao == 5:
            agendar_consulta()
        elif opcao == 6:
            listar_consultas_paciente()
        elif opcao == 7:
            listar_todas_consultas()
        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# ------------------- EXECUÇÃO -------------------

menu_principal()
