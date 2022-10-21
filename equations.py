
# Distance approximation
# Returns approximate distance from device to single router in meters
# ENVIRONMENTAL_FACTOR: Constant for the complexity of the environment
# MEASURED_POWER: RSSI value from 1 m
# INSTANT_RSSI: Measured value from current location
def distance_calculation(ENVIRONMENTAL_FACTOR, MEASURED_POWER, INSTANT_RSSI):
   return round((10**((MEASURED_POWER - INSTANT_RSSI)/(10*ENVIRONMENTAL_FACTOR))), 2)


# Trilateration 
# Returns approximate x and y position of device
# r is the distance
def trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*x2 - 2*x1
  B = 2*y2 - 2*y1
  C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
  D = 2*x3 - 2*x2
  E = 2*y3 - 2*y2
  F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
  x = round((C*E - F*B) / (E*A - B*D),2)
  y = round((C*D - A*F) / (B*D - A*E), 2)
  return x,y