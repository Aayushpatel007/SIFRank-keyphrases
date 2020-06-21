from flask import Flask,jsonify,request,make_response,url_for,redirect
import requests, json
import json
import nltk
from embeddings import sent_emb_sif, word_emb_elmo
from model.method import SIFRank, SIFRank_plus
from stanfordcorenlp import StanfordCoreNLP
import time

import sys

cpu_or_gpu = int(sys.argv[1])

options_file = "auxiliary_data/elmo_2x4096_512_2048cnn_2xhighway_options.json"
weight_file = "auxiliary_data/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"

porter = nltk.PorterStemmer()
ELMO = word_emb_elmo.WordEmbeddings(options_file, weight_file, cuda_device=cpu_or_gpu)
SIF = sent_emb_sif.SentEmbeddings(ELMO, lamda=1.0)
en_model = StanfordCoreNLP("auxiliary_data/stanford-corenlp-full-2018-10-05",quiet=True)#download from https://stanfordnlp.github.io/CoreNLP/
elmo_layers_weight = [0.0, 1.0, 0.0]

app = Flask(__name__)

@app.route('/sifrank', methods=['POST'])
def sifrank():
    req_data = request.get_json(force=True)
    #download from https://allennlp.org/elmo
    text = req_data['text']
    no_of_phrases = req_data['N']
    algo = int(req_data["Sifrankplus"])
    if algo == 0:
        keyphrases = SIFRank(text, SIF, en_model, N=no_of_phrases,elmo_layers_weight=elmo_layers_weight)
    else:
        keyphrases = SIFRank_plus(text, SIF, en_model, N=no_of_phrases, elmo_layers_weight=elmo_layers_weight)
    print(keyphrases)
    
    key_phrases = {
        'Kephrases': keyphrases,
    }
    
    return jsonify(key_phrases)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000,debug=False, use_reloader=True)
