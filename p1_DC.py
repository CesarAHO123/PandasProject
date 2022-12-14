import pandas as pd
import json
from types import SimpleNamespace


def get_genre(row):
    aux = ""
    aux2 = str(row.genre)
    aux2 = aux2.replace('[', '')
    aux2 = aux2.replace(']', '')
    aux2 = aux2.replace('},', '}},')
    aux3 = aux2.split("},")
    x = json.loads(aux3[0], object_hook=lambda d: SimpleNamespace(**d))
    aux = x.name
    row.genre = aux
    return row


def get_keywords(row):
    aux = []
    aux2 = str(row.keywords)
    aux2 = aux2.replace('[', '')
    aux2 = aux2.replace(']', '')
    aux2 = aux2.replace('},', '}},')
    aux3 = aux2.split("},")
    for key in aux3:
        x = json.loads(key, object_hook=lambda d: SimpleNamespace(**d))
        aux.append(x.name)
    row.keywords = aux
    return row


data = pd.read_csv("top_movies.csv")
data = data.drop(columns=["homepage", "production_countries",
                 "production_companies", "spoken_languages", "status", "original_title", "overview"])
data = data.dropna().set_index("id").sort_values("id")
data = data.loc[(data.budget > 10000) & (data.revenue > 100) &
                (data.genres != "[]") & (data.keywords != "[]") & (data.vote_count > 100)]
data = data.rename(columns={"vote_average": "score", "genres": "genre"})
data = data.apply(get_genre, axis="columns")
data = data.apply(get_keywords, axis="columns")
data.to_csv("./CleanDB/top_movies_clean.csv")
print(data)
