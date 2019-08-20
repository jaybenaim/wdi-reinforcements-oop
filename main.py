class Location: 
    def __init__(self, name):
        self.name = name 
    
toronto = Location('Toronto')
ottawa = Location('Ottawa')
montreal = Location('Montreal')
quebec_city = Location('Quebec city')
halifax = Location('Halifax')
st_johns = Location('St. Johns')

# print(home.name) 

class Trip: 
    destinations = [] 
    
    @classmethod
    def add_destination(cls, location):
        cls.destinations.append(location.name) 

    @classmethod
    def display_destinations(cls): 
        dest = cls.destinations
        print("Began trip.")
        for i in range(len(dest) - 1): 
            print(f'Travelled from {dest[i]} to {dest[i+1]}')
        print('Ended Trip')
     
# trip_a = Trip(['home', 'school'])

# print(trip_a.stops.name) 
# print(Location.names)
trip_a = Trip() 
trip_a.add_destination(toronto)
trip_a.add_destination(ottawa)
trip_a.add_destination(montreal)
trip_a.add_destination(quebec_city)
trip_a.add_destination(halifax)
trip_a.add_destination(st_johns)

# print(trip_a.destinations) 

trip_a.display_destinations()

