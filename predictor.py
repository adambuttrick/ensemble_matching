import os
import re
import fasttext
from contextlib import redirect_stderr
from unidecode import unidecode
from gensim.parsing.preprocessing import preprocess_string, strip_tags, strip_punctuation, strip_multiple_whitespaces

class Predictor():
	def __init__(self, path_to_model):
		with open(os.devnull, 'w') as devnull:
			with redirect_stderr(devnull):
				self.model = os.path.join(path_to_model, 'model.bin')
				self.classifier = fasttext.load_model(self.model)

	def preprocess_text(self, text):
		custom_filters = [lambda x: x.lower(), strip_tags,
						  strip_punctuation, strip_multiple_whitespaces]
		return unidecode(' '.join(preprocess_string(text, custom_filters)))

	def predict_ror_id(self, affiliation, confidence):
		affiliation = self.preprocess_text(affiliation)
		predicted_label = self.classifier.predict(affiliation, k=1)
		label, ratio = predicted_label[0][0], predicted_label[1][0]
		if ratio >= confidence:
			label = re.sub('__label__','', label)
			return label
		else:
			return None