import requests
import json
import pandas as pd
def get_matches():
    url="http://127.0.0.1:5000/matchs"
    partidos = requests.get(url).json()
    return partidos

def get_matchs_columns(columns):
    df = pd.DataFrame(get_matches())
    df = df[columns]
    return df

#Devuelve una serie de partidos segun parametros()
def search_matchs(parametros):
    url=f"http://127.0.0.1:5000/matchs/search"
    partidos = requests.get(url,params=parametros).json()
    return partidos

def lista_sel():
    url = "http://127.0.0.1:5000/matchs/list_sel"
    return requests.get(url).json()

def get_goals(partidos):
    df = pd.DataFrame(partidos)
    print(df)
    g_home = df.groupby(["team_name_home"]).sum().reset_index()
    g_away = df.groupby(["team_name_away"]).sum().reset_index()
    new = pd.DataFrame([g_away["team_name_away"],g_away["team_away_score"],g_home["team_home_score"]])
    new = new.T
    new["tot"]= new["team_home_score"]+new["team_away_score"]
    new.rename(columns={'team_home_score': 'home', 
                           'team_away_score': 'away',
                           'team_name_away': 'team'}, inplace=True)
    return new


def list_rounds():
    df = pd.DataFrame(get_matches())

    return df["stage"].unique()


