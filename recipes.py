# -----------------------------------------
# Program by Vayradyan.S.
#
# Hello everyone!
# ----------------------------------------
import pandas as pd
from joblib import load


class Forecast:

  '''
  Предсказание рейтинга блюда или его класса
  '''

  def __init__(self, l_ingredients):
    self.l_ingredients = l_ingredients
    epi_r = pd.read_csv("D:/DS/DS_15/epi_r_update2.csv", index_col='title')
    epi_r.drop(columns='rating', inplace=True)
    self.available_ingredients = epi_r.columns.to_list()

  def preprocess(self):

    '''
    Этот метод преобразует список ингредиентов в структуру данных,
    которые используется в алгоритмах машинного обучения, чтобы сделать предсказание
    '''

    vector = pd.DataFrame(0, index=[0], columns=self.available_ingredients)
    if set(self.l_ingredients).issubset(self.available_ingredients):
      vector[self.l_ingredients] = 1
    return vector

  def predict_rating(self):

    '''
    Этот метод возвращает рейтинг для списка ингредиетов, используя регрессионную модель,
    которая была обучена заранее. Помимо самого рейтинга, метод также возвращает текст,
    который дает интерпретацию этого рейтинга и дает рекомендацию, как в примере выше.
    '''

    X = self.preprocess()
    if X.sum(axis=1)[0] == 0:
      return None, "Рейтинга для этих блюд из данных ингредиентов нет"
    else:
      model = load("D:/DS/DS_15/best_regression.joblib")
      rating = model.predict(X)
      return round(rating[0], 3)

  def predict_rating_category(self):

    '''
    Этот метод возвращает рейтинговую категорию для списка ингредиентов,
    используея классификационную модель, которая была обучена заранее.
    Помимо самого рейтинга, метод возвращает также и текст, который дает интерпретацию этой категории и дает рекомендации,
    как в примере выше
    '''

    X = self.preprocess()
    if X.sum(axis=1)[0] == 0:
      return "Рейтинга для этих блюд из данных ингредиентов нет"
    else:
      model = load("D:/DS/DS_15/best_classifer_r_forest.joblib")
      rating = model.predict(X)
      if rating == 'bad':
        return "Невкусное"
      elif rating == 'so-so':
        return "Не плохое"
      else:
        return "Вкусное"



class NutritionFacts:

  '''
  Выдает информацию о пищевой ценности ингредиентов
  '''

  def __init__(self, l_ingredients):
    self.l_ingredients = l_ingredients
    self.day_per = pd.read_csv("D:/DS/DS_15/day_per_df.csv", index_col='ingredients')

  def retrieve(self):

    '''
    Этот метод получает всю имеющую информацию о пищевой ценности из файла с заранее собраной информацией по заданным данным.
    Он возвращает ее в том виде, который вам кажется наиболее удобным и подходящим.
    '''

    facts = {}
    for ingredient in self.l_ingredients:
      try:
        facts[ingredient] = self.day_per.loc[ingredient, :]
        facts[ingredient].dropna(inplace=True)
        facts[ingredient].sort_values(ascending=False, inplace=True)
        if facts[ingredient].shape[0] == 0:
          facts[ingredient] = 'Нет данных о пищевой ценности этого ингредиента'
      except:
        facts[ingredient] = 'Нет данных о пищевой ценности этого ингредиента'
    return facts

  def filter(self, nutrients, x):
    """"""
    print('II. ПИЩЕВАЯ ЦЕННОСТЬ', '\n')
    facts = self.retrieve()
    for i, j in facts.items():
      print(i, '\n')
      if type(j) == str:
        print(j)
      else:
        full_list = list(set(j.index[:x]).union(nutrients))
        short = j[full_list]
        short.sort_values(ascending=False, inplace=True)
        for indx in short.index:
          print(indx + ' - ' + str(round(short[indx])) + '% of daily value')
      print()


class SimilarRecipes:

  def __init__(self, l_ingredients):
    self.l_ingredients = l_ingredients
    epi_r = pd.read_csv('epi_r_update2.csv', index_col='title')
    epi_r.drop(columns='rating', inplace=True)
    self.epi_r = epi_r
    self.full_recipes = pd.read_json('full_format_recipes2.json', orient='records')
    self.full_recipes.set_index('title', inplace=True)


  def find_all(self):
    if set(self.l_ingredients).issubset(self.epi_r.columns):
      recipes = self.epi_r[self.l_ingredients]
      all_included = recipes.sum(axis=1) == len(self.l_ingredients)
      return recipes.loc[all_included].index.to_list()
    else:
      return []


  def top_similar(self, n):
    recipes = self.find_all()  # Список рецептов со всеми требуемыми продуктами
    if len(recipes) == 0:
      print('Рецептов с таким набором ингредиентов не найдено')
    else:
      df = self.epi_r.loc[recipes]
      df['total_ingredients'] = df.sum(axis=1)
      df.sort_values(by='total_ingredients', ascending=True, inplace=True)
      max_ingredients = len(self.l_ingredients) + 5
      df.query('total_ingredients <= @max_ingredients', inplace=True)
      final_list = df.index.to_list()
      if n < len(final_list):
        final_list = final_list[:n]
      if len(final_list) == 0:
        print('Подходящих рецептов не найдено (требуется > 5 дополнительных ингредиентов)')
      else:
          for name in final_list:
            print(name)
            print('Рейтинг: ', self.full_recipes.loc[name, 'rating'])
            print('Ингредиенты: ')
            for ingredient in self.full_recipes.loc[name, 'ingredients']:
              print('-----', ingredient)
            print('Порядок приготовления: ')
            for item in self.full_recipes.loc[name, 'directions']:
              print('   ', item)
            print('Калории: ', self.full_recipes.loc[name, 'calories'])
            print('Белки: ', self.full_recipes.loc[name, 'protein'])
            print('Жиры: ', self.full_recipes.loc[name, 'fat'])
            print('Натрий: ', self.full_recipes.loc[name, 'sodium'])
            print()
