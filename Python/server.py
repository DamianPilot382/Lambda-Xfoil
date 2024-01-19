from flask import Flask, request, jsonify, Response, send_file
from flask_cors import CORS
from Airfoil import compute
from naca4 import computeNacaAirfoil
from io import StringIO
import numpy as np

# creates a flask server for post requests
app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def test():
    return jsonify({'message': 'Pong'})

@app.route('/compute', methods=['POST'])
def compute_airfoil():
    data = request.get_json()
    vinf = float(data['v_inf'])
    aoa = float(data['aoa'])
    databuffer = np.array(data['data'])

    text, panel_geometry, geom_pts, control_pts, pressure = compute(vinf, aoa, databuffer)
    return jsonify({'text': text, 'panel_geometry': panel_geometry, 'geom_pts': geom_pts, 'control_pts': control_pts, 'pressure': pressure})

@app.route('/nacaAirfoil', methods=['POST'])
def nacaAirfoil():
    data = request.get_json()
    m = float(data['maxCamber'])
    p = float(data['maxCamberLoc'])
    t = float(data['maxThickness'])
    n = int(data['numPoints'])

    datapoints = computeNacaAirfoil(m, p, t, n)

    # return send_file(
    #     "n0012.csv",
    #     mimetype="text/csv",
    #     download_name="airfoil.csv",
    #     as_attachment=True)
        
    return Response(
       datapoints.to_csv(index=False),
       mimetype="text/csv",
       headers={"Content-disposition":"attachment; filename=airfoil.csv"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)