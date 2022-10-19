import pandas as pd

df = pd.DataFrame(columns=['Candidato', 'Votos'])

def votar(cand):
    cons = df.loc[df['Candidato'] == cand]
    if len(cons) > 0:
        votos = df['Votos'].loc[df['Candidato'] == cand]
        f = df.index[df['Candidato'] == cand].tolist()
        df.iat[f[0], 1] = votos[f[0]] + 1
    else:
        df.loc[len(df), ['Candidato','Votos']] = cand, 1

