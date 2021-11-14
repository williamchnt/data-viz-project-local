import time
import streamlit as st
# importing numpy and pandas for to work with sample data.
import pandas as pd
import numpy as np
import datetime
from datetime import date
from streamlit.elements.arrow import Data
from streamlit_folium import folium_static
import folium
import plotly_express as px
import streamlit.components.v1 as components
import os

def setIconPage():
    st.set_page_config(
        page_title = "Transaction immobilère en France",
        page_icon = 'ressources/selling.png',
        layout = 'wide'
    )

def HideStreamlitContent():
    
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def logFunction(func):
    
    def inner(*args, **kwargs):
        print("Exécution de ",func.__name__)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        interv = end-start
        f = open("ressources/Log_Time_Function.txt", "a")
        print(interv)
        mes=str(date.today())+" :  Execution of "+func.__name__+" in "+str(interv) + "\n"
        f.write(mes)
        f.close()
        return result
    return inner

def get_weekday(df):
    return df.weekday()

def get_dom(df):
    return df.day

def get_hours(df):
    return df.hour

def count_rows(rows):
    return len(rows)

@logFunction
@st.cache
def FirstLoad():
    findLocal=False
    for filename in os.listdir("data"):
        if filename == "full_2020.csv":
            findLocal = True

    try:
        df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/GOrVpuxe12bweaK9/full_2020_1.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/-mqSOhjWBxt-rSMZ/full_2020_2.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df2020=pd.concat([df1,df2])
 
        findWeb = True
    except:
        findWeb = False

    if (findLocal) & (not(findWeb)):
        df2020 = pd.read_csv("data/full_2020.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]


    if findLocal | findWeb:
        df2020 = df2020.fillna(0)
        
        df2020['date_mutation'] = pd.to_datetime(df2020['date_mutation'])
        df2020['adresse_suffixe'] = df2020['adresse_suffixe'].astype(str)
        df2020['nature_mutation'] = df2020['nature_mutation'].astype(str)
        df2020['adresse_nom_voie'] = df2020['adresse_nom_voie'].astype(str)
        df2020['adresse_code_voie'] = df2020['adresse_code_voie'].astype(str)
        df2020['nom_commune'] = df2020['nom_commune'].astype(str)
        df2020['code_postal'] = df2020['code_postal'].astype(str)
        df2020['adresse_numero'] = df2020['adresse_numero'].astype(str)
        df2020['code_commune'] = df2020['code_commune'].astype(str)
        df2020['code_departement'] = df2020['code_departement'].astype(str)
        df2020['type_local'] = df2020['type_local'].astype(str)
       
    else:
        df2020=pd.DataFrame()

    return df2020

@logFunction
@st.cache
def load2019():
    findLocal=False
    for filename in os.listdir("data"):
        if filename == "full_2019.csv":
            findLocal = True

    try:
        df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/U_Nn5m1-sXAux1qO/full_2019_1.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/zogg9pmrCYohCAyX/full_2019_2.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df3 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/QN5fX5w0qiLStf-o/full_2019_3.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df4 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/-hVR2tOISmPUcNEG/full_2019_4.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df=pd.concat([df1,df2,df3,df4])
        findWeb = True
    except:
        findWeb = False


    if (findLocal) & (not(findWeb)):
        df = pd.read_csv("data/full_2019.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]


    if findLocal | findWeb:
        df = df.fillna(0)
        df['date_mutation'] = pd.to_datetime(df['date_mutation'])
        df['adresse_suffixe'] = df['adresse_suffixe'].astype(str)
        df['nature_mutation'] = df['nature_mutation'].astype(str)
        df['adresse_nom_voie'] = df['adresse_nom_voie'].astype(str)
        df['adresse_code_voie'] = df['adresse_code_voie'].astype(str)
        df['nom_commune'] = df['nom_commune'].astype(str)
        df['code_postal'] = df['code_postal'].astype(str)
        df['adresse_numero'] = df['adresse_numero'].astype(str)
        df['code_commune'] = df['code_commune'].astype(str)
        df['code_departement'] = df['code_departement'].astype(str)
        df['type_local'] = df['type_local'].astype(str)
    else:
        df=pd.DataFrame()

    return df

@logFunction
@st.cache
def load2018():
    findLocal=False
    for filename in os.listdir("data"):
        if filename == "full_2018.csv":
            findLocal = True

    try:
        df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/p3tx8zc6cPox6zQX/full_2018_1.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/DkFD80NcEcAIg25c/full_2018_2.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df3 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/SraSQWyQrzEbcElX/full_2018_3.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df=pd.concat([df1,df2,df3])
        findWeb = True
    except:
        findWeb = False


    if (findLocal) & (not(findWeb)):
        df = pd.read_csv("data/full_2018.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]


    if findLocal | findWeb:
        df = df.fillna(0)
        df['date_mutation'] = pd.to_datetime(df['date_mutation'])
        df['adresse_suffixe'] = df['adresse_suffixe'].astype(str)
        df['nature_mutation'] = df['nature_mutation'].astype(str)
        df['adresse_nom_voie'] = df['adresse_nom_voie'].astype(str)
        df['adresse_code_voie'] = df['adresse_code_voie'].astype(str)
        df['nom_commune'] = df['nom_commune'].astype(str)
        df['code_postal'] = df['code_postal'].astype(str)
        df['adresse_numero'] = df['adresse_numero'].astype(str)
        df['code_commune'] = df['code_commune'].astype(str)
        df['code_departement'] = df['code_departement'].astype(str)
        df['type_local'] = df['type_local'].astype(str)
        
    else:
        df=pd.DataFrame()

    return df

@logFunction
@st.cache
def load2017():
    findLocal=False
    for filename in os.listdir("data"):
        if filename == "full_2017.csv":
            findLocal = True

    try:
        df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/82AUNnGD4l0vG4Xi/full_2017_1.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/WPgvmacBEIbAqgnC/full_2017_2.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df3 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/bSoOVU9O26a39gcD/full_2017_3.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df4 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/tgq3jXf8IJiN0zcF/full_2017_4.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df=pd.concat([df1,df2,df3,df4])
        findWeb = True
    except:
        findWeb = False


    if (findLocal) & (not(findWeb)):
        df = pd.read_csv("data/full_2017.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]

    if findLocal | findWeb:
        df = df.fillna(0)
        df['date_mutation'] = pd.to_datetime(df['date_mutation'])
        df['adresse_suffixe'] = df['adresse_suffixe'].astype(str)
        df['nature_mutation'] = df['nature_mutation'].astype(str)
        df['adresse_nom_voie'] = df['adresse_nom_voie'].astype(str)
        df['adresse_code_voie'] = df['adresse_code_voie'].astype(str)
        df['nom_commune'] = df['nom_commune'].astype(str)
        df['code_postal'] = df['code_postal'].astype(str)
        df['adresse_numero'] = df['adresse_numero'].astype(str)
        df['code_commune'] = df['code_commune'].astype(str)
        df['code_departement'] = df['code_departement'].astype(str)
        df['type_local'] = df['type_local'].astype(str)
    else:
        df=pd.DataFrame()

    return df

@logFunction
@st.cache
def load2016():
    findLocal=False
    for filename in os.listdir("data"):
        if filename == "full_2016.csv":
            findLocal = True

    try:
        df1 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/gBWoHAnDjy7bGnto/full_2016_1.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df2 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/PCqKGPaNzVHN1tM6/full_2016_2.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df3 = pd.read_csv("https://chenutfamily.freeboxos.fr:45883/share/ZJiZhPFEU2YB42Ru/full_2016_3.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]
        df=pd.concat([df1,df2,df3])
        findWeb = True
    except:
        findWeb = False


    if (findLocal) & (not(findWeb)):
        df = pd.read_csv("data/full_2016.csv",low_memory=False,usecols=['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude'])[['date_mutation','nature_mutation','valeur_fonciere','adresse_numero','adresse_suffixe','adresse_nom_voie','adresse_code_voie','code_postal','code_commune','nom_commune','code_departement','type_local','surface_reelle_bati','nombre_pieces_principales','surface_terrain','longitude','latitude']]


    if findLocal | findWeb:
        df = df.fillna(0)
        df['date_mutation'] = pd.to_datetime(df['date_mutation'])
        df['adresse_suffixe'] = df['adresse_suffixe'].astype(str)
        df['nature_mutation'] = df['nature_mutation'].astype(str)
        df['adresse_nom_voie'] = df['adresse_nom_voie'].astype(str)
        df['adresse_code_voie'] = df['adresse_code_voie'].astype(str)
        df['nom_commune'] = df['nom_commune'].astype(str)
        df['code_postal'] = df['code_postal'].astype(str)
        df['adresse_numero'] = df['adresse_numero'].astype(str)
        df['code_commune'] = df['code_commune'].astype(str)
        df['code_departement'] = df['code_departement'].astype(str)
        df['type_local'] = df['type_local'].astype(str)
    else:
        df=pd.DataFrame()

    return df

def filterHome(df):

    header_1_column, header_2_column,  = st.columns(2)
    date_debut = header_1_column.date_input(
        "Date de debut",
        datetime.date(2016, 1, 1),
        datetime.date(2016, 1, 1),
        datetime.date(2020, 12, 31),
        )
            
    date_fin = header_2_column.date_input(
        "Date de fin",
        datetime.date(2020, 12, 31),
        date_debut,
        datetime.date(2020, 12, 31)
        )
        
    mask = (df['date_mutation'].dt.date > date_debut) & (df['date_mutation'].dt.date <= date_fin)
    df = df.loc[mask]

    advanced_search = st.checkbox("Recherche avancée")
    
    vente = False
    Adjudication = False
    Echange = False
    Expropriation = False
    terrain = False
    achèvement = False

    if advanced_search:
        st.markdown("Affichier les :")
        a,b,c,d,e,f  = st.columns(6)
        vente = a.checkbox("Vente",True)
        Adjudication = b.checkbox("Adjudication",True)
        Echange = c.checkbox("Echange",True)
        Expropriation = d.checkbox("Expropriation",True)
        terrain = e.checkbox("Vente terrain à batir",True)
        achèvement = f.checkbox("Vente en l'état future d'achèvement",True)

        df2 = df[0:0]
        if vente:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Vente')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if Adjudication:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Adjudication')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if Echange:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Echange')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if Expropriation:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Expropriation')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if terrain:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Vente terrain à batir')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if achèvement:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == "Vente en l'état future d'achèvement")
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        
        df=df2
    
    return df

def ComDepHome():
    ChooseFilter = st.selectbox("Afficher les ",["Commune","Département"],index = 0)
    return ChooseFilter

def filterCity(df):
    header_1_column, header_2_column,  = st.columns(2)

    ChooseFilter = header_1_column.selectbox("Rechercher par",["Commune","Département"],index = 0)
    if ChooseFilter== "Commune":
        town_search = header_2_column.text_input('Nom de ville', 'Nantes')
    if ChooseFilter== "Département":
        town_search = header_2_column.text_input('Numéro de département', '95')

    date_debut = header_1_column.date_input(
        "Date de debut",
        datetime.date(2016, 1, 1),
        datetime.date(2016, 1, 1),
        datetime.date(2020, 12, 31),
        )
            
    date_fin = header_2_column.date_input(
        "Date de fin",
        datetime.date(2020, 12, 31),
        date_debut,
        datetime.date(2020, 12, 31)
        )

    advanced_search = st.checkbox("Recherche avancée")
    
    vente = False
    Adjudication = False
    Echange = False
    Expropriation = False
    terrain = False
    achèvement = False

    if advanced_search:
        st.markdown("Affichier les :")
        a,b,c,d,e,f  = st.columns(6)
        vente = a.checkbox("Vente",True)
        Adjudication = b.checkbox("Adjudication",True)
        Echange = c.checkbox("Echange",True)
        Expropriation = d.checkbox("Expropriation",True)
        terrain = e.checkbox("Vente terrain à batir",True)
        achèvement = f.checkbox("Vente en l'état future d'achèvement",True)

        df2 = df[0:0]
        if vente:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Vente')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if Adjudication:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Adjudication')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if Echange:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Echange')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if Expropriation:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Expropriation')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if terrain:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == 'Vente terrain à batir')
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        if achèvement:
            df3 = pd.DataFrame()
            mask = (df['nature_mutation'] == "Vente en l'état future d'achèvement")
            df3 = df.loc[mask]
            df2=pd.concat([df2,df3])
        
        df=df2
        
    if (ChooseFilter=="Commune"):
        mask = (df['date_mutation'].dt.date > date_debut) & (df['date_mutation'].dt.date <= date_fin) & (df['nom_commune']== town_search)
        df = df.loc[mask]

    if (ChooseFilter=="Département"):
        mask = (df['date_mutation'].dt.date > date_debut) & (df['date_mutation'].dt.date <= date_fin) & (df['code_departement']== town_search)
        df = df.loc[mask]

    return df, town_search, ChooseFilter

