import nltk, json


# Model Interface
class ModelInterface():
  
  tag_map = {
    "cc": "conjunction",
    "cd": "numeral",
    "dt": "determiner",
    "ex": "existential there",
    "fw": "foreign word",
    "in": "preposition or conjunction",
    "jj": "adjective or numeral",
    "jjr": "adjective, comparative",
    "jjs": "adjective, superlative",
    "ls":  "list item marker",
    "md": "modal auxiliary",
    "nn": "noun, common, singular or mass",
    "nnp": "noun, proper, singular",
    "nnps": "noun, proper, plural",
    "nns": "noun, common, plural",
    "pdt": "pre-determiner",
    "pos": "genitive marker",
    "prp": "pronoun, personal",
    "prp$": "pronoun, possessive",
    "rb": "adverb",
    "rbr": "adverb, comparative",
    "rbs": "adverb, superlative",
    "rp": "particle",
    "sym": "symbol",
    "to": "preposition",
    "uh": "interjection",
    "vb": "verb, base form",
    "vbd": "verb, past tense",
    "vbg": "verb, present participle",
    "vbn": "verb, past participle",
    "vbp": "verb, present tense, not 3rd person singular",
    "vbz": "verb, present tense, 3rd person singular",
    "wdt": "wh-determiner",
    "wp": "WH-pronoun",
    "wp$": "WH-pronoun, possessive",
    "wrb": "Wh-adverb"
  }
  
  def __init__(self):
    nltk.data.path = [ "/tmp/nltk_data" ]
    nltk.download('punkt', download_dir="/tmp/nltk_data")
    nltk.download('averaged_perceptron_tagger', download_dir="/tmp/nltk_data")

  
  def prediction(self, input):    
    if "texts" not in input:
      raise KeyError("Expected key named 'texts' in input.") 
    
    if not isinstance(input["texts"], str):
      raise ValueError("'texts' should be a string.")
     
    responses = []
    
    for sentence in input["texts"].split("."):
      output = nltk.pos_tag(nltk.word_tokenize(sentence.strip()))
      output = [ {
        "word": x[0],
        "tag": x[1],
        "description_short": self.tag_map[x[1].lower()].split(" ")[0].split(",")[0],
        "description_long": self.tag_map[x[1].lower()]
      } for x in output if x[1] != "," ]
      responses.append(output)
      
    responses = [ x for x in responses if len(x) > 0 ]
    return { "texts": responses }
    
    
# Local Testing
if __name__ == '__main__':
  interface = ModelInterface()
  print(json.dumps(interface.prediction({
    "texts": "Doppler makes building and deploying machine learning models easy. Discover pretrained models and predict on them with our API."
  })))