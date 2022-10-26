import pandas as pd

df = pd.DataFrame(columns=['Candidato', 'Votos'])
df1 = pd.DataFrame(columns=['Candidato', 'Votos'])


def votar(cand):
    cons = df.loc[df['Candidato'] == cand]
    if len(cons) > 0:
        votos = df['Votos'].loc[df['Candidato'] == cand]
        f = df.index[df['Candidato'] == cand].tolist()
        df.iat[f[0], 1] = votos[f[0]] + 1
    else:
        df.loc[len(df), ['Candidato', 'Votos']] = cand, 1


def votar1(cand):
    cons = df1.loc[df1['Candidato'] == cand]
    if len(cons) > 0:
        votos = df1['Votos'].loc[df1['Candidato'] == cand]
        f = df1.index[df1['Candidato'] == cand].tolist()
        df1.iat[f[0], 1] = votos[f[0]] + 1
    else:
        df1.loc[len(df1), ['Candidato', 'Votos']] = cand, 1
