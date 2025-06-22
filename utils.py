from functools import reduce
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def list_column_count_inplace(df, column_name):
   col_json = df[column_name].apply(lambda x: eval(x) if not pd.isnull(x) else [])
   possible_values = reduce(lambda x, y: set(x).union(y), col_json)
   col_names = []

   for value in possible_values:
      value_exists = col_json.apply(lambda x: list(x).count(value))
      df[f'{column_name}_{value}'] = value_exists
      col_names.append(f'{column_name}_{value}')

   return column_name, list(possible_values)


def list_column_binarize_inplace(df, column_name):
   col_json = df[column_name].apply(lambda x: eval(x) if not pd.isnull(x) else [])
   possible_values = reduce(lambda x, y: set(x).union(y), col_json)
   col_names = []


   for value in possible_values:
      value_exists = col_json.apply(lambda x: 1 if value in x else 0)
      df[f'{column_name}_{value}'] = value_exists
      col_names.append(f'{column_name}_{value}')

   return column_name, list(possible_values)


def get_possible_values(df, column_name):
   col_json = df[column_name].apply(lambda x: eval(x) if not pd.isnull(x) else [])
   possible_values = reduce(lambda x, y: set(x).union(y), col_json)
   return possible_values


def split_words(df, col):
   items = df[col].unique()
   words = []
   for item in items:
      split_words = item.split(' ')
      words.extend(split_words)

   words = [w.strip(' ').strip(',') for w in words]
   return words


def to_array(val):
   split_words = val.split(' ')
   words = [w.strip(' ').strip(',') for w in split_words]
   return str(words)


def plot_histograms_for_col_group(df, cols):
   fig, ax = plt.subplots(1, len(cols[1]), figsize=(12,5), sharey=True)

   for i, col in enumerate(cols[1]):
      df[f"{cols[0]}_{col}"].plot(kind='hist', ax=ax[i])
      ax[i].set_title(col)

   plt.show()



def count_binarized_group(df, col_names):
    aux_df = df[[f"{col_names[0]}_{col_names[1][i]}" for i in range(1, len(col_names[1]))]]
    counts = pd.DataFrame(aux_df.sum(), columns=["count"])
    counts.sort_values(by="count", ascending=False, inplace=True)
    return counts
