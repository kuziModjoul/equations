import matplotlib.pyplot as plt

# Environment Variables
ENVIRONMENTAL_FACTOR = 2.3
MEASURED_POWER_WAP1 = -34
MEASURED_POWER_WAP2 = -40.7
MEASURED_POWER_WAP3 = -46.3
# WAP1 position
x1 = 1.908
y1 = 0
# WAP2 position
x2 = 3.816
y2 = 11.049
# WAP3 position
x3 = 0
y3 = 11.049

# Add reading values here
locations = [
    {
        'location': 'Top-right',
        'RSSI_WAP1': -57.3, 
        'RSSI_WAP2': -35.67,
        'RSSI_WAP3': -59.67
    },
    {
        'location': 'Middle',
        'RSSI_WAP1': -47.33,
        'RSSI_WAP2': -45.67,
        'RSSI_WAP3': -47.3
    },
    {
        'location': 'Bottom-middle',
        'RSSI_WAP1': -37.67, 
        'RSSI_WAP2': -54.3,
        'RSSI_WAP3': -51.33
    },
]

# distance approximation and trilateration functions
def distance_calculation(ENVIRONMENTAL_FACTOR, measured_power, instant_rssi):
   return round((10**((measured_power - instant_rssi)/(10*ENVIRONMENTAL_FACTOR))), 2)

def trackDevice(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*x2 - 2*x1
  B = 2*y2 - 2*y1
  C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
  D = 2*x3 - 2*x2
  E = 2*y3 - 2*y2
  F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
  x = round((C*E - F*B) / (E*A - B*D),2)
  y = round((C*D - A*F) / (B*D - A*E), 2)
  return x,y

# Loop through locations list and calculate distances to plug into trilateration function
coordinates_tuples = []
x_coordinates = []
y_coordinates = []
for location in locations:
    if location['RSSI_WAP1']:
        r1 = distance_calculation(ENVIRONMENTAL_FACTOR, MEASURED_POWER_WAP1, location['RSSI_WAP1'] )
    if location['RSSI_WAP2']:
        r2 = distance_calculation(ENVIRONMENTAL_FACTOR, MEASURED_POWER_WAP2, location['RSSI_WAP2'] )
    if location['RSSI_WAP3']:
        r3 = distance_calculation(ENVIRONMENTAL_FACTOR, MEASURED_POWER_WAP3, location['RSSI_WAP3'] )
    x,y = trackDevice(x1,y1,r1,x2,y2,r2,x3,y3,r3)
    x_coordinates.append(x)
    y_coordinates.append(y)
    coord_tuple = (x,y)
    coordinates_tuples.append(coord_tuple)
    area = location['location']
    print(f'\n{area} approximate position: {x,y} \n')
print(coordinates_tuples)

# Plot coordinates with MatPlotLib 
plt.rcParams["figure.figsize"] = [3.34, 5.89]
plt.rcParams["figure.autolayout"] = True
plt.plot(x_coordinates, y_coordinates, 'r*')
# Coordinates were measured in warehouse
plt.axis([0, 3.816, 0, 11.049])
for i, j in zip(x_coordinates, y_coordinates):
   plt.text(i, j+0.5, '({}, {})'.format(i, j))
plt.show()


 

    



