import streamlit as st

def run():
    col1, col2, col3  = st.columns([1, 4, 1])

    # Exibir a imagem na coluna central e ajustar o tamanho
    with col2:
        st.markdown(
        """
        <style>
        .title-page {
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 18px;
            margin-bottom: 50px
        }
        .subtitle {
            font-size: 16px;
            font-weight: bold;
        }
        .authors {
            font-size: 16px;
            font-weight: bold;
        }
        .text {
            font-size: 16px;
            margin-top: 20px;
        }
        .university {
            font-size: 35px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .curso{
            font-size: 25px;
            font-weight: bold;
        }
        </style>
        <div class="title-page">
            <div class="university">Universidade Federal do Maranhão</div>
            <div class="curso">Engenharia da Computação</div>
            <div class="subtitle">Disciplina de Sistemas Distribuídos</div>
            <div class="authors">Orientador: Prof. Me. Luiz Herinque Neves Rodrigues</div>
            <div class="authors">Caio Reis</div>
            <div class="authors">Emanoel Silva</div>
            <div class="authors">Francisco Elias</div>
            <div class="authors">Leandro Lisboa</div>
            <div class="authors">Rosivânia Silva</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    .title {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px
    }
    </style>
    <h1 class='title'>PROJETO SMARTWEATHER</h1>
    """, unsafe_allow_html=True)

    # Texto justificado e centralizado
    st.markdown("""
    <div style="text-align: justify; text-justify: inter-word; margin-left: auto; margin-right: auto; width: 80%;">
        O projeto de estação meteorológica é uma iniciativa que visa facilitar a maneira como informações importantes
        são captadas e gerenciadas e como os dados podem ser manipulados para controlar um ambiente, por meio do desenvolvimento
        de um sensor inteligente que integra um microcontrolador, o qual envia os dados para uma página web, atualizando o status
        da pressão, temperatura, altitude e umidade. Dessa forma, busca-se obter um melhor controle dos ambientes. Neste projeto,
        exploraremos como a integração desses componentes pode criar uma solução inteligente e eficaz para beneficiar o cotidiano dos usuários.
        <br><br>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        ## Projeto de Estação Meteorológica

        O projeto de estação meteorológica é uma iniciativa que visa facilitar a maneira como informações importantes são captadas e gerenciadas e como os dados podem ser manipulados para controlar um ambiente, por meio do desenvolvimento de um sensor inteligente que integra um microcontrolador, o qual envia os dados para uma página web, atualizando o status da pressão, temperatura, altitude e umidade. Dessa forma, busca-se obter um melhor controle dos ambientes. Neste projeto, exploraremos como a integração desses componentes pode criar uma solução inteligente e eficaz para beneficiar o cotidiano dos usuários.

        ### Objetivos
        - Controle de temperatura automático;
        - Controle de pressão inteligente;
        - Coleta de dados valiosos para análise do ambiente;
        - Demonstrar como a integração de tecnologias como IoT podem ser aplicadas de forma prática e benéfica para resolver desafios cotidianos.

        ### Recursos do Projeto
        - **Microcontrolador**: ESP32 NodeMCU;
        - **Sensor**: BME280;
        - **Interface**: Página Web;
        - **Armazenamento e Análise**: Os dados serão armazenados na Web e resgatados com o Power BI para análise;
        - **Hardware Adicional**: Computadores, protoboard, jumpers são os recursos de hardware usados para desenvolver, testar e programar o ESP32.
        """
    )
