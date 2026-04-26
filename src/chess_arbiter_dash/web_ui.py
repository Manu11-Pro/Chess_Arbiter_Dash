import streamlit as st
import pandas as pd
import time
from logic import is_token_valid

st.title("♟Chess_Arbiter_Dash♟")
st.markdown("## Welcome to Chess_Arbiter_Dash!")

add_game_bt = st.sidebar.button("+ Add Game", key="add_game_bt")
token_bt = st.sidebar.button("Insert Your Token", key="token_bt")
game_add = False
typed_in_both = False

#Add & View Game
if "present_games" not in st.session_state:
    st.session_state.present_games = []

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

if "valid_token" not in st.session_state:
    st.session_state.valid_token = False

if st.session_state.get("token_container"):
     with st.container(key="token_input", border=True, autoscroll=True):
            token = st.text_input(label="Insert Your Token", value="", placeholder="Token", type="password")
            if st.button("Confirm Token", key="confirm_token_bt")== True:
                if is_token_valid(token):
                      st.session_state.valid_token = True
                      st.session_state.token_container = False
                      st.success("Valid Token!")
                      st.rerun()
                else:
                    st.error("Invalid Token, Retry!")


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