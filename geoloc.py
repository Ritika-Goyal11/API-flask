from flask import *
import requests
import os

app = Flask(__name__)

print(os.environ.get('API_KEY'))
api_key = os.environ.get('API_KEY')

api_endpoint = "https://api.ipgeolocation.io/ipgeo"

def extract_location_data(json_data):
    location_info = {
        "ip":json_data["ip"],
        "latitude": json_data["latitude"],
        "longitude": json_data["longitude"],
        "city": json_data["city"],
        "state": json_data["state_prov"],
        "country": json_data["country_name"],
        "zip_code": json_data["zipcode"],
        "country_flag": json_data["country_flag"],
        "current_time": json_data['time_zone']['current_time'],
        "time_zone":json_data['time_zone']['name']
    }
    return location_info

@app.route('/')
def get_geolocation():

    params = {
        'apiKey': api_key,
        'ip': ''    # IP can be left blank to get our current IP
    }

    ip = request.args.get('ip')
    if ip:
        params['ip']=ip

    response = requests.get(api_endpoint, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return render_template('home.html',data=extract_location_data(data))
    else:
        return f"Error: {response.status_code}, {response.text}"

@app.route('/inp')
def index():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def h():
    ip = request.form.get('ip')
    return redirect(url_for('get_geolocation', ip=ip))

app.run(debug=True)
