import streamlit as st
import pandas as pd
import time

on = st.toggle("←runボタン。これがonの間、有林が働き続ける。")
output=""
now_location_x = 0
now_location_y = 0
now_direction  = 0 #0が右、1が下、2が左、3が上

df = pd.DataFrame(
    [
        {"0": "みぎ", "1": "", "2": "", "3": "した", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "おわり", "3": "ひだり", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""}, 
        {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""} 
    ]
)

now_cell=df.loc[now_location_y,str(now_location_x)]
st.table(df)

if on:
    while now_cell != "おわり":
        time.sleep(0.1)
        now_cell=df.loc[now_location_y,str(now_location_x)]
        if now_cell == "みぎ":
            now_direction=0
        elif now_cell == "した":
            now_direction=1
        elif now_cell == "ひだり":
            now_direction=2
        elif now_cell == "うえ":
            now_direction=3

        if now_direction == 0:
            now_location_x = now_location_x + 1
            now_location_y = now_location_y + 0
        elif now_direction == 1:
            now_location_x = now_location_x + 0
            now_location_y = now_location_y + 1
        elif now_direction == 2:
            now_location_x = now_location_x - 1
            now_location_y = now_location_y + 0
        elif now_direction == 2:
            now_location_x = now_location_x + 0
            now_location_y = now_location_y - 1

    st.title("出力")
    st.write(output)
    time.sleep(300)