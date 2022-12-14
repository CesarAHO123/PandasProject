from unicodedata import category
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm
data = pd.read_csv("CleanDB/top_movies_clean.csv")
#data = data.loc[(data.budget > 10000) & (data.revenue > 10000)]
data_test = data.groupby(['genre', 'release_date'])[
    'revenue'].aggregate(pd.DataFrame.sum)
#data_test = data_test.to_frame()
data_test = data_test.to_frame()
data_test.boxplot(by="genre", figsize=(18, 9))
plt.xlabel("Genero")
plt.ylabel("Ganancia")
plt.title("Ganancia de las peliculas por genero")
plt.savefig("img/p7_classificatedData.png")
plt.show()
plt.close()
