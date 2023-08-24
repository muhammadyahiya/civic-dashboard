import streamlit as st
import json
from api_wrapper import api_client
import pandas as pd

st.title("Civic Dashboards")

st.subheader("Power Load consumption for May 2023")

# https://data.telangana.gov.in/api/1/datastore/query/ae305fca-068b-4e61-b7f8-d9bf651e1b69/8
api_c = api_client.ApiClient()

data = api_c.get_data("ae305fca-068b-4e61-b7f8-d9bf651e1b69/52");

#data framing and clean up.
res = pd.DataFrame(data['results'])
res['load'] = res['load'].astype(float)
res.rename(columns = {'circle':'District','subdivision':'Mandal'}, inplace = True)

st.area_chart(res,x='Mandal',y='load')
st.bar_chart(res,x='area',y='load')
st.area_chart(res,x='section',y='load')
