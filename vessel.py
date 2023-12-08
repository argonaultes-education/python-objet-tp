class Starship:
    '''
    speed in m/s
    tts in seconds : Time To Speed
    '''
    def __init__(self, name, color, speed, tts):
        self.name = name
        self.color = color
        self.speed = speed
        self.tts = tts
        # nouvelles propriétés pour calculer la distance parcourue pour une nouvelle seconde
        self.distance = 0
        self.current_speed = 0
        self.elapsed_time = 0
        self.coefficient_acceleration = self.speed / self.tts # utiliser la speed et le tts

    # calculer la distance parcourue en 1 seconde
    def nouvelle_seconde_passee(self):
        self.elapsed_time += 1
        # phase de course nominale
        if self.elapsed_time > self.tts:
            self.distance += self.speed
        # phase d'accélération
        else:
            # coefficient A ou coefficient_acceleration ?
            self.current_speed = self.coefficient_acceleration * self.elapsed_time
            # utiliser ce coefficient pour calculer la vitesse à cet instant
            # simplifier le modèle et donc prendre la vitesse calculée qui sera la même sur toute la seconde passée
            self.distance += self.speed

    def __repr__(self):
        return f'{self.name}, temps passé: {self.elapsed_time}'

    

class Track:
    '''
    distance in meters
    '''
    def __init__(self, distance, nbLaps):
        self.distance = distance
        self.nbLaps = nbLaps

class Race:
    def __init__(self, name, track):
        self.name = name #nom de la course, pour que ça rende bien sur le tableau des scores
        self.track = track #circuit sur lequel la course va avoir lieu
        self.starships = set() #liste des participants

    def add_starship(self, starship): #ajouter un nouveau participant à la course
        self.starships.add(starship)

    # créer une méthode d'instance qui parcourt l'ensemble des vaisseaux et les affiche
    def print_leaderboards(self):
        print('=== Leaderboards ===')
        for starship in self.starships:
            print(starship)

    def start_race(self):
        tout_le_monde_a_fini = False
        while not tout_le_monde_a_fini: # 1 nouvelle seconde passe à chaque tour de boucle
            tout_le_monde_a_fini = True
            for starship in self.starships:
                distance_parcourue_par_le_vaisseau = starship.distance
                distance_totale_a_parcourir = self.track.distance * self.track.nbLaps
                if (distance_parcourue_par_le_vaisseau >= distance_totale_a_parcourir):
                    print(f'le vaisseau {starship.name} a fini la course')
                else:
                    starship.nouvelle_seconde_passee()
                    tout_le_monde_a_fini = False




if __name__ == '__main__':
    # crée un circuit de 2km avec 3 tours
    track1 = Track(2000, 3)
    # crée 3 vaisseaux
    starship1 = Starship('star1', 'blue', 120, 10)
    starship2 = Starship('star2', 'red', 131, 13)
    starship3 = Starship('star3', 'yellow', 118, 11)
    starship4 = Starship('star4', 'pink', 213, 40)
    # crée une course avec le circuit et les 3 vaisseaux
    winterRace = Race('winter-race-2023', track1)
    winterRace.add_starship(starship1)
    winterRace.add_starship(starship2)
    winterRace.add_starship(starship3)
    winterRace.add_starship(starship4)
    winterRace.add_starship(starship1)
    winterRace.print_leaderboards()
#    winterRace.start_race()