def filterAdress(df):
    header_1_column, header_2_column,  = st.columns(2)

    rue = header_1_column.text_input('Nom de la voie',"RUE DES GRAVES")
    ville = header_2_column.text_input('Ville',"Bourg-en-Bresse")

    date_debut = header_1_column.date_input(
        "Date de debut",
        datetime.date(2016, 1, 1),
        datetime.date(2016, 1, 1),
        datetime.date(2020, 12, 31),
        )
            
    date_fin = header_2_column.date_input(
        "Date de fin",
        datetime.date(2020, 12, 31),
        date_debut,
        datetime.date(2020, 12, 31)
        )
    mask = (df['nom_commune']== ville) & (df['adresse_nom_voie']==rue) &(df['date_mutation'].dt.date > date_debut) & (df['date_mutation'].dt.date <= date_fin)
    df = df.loc[mask].reset_index()
    liste = []
    for i in df.index:
        s =str(i)+") "+str(df['date_mutation'][i])[:-8]+" - "+str(df['nature_mutation'][i]) + " : " +str(df['adresse_numero'][i])[:-2] + " "+ str(df['adresse_nom_voie'][i]) + ", " + str(df['nom_commune'][i]) + ", "  + str(df['code_postal'][i])[:-2]
        liste.append(s)
    adresse = st.selectbox("Choisissez votre adresse",liste,index = 0)

    stop=True
    indice=""
    for letter in adresse:
        if stop:
            if letter==")":
                stop=False
            else:
                indice+=letter

    indice = int(indice)

    return df,indice


