races = ["100m    ", "200m    ", "400m    ", "800m    ", "1km     ", "1mi     ", "5km     ", "10km    ", "13.1mi  ", "26.2mi  "];

d100m = [1, 2, 4, 8, 10, 16.09344, 50, 100, 210.8236, 421.6471];

d200m = [0.5, 1, 2, 4, 5, 8.04672, 25, 50, 105.4118, 210.8236];

d400m = [0.25, 0.5, 1, 2, 2.5, 4.02336, 12.5, 25, 52.70589, 105.4118];

d800m = [0.125, 0.25, 0.5, 1, 1.25, 2.01168, 6.25, 12.5, 26.35294, 52.70589];

d1km = [0.1, 0.2, 0.4, 0.8, 1, 1.609344, 5, 10, 21.08236, 42.16471];

d1mi = [0.06213712, 0.124274238, 0.248548, 0.497097, 0.621371, 1, 3.106856, 6.213712, 13.09997, 26.19994];

d5km = [0.02, 0.04, 0.08, 0.16, 0.2, 0.321869, 1, 2, 4.216471, 8.432942];

d10km = [0.01, 0.02, 0.04, 0.08, 0.1, 0.160934, 0.5, 1, 2.108236, 4.216471];

d13mi = [0.0047433, 0.009486606, 0.018973, 0.037946, 0.047433, 0.076336, 0.237165, 0.47433, 1, 2];

d26mi = [0.00237165, 0.004743303, 0.009487, 0.018973, 0.023717, 0.038168, 0.118583, 0.237165, 0.5, 1];

pointer = [d100m, d200m, d400m, d800m, d1km, d1mi, d5km, d10km, d13mi, d26mi];

def conversion(w, z, y, x):
	if x < 0:
		factor = "-"
	else:
		factor = "+";
	x = abs(x)
	if ((x/3600)>=1):
		hour = str(int(x // 3600))
		minutes = str(int((x%3600) // 60))
		seconds = str((x%3600) % 60)
		if float(hour) < 10:
			hour = "0" + hour
		if float(minutes) < 10:
			minutes = "0" + minutes
		if float(seconds) < 10:
			seconds = "0" + seconds
		print(y[z] + factor + hour + ":" + minutes + ":" + seconds)
	elif((x/60)>=1):
		minutes = str(int(x // 60))
		seconds = str(x%60)
		if float(minutes) < 10:
			minutes = "0" + minutes
		if float(seconds) < 10:
			seconds = "0" + seconds
		print(y[z] + factor + "00:" + minutes + ":" + seconds)
	else:
		x = str(x)
		if float(x) < 10:
			x = "0" + x
		print(y[z] + factor + "00:00:" + x)

#def perHour(x, y, z):


def distance():
	counter1 = 0;
	counter4 = 0;
	counter5 = 0;
	counter2 = 1;
	print(" ")
	print("***************************")
	print("RUNNING METRICS APPLICATION")
	print("***************************")
	print(" ")
	print("Which race do you want metrics on?")
	print(" ")
	for i in races:
		print(str(counter2) + ". " + i)
		counter2 = counter2 + 1;
	print(" ")
	counter3 = int(input("#:  "));
	print(" ")
	print("How long does it take you to run " + races[counter3-1] + "?")
	print(" ")
	hh = int(input("Hours:  ")) * 3600
	mm = int(input("Minutes:  ")) * 60
	ss = float(input("Seconds:  "))
	print(" ")
	print("***************************")
	print(" ")
	speed = hh + mm + ss;
	print("Metrics:")
	print(" ")
	for i in pointer[counter3-1]:
		timey = speed*i;
		conversion(speed, counter1, races, timey);
		counter1 = counter1+1;
	raw1 = pointer[counter3-1]
	rawkm = raw1[4]
	cha1 = speed*rawkm
	kmph = 3600 / cha1
	print("kmph:    " + str(float(kmph)));
	rawmi = raw1[5]
	cha2 = speed*rawmi
	mph = 3600 / cha2
	print("mph:     " + str(float(mph)));
	print(" ")
	print("***************************")
	print(" ")
	print("How fast do you want to run " +races[counter3-1] + "?")
	print(" ")
	hhh = int(input("Hours:  ")) * 3600
	mmm = int(input("Minutes:  ")) * 60
	sss = float(input("Seconds:  "))
	print(" ")
	print("***************************")
	print(" ")
	speed2 = hhh+mmm+sss
	speed3 = speed - speed2
	print("Metric breakdown of revised time by race:")
	print(" ")
	for i in pointer[counter3-1]:
		timey = speed2*i;
		conversion(speed2, counter5, races, timey);
		counter5 = counter5+1;
	rawkm = raw1[4]
	cha1 = speed2*rawkm
	kmph2 = 3600 / cha1
	print("kmph:    " + str(float(kmph2)));
	rawmi = raw1[5]
	cha2 = speed2*rawmi
	mph2 = 3600 / cha2
	print("mph:     " + str(float(mph2)));
	print(" ")
	print("Metric breakdown on time improvements:")
	print(" ")
	for i in pointer[counter3-1]:
		timey = speed3*i;
		conversion(speed3, counter4, races, timey);
		counter4 = counter4+1;
	print("kmph:   +" + str(kmph2-kmph));
	print("mph:    +" + str(mph2-mph));
	print(" ")
	print("***************************")
	print(" ")
	rs = str(raw_input("Type 'r' to restart: "))
	rs = rs.upper()
	if rs == "R":
		distance()
	else:
		print(" ")
		exit()

distance()
