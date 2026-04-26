import streamlit as st
import pandas as pd
import time

st.title("♟Chess_Arbiter_Dash♟")
st.markdown("## Welcome to Chess_Arbiter_Dash!")

add_game = st.sidebar.button("+ Add Game")
game_add = False