def PriceMeterQuareCity(df,townSearch,ChooseFilter):
    mask = df['surface_reelle_bati']>0
    df = df.loc[mask]
    if(ChooseFilter=='Commune'):
        mask = (df['nom_commune']==townSearch)
        df = df.loc[mask]
        Price = df['valeur_fonciere'].mean()
        Surface = df['surface_reelle_bati'].mean()
    if(ChooseFilter=='Département'):
        mask = (df['code_departement']==townSearch)
        df = df.loc[mask]
        Price = df['valeur_fonciere'].mean()
        Surface = df['surface_reelle_bati'].mean()

    result = round(Price/Surface,2)
    return result

def PriceMeanCity(df,townSearch,ChooseFilter):
    
    if(ChooseFilter=='Commune'):
        mask = (df['nom_commune']==townSearch)
        df = df.loc[mask]
        Price = df['valeur_fonciere'].mean()
    if(ChooseFilter=='Département'):
        mask = (df['code_departement']==townSearch)
        df = df.loc[mask]
        Price = df['valeur_fonciere'].mean()


    result = round(Price,2)
    return result

def metricsCity(PriceMeterQuare,PriceMeanCity):
    col1, col2 = st.columns(2)
    col1.metric("Prix au métre carré", str(PriceMeterQuare)+"€","")
    col2.metric("Moyenne du prix de ventes : ", str(PriceMeanCity)+"€","")

