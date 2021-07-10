# Text 2 SPARQL

- (itm prop vlu) 
- Q=identifier
P- =Property

## Wikidata Q/Ps

[Dictionary of all properties and identifiers in Wikidata](https://www.kaggle.com/kenshoresearch/kdwd-wikidata-small-ontology)

## Data Sample

- <https://huggingface.co/datasets/lc_quad>
- <https://huggingface.co/datasets/viewer/?dataset=lc_quad>

```
{'NNQT_question': 'What is the {periodical literature} for {mouthpiece} of {Delta Air Lines}',

 'paraphrased_question': "What is Delta Air Line's periodical literature mouthpiece?",

'question': 'What periodical literature does Delta Air Lines use as a moutpiece?',

'sparql_dbpedia18': 'select distinct ?obj where { ?statement <http://www.w3.org/1999/02/22-rdf-syntax-ns#subject> <http://wikidata.dbpedia.org/resource/Q188920> . ?statement <http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate> <http://www.wikidata.org/entity/P2813> . ?statement <http://www.w3.org/1999/02/22-rdf-syntax-ns#object> ?obj . ?obj <http://www.wikidata.org/entity/P31> <http://wikidata.dbpedia.org/resource/Q1002697> } ',

'sparql_wikidata': ' select distinct ?obj where { wd:Q188920 wdt:P2813 ?obj . ?obj wdt:P31 wd:Q1002697 } ',

'subgraph': 'simple question right',

'template': ' <S P ?O ; ?O instanceOf Type>',

'template_index': 65,

'uid': 19719}
```

## Tools

- Parsing SPARQL: https://github.com/yazdipour/sparql_parser
- https://github.com/BonaBeavis/tree-sitter-sparql
- Function Parser used in CodeSearchNet: https://github.com/ncoop57/function_parser
- DBPedia Query Service: https://dbpedia.org/sparql/
- wikidata Query Service: https://query.wikidata.org/
- Python Wikidata proxy: https://github.com/kensho-technologies/qwikidata

## Researches

- T5 wikiSQL https://huggingface.co/mrm8488/t5-base-finetuned-wikiSQL
- Finetuning T5 https://github.com/patil-suraj/exploring-T5
- T5 QG https://github.com/patil-suraj/question_generation
- CodeSearchNets: We used our TreeSitter infrastructure for this effort, and we’re also releasing our data preprocessing pipeline for others to use as a starting point in applying machine learning to code. 
- t5 FineTuning https://shivanandroy.com/fine-tune-t5-transformer-with-pytorch/#model-parameters
- t5 summarization finetuning & tf2pytorch2HuggingFace https://github.com/huseinzol05/Malaya/tree/master/pretrained-model/t5

## Similar

- Paper `SPARQL QUERY GENERATION FOR COMPLEX QUESTION ANSWERING WITH BERT AND BILSTM-BASED MODEL`
- Code https://github.com/deepmipt/DeepPavlov/
- https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/models/kbqa/tree_to_sparql.py
- https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/models/kbqa/wiki_parser.py

# Dataset

## WikiMedia

- https://www.kaggle.com/kenshoresearch/kensho-derived-wikimedia-data
- Properties with popularity: https://github.com/iacs-capstone-kensho/named-entity-linking/blob/master/data/generate_properties.ipynb

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

## General Transfer Models

- ALBERT, a Lite BERT for Self-supervised Learning of Language Representations, https://arxiv.org/abs/1909.11942
- ALXLNET, a Lite XLNET, no paper produced.
- BERT, Pre-training of Deep Bidirectional Transformers for Language Understanding, https://arxiv.org/abs/1810.04805
- BigBird, Transformers for Longer Sequences, https://arxiv.org/abs/2007.14062
- ELECTRA, Pre-training Text Encoders as Discriminators Rather Than Generators, https://arxiv.org/abs/2003.10555
- GPT2, Language Models are Unsupervised Multitask Learners, https://github.com/openai/gpt-2
- LM-Transformer, Exactly like T5, but use Tensor2Tensor instead Mesh Tensorflow with little tweak, no paper produced.
- PEGASUS, Pre-training with Extracted Gap-sentences for Abstractive Summarization, https://arxiv.org/abs/1912.08777
- T5, Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer, https://arxiv.org/abs/1910.10683
- TinyBERT, Distilling BERT for Natural Language Understanding, https://arxiv.org/abs/1909.10351
- Word2Vec, Efficient Estimation of Word Representations in Vector Space, https://arxiv.org/abs/1301.3781
- XLNET, Generalized Autoregressive Pretraining for Language Understanding, https://arxiv.org/abs/1906.08237
- FNet, FNet: Mixing Tokens with Fourier Transforms, https://arxiv.org/abs/2105.03824