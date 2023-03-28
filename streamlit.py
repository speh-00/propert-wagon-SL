import streamlit as st
import pandas as pd
import requests
st.set_page_config(layout="wide")
st.title('Property Wagon - HDB resale prices')

st.sidebar.header('Tell us about the HDB you are interested in')

df_flat_type = pd.DataFrame({'flat_type': ['1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION']})
df_storey_range = pd.DataFrame({'storey_range': ['01 TO 03', '04 TO 06', '07 TO 09', '10 TO 12', '13 TO 15', '16 TO 18', '19 TO 21', '22 TO 24', '25 TO 27', '28 TO 30', '31 TO 33', '34 TO 36', '37 TO 39', '40 TO 42', '43 TO 45', '46 TO 48', '49 TO 51']})

address = st.sidebar.text_input('Address', 'Enter Address')
flat_type = st.sidebar.selectbox('Select number of rooms', df_flat_type['flat_type'])
storey_range = st.sidebar.selectbox('Select level of flat', df_storey_range['storey_range'])
submit_button = st.sidebar.button('SUBMIT')

st.sidebar.header('Nearby Amenities')

if submit_button:
    
#         # Make API call and display results in main section
#         response = requests.get(f"https://some-api.com?address={address}&flat_type={flat_type}&storey_range={storey_range}")
#         result = response.json()
    
    st.sidebar.write('API for nearest train station and distance from location')
    st.sidebar.write('API for nearest mall and distance from location')
    st.sidebar.write('API for nearest hawker and distance from location')
    st.sidebar.write('API for nearest school and distance from location')
                     
        
        
        
# st.subtitle('ADD INTERACTIVE MAP SHOwING RESALE TRANSACTIONS IN PAST 12 MONTHS WITHIN 5KM')
# @st.cache
# def get_map_data():
#     return pd.DataFrame(
#             np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#             columns=['lat', 'lon'])
# df = get_map_data()
# st.map(df)

# st.subtitle('ADD PREDICTED PRICE WITH FORECAST CHART')

# st.subtitle('ADD LEASE DECAY WITH AVG RENTAL DATA FOR PAST 1 YEAR')




# ADD INTERACTIVE MAP?

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
