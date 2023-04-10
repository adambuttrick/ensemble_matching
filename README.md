# ensemble_matching
Example using combined fasttext and ROR affiliation matching


Install requirements.txt
````
pip install -r requirements.txt
````
[Download the model files from Hugging Face](https://huggingface.co/poodledude/ror-predictor/tree/main) and place in a directory. Pass this directory to the Predictor class when creating, e.g.:
````
PREDICTOR = Predictor('path_to/model_files_dir/')
````
