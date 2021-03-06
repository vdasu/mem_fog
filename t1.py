from trafficlight import TrafficLight
import ip_address

PORT 		= 5001
SPEED_LIMIT = 60 
STATE = {
	'active_siblings' 	: [ip_address.IP_T1],
	'inactive_siblings' : [	ip_address.IP_T2,
							ip_address.IP_T3, 
							ip_address.IP_T4, 
							ip_address.IP_T5, 
							ip_address.IP_T6, 
							ip_address.IP_T7],
	'parents'			: [ip_address.IP_AUTHO],
	'children'			: [ip_address.IP_VEHICLE],
	'aspects'			: {'request_count':0},
	'port'				: PORT
}

app = TrafficLight(__name__, PORT, STATE, SPEED_LIMIT)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=PORT)