rotation_angle = int(input())
longitude = float(input())

distance = (rotation_angle*longitude)/360
distance = distance*60

hour = distance//60
hour = hour%12
minutes = distance%60

min_angle = minutes*6
hour_angle = hour*30 + minutes*30/60

diff = abs(min_angle-hour_angle)

if diff>180:
    diff = 360-diff
    

print(diff)

