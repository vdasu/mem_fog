from trafficlight import TrafficLight

PORT 		= 5000
SPEED_LIMIT = 60 
STATE = {
	'active_siblings' 	: ['http://127.0.0.1:5000/'],
	'inactive_siblings' : [	'http://127.0.0.1:5001/', 
							'http://127.0.0.1:5002/', 
							'http://127.0.0.1:5003/', 
							'http://127.0.0.1:5004/',
							'http://127.0.0.1:5005/'],
	'parents'			: ['http://127.0.0.1:6000/'],
	'children'			: ['http://127.0.0.1:4000/'],
	'aspects'			: {'request_count':0},
	'port'				: PORT
}

app = TrafficLight(__name__, PORT, STATE, SPEED_LIMIT)

if __name__ == '__main__':
	app.run(debug=True, port=PORT)