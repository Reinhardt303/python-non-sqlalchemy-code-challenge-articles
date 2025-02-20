class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 50 >= len(title) >= 5 and not hasattr(self, '_title'):
            self._title = title
        else:
            raise Exception('Invalid title')

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception('Author not found')

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception('Magazine not found')
        
class Author:
    
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, 'name'): #check hasattr if fails
            self._name = name
        else:
            raise Exception('Invalid author')

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(list(set([article.magazine.category for article in Article.all if article.author == self]))) ==0:
            return None
        else:
            return list(set([article.magazine.category for article in Article.all if article.author == self]))

class Magazine:
    
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 16 >= len(name) >= 2:
            self._name = name
        else:
            raise Exception('Invalid name')

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise Exception('Invalid category')

    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))

    def article_titles(self):
        if len([article.title for article in Article.all if article.magazine == self]) == 0:
            return None
        
        else:
            return [article.title for article in Article.all if article.magazine == self]

    def contributing_authors(self):
        
        if len([article.author for article in Article.all if article.magazine == self]) <= 2:
            return None
        
        else:
            return [article.author for article in Article.all if article.magazine == self]
