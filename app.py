import streamlit as st
from datetime import datetime

st.set_page_config(page_title='Meu Site', page_icon='🌐', layout='wide')

st.title('🌐 Bem-vindo ao meu site!')
st.write('Este site foi criado inteiramente em Python com Streamlit.')
st.write(f'📅 Data atual: **{datetime.now().strftime("%d/%m/%Y %H:%M")}**')

st.divider()

menu = st.sidebar.selectbox(
    'Navegue pelo site:',
    ['🏠 Início', '📖 Sobre', '📞 Contato', '🧮 Calculadora'],
)

if menu == '🏠 Início':
    st.header('Página Inicial')
    st.write('Bem-vindo ao meu site pessoal!')
    col1, col2, col3 = st.columns(3)
    col1.metric('Visitas', '1.234')
    col2.metric('Projetos', '12')
    col3.metric('Anos de experiência', '5')
    st.image('https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1200', caption='Bem-vindo!', use_column_width=True)

elif menu == '📖 Sobre':
    st.header('Sobre mim')
    st.write('Olá! Sou Mattheus, engenheiro e entusiasta de Python.')
    st.write('Trabalho com planilhas, engenharia civil e automação com Python.')

elif menu == '📞 Contato':
    st.header('Fale comigo')
    with st.form('form_contato'):
        nome = st.text_input('Seu nome')
        email = st.text_input('Seu email')
        mensagem = st.text_area('Mensagem')
        enviar = st.form_submit_button('Enviar')
        if enviar:
            st.success(f'Obrigado, {nome}! Sua mensagem foi recebida.')

elif menu == '🧮 Calculadora':
    st.header('Calculadora Simples')
    a = st.number_input('Primeiro número', value=0.0)
    b = st.number_input('Segundo número', value=0.0)
    operacao = st.selectbox('Operação', ['+', '-', '×', '÷'])
    if st.button('Calcular'):
        if operacao == '+':
            resultado = a + b
        elif operacao == '-':
            resultado = a - b
        elif operacao == '×':
            resultado = a * b
        elif operacao == '÷':
            resultado = a / b if b != 0 else 'Erro: divisão por zero'
        st.success(f'📊 Resultado: **{resultado}**')

st.divider()
st.caption('© 2026 — Site feito em Python')
