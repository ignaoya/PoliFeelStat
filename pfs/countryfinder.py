from pfs.countryinfo import countries
import codecs

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polifeelstat.settings')

import django
django.setup()


def find_country(textfile):
    with codecs.open(textfile, "r", encodings="utf-8", errors='ignore') as f:
        text = f.read()
        countryList = [c['name'] for c in countries if (c['name'] in text | c['capital'] in text)]
        f.closed
        return countryList

if __name__ == '__main__':
    print("This module works with newsAnalyser.py")
