class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        books = [contract.book for contract in Contract.all if contract.author == self]
        return books
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        total = sum([contract.royalties for contract in Contract.all if contract.author == self])
        return total

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        contracts = [contract for contract in Contract.all if contract.book == self]
        return contracts
    
    def authors(self):
        author = [contract.author for contract in Contract.all if contract.book == self] 
        return author

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else: raise Exception

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else: raise Exception

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else: raise Exception

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else: raise Exception

    @classmethod
    def contracts_by_date(cls, date):
        contracts = [contract for contract in cls.all if contract.date == str(date)]
        return contracts
    