from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return("""
          <h1>Hey!</h1>
      
          <p>Given a phrase, this microservice returns a list of related terms from Wikipedia.<br />
          <br />
          Use the pattern <i>/{your chosen term}</i> to query a word.<br />
          For example, to get the related terms for hummus, visit the url <br/>
          https://max-quantum-words.herokuapp.com/<u>hummus</u><br/>
          <br/>
          Phrases with multiple words can use underscores or spaces to join the words.<br/>
          E.g. both 'Green_Apple' and 'Green Apple' are acceptable.<br/>
          </p.
    
           """)

@app.route('/<name>')
def related_terms(name):
    
    url = 'https://en.wikipedia.org/api/rest_v1/page/related/'  
    resp = requests.get(url+name)
    if resp.status_code == 404:
        return("Error: There is no Wikipedia page titled '{}'.".format(name))
    else:
        resp = resp.json()
        terms = []
        for c in range(len(resp['pages'])):
            terms.append(resp['pages'][c]['normalizedtitle'])
        word_dict = {name: terms}
        return(json.dumps(word_dict))
    
		   
if __name__ == "__main__":
    app.run()
    
related_terms("Green_Apple")

