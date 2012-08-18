import requests
import BeautifulSoup as soup

from os.path import exists

SEPERATOR = '===============++++SEPERATOR++++====================\n'
DEFAULT_FILENAME = 'animals.saved'


def get_animals():

    r = requests.get('http://www.heartnsoul.com/ascii_art/ascii_animals_indx.htm')
    s = soup.BeautifulSoup(r.content)
    animals = []
    for c in [b.get('href') for b in s.findAll('a') if b.get('href').endswith('.txt')]:
        animal_txt = requests.get('http://www.heartnsoul.com/ascii_art/{0}'.format(c))
        animal = ''
        lines_added = 0
        for line in animal_txt.content.split('\n'):
            stripped = line.strip()
            if len(stripped) == 0:
                if len(animal) > 0 and lines_added > 4:
                    animals.append(animal)
                animal = ''
                lines_added = 0
            else:
                animal += line + '\n'
                lines_added += 1

    return animals


def save_animals(animals, filename=DEFAULT_FILENAME):
    f = open(filename, 'w+')
    for animal in animals:
        f.write(animal)
        f.write(SEPERATOR)
    f.close()


def load_animals(filename=DEFAULT_FILENAME):
    if exists(filename):
        f = open(filename, 'r+')
        body = f.read()
        return body.split(SEPERATOR)
        f.close()
    else:
        return None

animals = load_animals()
if animals == None:
    animals = get_animals()
    save_animals(animals)
