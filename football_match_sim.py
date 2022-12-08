import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
import re
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
import random as rnd
 




st.write("""
# Football match simulator

""")

st.sidebar.header('Choose teams')


t1league=st.sidebar.selectbox('Team#1 League',('Premier League','LaLiga','Serie A','Bundesliga','Ligue 1','Liga Portugal','Eredvisie'))
if t1league=='Premier League':
    t1leagueref='/en/comps/9/Premier-League-Stats'
    team1=st.sidebar.selectbox('Team #1', ('Arsenal','Aston Villa','Bournemouth','Brentford','Brighton','Chelsea','Crystal Palace','Everton','Fulham','Leeds United',
            'Leicester City','Liverpool','Manchester City','Manchester Utd','Newcastle Utd','Nott\'ham Forest','Southampton',
            'Tottenham','West Ham', 'Wolves'))
elif t1league =='LaLiga':
    t1leagueref='/en/comps/12/La-Liga-Stats'
    team1=st.sidebar.selectbox('Team #1',('Almería','Athletic Club','Atlético Madrid','Barcelona','Betis','Cádiz','Celta Vigo','Elche','Espanyol','Getafe','Girona','Mallorca',
           'Osasuna','Rayo Vallecano','Real Madrid','Real Sociedad','Sevilla','Valencia','Valladolid','Villarreal'))
elif t1league == 'Serie A':
    t1leagueref='/en/comps/11/Serie-A-Stats'
    team1=st.sidebar.selectbox('Team #1', ('Atalanta','Bologna','Cremonese','Empoli','Fiorentina','Hellas Verona','Inter','Juventus','Lazio','Lecce','Milan',
            'Monza','Napoli','Roma','Salernitana','Sampdoria','Sassuolo','Spezia','Torino','Udinese'))
elif t1league == 'Bundesliga':
    t1leagueref='/en/comps/20/Bundesliga-Stats'
    team1=st.sidebar.selectbox('Team #1',('Augsburg','Bayern Munich','Bochum','Dortmund','Eint Frankfurt','Freiburg','Hertha BSC','Hoffenheim','Köln','Leverkusen',
           'M\'Gladbach','Mainz 05','RB Leipzig','Schalke 04','Stuttgart','Union Berlin','Werder Bremen','Wolfsburg'))
elif t1league == 'Ligue 1':
    t1leagueref='/en/comps/13/Ligue-1-Stats'
    team1=st.sidebar.selectbox('Team #1',('Ajaccio','Angers','Auxerre','Brest','Clermont Foot','Lens','Lille','Lorient','Lyon','Marseille','Monaco','Montpellier','Nantes',
           'Nice','Paris S-G','Reims','Rennes','Strasbourg','Toulouse','Troyes'))
elif t1league == 'Liga Portugal':
    t1leagueref='/en/comps/32/Primeira-Liga-Stats'
    team1=st.sidebar.selectbox('Team #1',('Arouca','Benfica','Boavista','Braga','Casa Pia','Chaves','Estoril','Famalicão','Gil Vicente FC','Marítimo','Paços',
            'Portimonense','Porto','Rio Ave','Santa Clara','Sporting CP','Vitória','Vizela'))
elif t1league == 'Eredvisie':  
    t1leagueref='/en/comps/23/Eredivisie-Stats'
    team1=st.sidebar.selectbox('Team #1',('Ajax','AZ Alkmaar','Cambuur','Emmen','Excelsior','Feyenoord','Fortuna Sittard','Go Ahead Eag','Groningen','Heerenveen','NEC Nijmegen',
            'PSV Eindhoven','RKC Waalwijk','Sparta R\'dam','Twente','Utrecht','Vitesse','Volendam'))
     
t2league=st.sidebar.selectbox('Team#2 League',('Premier League','LaLiga','Serie A','Bundesliga','Ligue 1','Liga Portugal','Eredvisie'))
if t2league=='Premier League':
    t2leagueref='/en/comps/9/Premier-League-Stats'
    team2=st.sidebar.selectbox('Team #2', ('Arsenal','Aston Villa','Bournemouth','Brentford','Brighton','Chelsea','Crystal Palace','Everton','Fulham','Leeds United',
            'Leicester City','Liverpool','Manchester City','Manchester Utd','Newcastle Utd','Nott\'ham Forest','Southampton',
            'Tottenham','West Ham', 'Wolves'))
