import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('../boardgames.csv')
df.drop(df.loc[df['best_for'] == 0].index, inplace=True)


def best_for_chart_bar():
  chart = df.groupby(['best_for']).best_for.count().sort_values().plot(kind='bar')
  plt.savefig('./best_for_chart_bar.png')
  return chart


def correlation_matrix():
  corr_df = df.corr(method='pearson')
  plt.figure(figsize=(8, 6))
  sns.heatmap(corr_df, annot=True)
  plt.show()
  plt.savefig('./corr.png')
  # Just to check possible relation between year and popularity ~ Don't relevant in this case.


def get_most_popular_game():
  most_popular = df.loc[df['popularity'] == df['popularity'].max()]
  return most_popular


def get_less_popular_game():
  less_popular = df.loc[df['popularity'] == df['popularity'].min()]
  return less_popular


def heavier_game():
    heavier = df.loc[df['weigth'] == df['weigth'].max()]
    return heavier


def lighter_game():
    lighter = df.loc[df['weigth'] == df['weigth'].min()]
    return lighter
