import streamlit as st
import pandas as pd
import time

on = st.toggle("←runボタン。これがonの間、有林が働き続ける。")
output=""
now_location_x=0
now_location_y=0

df = pd.DataFrame(
    [
       {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": ""},
   ]
)

edited_df = st.data_editor(df,num_rows='dynamic')


if on:
    while current_cell != "おわり":
        time.sleep(0.1)



    st.title("出力")
    st.write(output)
    time.sleep(300)