elif t2league =='LaLiga':
    t2leagueref='/en/comps/12/La-Liga-Stats'
    team2=st.sidebar.selectbox('Team #2',('Almería','Athletic Club','Atlético Madrid','Barcelona','Betis','Cádiz','Celta Vigo','Elche','Espanyol','Getafe','Girona','Mallorca',
           'Osasuna','Rayo Vallecano','Real Madrid','Real Sociedad','Sevilla','Valencia','Valladolid','Villarreal'))
elif t2league == 'Serie A':
    t2leagueref='/en/comps/11/Serie-A-Stats'
    team2=st.sidebar.selectbox('Team #2', ('Atalanta','Bologna','Cremonese','Empoli','Fiorentina','Hellas Verona','Inter','Juventus','Lazio','Lecce','Milan',
            'Monza','Napoli','Roma','Salernitana','Sampdoria','Sassuolo','Spezia','Torino','Udinese'))
elif t2league == 'Bundesliga':
    t2leagueref='/en/comps/20/Bundesliga-Stats'
    team2=st.sidebar.selectbox('Team #2',('Augsburg','Bayern Munich','Bochum','Dortmund','Eint Frankfurt','Freiburg','Hertha BSC','Hoffenheim','Köln','Leverkusen',
           'M\'Gladbach','Mainz 05','RB Leipzig','Schalke 04','Stuttgart','Union Berlin','Werder Bremen','Wolfsburg'))
elif t2league == 'Ligue 1':
    t2leagueref='/en/comps/13/Ligue-1-Stats'
    team2=st.sidebar.selectbox('Team #2',('Ajaccio','Angers','Auxerre','Brest','Clermont Foot','Lens','Lille','Lorient','Lyon','Marseille','Monaco','Montpellier','Nantes',
           'Nice','Paris S-G','Reims','Rennes','Strasbourg','Toulouse','Troyes'))
elif t2league == 'Liga Portugal':
    t2leagueref='/en/comps/32/Primeira-Liga-Stats'
    team2=st.sidebar.selectbox('Team #2',('Arouca','Benfica','Boavista','Braga','Casa Pia','Chaves','Estoril','Famalicão','Gil Vicente FC','Marítimo','Paços',
            'Portimonense','Porto','Rio Ave','Santa Clara','Sporting CP','Vitória','Vizela'))
elif t2league == 'Eredvisie':  
    t2leagueref='/en/comps/23/Eredivisie-Stats'
    team2=st.sidebar.selectbox('Team #2',('Ajax','AZ Alkmaar','Cambuur','Emmen','Excelsior','Feyenoord','Fortuna Sittard','Go Ahead Eag','Groningen','Heerenveen','NEC Nijmegen',
            'PSV Eindhoven','RKC Waalwijk','Sparta R\'dam','Twente','Utrecht','Vitesse','Volendam'))   
     
     
def get_soup(url: str) -> BeautifulSoup:
    """
    Fetch the html for the given player URL and return a BeautifulSoup object.
    Arguments:
        url -- player's URL path as a string
    """
    try:
        request = Request(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                                            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                                                      'q=0.9,image/webp,*/*;q=0.8'})
    except ValueError as e:
        print("requests: get_soup: ", e)
        return None

    try:
        html = urlopen(request)
    except (ValueError, URLError) as e:
        print("requests: get_soup: ", e)
        return None
    
    try:
        return BeautifulSoup(html, 'html.parser')
    except Exception as e:
        print("requests: get_soup: ", e)
        return None

        
def get_squads_new(league,team):
    """
    Crawl a league page and collect all team URLs.
    Arguments:
         league -- single URL of a league
    Returns:
        List of strings. Each string is a unique team URL.
    """
    url = f'https://fbref.com{league}'
    soup = get_soup(url)

    links = []

    for link in soup.find("table").find_all('a', href=re.compile('(\/squads\/)')):
        links.append(link.attrs['href'])
    
    table=soup.find_all('table')[0]
    names1 = pd.read_html(str(table))[0]
    names=names1['Squad'].tolist()
    
    dic = {names[i]: links[i] for i in range(len(names))}
    
    url1 = f'https://fbref.com{dic[team]}'
    soup1 = get_soup(url1)
    team_table = soup1.find_all(id="matchlogs_for")[0]
    tm_tb = pd.read_html(str(team_table))[0]
    return tm_tb

def time_update(team):
    team.Date = team.Date.apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d', errors='ignore'))
    today = date.today()
    d1 = today.strftime("%Y/%m/%d")
    team1 = team[team['Date'] < pd.to_datetime(d1, format='%Y%m%d', errors='ignore')]
    return team1


def if_pen(x):
    if '(' in x:
        return x.split('(')[0]
    else:
        return x

