import sys
import logging

from genassist.plant import GenericPlant, CloneStack
from genassist.genetics import GeneticPool

from flask import Flask, jsonify, request
from flask_cors import CORS

logger = logging.getLogger()


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET', 'POST'])
def ping_pong():
    response_object = {'status': 'success'}

    logger.debug("Initializing Genetics Assistant...")
    
    post_data = request.get_json()
    clone_genes = post_data.get('genes')

    clones = [CloneStack(species='hemp', genes=g, navail=3) for g in clone_genes]
    
    
    gpool = GeneticPool("hemp", best_gene="G")
    for clone in clones:
    	gpool.add_clones(parse_clone=clone)
    
    rtn = {}
    if gpool.best_crossbreeds:
        winner = next(iter( gpool.best_crossbreeds.items() ))
        rtn = {
            'genes': winner[0],
            'score': winner[1]['score'],
            'combination': winner[1]['comb'],
            'warning_5050': winner[1]['warning_5050'], 
            'warning_many5050': winner[1]['warning_many5050']
        }

    rtn_5050 = {}
    if gpool.best_5050:
        winner_5050 = next(iter( gpool.best_5050.items() ))
        rtn_5050 = {
            'genes': winner_5050[0],
            'score': winner_5050[1]['score'],
            'combination': winner_5050[1]['comb']
        }
    print(rtn)
    print(rtn_5050)
    response_object['best_crossbreeds'] = rtn
    response_object['best_5050'       ] = rtn_5050
    
    return jsonify(response_object)




if __name__ == '__main__':
    app.run()