import streamlit
import pandas 
import requests
import snowflake.connector 
from urllib.error import URLError


streamlit.title('My Moms New Healthy Diner') 


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# The fruit list is indexed and will show which fruits are in the table
my_fruit_list = my_fruit_list.set_index('Fruit')

#Creating a pick list for the user to filter the table. 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected] # the loc function finds the fruits

#displaying the table on the page
streamlit.dataframe(fruits_to_show)

#create the repeatable code block called a function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized


# New section to display fruityvice api response 
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()


streamlit.stop()

#import snowflake.connector 

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
 
#Add a button to load the fruit
if streamlit.button("Get Fruit Load List'):
                     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
                     my_data_rows = get_fruit_load_list()
                     streamlit.dataframe(my_data_rows)
   
                    
# Allowing the user to add new fruits to the list

add_my_fruit = streamlit.text_input("What would you like to add?", "Jackfruit")
streamlit.write("Thanks for writing", add_my_fruit)
#wrong
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
