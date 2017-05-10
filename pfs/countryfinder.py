from pfs.countryinfo import countries
import codecs

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polifeelstat.settings')

import django
django.setup()


def find_country(textfile):
    with codecs.open(textfile, "r", encodings="utf-8", errors='ignore') as f:
        text = f.read()
        countryList = []
        for c in countries:
            if c['name'] in text:
                countryList.append(c['name'])
        f.closed
        return countryList

if __name__ == '__main__':
    print("This module does works with newsAnalyser.py")
