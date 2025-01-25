import streamlit as st
import pandas as pd
import time

on = st.toggle("←runボタン。これがonの間、有林が働き続ける。")
output=""
now_location_x=0
now_location_y=0

l = [["みぎ", "", "した"], ["", "", ""], ["", "おわり", "ひだり"]]

edited_df = st.data_editor(l,num_rows='dynamic')


if on:
    time.sleep(0.1)



    st.title("出力")
    st.write(output)
    time.sleep(300)