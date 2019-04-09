from trafficlight import TrafficLight

state = {
	'active_siblings' 	: ['http://127.0.0.1:5000/'],
	'inactive_siblings' : ['http://127.0.0.1:5001/'],
	'parents'			: ['http://127.0.0.1:4000/'],
	'children'			: ['http://127.0.0.1:4000/'],
	'aspects'			: {
							'port':5000
						}
}

if __name__ == '__main__':
	t1 = TrafficLight(5000, state, 60)