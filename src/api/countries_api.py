# ########################################
# File: countries_api.py
# version: 0.1
# version: 0.2 - obter lista de paises da api
# https://restcountries.com/
# https://restcountries.com/v3.1/alpha/br
# 
# ########################################
from flask import Flask, request, jsonify
import requests # pip install requests
app = Flask(__name__) 
# Dictionary mapping ISO codes to country names
country_data = {
    "US": "United States",
    "CA": "Canada",
    "GB": "United Kingdom"
}
@app.route('/get_country_name', methods=['GET'])
def get_country_name():
    iso_code = request.args.get('iso_code') # <= obrigatorio
    if not iso_code:
        return jsonify({"error": "ISO code not provided"}), 400
    country_name = country_data.get(iso_code.upper())
    if country_name:
        return jsonify({"country_name": country_name})
    else:
        # teste do iso_code "ZZ" que não existe
        return jsonify({"error": "Country not found"}), 404 

def get_country_name_rest():
    """ 
    TODO: implementar rota para fazer 
    request para a api restcountries passando o código iso "BR"
    e retorna o nome do país
    - https://restcountries.com/v3.1/alpha/br
    - retornar data['name']['common']
    """
    ...

if __name__ == '__main__':
    app.run(debug=True)
