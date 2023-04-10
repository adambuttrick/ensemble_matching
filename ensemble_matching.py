import requests
import fasttext
from predictor import Predictor
from urllib.parse import quote

PREDICTOR = Predictor('../models/')

def query_affiliation(affiliation):
    chosen_id = None
    affiliation_encoded = quote(affiliation)
    url = f"https://api.ror.org/organizations?affiliation={affiliation_encoded}"
    r = requests.get(url)
    if r.ok:
        api_response = r.json()
        results = api_response['items']
        if results != []:
            for result in results:
                if result['chosen']:
                    chosen_id = result['organization']['id']
    return chosen_id


def ensemble_match(affiliation, confidence=0.8):
    fasttext_prediction = PREDICTOR.predict_ror_id(affiliation, confidence)
    if fasttext_prediction is not None:
        return fasttext_prediction
    else:
        affiliation_prediction = query_affiliation(affiliation)
        if affiliation_prediction is not None:
            return affiliation_prediction


if __name__ == '__main__':
    print(ensemble_match('Department of Engineering, University of Michigan, Ann Arbor, MI 48103'))