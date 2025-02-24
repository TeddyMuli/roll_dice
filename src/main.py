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
    st.session_state.rolls.append(result)
    st.session_state.roll_count += 1
    return result

st.title('🎲 Rolling Dice Game')

if st.button('Roll Dice'):
    result = roll_dice()
    st.header(f'You rolled a {result}')

if st.session_state.roll_count > 0:
    roll_data = pd.DataFrame(st.session_state.rolls, columns=['Result'])
    stats = roll_data['Result'].value_counts().reset_index()
    stats.columns['Number', 'Count']
    stats = stats.sort_values('Number')
    stats['Percentage'] = (stats['Count'] / len(st.session_state.rolls) * 100).round(2)

    st.subheader('Roll Statistics')
    st.dataframe(stats)

    bar_chart = px.bar(stats,
                       x='Number',
                       y='Count',
                       title='Distribution of Dice Rolls',
                       labels={'Number': 'Dice Number', 'Count': 'Number of Rolls'},
                       text=stats['Percentage'].apply(lambda x: f'{x}%'))
    
    bar_chart.update_traces(textposition='outside')
    st.plotly_chart(bar_chart)

    st.markdown(f'**Total Rolls** {st.session_state.roll_count}')

if st.button('Reset'):
    st.session_state.roll_count = 0
    st.session_state.rolls = []
    st.experimental_rerun()