@logFunction
def printCityMax(df,nb):
    header_1_column, header_2_column,  = st.columns(2)

    mask = (df['nature_mutation']=="Vente")
    df = df.loc[mask]

    dfCom = df.groupby('nom_commune').apply(count_rows)
    dfCom = dfCom.reset_index()
    dfCom = dfCom.sort_values(by=0,ascending = False)
    fig1 = px.pie(dfCom.head(nb), values=0, names="nom_commune", title=str('Part des mutations par Commune'))

    dfDep = df.groupby('code_departement').apply(count_rows)
    dfDep = dfDep.reset_index()
    dfDep = dfDep.sort_values(by=0,ascending = False)
    fig2 = px.pie(dfDep.head(nb), values=0, names="code_departement", title=str('Part des mutations par Département'))

    header_1_column.plotly_chart(fig1)
    header_2_column.plotly_chart(fig2)


def HighestPriceSquareMeter(df,nb):
    header_1_column, header_2_column,  = st.columns(2)
    mask = (df['nature_mutation']=="Vente")
    df = df.loc[mask]

    df['Price_Square_Meter'] = df['valeur_fonciere'] / df['surface_reelle_bati']

    dfCom = df.groupby('nom_commune').mean('Price_Square_Meter').reset_index()
    dfCom.replace([np.inf, -np.inf], np.nan, inplace=True)
    dfCom = dfCom.sort_values(by='Price_Square_Meter',ascending = False)
    fig1 = px.bar(dfCom.head(nb), x='nom_commune', y='Price_Square_Meter', title=str("Prix au mètre carré maximum des ventes par Commune"))

    dfDep = df.groupby('code_departement').mean('Price_Square_Meter').reset_index()
    dfDep.replace([np.inf, -np.inf], np.nan, inplace=True)
    dfDep = dfDep.dropna()
    dfDep = dfDep.sort_values(by='Price_Square_Meter',ascending = False)
    fig2 = px.bar(dfDep.head(nb), x='code_departement', y='Price_Square_Meter', title=str("Prix au mètre carré maximum des ventes par Département"))

    header_1_column.plotly_chart(fig1)
    header_2_column.plotly_chart(fig2)

