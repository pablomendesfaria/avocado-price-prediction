import streamlit as st
import numpy as np
import pandas as pd
import pickle
import mlflow
from PIL import Image


st.set_page_config(
    page_title="Avocado project",
    page_icon="🥑"
)

st.markdown('# Avocado project')
st.image('avocado.jpg', caption='Avocado project')

st.markdown('## Fill in the avocado sales information of the week')

plu4046 = st.number_input(
    'PLU4046:',
    min_value=0.0,
    max_value=5160896.68,
    value=1036.74
)

plu4225 = st.number_input(
    'PLU4225:',
    min_value=0.0,
    max_value=4097591.67,
    value=54454.85
)

plu4770 = st.number_input(
    'PLU4770:',
    min_value=0.0,
    max_value=804558.25,
    value=48.16
)

small_bags = st.number_input(
    'Small Bags:',
    min_value=0.0,
    max_value=3403581.49,
    value=8603.62
)

large_bags = st.number_input(
    'Large Bags:',
    min_value=0.0,
    max_value=1049435.14,
    value=93.25
)

xlarge_bags = st.number_input(
    'XLarge Bags:',
    min_value=0.0,
    max_value=131300.76,
    value=0.0
)

avocado_type = st.selectbox(
    'Type:',
    ['Conventional', 'Organic'],
    index=0
)

year = st.number_input(
    'Year:',
    min_value=2015,
    max_value=2018,
    value=2015
)

mounth = st.number_input(
    'Mounth:',
    min_value=1,
    max_value=12,
    value=12
)

day = st.number_input(
    'Day:',
    min_value=1,
    max_value=31,
    value=27
)

region = st.selectbox(
    'Region',
    ['Albany', 'Atlanta', 'BaltimoreWashington', 'Boise', 'Boston', 'BuffaloRochester', 'California', 
     'Charlotte', 'Chicago', 'CincinnatiDayton', 'Columbus', 'DallasFtWorth', 'Denver', 'Detroit', 
     'GrandRapids', 'GreatLakes', 'HarrisburgScranton', 'HartfordSpringfield', 'Houston', 'Indianapolis', 
     'Jacksonville', 'LasVegas', 'LosAngeles', 'Louisville', 'MiamiFtLauderdale', 'Nashville', 'NewOrleansMobile', 
     'NewYork', 'NorthernNewEngland', 'Orlando', 'Philadelphia', 'PhoenixTucson', 'Pittsburgh', 'Plains', 'Portland', 
     'RaleighGreensboro', 'RichmondNorfolk', 'Roanoke', 'Sacramento', 'SanDiego', 'SanFrancisco', 'Seattle', 
     'SouthCarolina', 'SouthCentral', 'Spokane', 'StLouis', 'Syracuse', 'Tampa', 'WestTexNewMexico'],
    index=0
)

d = {
    'PLU4046': [plu4046], 
    'PLU4225': [plu4225], 
    'PLU4770': [plu4770], 
    'SmallBags': [small_bags], 
    'LargeBags': [large_bags], 
    'XLargeBags': [xlarge_bags], 
    'type': [1 if avocado_type == 'Conventional' else 0], 
    'year': [year], 
    'mounth': [mounth], 
    'day': [day], 
    'Albany': [1 if region == 'Albany' else 0], 
    'Atlanta': [1 if region == 'Atlanta' else 0], 
    'BaltimoreWashington': [1 if region == 'BaltimoreWashington' else 0], 
    'Boise': [1 if region == 'Boise' else 0], 
    'Boston': [1 if region == 'Boston' else 0], 
    'BuffaloRochester': [1 if region == 'BuffaloRochester' else 0], 
    'California': [1 if region == 'California' else 0], 
    'Charlotte': [1 if region == 'Charlotte' else 0], 
    'Chicago': [1 if region == 'Chicago' else 0], 
    'CincinnatiDayton': [1 if region == 'CincinnatiDayton' else 0], 
    'Columbus': [1 if region == 'Columbus' else 0], 
    'DallasFtWorth': [1 if region == 'DallasFtWorth' else 0], 
    'Denver': [1 if region == 'Denver' else 0], 
    'Detroit': [1 if region == 'Detroit' else 0], 
    'GrandRapids': [1 if region == 'GrandRapids' else 0], 
    'GreatLakes': [1 if region == 'GreatLakes' else 0], 
    'HarrisburgScranton': [1 if region == 'HarrisburgScranton' else 0], 
    'HartfordSpringfield': [1 if region == 'HartfordSpringfield' else 0], 
    'Houston': [1 if region == 'Houston' else 0], 
    'Indianapolis': [1 if region == 'Indianapolis' else 0], 
    'Jacksonville': [1 if region == 'Jacksonville' else 0], 
    'LasVegas': [1 if region == 'LasVegas' else 0], 
    'LosAngeles': [1 if region == 'LosAngeles' else 0], 
    'Louisville': [1 if region == 'Louisville' else 0], 
    'MiamiFtLauderdale': [1 if region == 'MiamiFtLauderdale' else 0], 
    'Nashville': [1 if region == 'Nashville' else 0], 
    'NewOrleansMobile': [1 if region == 'NewOrleansMobile' else 0], 
    'NewYork': [1 if region == 'NewYork' else 0], 
    'NorthernNewEngland': [1 if region == 'NorthernNewEngland' else 0], 
    'Orlando': [1 if region == 'Orlando' else 0], 
    'Philadelphia': [1 if region == 'Philadelphia' else 0], 
    'PhoenixTucson': [1 if region == 'PhoenixTucson' else 0], 
    'Pittsburgh': [1 if region == 'Pittsburgh' else 0], 
    'Plains': [1 if region == 'Plains' else 0], 
    'Portland': [1 if region == 'Portland' else 0], 
    'RaleighGreensboro': [1 if region == 'RaleighGreensboro' else 0], 
    'RichmondNorfolk': [1 if region == 'RichmondNorfolk' else 0], 
    'Roanoke': [1 if region == 'Roanoke' else 0], 
    'Sacramento': [1 if region == 'Sacramento' else 0], 
    'SanDiego': [1 if region == 'SanDiego' else 0], 
    'SanFrancisco': [1 if region == 'SanFrancisco' else 0], 
    'Seattle': [1 if region == 'Seattle' else 0], 
    'SouthCarolina': [1 if region == 'SouthCarolina' else 0], 
    'SouthCentral': [1 if region == 'SouthCentral' else 0], 
    'Spokane': [1 if region == 'Spokane' else 0], 
    'StLouis': [1 if region == 'StLouis' else 0], 
    'Syracuse': [1 if region == 'Syracuse' else 0], 
    'Tampa': [1 if region == 'Tampa' else 0], 
    'WestTexNewMexico': [1 if region == 'WestTexNewMexico' else 0]
}   

df = pd.DataFrame(d)
st.dataframe(df)

if st.button('Predict'):
    if (plu4046 == 0.0 and plu4225 == 0.0 and plu4770 == 0.0 and small_bags == 0.0 and large_bags == 0.0 and xlarge_bags == 0.0):
        st.error('Please fill in the fields related to the quantity of sale! aka PLU4046, PLU4225, PLU4770, Small Bags, Large Bags, XLarge Bags')
    else:
        logged_model = 'runs:/f5b154c4434c4f35a73248d9aae87e85/model'

        # Load model as a PyFuncModel.
        model = mlflow.pyfunc.load_model(logged_model)

        r = model.predict(df)

        st.success(f'Average Price: {r}')
