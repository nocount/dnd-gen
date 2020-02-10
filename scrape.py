from random import randint

from bs4 import BeautifulSoup
from urllib.request import urlopen as url


# Loading the page into bs from weapon page url
page_link = 'http://dnd5e.wikidot.com/'
page = url(page_link)
soup = BeautifulSoup(page, 'html.parser')

page_content = soup.findAll('div', {'id': 'page-content'})


def scrape_classes():
    classes = {}
    class_categories = page_content[0].findAll('div', {'class': 'col-md-7'})
    for c in class_categories:
        single_class = c.find('h1')
        if single_class:
            class_name = single_class.find('a').text

            if c.find('p'):
                sub_classes_ref = c.p.findAll('a')
                sub_classes = []
                for i in sub_classes_ref:
                    sub_classes.append(i.text)

                classes[class_name] = sub_classes

    return classes


def scrape_races():
    races = []
    race_cats = []

    race_ids = ['toc1', 'toc2', 'toc3']
    for r in race_ids:
        race_cats.append(page_content[0].find('h1', {'id': r}).next_sibling.next_sibling)

    for r in race_cats:
        for rf in r.findAll('a'):
            races.append(rf.text)

    return races


def generate_character(classes, races):
    class_list = list(classes)
    class_num = randint(0, len(class_list)-1)
    class_pick = class_list[class_num]

    sub_class_list = classes.get(class_pick)
    sub_class_num = randint(0, len(sub_class_list)-1)
    sub_class_pick = sub_class_list[sub_class_num]

    race_num = randint(0, len(races)-1)
    race_pick = races[race_num]

    return class_pick, sub_class_pick, race_pick


if __name__ == '__main__':
    classes = scrape_classes()
    races = scrape_races()
    main_class, sub_class, race = generate_character(classes, races)

    print('Congratulations you are a: ' + race + ', ' + sub_class + ' ' + main_class)

