import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

#Timer wyboru zwierzaka
start_time = pygame.time.get_ticks()

# Wymiary okna
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pokegotchi")

# Kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Czcionki
font = pygame.font.SysFont(None, 36)

squirtle_image = pygame.image.load("assets/squirtle.png")
charmander_image = pygame.image.load("assets/charmander.png")
bulbasaur_image = pygame.image.load("assets/bulbasaur.png")
pikachu_image = pygame.image.load("assets/pikachu.png")
squirtle_image = pygame.transform.scale(squirtle_image,(200, 200))  # Skalowanie obrazu do odpowiednich rozmiarów
charmander_image = pygame.transform.scale(charmander_image, (220, 200))
bulbasaur_image = pygame.transform.scale(bulbasaur_image, (200, 200))
pikachu_image = pygame.transform.scale(pikachu_image, (200, 200))



# Tworzenie klasy Pokemon
class Pet:
    def __init__(self, name):

        self.name = name
        self.hunger = 100  # 0 - najedzony, 100 - głodny
        self.happiness = 100  # 0 - smutny, 100 - szczęśliwy
        self.sleepiness = 100  # 0 - wyspany, 100 - zmęczony
        self.hunger_timer = 0  # Licznik czasu głodu (w klatkach)
        self.happiness_timer = 0
        self.sleepiness_timer = 0
        self.hunger_increment_interval = 100 # Co ile klatek głód ma wzrosnąć (np. co 5 klatek)
        self.happiness_increment_interval = 400 # Co ile klatek głód ma wzrosnąć (np. co 5 klatek)
        self.sleepness_increment_interval = 300 # Co ile klatek głód ma wzrosnąć (np. co 5 klatek)
        self.experience = 0 # EXP
        self.max_experience = width - 12
        self.evolution_stage = 0
        self.level = 1
        self.load_image()

    def level_up(self):
        self.level += 1
        self.evolve()
        self.experience = 0

    def gainExperience(self):
        self.experience += 1
        if self.experience >= self.max_experience:
            self.level_up()


    def getExperience(self):
        return self.experience

    def evolve(self):
        if self.level == 25:
            if self.name == "Squirtle":
                self.name = "Wartotle"
                self.load_image()
                self.experience = 0
        if self.level == 50:
            if self.name == "Wartotle":
                self.name = "Blastoise"
                self.load_image()
                self.experience = 0
        if self.level == 25:
            if self.name == "Bulbasaur":
                self.name = "Ivysaur"
                self.load_image()
                self.experience = 0
        if self.level == 50:
            if self.name == "Ivysaur":
                self.name = "Venusaur"
                self.load_image()
                self.experience = 0
            if self.level == 25:
                if self.name == "Charmander":
                    self.name = "Charmeleon"
                    self.load_image()
                    self.experience = 0
        if self.level == 50:
            if self.name == "Charmeleon":
                self.name = "Charizard"
                self.load_image()
                self.experience = 0


    def feed(self):
        self.hunger = max(self.hunger - 5, 0)

    def play(self):
        self.happiness = min(self.happiness + 5, 100)
        #self.sleepiness = min(self.sleepiness + 20, 100)

    def sleep(self):
        self.sleepiness = max(self.sleepiness - 5, 0)

    def update(self):

        # For test purposes
        self.gainExperience()

        self.hunger_timer += 1
        if self.hunger_timer >= self.hunger_increment_interval:
            self.hunger = min(self.hunger + 1, 100)  # Zwiększamy głód o 1
            self.hunger_timer = 0  # Resetujemy licznik

        self.happiness_timer += 1
        if self.happiness_timer >= self.happiness_increment_interval:
            self.happiness = min(self.happiness - 1, 100)  # Zwiększamy szczęście o 1
            self.happiness_timer = 0  # Resetujemy licznik

        self.sleepiness_timer += 1
        if self.sleepiness_timer >= self.sleepness_increment_interval:
            self.sleepiness = min(self.sleepiness + 1, 100)  # Zwiększamy szczęście o 1
            self.sleepiness_timer = 0  # Resetujemy licznik

    def draw(self):
        # Rysuj pokemona
        screen.blit(self.image, (250, 250))

        # Rysuj pasek expa
        pygame.draw.rect(screen, WHITE, (5, 5, 790, 50))
        pygame.draw.rect(screen, RED, (6, 6, self.getExperience(), 48))

        # Rysowanie statusów
        hunger_text = font.render(f"Głód: {self.hunger}", True, WHITE)
        happiness_text = font.render(f"Szczęście: {self.happiness}", True, WHITE)
        sleep_text = font.render(f"Sny: {self.sleepiness}", True, WHITE)
        level_text = font.render(f"Poziom: {self.level}", True, BLACK)

        screen.blit(hunger_text, (20, 60))
        screen.blit(happiness_text, (20, 100))
        screen.blit(sleep_text, (20, 140))
        screen.blit(level_text, (320, 20))

        # Przyciski interakcji
        pygame.draw.rect(screen, BLUE, (60, 500, 200, 50))
        feed_text = font.render("Nakarm", True, WHITE)
        screen.blit(feed_text, (75, 515))

        pygame.draw.rect(screen, GREEN, (290, 500, 200, 50))
        play_text = font.render("Baw się", True, WHITE)
        screen.blit(play_text, (310, 515))

        pygame.draw.rect(screen, RED, (520, 500, 200, 50))
        sleep_text = font.render("Śpij", True, WHITE)
        screen.blit(sleep_text, (545, 515))

    def load_image(self):
        if self.name == "Squirtle":
            self.image = pygame.transform.scale(pygame.image.load("assets/squirtle.png"), (200, 200))
        elif self.name == "Wartotle":
            self.image = pygame.transform.scale(pygame.image.load("assets/wartotle.png"), (200, 200))
        elif self.name == "Blastoise":
            self.image = pygame.transform.scale(pygame.image.load("assets/blastoise.png"), (200, 200))
        elif self.name == "Charmander":
            self.image = pygame.transform.scale(pygame.image.load("assets/charmander.png"), (200, 200))
        elif self.name == "Charmeleon":
            self.image = pygame.transform.scale(pygame.image.load("assets/charmeleon.png"), (200, 200))
        elif self.name == "Charizard":
            self.image = pygame.transform.scale(pygame.image.load("assets/charizard.png"), (200, 200))
        elif self.name == "Bulbasaur":
            self.image = pygame.transform.scale(pygame.image.load("assets/bulbasaur.png"), (200, 200))
        elif self.name == "Ivysaur":
            self.image = pygame.transform.scale(pygame.image.load("assets/ivysaur.png"), (200, 200))
        elif self.name == "Venusaur":
            self.image = pygame.transform.scale(pygame.image.load("assets/venusaur.png"), (200, 200))
        elif self.name == "Pikachu":
            self.image = pygame.transform.scale(pygame.image.load("assets/pikachu.png"), (200, 200))


