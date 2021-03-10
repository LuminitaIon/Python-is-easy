# classes
class Vehicle:
	def __init__(self, make, model, year, weight):
		self.Make = make
		self.Model = model
		self.Year = year
		self.Weight = weight
		self.NeedsMaintenance = False
		self.TripsSinceMaintenance = 0

	def Make(self):
		return self.Make

	# SETTERS
	def setMake(self, make):
		self.Make = make

	def setModel(self, model):
		self.Model = model

	def setYear(self, year):
		self.Year = year

	def setWeight(self, weight):
		self.Weight = weight

	def ManageMaintenance(self):
		if self.TripsSinceMaintenance > 100:
			self.NeedsMaintenance = True

	def Repair(self):
		self.NeedsMaintenance = False
		self.TripsSinceMaintenance = 0

	def __str__(self):
		return ("Make: " + str(self.Make) + "\nModel: " + str(self.Model) + "\nYear: " + str(self.Year) + "\nWeight: " + str(self.Weight) + "\nNeedsMaintenance: "+str(self.NeedsMaintenance)+"\nTripsSinceMaintenance: "+str(self.TripsSinceMaintenance))

class Cars(Vehicle):
	def __init__(self, make, model, year, weight):
		Vehicle.__init__(self, make, model, year, weight)
		self.isDriving = False

	def Drive(self):
		self.isDriving = True

	def ManageTrips(self):
		if self.isDriving == True:
			self.TripsSinceMaintenance += 1

	def Stop(self):
		self.ManageTrips()
		self.isDriving = False
		self.ManageMaintenance()

Golf = Cars("Volkswagen", "Golf", 2018, 1200)
Fiesta = Cars("Fiat", "Fiesta", 2015, 1159)
Audi = Cars("Audi", "A3", 2016, 1500)
CarLists = [Golf, Fiesta, Audi]

for trip in range(120):
    Fiesta.Drive()
    if(trip % 2 == 0):
        Golf.Drive()
    if(trip % 3 == 0):
        Audi.Drive()
    for car in CarLists:
        car.Stop()

for car in CarLists:
    print(car)

class Planes(Vehicle):
	def __init__(self, make, model, year, weight):
		Vehicle.__init__(self, make, model, year, weight)
		self.IsFlying = False

	def ManageTrips(self):
		if self.IsFlying == True:
			self.TripsSinceMaintenance += 1

	def Flying(self):
		if self.NeedsMaintenance == True:
			self.IsFlying = False
			print("{0} {1} can't fly until it's repair".format(self.Make, self.Model))
		else:
			self.IsFlying = True
		return self.IsFlying

	def Landing(self):
		self.ManageTrips()
		self.IsFlying = False
		self.ManageMaintenance()

Boeing = Planes("Boeing", "WonderLand 757", 2014, 12000)
AirWays = Planes("AirWays", "A222", 2013, 20000)
PlaneLists = [Boeing, AirWays]

for trip in range(120):
    Boeing.Flying()
    if(trip % 2 == 0):
        AirWays.Flying()
    for plane in PlaneLists:
        plane.Landing()

for plane in PlaneLists:
    print(plane)