def norm(team):
    team=team.drop(team[pd.isnull(team['Result'])].index)
    if type(team.iloc[1]['GF'])!=str:
        return team
    else:
        team['GF']=team['GF'].apply(lambda x:if_pen(x))
        team['GA']=team['GA'].apply(lambda x:if_pen(x))
        team['GF']=team['GF'].astype(int)
        team['GA']=team['GA'].astype(int)
        return team    

# team1_fix=get_squads_new(t1leagueref,team1)
# team2_fix=get_squads_new(t2leagueref,team2)
# team11=time_update(team1_fix)
# team22=time_update(team2_fix)

# team11=norm(team11)
# team22=norm(team22)



# team1gf = team11['GF'].mean()
# team2gf = team22['GF'].mean()
# team1gfstd = team11['GF'].std()
# team2gfstd = team22['GF'].std()

# team1ga = team11['GA'].mean()
# team2ga = team22['GA'].mean()
# team1gastd = team11['GA'].std()
# team2gastd = team22['GA'].std()



# team1xg = team11['xG'].mean()
# team2xg = team22['xG'].mean()
# team1xgstd = team11['xG'].std()
# team2xgstd = team22['xG'].std()

# team1xa = team11['xGA'].mean()
# team2xa = team22['xGA'].mean()
# team1xastd = team11['xGA'].std()
# team2xastd = team22['xGA'].std()


def gameSimScore():
    Team1Score = (rnd.gauss(team1gf,team1gfstd)+ rnd.gauss(team2ga,team2gastd)+rnd.gauss(team1xg,team1xgstd)+ rnd.gauss(team2xa,team2xastd))/4
    Team2Score = (rnd.gauss(team2gf,team2gfstd)+ rnd.gauss(team1ga,team1gastd)+rnd.gauss(team2xg,team2xgstd)+ rnd.gauss(team1xa,team1xastd))/4
    return round(Team1Score),round(Team2Score)
    


def gameSimAd():
    Team1Score = (rnd.gauss(team1gf,team1gfstd)+ rnd.gauss(team2ga,team2gastd)+rnd.gauss(team1xg,team1xgstd)+ rnd.gauss(team2xa,team2xastd))/4
    Team2Score = (rnd.gauss(team2gf,team2gfstd)+ rnd.gauss(team1ga,team1gastd)+rnd.gauss(team2xg,team2xgstd)+ rnd.gauss(team1xa,team1xastd))/4
    if int(round(Team1Score)) > int(round(Team2Score)):
        return 1
    elif int(round(Team1Score)) < int(round(Team2Score)):
        return -1
    else: return 0
    
    
    
def gamesSimAD(ns):
    gamesout = []
    team1win = 0
    team2win = 0
    tie = 0
    for i in range(ns):
        gm = gameSimAd()
        gamesout.append(gm)
        if gm == 1:
            team1win +=1 
        elif gm == -1:
            team2win +=1
        else: tie +=1 
    print('Team1 Win', team1win/(team1win+team2win+tie),'%')
    print('Team2 Win ', team2win/(team1win+team2win+tie),'%')
    print('Draw ', tie/(team1win+team2win+tie), '%')
    return team1win/(team1win+team2win+tie),team2win/(team1win+team2win+tie),tie/(team1win+team2win+tie)



st.subheader('Result')
if st.button('Simulate'):
    team1_fix=get_squads_new(t1leagueref,team1)
    team2_fix=get_squads_new(t2leagueref,team2)
    team11=time_update(team1_fix)
    team22=time_update(team2_fix)

    team11=norm(team11)
    team22=norm(team22)



    team1gf = team11['GF'].mean()
    team2gf = team22['GF'].mean()
    team1gfstd = team11['GF'].std()
    team2gfstd = team22['GF'].std()

    team1ga = team11['GA'].mean()
    team2ga = team22['GA'].mean()
    team1gastd = team11['GA'].std()
    team2gastd = team22['GA'].std()



    team1xg = team11['xG'].mean()
    team2xg = team22['xG'].mean()
    team1xgstd = team11['xG'].std()
    team2xgstd = team22['xG'].std()
    
    team1xa = team11['xGA'].mean()
    team2xa = team22['xGA'].mean()
    team1xastd = team11['xGA'].std()
    team2xastd = team22['xGA'].std()
    last=gameSimScore()
    res=gamesSimAD(100000)
    r1=res[0]
    r2=res[1]
    r3=res[2]
    st.write('Last game')
    st.write(team1, last[0],' - ', last[1], team2)
    st.write(team1,'wins -', r1*100,'%')
    st.write(team2,'wins -', r2*100,'%')
    st.write('Draw -', r3*100,'%')

    

     
     
     
     
     
    
    
    