# Vous devez modéliser une course de vaisseaux spatiaux.

# Ces vaisseaux ont comme particularité un nom, une couleur, une vitesse nominale, une durée d'accélération pour atteindre la vitesse nominale. 

# Les vaisseaux évoluent sur un circuit qui a une distance d'un tour et un nombre de tours.

# Pour une configuration donnée, à chaque tick (seconde), indiquer la position des vaisseaux.

class Spaceship:

    def __init__(self, name, color, max_speed, acceleration_time):
        self.name = name
        self.color = color
        self.max_speed = max_speed # 200 m/s
        self.acceleration_time = acceleration_time # 5 secondes
        self.distance = 0
        self.elapsed_time = 0

    def move(self):
        self.elapsed_time += 1
        if (self.elapsed_time > self.acceleration_time):
            self.distance = self.distance + self.max_speed
        else:
            self.distance += (self.max_speed / self.acceleration_time) * self.elapsed_time

    def __repr__(self):
        return f'{self.name}: elapsed_time[{self.elapsed_time}], distance[{self.distance}]'
    
    def __lt__(self, other):
        return self.elapsed_time < other.elapsed_time

class Track:

    def __init__(self, distance, nb_laps):
        self.distance = distance
        self.nb_laps = nb_laps
        self.total_distance = self.distance * self.nb_laps

    #donner la distance totale
    def get_total_distance(self):
        return self.distance * self.nb_laps



class Race:

    def __init__(self, track: Track):
        self.track = track
        self.spaceships = set()

    def add_spaceship(self, spaceship):
        self.spaceships.add(spaceship)
    
    def start(self):
        
        #tant que tous mes vaisseaux ne sont pas arrivés
        for spaceship in self.spaceships:
            # si le vaisseau n'est pas arrivé
            while spaceship.distance < self.track.total_distance:
            # continuer à déplacer le vaisseau
                spaceship.move()
            self.print_leader_board()
        #déplacer tous mes vaisseaux

    def start_v2(self):
        
        #tant que tous mes vaisseaux ne sont pas arrivés
        completed = False
        print(self.track.total_distance)

        while not completed:
            completed = True
            for spaceship in self.spaceships:
                if spaceship.distance < self.track.total_distance:
                    spaceship.move()
                    completed = False
                else:
                    completed = completed and True
            # si le vaisseau n'est pas arrivé
            # continuer à déplacer le vaisseau

            self.print_leader_board()
            
        #déplacer tous mes vaisseaux


    def print_leader_board(self):
        # trier les participants du 1er au dernier
        leaderboard = list(self.spaceships)
        leaderboard.sort()
        for idx, spaceship in enumerate(leaderboard):
        # for spaceship in self.spaceships:
            print(f'{idx+1} {spaceship}')


v1 = Spaceship('v1', 'red', 200, 10)
v2 = Spaceship('v2', 'blue', 250, 12)
v3 = Spaceship('v3', 'purple', 190, 50)

yellow_stone = Track(1500, 3)

championship = Race(yellow_stone)
championship.add_spaceship(v1)
championship.add_spaceship(v2)
championship.add_spaceship(v3)

championship.start_v2()

championship.print_leader_board()