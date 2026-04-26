import streamlit as st
import pandas as pd
import time

st.title("♟Chess_Arbiter_Dash♟")
st.markdown("## Welcome to Chess_Arbiter_Dash!")

add_game_bt = st.sidebar.button("+ Add Game")
game_add = False

if add_game_bt == True:
    game_add = True
    with st.container(key="game_view", border=True, autoscroll=True):
        st.markdown("view_the_games")


#CSS

st.markdown("""
    <style>
        .game_view{
            width: 50%;
            height: 25vh;
            border: 10px solid #FFFFFF;
        }        
    </style>
""", unsafe_allow_html=True)