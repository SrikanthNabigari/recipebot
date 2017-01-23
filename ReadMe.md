## Food Recipes Web Crawling Bot

### Tools required to run the bots

```
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

```
sudo pip install scrapy
```

### Commands to run the bots to crawl recipes from Recipe Websites

1. [Epicurious](http://epicurious.com)

```
scrapy crawl epicuriousrecipebot -o epicuriousrecipes.json
```

2. [Yummly](http://yummly.com) (Unfinished)

```
scrapy crawl yummlyrecipebot -o epicuriousrecipes.json
```

3. [BbcGoodFood](http://bbcgoodfood.com)

```
scrapy crawl bbcgfrecipebot -o bbcgfsrecipes.json
```