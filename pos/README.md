# Part of Speech Tagger
Identify part of speech tags (Nouns, Verbs, and so on...). You give it sentence, it gives you a list of tags back.. 
You can use it to extract information about people, places, events and much more, mentioned in text documents, news articles or blog posts.
  

## Input Scheme
The input should contain a field `texts`, which should be a string of text. The paragraph of text will be split by sentence and then 
run on the part of speech tagger machine learning model.
 
``` json
{
  "texts": "Doppler makes building and deploying machine learning models easy. Discover pretrained models and predict on them with our API."
}
```


## Output Scheme
The output will be a 2 dimensional array of part of speech tags. The first dimension is of sentences where the 2nd dimension is of tags by word in that sentence.
You can read about what the different tags mean at the [Universal Dependencies project](http://universaldependencies.org/u/pos/index.html).

``` json
{
  "texts":[
    [
      {
        "word":"Doppler",
        "tag":"NNP"
      },
      {
        "word":"makes",
        "tag":"VBZ"
      },
      {
        "word":"building",
        "tag":"NN"
      },
      {
        "word":"and",
        "tag":"CC"
      },
      {
        "word":"deploying",
        "tag":"NN"
      },
      {
        "word":"machine",
        "tag":"NN"
      },
      {
        "word":"learning",
        "tag":"VBG"
      },
      {
        "word":"models",
        "tag":"NNS"
      },
      {
        "word":"easy",
        "tag":"JJ"
      }
    ],
    [
      {
        "word":"Discover",
        "tag":"NNP"
      },
      {
        "word":"pretrained",
        "tag":"VBD"
      },
      {
        "word":"models",
        "tag":"NNS"
      },
      {
        "word":"and",
        "tag":"CC"
      },
      {
        "word":"predict",
        "tag":"VBP"
      },
      {
        "word":"on",
        "tag":"IN"
      },
      {
        "word":"them",
        "tag":"PRP"
      },
      {
        "word":"with",
        "tag":"IN"
      },
      {
        "word":"our",
        "tag":"PRP$"
      },
      {
        "word":"API",
        "tag":"NN"
      }
    ]
  ]
}
```

