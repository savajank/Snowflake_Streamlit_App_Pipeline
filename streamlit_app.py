import streamlit
import pandas as pd

streamlit.title('My Moms New Healthy Diner') 


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Craeting a pick list for the user to filter the table. 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#displaying the table on the page
streamlit.dataframe(my_fruit_list)
