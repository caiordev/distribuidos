import streamlit as st
import pandas as pd
import numpy as np
import pytz
from datetime import datetime
from datetime import date
from PIL import Image
from get_weather import *
from streamlit_autorefresh import st_autorefresh


def run():

    # Estilização com HTML e CSS para criar cards
    st_autorefresh(interval=10000, key="data_refresh")
    
    st.markdown("""
    <style>
    body {
            background-color: #2B3E50; /* Fundo escuro */
            color: white;
        }
    /* Estilo do container principal dos cards */
    .card-container {
        display: flex;
        flex-wrap: wrap;
        margin-bottom: 50px;
        gap: 24px;
        justify-content: center;
    }

    /* Estilo individual dos cards */
    .card {
        background-color: #36454F; /* Fundo do card */
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); /* Sombra */
        padding: 20px;
        text-align: center;
        width: 400px;
        color: white;
    }

    .card h3 {
        font-size: 18px;
        color: #B0C4DE;
        margin-bottom: 8px;
    }
    
    .card p {
        font-size: 24px;
        font-weight: bold;
        color: #66CDAA;
        margin: 0;
    }
    .card small {
        font-size: 14px;
        color: red;
    }
    </style>
    """, unsafe_allow_html=True)


    st.title("TEMPO EM TODA REGIÃO")

    #Time
    nowTime = datetime.now()
    
    today = str(date.today())
    def horario():
        current_time = nowTime.strftime("%H:%M")
        return current_time
    # st.write(today)
    timeMetric,= st.columns(1)
    timeMetric.metric("",today)

    # Row A
    a1, a2, a3 = st.columns(3)
   
    with a1:
        st.markdown("""
        <div class="card-container">
            <div class="card">
                <h3>🌡️ Temperatura Atual</h3>
                <p>{temp}</p>
            </div>
        </div>
        """.format(
                temp=get_temp()
            ), unsafe_allow_html=True)

    with a2:
        st.markdown("""
        <div class="card-container">
            <div class="card">
                <h3>🔥 Variação da Temperatura</h3>
                <p>{temp_diff}</p>
            </div>
        </div>
        """.format(
                temp_diff=temp_difference(arg1(), arg2(), arg3()),
            ), unsafe_allow_html=True)

    with a3:
        st.markdown("""
        <div class="card-container">
            <div class="card">
                <h3>🕒 Horário</h3>
                <p>{horario}</p>
            </div>
        </div>
        """.format(
                horario = horario()
            ), unsafe_allow_html=True)

    # Row B
    b1, b2, b3, b4 = st.columns(4)

    with b1:
        st.markdown("""
        <div class="card-container">
            <div class="card">
                <h3>💧 Úmidade</h3>
                <p>{humidity}%</p>
            </div>
        </div>
        """.format(
                humidity=get_humidity()
            ), unsafe_allow_html=True)

    with b2:
        st.markdown("""
        <div class="card-container">
            <div class="card">
                <h3>📈 Maior Temperatura</h3>
                <p>{temp_max}</p>
            </div>
        </div>
        """.format(
                temp_max=get_temp_max()
            ), unsafe_allow_html=True)
    
    with b3:
        st.markdown("""
        <div class="card-container">
            <div class="card">
                <h3>🌞 Sensação Térmica</h3>
                <p>{feel}</p>
            </div>
        </div>
        """.format(
                feel=get_feel()
            ), unsafe_allow_html=True)

    with b4:
        st.markdown("""
        <div class="card-container">
            <div class="card">
                <h3>📉 Menor Temperatura</h3>
                <p>{temp_min}</p>
            </div>
        </div>
        """.format(
                temp_min=get_temp_min()
            ), unsafe_allow_html=True)

    # Row C
    #C1 being the graph, C2 The Table.
    c1, c2 = st.columns((7,3))

    with c2:
        # Criar seletores para ano, mês e dia
        st.write("### Escolha a data")
        year = st.selectbox("Selecione o ano", [2023, 2024, 2025], index=0)
        month = st.selectbox("Selecione o mês", list(range(1, 13)), format_func=lambda x: f"{x:02d}")
        day = st.selectbox("Selecione o dia", list(range(1, 32)), format_func=lambda x: f"{x:02d}")

        # Construir a data selecionada
        try:
            selected_date = pd.Timestamp(year=year, month=month, day=day)
            st.success(f"Data selecionada: {selected_date.date()}")
            
            # Simulação de dados para 24 horas no dia selecionado
            time_series = pd.date_range(start=selected_date, periods=24, freq="H")  # 24 horas
            data = pd.DataFrame({
                "Time": time_series,
                "Temperatura (°C)": np.random.uniform(20, 35, size=24),
                "Pressão (hPa)": np.random.uniform(1000, 1020, size=24),
                "Úmidade (%)": np.random.uniform(40, 90, size=24),
            })

            # Criar seleção para variável a ser visualizada
            variable = st.selectbox(
                "Selecione a variável que deseja visualizar:",
                data.columns.drop('Time')
            )
        except ValueError:
            st.error("Data inválida! Por favor, selecione um dia válido para o mês escolhido.")
            st.stop()

    # Parte do Gráfico (Coluna C1)
    with c1:
        # Configurar o índice como tempo
        data.set_index("Time", inplace=True)

        # Exibir o gráfico para a variável selecionada
        st.write(f"### Gráfico de {variable} ao longo do dia {selected_date.date()}")
        st.line_chart(data[[variable]])