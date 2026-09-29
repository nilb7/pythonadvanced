from http.client import responses

import streamlit as st
import requests
import pandas as pd

st.title("Add a developer")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Expreience (Years)", min_value=0,max_value=50,value=0)

if st.button("Create Developer"):
    dev_data = {"name":dev_name,"expreience":dev_experience}
    response = requests.post("http://localhost:8000/developers",json=dev_data)
    st.json(response.json())

st.header("Add Project")
proj_title = st.text_input("Project title")
proj_desc = st.text_input("Project description")
proj_lang = st.text_input("Languages Used (Coma-separated)")
lead_dev_name = st.text_input("Lead Developer Name")
lead_dev_exp = st.number_input(" Lead Expreience (Years)", min_value=0,max_value=50,value=0)

if st.button("Lead Create Developer"):
    lead_dev_data = {"name":dev_name,"expreience":dev_experience}
    proj_data={
        "title":proj_title,
        "description":proj_desc,
        "languages":proj_lang.split(","),
        "lead_developer":lead_dev_data

    }
    response = requests.post("http://localhost:8000/developers",json=proj_data)
    st.json(response.json())