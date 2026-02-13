clientes = []
agendamentos = []

def cadastrar_cliente(nome, telefone, placa, modelo) :

    for c in clientes:
        if c["placa"].lower() == placa.lower():
            return "Já existe cliente com essa placa"
        
    cliente = {
        "nome" : nome,
        "telefone" : telefone,
        "placa" : placa,
        "modelo" : modelo
    }
    clientes.append(cliente)
    return " Cliente cadastrado com sucesso "


def listar_clientes():
    return clientes

def agendar_servico(cliente_nome, servico, data):
    data = data.strftime("%d/%m/%y")

    agendamento = {
        "cliente" : cliente_nome,
        "servico" : servico,
        "data" : data

    }
    agendamentos.append(agendamento)
    return " Serviço agendado com sucesso "

def listar_agendamentos():
    return agendamentos