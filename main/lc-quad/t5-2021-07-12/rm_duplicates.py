# Reduce item.csv 43232907 rows to 39368590 rows

#%%
import pandas as pd

#%%
df = pd.read_csv("../../../data/kdwd/item_no_desc.csv")
# %%
df.set_index(["item_id"], inplace=True)
# %%
df["en_label"] = df["en_label"].str.lower()
df.drop_duplicates(subset=["en_label"], keep="first", inplace=True)
# %%
df.to_csv("../../../data/kdwd/item_no_dupl.csv")

# %%
# No Duplicates in property.csv - remove description column
#%%
df = pd.read_csv("../../../data/kdwd/property.csv")
# %%
del df["en_description"]
df.set_index(["property_id"], inplace=True)

# %%
df["en_label"] = df["en_label"].str.lower()
df.drop_duplicates(subset=["en_label"], keep="first", inplace=True)
# %%
df.to_csv("../../../data/kdwd/property_no_dupl.csv")

# %%
# Reduce aliases from 6823024 to 4798163
#%%
df = pd.read_csv("../../../data/kdwd/item_aliases.csv")
#%%
df
# %%
df.set_index(["item_id"], inplace=True)
# %%
df["en_alias"] = df["en_alias"].str.lower()
df.drop_duplicates(subset=["en_alias"], keep="first", inplace=True)

# %%
df.to_csv("../../../data/kdwd/item_aliases_no_dupl.csv")