def CotaTypeLocalCity(df,ChooseFilter,townSearch):
    if(ChooseFilter=='Commune'):
        mask = (df['nom_commune']==townSearch)
        df = df.loc[mask]
    if(ChooseFilter=='Département'):
        mask = (df['code_departement']==townSearch)
        df = df.loc[mask]

    df = df.groupby('type_local').apply(count_rows).reset_index()
    fig = px.pie(df, values=0, names="type_local", title=str('Répartition des type de local'))

    st.plotly_chart(fig)

def MaxIncrease(df,nb,ChooseFilter):
    st.subheader("Augmentation des prix du marché par "+ChooseFilter)
    mask = (df['nature_mutation']=="Vente")
    df = df.loc[mask]
    
    if(ChooseFilter=='Commune'):
        df = df.groupby('nom_commune').apply(count_rows)
    if(ChooseFilter=='Département'):
        df = df.groupby('code_departement').apply(count_rows)

    df = df.sort_values(ascending = False)

    fig = px.bar(df.head(nb))
    st.plotly_chart(fig)

def mapCity(df,ChooseFilter,townSearch):
    mask = df['longitude']!=0
    df = df.loc[mask]
    buttonTextMap='Afficher la carte'
    mapButton = st.button(buttonTextMap)
    df_map = pd.DataFrame()
    if mapButton:
        if(ChooseFilter=='Commune'):
            mask = (df['nom_commune']==townSearch)
        df = df.loc[mask]
        if(ChooseFilter=='Département'):
            mask = (df['code_departement']==townSearch)
            df = df.loc[mask]
        mapButtonHide = st.button("cacher la carte")
        df_map['longitude'] = df['longitude']
        df_map['latitude'] = df['latitude']
        st.map(df_map)

        if mapButtonHide:
            mapButton=False

def chartValeurFonciereMoyenne(df):
    st.subheader("Evolution de la valeur foncière")
    df = df.groupby('date_mutation').mean('valeur_fonciere')
    dfToPlot = pd.DataFrame()
    #dfToPlot['date'] = df['date_mutation']
    dfToPlot['Valeur fonciere'] = df['valeur_fonciere']
    st.line_chart(dfToPlot)

def chartValeurPriceSquareMeter(df):
    st.subheader("Evolution du prix au métre carré")
    df['Price_Square_Meter'] = df['valeur_fonciere'] / df['surface_reelle_bati']
    df = df.groupby('date_mutation').mean('Price_Square_Meter')
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df = df.dropna()
    dfToPlot = pd.DataFrame()
    #dfToPlot['date'] = df['date_mutation']
    dfToPlot['Price_Square_Meter'] = df['Price_Square_Meter']
    st.line_chart(dfToPlot)

def chartValeurPriceSquareMeterCity(df,ChooseFilter,townSearch):
    st.subheader("Evolution du prix au mètre carré")
    if(ChooseFilter=='Commune'):
        mask = (df['nom_commune']==townSearch)
        df = df.loc[mask]
    if(ChooseFilter=='Département'):
        mask = (df['code_departement']==townSearch)
        df = df.loc[mask]
    df['Price_Square_Meter'] = df['valeur_fonciere'] / df['surface_reelle_bati']
    df = df.groupby('date_mutation').mean('Price_Square_Meter')
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df = df.dropna()
    dfToPlot = pd.DataFrame()
    #dfToPlot['date'] = df['date_mutation']
    dfToPlot['Price_Square_Meter'] = df['Price_Square_Meter']
    st.line_chart(dfToPlot)

