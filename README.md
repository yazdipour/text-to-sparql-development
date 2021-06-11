# Text 2 SPARQL

## Resources

- Function Parser used in CodeSearchNet: https://github.com/ncoop57/function_parser

# Dataset

## QALD

https://github.com/ag-sc/QALD/

- Can not merge QALD v9 with v8 and before, because of huge amount of similarity.
- Less than 700 records

## LC-QuAD

LC-QuAD 2.0 is a Large Question Answering dataset with 30,000 pairs of question and its corresponding SPARQL query. The target knowledge base is Wikidata and DBpedia, specifically the 2018 version.

- https://github.com/AskNowQA/LC-QuAD2.0
- http://lc-quad.sda.tech/
- 19293 + 4781 data

### LC-QuAD2 Data Fields

- NNQT_question: a string feature.
- uid: a int32 feature.
- subgraph: a string feature.
- template_index: a int32 feature.
- question: a string feature.
- sparql_wikidata: a string feature.
- sparql_dbpedia18: a string feature.
- template: a string feature.
- paraphrased_question: a string feature.

## Other Datasets

- https://github.com/AKSW/DBNQA
- https://github.com/castorini/SimpleDBpediaQA