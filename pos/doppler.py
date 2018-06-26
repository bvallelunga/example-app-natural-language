import nltk, json


# Model Interface
class ModelInterface():
  
  def __init__(self):
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

  
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
        "tag": x[1]
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