from flask import Flask, request, jsonify, Response, session, send_file
from flask_cors import CORS

import numpy as np
import os

from Airfoils.NACA4 import NACA4_airfoil
from Airfoils.Download import download_as_csv

from Solver.Airfoil import compute

# creates a flask server for post requests
app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def test():
    return jsonify({'message': 'Pong'})

@app.route('/xfoil', methods=['GET'])
def xfoil():
    ret = os.popen("xfoil").read()
    print(ret)
    return ret

@app.route('/compute', methods=['POST'])
def compute_airfoil():
    data = request.get_json()
    vinf = float(data['v_inf'])
    aoa = float(data['aoa'])
    databuffer = np.array(data['data'])
    text, panel_geometry, geom_pts, control_pts, pressure = compute(vinf, aoa, databuffer)
    return jsonify({'text': text, 'panel_geometry': panel_geometry, 'geom_pts': geom_pts, 'control_pts': control_pts, 'pressure': pressure})

@app.route('/NACA4Airfoil', methods=['POST'])
def get_NACA4_airfoil():
    data = request.get_json()
    m = float(data['maxCamber'])
    p = float(data['maxCamberLoc'])
    t = float(data['maxThickness'])
    n = int(data['numPoints'])

    datapoints = NACA4_airfoil(m, p, t, n)

    return datapoints.to_json(orient='records')

@app.route('/downloadAsCSV', methods=['POST'])
def download_as_csv():
    data = request.get_json()
    airfoilData = float(data['airfoilData'])

    datapoints = download_as_csv(airfoilData)

    return Response(
       datapoints.to_csv(index=False),
       mimetype="text/csv",
       headers={"Content-disposition":"attachment; filename=airfoil.csv"})
    
@app.route('/HelloXfoil', methods=['POST'])
def hello_xfoil():
    
    ret = os.popen("xfoil < inputXfoil.txt").read()
    app.logger.info(ret)
    return ret

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)