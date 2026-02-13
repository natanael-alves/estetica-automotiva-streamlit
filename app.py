import streamlit as st
import funcoes
import datetime


st.title("🚘 Sistema de Estética Automotiva ")

opcao = st.sidebar.selectbox(
    "MENU",
    [
        "Cadastrar Cliente",
        "Listar Clientes",
        "Agendar Serviço",
        "Ver Agendamentos"
    ]
)

if opcao == "Cadastrar Cliente": 
    st.header("Novo Cliente")

    with st.form("form_cliente", clear_on_submit=True):

        nome = st.text_input("Nome", autocomplete="off")
        telefone = st.text_input("Telefone", autocomplete="off")
        placa = st.text_input("Placa", autocomplete="off")
        modelo = st.text_input("Modelo",autocomplete="off")

        submitted = st.form_submit_button("Cadastrar")

        if submitted:

            if not nome or not telefone or not placa or not modelo: 
                st.error("Preencha todos os campos !")
            else:
                msg = funcoes.cadastrar_cliente(nome, telefone, placa, modelo)
                st.toast("Cliente cadastrado com sucesso ✅")


elif opcao == "Listar Clientes": 

    clientes = funcoes.listar_clientes()
    if clientes:
        st.table(clientes)

    else:
        st.info("Nenhum cliente cadastrado")
    
elif opcao == "Agendar Serviço":
    st.header("Novo Agendamento")

    with st.form("form_agendamento", clear_on_submit=True):

        cliente = st.text_input("Nome do Cliente", autocomplete="off")
        servico = st.selectbox(
        "servico",
        ["Lavagem simples", "Lavagem completa", "Polimento", "Higienização", "Vetrificação"]
    )
        data = st.date_input("Data", format="DD/MM/YYYY")
        submitted = st.form_submit_button("Agendar")

        if submitted:
            if not cliente:
                st.error("Informe o cliente")
            elif data < datetime.date.today():
                st.error("Data não pode ser no passado")

            else: 
                msg = funcoes.agendar_servico(cliente, servico, data)
                st.success(msg)


elif opcao == "Ver Agendamentos":
    agendamentos = funcoes.listar_agendamentos()

    if agendamentos:
        st.table(agendamentos)
    else:
        st.info("Nenhum agendamento ainda")