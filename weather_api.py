from flask import Flask
from flask_restful import Resource, Api, reqparse
from urllib.request import urlopen
from urllib.error import URLError

app = Flask(__name__)
api = Api(app)

INFO_URL = "https://tgftp.nws.noaa.gov/data/observations/metar/decoded/"


class Temperature(Resource):
    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('key', required=True)
        args = parser.parse_args()
        location = args['key']
        # To handle cases with valid location keys but no temperature data included in txt file
        data = {
            'temperature': f'Temperature data could not be found for location key {location}.'
        }
        target_url = INFO_URL + f"{location}.TXT"
        try:
            txt_data = urlopen(target_url)
            for line in txt_data:
                line = str(line)
                print(line)
                if 'temperature' in line.lower():
                    data['temperature'] = line.split(':')[-1].strip()[:-3]
                    break
            return {'data': data}, 200
        # To handle cases with invalid location keys
        except URLError:
            err_msg = f"The requested URL /data/observations/metar/decoded/{location}.TXT was not found on this server."
            return {'error': err_msg}, 404


class Pressure(Resource):
    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('key', required=True)
        args = parser.parse_args()
        location = args['key']
        # To handle cases with valid location keys but no pressure data included in txt file
        data = {
            'pressure': f'Pressure data could not be found for location key {location}.'
        }
        target_url = INFO_URL + f"{location}.TXT"
        try:
            txt_data = urlopen(target_url)
            for line in txt_data:
                line = str(line)
                if 'pressure' in line.lower():
                    data['pressure'] = line.split(':')[-1].strip()[:-3]
                    break
            return {'data': data}, 200
        # To handle cases with invalid location keys
        except URLError:
            err_msg = f"The requested URL /data/observations/metar/decoded/{location}.TXT was not found on this server."
            return {'error': err_msg}, 404


api.add_resource(Temperature, '/temperature')   # entry point for temperature
api.add_resource(Pressure, '/pressure')         # entry point pressure


if __name__=='__main__':
    app.run()

