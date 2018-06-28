import nltk, json
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from collections import defaultdict


# Model Interface
class ModelInterface():
  
  def __init__(self):
    nltk.data.path = [ "/tmp/nltk_data" ]
    nltk.download('wordnet', download_dir="/tmp/nltk_data")
    nltk.download('punkt', download_dir="/tmp/nltk_data")
    nltk.download('averaged_perceptron_tagger', download_dir="/tmp/nltk_data")
    
    self.tag_map = defaultdict(lambda : wn.NOUN)
    self.tag_map['J'] = wn.ADJ
    self.tag_map['V'] = wn.VERB
    self.tag_map['R'] = wn.ADV

  
  def prediction(self, input):    
    if "texts" not in input:
      raise KeyError("Expected key named 'texts' in input.") 
    
    if not isinstance(input["texts"], str):
      raise ValueError("'texts' should be a string.")
     
    responses = []
    
    tokens = word_tokenize(input["texts"])
    lmtzr = WordNetLemmatizer()
    
    for token, tag in pos_tag(tokens):    
      responses.append({
        "word": token,
        "lemma": lmtzr.lemmatize(token, pos=self.tag_map[tag[0]])
      })
    
    return { "texts": responses }
    
    
# Local Testing
if __name__ == '__main__':
  interface = ModelInterface()
  print(json.dumps(interface.prediction({
    "texts": "Doppler, headquartered in San Francisco, helps make machine learning simple to find pretrained models."
  })))
