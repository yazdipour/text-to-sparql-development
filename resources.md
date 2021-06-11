# Resources

- Function Parser used in CodeSearchNet: https://github.com/ncoop57/function_parser

# Dataset

https://github.com/AKSW/DBNQA
https://github.com/castorini/SimpleDBpediaQA

## 1st Attempt

https://github.com/ag-sc/QALD/

- Less than 700 records

## 2nd Attempt

http://lc-quad.sda.tech/
https://github.com/AskNowQA/LC-QuAD

LC-QuAD 2.0 is a Large Question Answering dataset with 30,000 pairs of question and its corresponding SPARQL query. The target knowledge base is Wikidata and DBpedia, specifically the 2018 version.

https://github.com/AskNowQA/LC-QuAD2.0 #19293+4781 data

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