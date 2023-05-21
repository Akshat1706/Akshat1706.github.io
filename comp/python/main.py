import numpy as np
import pandas as pd
dfDeliveries = pd.read_csv('E:\Portfolio\comp\data.csv')


dfMatches = pd.read_csv('E:\Portfolio\comp\data1.csv')
dfDeliveries.head()




dfDeliveries = pd.read_csv('E:\Portfolio\comp\data.csv')
dfDeliveries.head()
dfDeliveries = dfDeliveries.merge(dfMatches, on='ID')
dfDeliveries['BowlingTeam'] = np.where(dfDeliveries['BattingTeam']==dfDeliveries['Team1'],
                                       dfDeliveries['Team2'],
                                       dfDeliveries['Team1'])
dfDeliveries.head()
dfBatsmen = dfDeliveries.groupby('batter')\
            .agg({'ID':'nunique','batsman_run':'sum','isWicketDelivery':'sum'})\
            .reset_index()
dfBatsmen.head()
dfBatsmen.columns = ['Batter','Innings','Runs','Dismissals']
dfBatsmen.head()
dfBallsFaced = dfDeliveries[(dfDeliveries['extra_type']!='wides')].groupby('batter')['ID'].count().reset_index()
dfBallsFaced.columns = ['Batter','Balls Faced']
dfBallsFaced = dfDeliveries[(dfDeliveries['extra_type']!='wides')].groupby('batter')['ID'].count().reset_index()



dfBallsFaced.columns = ['Batter','Balls Faced']
dfBallsFaced.head()
dfBatter4s = dfDeliveries[(dfDeliveries['batsman_run']==4)&(dfDeliveries['non_boundary']==0)]\
            .groupby('batter')['ID']\
            .count()\
            .reset_index()\
            .sort_values('ID')
dfBatter4s.columns = ['Batter','4s']
dfBatter4s = dfDeliveries[(dfDeliveries['batsman_run']==4)&(dfDeliveries['non_boundary']==0)]\
            .groupby('batter')['ID']\
            .count()\
            .reset_index()\
            .sort_values('ID')

dfBatter4s.columns = ['Batter','4s']
dfBatter4s.head()
dfBatter6s = dfDeliveries[(dfDeliveries['batsman_run']==6)&(dfDeliveries['non_boundary']==0)]\
            .groupby('batter')['ID']\
            .count()\
            .reset_index()\
            .sort_values('ID')
dfBatter6s.columns = ['Batter','6s']
dfBatter6s.head()
dfMatchWise = dfDeliveries.groupby(['batter','ID'])['batsman_run'].sum().reset_index()
dfMatchWise.head()
dfHighScore = dfMatchWise.groupby(['batter'])['batsman_run'].max().reset_index()
dfHighScore.columns = ['Batter','High Score']
dfHighScore.head()
df50s = dfMatchWise[(dfMatchWise['batsman_run']>=50)&(dfMatchWise['batsman_run']<100)]\
        .groupby('batter')['batsman_run']\
        .count()\
        .reset_index()\
        .sort_values('batsman_run',ascending=False)
df50s.columns = ['Batter','50']
df50s.head()
df100s = dfMatchWise[(dfMatchWise['batsman_run']>=100)]\
        .groupby('batter')['batsman_run']\
        .count()\
        .reset_index()\
        .sort_values('batsman_run',ascending=False)
df100s.columns = ['Batter','100']
df100s.head()
dfBatsmen = dfBatsmen.merge(dfBallsFaced, on='Batter',how='outer').merge(dfBatter4s, on='Batter',how='outer')\
                     .merge(dfBatter6s, on='Batter',how='outer').merge(dfHighScore, on='Batter',how='outer')\
                     .merge(df50s, on='Batter',how='outer').merge(df100s, on='Batter',how='outer')
dfBatsmen.head()
dfBatsmen['Strike Rate'] = (dfBatsmen['Runs']/dfBatsmen['Balls Faced'])*100
dfBatsmen['Batting Average'] = dfBatsmen['Runs']/dfBatsmen['Dismissals']
dfBatsmen.fillna(0, inplace=True)
dfBatsmen.sort_values(by='Runs', ascending=False).head
def overClassifier(val):
    if val>=0 and val<6:
        return 'Power Play'
    elif val>=6 and val<15:
        return 'Middle Overs'
    else:
        return 'Death Overs'
    dfDeliveries['PhaseOfPlay'] = dfDeliveries['overs'].map(overClassifier)
    dfDeliveries[['overs','PhaseOfPlay']].sort_values('overs').drop_duplicates().reset_index(drop=True)
dfDeathOvers = dfDeliveries[dfDeliveries['PhaseOfPlay']=='Death Overs']
dfDeathOvers = dfDeliveries[dfDeliveries['PhaseOfPlay']=='Death Overs']
dfBatsmen.sort_values(by='Runs', ascending=False).head()
dfDeathBowling = dfDeathOvers.groupby('BowlingTeam').agg({'total_run':'sum','isWicketDelivery':'sum'}).reset_index()
dfBatsmen.sort_values(by='Runs', ascending=False).head()


