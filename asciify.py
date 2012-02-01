import requests
import BeautifulSoup as soup
import HTMLParser
from urllib import urlencode
from random import uniform

parser = HTMLParser.HTMLParser()

fonts = [ '3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'big', 'bigchief', 'binary', 'block', 'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal', 'computer', 'contessa', 'contrast', 'cosmic', 'cosmike', 'cyberlarge', 'cybermedium', 'cybersmall', 'cygnet', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'drpepper', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fuzzy', 'goofy', 'gothic', 'graffiti', 'hollywood', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'jazmine', 'kban', 'larry3d', 'lcd', 'lean', 'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'nipples', 'o8', 'ogre', 'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid', 'rectangles', 'relief', 'relief2', 'rev', 'roman', 'rot13', 'rounded', 'rowancap', 'rozzo', 'sblood', 'script', 'serifcap', 'shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello', 'standard', 'starwars', 'stellar', 'stop', 'straight', 'swan', 'tanja', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant', 'tinker-toy', 'tombstone', 'trek', 'twopoint', 'univers', 'usaflag', 'weird']


def get_random_font():
    return fonts[int(uniform(0, len(fonts)))]

def random_asciify(s, width):
    font = get_random_font()
    print font
    return asciify(s, font, width) 
    
def asciify(s, font, width):
    data = {'TEXT': s, 'x': 0, 'y': 0, 'FONT': font, 'RICH': 'no', 'FORM': 'left', 'STRE': 'no', 'WIDT': width}
    query_string = urlencode(data)    
    url = '{0}?{1}'.format('http://www.network-science.de/ascii/ascii.php', query_string)
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        s = soup.BeautifulSoup(r.content)
        t = s.findAll('pre')[1].contents[0]
        t2 = parser.unescape(t)
        return t2


result = random_asciify('appropriete message', 80)
print result if result != None else 'Didnt work'


