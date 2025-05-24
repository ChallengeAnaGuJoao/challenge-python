from datetime import datetime

pacientes = []
consultas = []
paciente_logado = None

# ------------------- FUNÇÕES DE VALIDAÇÃO -------------------

def input_nome_valido():
    while True:
        nome = input("Nome: ").strip()
        if not nome:
            print("Nome não pode ser vazio.")
        elif nome.isdigit():
            print("Nome não pode conter apenas números.")
        else:
            return nome

def input_email_valido():
    while True:
        email = input("Email: ").strip()
        if not email or '@' not in email or '.' not in email:
            print("Email inválido. Exemplo válido: usuario@email.com")
        else:
            return email

def input_senha_valida():
    while True:
        senha = input("Senha: ").strip()
        if len(senha) < 4:
            print("A senha deve ter pelo menos 4 caracteres.")
        else:
            return senha

def input_data_valida():
    while True:
        data = input("Data (dd/mm/aaaa): ").strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")

def input_hora_valida():
    while True:
        hora = input("Hora (hh:mm): ").strip()
        try:
            datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            print("Hora inválida! Use o formato hh:mm.")

def input_texto_nao_vazio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if not texto:
            print("Este campo não pode ser vazio.")
        else:
            return texto

def buscar_paciente_por_email(email):
    for paciente in pacientes:
        if paciente['email'] == email:
            return paciente
    return None

# ------------------- FUNÇÕES DE PACIENTE -------------------

def cadastrar_paciente():
    print("\n[CADASTRO DE PACIENTE]")
    nome = input_nome_valido()
    email = input_email_valido()

    if buscar_paciente_por_email(email):
        print("Email já cadastrado!")
        return

    senha = input_senha_valida()

    pacientes.append({
        'nome': nome,
        'email': email,
        'senha': senha
    })
    print("Paciente cadastrado com sucesso!")

def login():
    global paciente_logado
    print("\n[LOGIN]")
    email = input_email_valido()
    senha = input_texto_nao_vazio("Senha: ")

    paciente = buscar_paciente_por_email(email)
    if paciente and paciente['senha'] == senha:
        paciente_logado = paciente
        print(f"Login bem-sucedido! Bem-vindo(a), {paciente['nome']}.")
    else:
        print("Email ou senha inválidos!")

def logout():
    global paciente_logado
    if paciente_logado:
        print(f"Logout de {paciente_logado['nome']} realizado com sucesso.")
        paciente_logado = None
    else:
        print("Você não está logado.")

#Apenas para demonstração, não está alinhado com a solução proposta
def listar_pacientes():
    print("\n[LISTA DE PACIENTES]")
    for p in pacientes:
        print(f"- {p['nome']} ({p['email']})")

# ------------------- FUNÇÕES DE CONSULTA -------------------

def agendar_consulta():
    if not paciente_logado:
        print("Você precisa estar logado para agendar uma consulta.")
        return

    print("\n[AGENDAR CONSULTA]")
    data = input_data_valida()
    hora = input_hora_valida()
    descricao = input_texto_nao_vazio("Descrição da consulta: ")

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

#Apenas para demonstração, não está alinhado com a solução proposta
def listar_todas_consultas():
    print("\n[TODAS AS CONSULTAS]")
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
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida!")

# Executa o sistema
menu_principal()