# Funkcja, która rysuje menu wyboru zwierzaka
def choose_pet():

    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - start_time

    screen.fill(BLACK)
    title_text = font.render("Wybierz swojego pokemona!", True, WHITE)
    screen.blit(title_text, (250, 50))



    # Jeżeli nie dokonamy wyboru w ciągu 5 minut, zostanie przypisany pikatchu
    if time_elapsed  > 5 * 60 * 60:
        screen.blit(pikachu_image, (270, 190))
        pygame.draw.rect(screen, YELLOW, (270, 400, 200, 50))
        pikachu_text = font.render("Pikachu", True, WHITE)
        screen.blit(pikachu_text, (275, 415))
    else :
        # Przycisk 1: Squirtle
        screen.blit(squirtle_image, (50, 190))
        pygame.draw.rect(screen, BLUE, (50, 400, 200, 50))
        squirtle_text = font.render("Squirtle", True, WHITE)
        screen.blit(squirtle_text, (55, 415))

        # Przycisk 2: Charmander
        screen.blit(charmander_image, (270, 190))
        pygame.draw.rect(screen, RED, (270, 400, 200, 50))
        cat_text = font.render("Charmander", True, WHITE)
        screen.blit(cat_text, (275, 415))

        # Przycisk 3: Bulbasaur
        screen.blit(bulbasaur_image, (490, 190))
        pygame.draw.rect(screen, GREEN, (490, 400, 200, 50))
        cat_text = font.render("Bulbasaur", True, WHITE)
        screen.blit(cat_text, (495, 415))

    pygame.display.update()

# Główna pętla gry
def game_loop():
    running = True
    pet = None

    while running:
        screen.fill(BLACK)

        if pet is None:
            choose_pet()
        else:
            pet.update()
            pet.draw()


        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if pet is None:
                    if 50 <= x <= 250 and 400 <= y <= 450:
                        pet = Pet("Squirtle")
                    elif 270 <= x <= 470 and 400 <= y <= 450:
                        pet = Pet("Charmander")
                    elif 490 <= x <= 690 and 400 <= y <= 450:
                        pet = Pet("Bulbasaur")

                # Sprawdzanie kliknięć przycisków
                if pet:
                    if 60 <= x <= 260 and 500 <= y <= 550:  # Nakarm
                        pet.feed()
                        pet.gainExperience()
                    elif 290 <= x <= 490 and 500 <= y <= 550:  # Baw się
                        pet.play()
                        pet.gainExperience()
                    elif 520 <= x <= 720 and 500 <= y <= 550:  # Śpij
                        pet.sleep()
                        pet.gainExperience()
        pygame.display.update()

# Uruchomienie gry
game_loop()