def chartValeurFonciereMoyenneCity(df,ChooseFilter,townSearch):
    st.subheader("Evolution de la valeur foncière")
    if(ChooseFilter=='Commune'):
        mask = (df['nom_commune']==townSearch)
        df = df.loc[mask]
    if(ChooseFilter=='Département'):
        mask = (df['code_departement']==townSearch)
        df = df.loc[mask]
    df = df.groupby('date_mutation').mean('valeur_fonciere')
    dfToPlot = pd.DataFrame()
    #dfToPlot['date'] = df['date_mutation']
    dfToPlot['Valeur fonciere'] = df['valeur_fonciere']
    st.line_chart(dfToPlot)

def scatterPlotPricetoSurface(df):
    st.subheader("Aperçu général du prix en fonction de la surface")
    fig = px.scatter(df, x="valeur_fonciere", y="surface_reelle_bati")
    st.plotly_chart(fig)

def scatterPlotPricetoSurfaceCity(df,ChooseFilter,townSearch):
    st.subheader("Prix en fonction de la surface")
    if(ChooseFilter=='Commune'):
        mask = (df['nom_commune']==townSearch)
        df = df.loc[mask]
    if(ChooseFilter=='Département'):
        mask = (df['code_departement']==townSearch)
        df = df.loc[mask]
    fig = px.scatter(df, x="valeur_fonciere", y="surface_reelle_bati",color='valeur_fonciere',hover_data=['nature_mutation','adresse_numero','adresse_nom_voie','nom_commune','code_postal'])
    st.plotly_chart(fig)


def slider():
    number = st.slider('Combien de données souhaitez vous afficher ?', 2, 50, 10)
    return number

def PrintDataSet(df):
    st.write(df)

def printData(df):
    st.subheader('Aperçu des données')

    if st.checkbox("Afficher l'ensemble des données"):
        try:
            PrintDataSet(df)
        except:
            st.warning("Nombre de données trop importe, seulement 500 000 données peuvent être affichées")
            PrintDataSet(df(500000))
    else:
        PrintDataSet(df.head(10))

def FindAdressOnmap(df):
    # center on Liberty Bell
    m = folium.Map(location=[df['latitude'], df['longitude']], zoom_start=16)

    # add marker for Liberty Bell
    #tooltip = df['adresse_numero']+" "+df['adresse_nom_voie']+", "+df['nom_commune']+", "+df['code_postal']
    tooltip = " "
    folium.Marker(
        [df['latitude'], df['longitude']], popup=" ", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)

def nav():
    st.sidebar.title("Menu")
    st.sidebar.subheader("Navigation")
    rad = st.sidebar.radio("",["Accueil","Rechercher par commune ou département","Rechercher une adresse"])
    st.sidebar.subheader("Selectionner les années")
    a = st.sidebar.checkbox("2020")
    b = st.sidebar.checkbox("2019")
    c = st.sidebar.checkbox("2018")
    d = st.sidebar.checkbox("2017",True)
    e = st.sidebar.checkbox("2016")
    return rad,a,b,c,d,e

def PrintInfoAdress(df,indice):
    header_1_column, header_2_column,  = st.columns(2)
    header_1_column.text("Type de bien : "+str(df['type_local'][indice]))
    header_2_column.text("Valeur foncière : "+str(df['valeur_fonciere'][indice])+" €")
    header_1_column.text("Surface réelle bati : "+str(df['surface_reelle_bati'][indice]))
    header_2_column.text("Surface du terrain : "+str(df['surface_terrain'][indice]))
    st.text("Nombre de Pieces Principales : "+str(int(df['nombre_pieces_principales'][indice])))
    

def header():
    
    components.html("""
    <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
    <body class="text-gray-700 font-serif"></body>

    <div class="flex flex-col justify-center items-center h-screen w-screen">
    <h1 class="text-4xl font-light text-center leading-tight mb-4">DashBoard<br>Data visualization project</h1>
    <p>by <a href="https://www.linkedin.com/in/william-chenut-875298171/" class="text-blue-500">@Williamcht</a></p>
    </div>
    """,height=200,
    )

