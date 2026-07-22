import streamlit as st
import pandas as pd
import numpy as np


#streamlit tutorial
st.title("Hello, Streamlit")
st.write(":streamlit: this is your first streamlit app")
st.text("Lets Get Started")

#conditional logic with widgets
name = st.text_input("Enter your name :")
if st.button("Greet"):
   st.success(f"Hello,{name}")

#Display Data Charts 
df = pd.DataFrame(np.random.randn(10,2),columns = ['A','B'])
st.line_chart(df)
st.bar_chart(df)

#File uploading and catching topics
upload_file = st.file_uploader("upload CSV file", type="csv")
if upload_file:
   df = pd.read_csv(upload_file)
   st.dataframe(df)

st.header("this is a header ")
st.subheader("This is a subheader" )
st.markdown(" **Bold**, *Italic*, 'code', [Link](http://streamlit.io/)")
#st.code("for i in ranges(5): print(i)", languages="python")

st.text_input("What is your name")
st.text_area("Write your massage")
st.number_input("pick a number",min_value=0, max_value=100)
st.slider("choose a range",0, 100)
st.selectbox("select a fruit", ["Apple", "Orange", "Mango"])
st.multiselect("choose toppings", ["cheese", "tomato", "olives"])
st.radio("pick one",["option A", "option B"])
st.checkbox("I Agree Terms And Condition")

option = st.radio("choose view", ["show chart", "Show table"])
if option == "show chart":
   st.write("char would be appear here")
else:
   st.write("table would be appear here")

# creating form 
with st.form("Login Form"):
   username = st.text_input("Enter Username:")
   password = st.text_input("password",type="password")
   submitted = st.form_submit_button("Login")

   if submitted:
      st.success(f"Welcome {username}!") 