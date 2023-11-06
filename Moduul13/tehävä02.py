from flask import Flask, jsonify

app = Flask(__name__)

airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
}
@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport(icao_code):
    icao_code = icao_code.upper()
    airport = airport_database.get(icao_code)

    if airport is not None:
        return jsonify({"ICAO": icao_code, **airport})
    else:
        return jsonify({"error": "Airport not found"}), 404


app.run(debug=True)
