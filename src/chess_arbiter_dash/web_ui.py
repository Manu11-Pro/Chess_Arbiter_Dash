import streamlit as st
import pandas as pd
import time

st.title("♟Chess_Arbiter_Dash♟")
st.markdown("## Welcome to Chess_Arbiter_Dash!")

add_game_bt = st.sidebar.button("+ Add Game")
token_bt = st.sidebar.button("Insert Your Token")
game_add = False
typed_in_both = False

#Add & View Game
if "usernames_container" not in st.session_state:
    st.session_state.usernames_container = False

if add_game_bt == True:
    st.session_state.usernames_container = True
    game_add = True

if st.session_state.get("usernames_container"):
    with st.container(key="usernames_input", border=True, autoscroll=True):
            player_1 = st.text_input(label="Type Username of the player1", value="", placeholder="Username")
            player_2 = st.text_input(label="Type Username of the player2", value="", placeholder="Username")

# if st.button("Confirm and View Game")== True:
#      print

#Insert Token
if "token_container" not in st.session_state:
    st.session_state.token_container = False

if token_bt == True:
    st.session_state.token_container = True

if st.session_state.get("token_container"):
    with st.container(key="token_input", border=True, autoscroll=True):
            player_1 = st.text_input(label="Insert Your Token", value="", placeholder="Token")

# if st.button("Confirm Token")== True:
#      print

#CSS

st.markdown("""
    <style>
        .usernames_input{
            width: 50%;
            height: 25vh;
            border: 10px solid #FFFFFF;
        }   

        .game_view{
            width: 50%;
            height: 25vh;
            border: 10px solid #FFFFFF;
        }  
            
        .token_container{
            width: 50%;
            height: 25vh;
            border: 10px solid #FFFFFF;
        }
    </style>
""", unsafe_allow_html=True)