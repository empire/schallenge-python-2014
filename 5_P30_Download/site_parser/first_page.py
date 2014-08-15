import random

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def pick_random_category(soup):
    categories = get_categories(soup)
    return random.choice(categories)

def get_categories(soup):
    categories_tags = get_base_categories_lists(soup)
    return extract_categories(categories_tags)


def extract_categories(categories_tags):
    categories_links = []
    for category_tag in categories_tags:
        href = category_tag.attrs['href']
        if href.startswith('http://p30download.com/'):
            categories_links.append(href)

    return categories_links


def get_base_categories_lists(soup):
    all_links = set(soup.select('#nav-wrapper > nav li > a'))
    homepage_links = set(soup.select('#nav-wrapper > nav .homepage li > a'))
    return all_links - homepage_links
    # return soup.select('#nav-wrapper nav > ul > li')
