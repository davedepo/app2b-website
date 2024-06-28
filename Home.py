# This is a program to create a website using streamlit framework

import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")

content1 = """

The Best Company is a distinguished Fortune 500 organization committed to excellence and innovation. Since our inception in 1985, we have consistently delivered exceptional services to our global clientele. Our services include Cutting-Edge Technology Solutions, Strategic Consulting, Global Supply Chain Management.

Founded in 1985, The Best Company has been a trailblazer in the industry, setting new standards for excellence and client satisfaction.
"""
st.write(content1)

content2 = """
Our Team
"""
st.subheader(content2)

df = pandas.read_csv("data.csv")

col1, col2, col3 = st.columns(3)

with col1:
	for index, row in df[:4].iterrows():
		st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
		st.write(row["role"])
		st.image("images/" + row["image"])

with col2:
	for index, row in df[4:8].iterrows():
		st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
		st.write(row["role"])
		st.image("images/" + row["image"])

with col3:
	for index, row in df[8:].iterrows():
		st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
		st.write(row["role"])
		st.image("images/" + row["image"])
