import streamlit as st
import pandas
from send_email import send_email

st.header("Contact")

with st.form(key="email_form"):
	user_email = st.text_input("Your email address: ")

	df2 = pandas.read_csv("topics.csv")
	drop_down = df2['topic'].unique()
	selection = st.selectbox("What topic do you want to discuss?", drop_down,
	                         index=None, placeholder="Choose an option...")

	raw_message = st.text_area("Message")
	message = f"""\
Subject: Best Company App - {user_email}

From: {user_email}
{raw_message}
"""
	button = st.form_submit_button("Submit")
	if button:
		send_email(message)
		st.info("Your email was sent successfully!")
