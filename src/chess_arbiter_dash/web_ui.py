import streamlit as st
import pandas as pd
import time

st.title("♟Chess_Arbiter_Dash♟")
st.markdown("## Welcome to Chess_Arbiter_Dash!")

add_game = st.sidebar.button("+ Add Game")
game_add = False


# while True:
#     if add_game :
#         game_add = True
#         print(game_add)
#         time.sleep(10)
#     else:
#         game_add = False
#         print(game_add)
#         time.sleep(10)