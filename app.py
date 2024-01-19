from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from NACA4 import NACA4_airfoil
import numpy as np
import os

# creates a flask server for post requests
app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def test():
    return jsonify({'message': 'Pong'})

@app.route("/xfoil", methods=['GET'])
def xfoil():
    ret = os.popen("xfoil").read()
    print(ret)
    return ret

@app.route('/compute', methods=['POST'])
# TODO Implement
def compute_airfoil():
    data = request.get_json()
    vinf = float(data['v_inf'])
    aoa = float(data['aoa'])
    databuffer = np.array(data['data'])
    # text, panel_geometry, geom_pts, control_pts, pressure = compute(vinf, aoa, databuffer)
    return jsonify({'text': "TODO", 'panel_geometry': "TODO", 'geom_pts': "TODO", 'control_pts': "TODO", 'pressure': "TODO"})

@app.route('/NACA4Airfoil', methods=['POST'])
def get_NACA4_airfoil():
    data = request.get_json()
    m = float(data['maxCamber'])
    p = float(data['maxCamberLoc'])
    t = float(data['maxThickness'])
    n = int(data['numPoints'])

    datapoints = NACA4_airfoil(m, p, t, n)
        
    return Response(
       datapoints.to_csv(index=False),
       mimetype="text/csv",
       headers={"Content-disposition":"attachment; filename=airfoil.csv"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)