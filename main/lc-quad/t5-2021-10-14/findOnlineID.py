# !pip install timeout-decorator
# https://www.wikidata.org/wiki/Q1
# https://www.wikidata.org/wiki/Property:P106
# https://github.com/dahlia/wikidata
from wikidata.client import Client
from wikidata.entity import EntityId
import timeout_decorator
import pandas as pd

client = Client()


@timeout_decorator.timeout(1)
def findOnline(idWithPrefix):
    return client.get(EntityId(idWithPrefix), load=False).label["en"]

    # read a file line by line


def read_file_list(file_name):
    with open(file_name, "r") as f:
        return list(f)


unknowns = read_file_list("err.txt")
# remove duplicates in a list
def remove_duplicates(l):
    return list(dict.fromkeys(l))


unknowns = remove_duplicates(unknowns)
del unknowns[0]
print(len(unknowns))
findings = {}
err = []
for d in tqdm(unknowns):
    try:
        findings[int(d[1:-1])] = findOnline(d[:-1])
    except:
        err.append(d)
# dict to dataframe
def dict_to_df(d):
    df = pd.DataFrame(columns=["id", "en"])
    for k, v in d.items():
        df = df.append({"id": k, "en": v}, ignore_index=True)
    return df


foundIDS = dict_to_df(findings).set_index("id")
# save dataframe
foundIDS.to_csv("item5.csv")
