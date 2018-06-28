# Lemma Form
Identify the canonical form, dictionary form, or citation form for a set of words using NLP (natural language processing). 
You can use it to extract information about people, places, events and much more, mentioned in 
text documents, news articles or blog posts.
  

## Input Scheme
The input should contain a field `text`, which should be a string of text. 
``` json
{
  "texts": "Doppler, headquartered in San Francisco, helps make machine learning simple to find pretrained models."
}
```


## Output Scheme
The output will be an array of part of lemma words.

``` javascript
{
  "texts":[
    {
      "word":"Doppler",
      "lemma":"Doppler"
    },
    {
      "word":",",
      "lemma":","
    },
    {
      "word":"headquartered",
      "lemma":"headquarter"
    },
    {
      "word":"in",
      "lemma":"in"
    },
    {
      "word":"San",
      "lemma":"San"
    },
    {
      "word":"Francisco",
      "lemma":"Francisco"
    },
    {
      "word":",",
      "lemma":","
    },
    {
      "word":"helps",
      "lemma":"help"
    },
    {
      "word":"make",
      "lemma":"make"
    },
    {
      "word":"machine",
      "lemma":"machine"
    },
    {
      "word":"learning",
      "lemma":"learn"
    },
    {
      "word":"simple",
      "lemma":"simple"
    },
    {
      "word":"to",
      "lemma":"to"
    },
    {
      "word":"find",
      "lemma":"find"
    },
    {
      "word":"pretrained",
      "lemma":"pretrained"
    },
    {
      "word":"models",
      "lemma":"model"
    },
    {
      "word":".",
      "lemma":"."
    }
  ]
}
```
