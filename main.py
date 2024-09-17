from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_geo_header():
    geo_header = os.getenv("GEO_LOCATION")
    s = request.headers.get("X-Country")
    if geo_header:
        return f"Server location: {geo_header} User Country header {s}", 200
    else:
        return "No geolocation header found", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)