# ########################################
# File: countries_api.py
# ########################################

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary mapping ISO codes to country names
country_data = {
    "US": "United States",
    "CA": "Canada",
    "GB": "United Kingdom",
    # Add more country mappings as needed
}

@app.route('/get_country_name', methods=['GET'])
def get_country_name():
    iso_code = request.args.get('iso_code')

    if not iso_code:
        return jsonify({"error": "ISO code not provided"}), 400

    country_name = country_data.get(iso_code.upper())

    if country_name:
        return jsonify({"country_name": country_name})
    else:
        return jsonify({"error": "Country not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