def main():
    setIconPage()
    HideStreamlitContent()
    header()
    rad,a,b,c,d,e = nav()
    df=pd.DataFrame()
    df2020=pd.DataFrame()
    df2019=pd.DataFrame()
    df2018=pd.DataFrame()
    df2017=pd.DataFrame()
    df2016=pd.DataFrame()
    loadDataset = st.warning("Loading dataset...")
    if a :
        df2020=FirstLoad()
        if df2020.empty:
            st.error("Erreur données : fichier 'full_2020.csv introuvable'")
    if b :
        df2019=load2019()
        if df2019.empty:
            st.error("Erreur données : fichier 'full_2019.csv introuvable'")
    if c :
        df2018=load2018()
        if df2018.empty:
            st.error("Erreur données : fichier 'full_2018.csv introuvable'")
    if d :
        df2017=load2017()
        if df2017.empty:
            st.error("Erreur données : fichier 'full_2017.csv introuvable'")
    if e :
        df2016=load2016()
        if df2016.empty:
            st.error("Erreur données : fichier 'full_2016.csv introuvable'")

    frames = [df2016,df2017,df2018,df2019,df2020]
    df = pd.concat(frames)
    loadDataset.empty()

    if (rad == "Accueil"):
        
        st.title("Accueil")
        load = st.warning("Loading...")
        progress = st.progress(0)
        
        if not(df.empty):
            df = filterHome(df)
            progress.progress(20) 
            st.success(str(len(df))+" données trouvées")
            progress.progress(30) 
            printData(df)
            progress.progress(40)
            number_of_city_print = slider()
            progress.progress(50) 
            printCityMax(df,number_of_city_print)
            progress.progress(60)
            HighestPriceSquareMeter(df,number_of_city_print)
            progress.progress(70)
            chartValeurFonciereMoyenne(df)
            progress.progress(80)
            chartValeurPriceSquareMeter(df)
            progress.progress(90)
            scatterPlotPricetoSurface(df)
            progress.progress(100) 
        load.empty()
        progress.empty()

    if (rad=="Rechercher par commune ou département"):
        st.title("Rechercher par commune ou département")
        load = st.warning("Loading...")
        progress = st.progress(0)
        if not(df.empty):
            df,townSearch,ChooseFilter = filterCity(df)
            progress.progress(10) 
            st.header("Resultat pour "+townSearch)
            if df.empty:
                st.error("Aucune donnée")
            else:
                st.success(str(len(df))+" données trouvées")
                printData(df)
                progress.progress(20) 
                PriceMeterQuare = PriceMeterQuareCity(df,townSearch,ChooseFilter)
                progress.progress(30) 
                PriceMean = PriceMeanCity(df,townSearch,ChooseFilter)
                progress.progress(40) 
                metricsCity(PriceMeterQuare, PriceMean)
                progress.progress(50) 
                CotaTypeLocalCity(df,ChooseFilter,townSearch)
                progress.progress(60) 
                chartValeurFonciereMoyenneCity(df,ChooseFilter,townSearch)
                progress.progress(70) 
                chartValeurPriceSquareMeterCity(df,ChooseFilter,townSearch)
                progress.progress(80) 
                scatterPlotPricetoSurfaceCity(df,ChooseFilter,townSearch)
                progress.progress(90) 
                mapCity(df,ChooseFilter,townSearch)
                progress.progress(100) 
        load.empty()
        progress.empty()

    if (rad=="Rechercher une adresse"):
        st.title("Rechercher une adresse")
        load = st.warning("Loading...")
        progress = st.progress(0)
        if not(df.empty):
            adresse,indice = filterAdress(df)
            progress.progress(10) 
            adresse=adresse.reset_index()    
            if df.empty:
                st.error("Aucune donnée pour " +str(adresse['adresse_numero'][indice])[:-2] + " "+ str(adresse['adresse_nom_voie'][0]) + ", " + str(adresse['nom_commune'][indice]) + ", "  + str(adresse['code_postal'][indice])[:-2])
            else:
                st.header("Resultat pour " +str(adresse['adresse_numero'][indice])[:-2] + " "+ str(adresse['adresse_nom_voie'][0]) + ", " + str(adresse['nom_commune'][indice]) + ", "  + str(adresse['code_postal'][indice])[:-2])
                PrintInfoAdress(adresse,indice)
                progress.progress(50) 
                FindAdressOnmap(adresse.iloc[[indice]])
                progress.progress(100) 
        load.empty()
        progress.empty()

if __name__ == "__main__":
    main()


