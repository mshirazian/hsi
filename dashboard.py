import leafmap.foliumap as leafmap
import folium
import streamlit as st
import streamlit.components.v1 as components
import streamlit_authenticator as stauth
# import ee
# import geemap.foliumap as geemap

## Trigger the authentication flow. You only need to do this once
# ee.Authenticate()

# Initialize the library.
# ee.Initialize()

# dem = ee.Image('USGS/SRTMGL1_003')
# xy = ee.Geometry.Point([86.9250, 27.9881])
# elev = dem.sample(xy, 30).first().get('elevation').getInfo()
# print('Mount Everest elevation (m):', elev)

st.set_page_config(layout="wide")
# html = "data/html/sfo_buildings.html"
# leafmap.cesium_to_streamlit(html, height=800)

names = ['Sam Bigdeli','Massoud Shirazian']
usernames = ['sbigdeli','mshirazian']
passwords = ['123','456']
tiles = None
width = 800
height = 600

# hashed_passwords = stauth.hasher(passwords).generate()

HtmlFile = open("assets/sketchfab.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()

# authenticator = stauth.authenticate(names,usernames,hashed_passwords,
#     'some_cookie_name','some_signature_key',cookie_expiry_days=30)
#
# name, authentication_status = authenticator.login('Login','sidebar')

# if st.session_state['authentication_status']:
    # html = "assets\sfo.html"
    # leafmap.cesium_to_streamlit(html, height=800)
    # m = geemap.Map(location=[33.81712, -118.34365], zoom_start=18)
m = leafmap.Map(location=[33.81712, -118.34365], zoom_start=18)
folium.Marker([33.81712, -118.34365], popup = ' HSI Lab ').add_to(m)

folium.TileLayer('Stamen Terrain').add_to(m)
folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('Stamen Water Color').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.LayerControl().add_to(m)
# CircleMarker with radius
folium.CircleMarker(location = [33.81730, -118.343395], radius = 50, fill_color='blue',popup = ' HSI Lab ').add_to(m)

if tiles is not None:
    for tile in tiles:
        m.add_xyz_service(tile)

# m.to_streamlit(width, height)
with st.sidebar:
    # st.write('Welcome *%s*' % (st.session_state['name']))
    st.image("assets/logo_gold.png", width=200)
    selection = st.selectbox('Facility:', ['...','HSI Lab'])
if selection ==  'HSI Lab':
        components.html(source_code)
        m.to_streamlit(width, height)
# elif st.session_state['authentication_status'] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state['authentication_status'] == None:
#     st.warning('Please enter your username and password')

