import requests
import streamlit as st
#from streamlit_lottie import st_lottie


# Configurações da página
st.set_page_config(
    page_title='Meu Portifólio',
    page_icon='👨‍💻',
    layout='wide'
)


#def load_lottieurl(url):
    #r = requests.get(url)
    #if r.status_code != 200:
     #   return None
    #return r.json()


#Animação
#lottie_coding = load_lottieurl("https://lottie.host/13824666-a8c2-4771-96d2-abc06cb22500/SrCBaTi5GI.json")


#Cabeçalho
with st.container():
    st.subheader('Olá, Meu nome é Matheus Tonini :wave:')
    st.title('Bem-vindo ao meu portifólio, navegue com moderação. ⌨️🤖')
    st.write('Tenho 21 anos, sou do Brasil e no momento estou estudando Análise e Desenvolvimento de Sistemas na FATEC-SP. Sou um entusiasta por tecnologia principalmente com a linguagem de programção Python para Manipular dados, Desenvolver indicadores e criar sistemas de RPA (Robotic Process Automation).')
    st.write('Alguns dos meus projetos estão postados no meu GitHub. Acesse o link abaixo.')
    st.write('[<Meu github>](https://github.com/ztonini0)')


#Container Experiencia Profissional
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Experiência profissional")
        st.subheader('Votorantim Cimentos')
        st.write('Outubro de 2022 - o momento - 1 ano 1 mês')
        st.write(
             """
            Algumas das minhas atividades do dia-dia:
            - Gestão, Análise e Governança dos KPI'S de Operções Logísticas (TMAC).
            - Suporte as áreas de interface (Cimentos, Argamassa, Agregados, Viter).
            - Desenvolvimento de relatórios logísticos e otimização de processos.
            - Atuação como PMO em projetos estratégicos da área de Logísticas.
            
            Para impactos positivos, entender como funciona todo o fluxo dos KPIS para implementar
            um sistema RPA por conta de ser uma tarefa repetitiva no dia-dia obtendo ganhos de produtivdade.
            
           
            """
        )
        st.subheader('Almaria Plus Size')
        st.write('Março de 2022 - agosto de 2022 - 6 meses')
        st.write(
             """
            Descrição das minhas atividades:
            - Desenvolvimento de relatório de mercadorias expedidas (fluxo operacional completo).
            - Desenvolvimento e atualização de relatório de mercadorias entregues (fluxo transportadora).
            - Atualização de relatório de quebras de estoque.
            - Desenvolvimento de relatório de motivos de contatos SAC.
            - Levantamento de processos operacionais. 
            

            """
        )         
    #with right_column:
        #st_lottie(lottie_coding, height=400, key="coding")
        
#Container Projetos

with st.container():
    st.write('---')
    st.header('Meus Projetos')
    st.subheader('Projeto API - Moedas Comemorativas')
    st.write(
             """
            Projeto criado para integrar uma API (Interface de Programação de Aplicação) do Banco Central do Brasil e realizar algumas consultas.

No projeto também foram aplicadas algumas funcionalidades para filtrar o ano, mês e tipo da categoria da moeda comemorativa e conforme é selecionado os gráficos e os indicadores são alterados. Com o python e pandas foi possível manipular os dados e criar os indicadores com algumas operações simples
            """
        ) 
    st.subheader('Projeto Relatório de Vendas - Análise de Dados')
    st.write(
             """
               Projeto construído para analisar os dados em cima da base de dados do excel e enviar um relatório por email e via sms também.

               Para extrair das demais lojas o faturamento total de cada uma, quantidade e ticket-médio.
            """
        )   
    st.subheader('Projeto RPA com Power BI')
    st.write(
             """
            Desenvolvi uma projeto em cima de uma necessidade que tinhamos sobre ser mais produtivo e 
            não tomar tanto tempo. Nisso apliquei alguns conhecimentos com Python e utilizei o Selenium que é 
            uma biblioteca de RPA que ajuda na automação web. O script era um robõ que acessava com as 
            crendencias o Qlik Sense e buscava o conjunto de dados e baixava, feito isso atualizava as pastas 
            na nuvem e o Power Bi era alimentando atráves dessas bases
            """
        )