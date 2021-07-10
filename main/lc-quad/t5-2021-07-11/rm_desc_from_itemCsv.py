# %%
# https://www.kaggle.com/kenshoresearch/kdwd-wikidata-small-ontology

#%%
import pandas as pd
import numpy as np
#%%
df_item = pd.read_csv('../../../data/kdwd/item.csv')
del df_item['en_description']

# %%
df_item.head()
# %%
df_item.to_csv('../../../data/kdwd/item_no_des.csv')
# %%
df_item = pd.read_csv('../../../data/kdwd/item_no_des.csv').set_index('item_id')
# %%
del df_item['Unnamed: 0']
df_item['en_label'].replace('', np.nan, inplace=True)
#%%
df_item.dropna(subset=['en_label'], inplace=True)
#%%
df_item['en_label'] = df_item['en_label'].str.lower()
# %%
df_item.to_csv('../../../data/kdwd/item_no_desc.csv')
