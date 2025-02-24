#!/usr/bin/env python3

import streamlit as st
import random
import pandas as pd
import plotly.express as px

def roll_dice():
    result = random.randint(1, 6)
    return result
