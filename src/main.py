#!/usr/bin/env python3

import streamlit as st
import random
import pandas as pd
import plotly.express as px

if 'rolls' not in st.session_state:
    st.session_state.rolls = []
if 'roll_count' not in st.session_state:
    st.session_state.roll_count = 0

def roll_dice():
    result = random.randint(1, 6)
    return result

st.title('🎲 Rolling Dice Game')

if st.button('Roll Dice'):
    result = roll_dice()
    st.header(f'You rolled a {result}')

