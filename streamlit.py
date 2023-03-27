import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")
col1, col2 = st.beta_columns(2)

col1.write("Tell us about the HDB\nyou are interested in")

with st.form(key='params_for_api'):

  df_flat_type = pd.DataFrame({'flat_type': ['1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION']})
  df_storey_range = pd.DataFrame({'storey_range': ['01 TO 03', '04 TO 06', '07 TO 09', '10 TO 12', '13 TO 15', '16 TO 18', '19 TO 21', '22 TO 24', '25 TO 27', '28 TO 30', '31 TO 33', '34 TO 36', '37 TO 39', '40 TO 42', '43 TO 45', '46 TO 48', '49 TO 51']})
  
  address = col1.text_input('', 'Enter Address')
  flat_type = col1.selectbox('Select number of rooms', df_flat_type['flat_type'])
  df_storey_range = col1.selectbox('Select level of flat', df_storey_range['storey_range'])
  
  col1.form_submit_button('SUBMIT')

  
  
col2.write("Property Wagon - HDB resale prices")  



# CHANGE TO INTERACTIVE MAP?

# def get_map_data():
#     return pd.DataFrame(
#             np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#             columns=['lat', 'lon']
#         )
# df = get_map_data()
# st.map(df)














# '''

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction


# '''

# url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
