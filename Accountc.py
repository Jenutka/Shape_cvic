class Transaction:

    def __init__(self, amount, date, currency="EUR", eur_conversion_rate=1, description=None):
        """
        >>> t = Transaction(100, "2008-12-09")
        >>> t.amount, t.currency, t.eur_conversion_rate, t.eur
        (100, 'EUR', 1, 100)
        >>> t = Transaction(250, "2009-03-12", "CZ", 0.26)
        >>> t.amount, t.currency, t.eur_conversion_rate, t.eur
        (250, 'CZ', 0.26, 65.0)
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__eur_conversion_rate = eur_conversion_rate
        self.__description = description

    def __repr__(self):
        return self.description

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency

    @property
    def eur_conversion_rate(self):
        return self.__eur_conversion_rate

    @property
    def description(self):
        return self.__description

    @property
    def eur(self):
        return (self.amount * self.eur_conversion_rate)


class Account:

    def __init__(self, number, name, transactions=None):
        """
        >>> tr_1 = Transaction(350, "2022-03-01", "CZK", 25, "Nákup číslo 1")
        >>> tr_2 = Transaction(1560, "2018-03-01", "EUR", 1, "Nákup číslo 2")
        >>> tr_1.amount, tr_1.currency, tr_1.date, tr_1.description
        (350, 'CZK', '2022-03-01', 'Nákup číslo 1')
        >>> tr_2.amount, tr_2.currency, tr_2.date, tr_2.description
        (1560, 'EUR', '2018-03-01', 'Nákup číslo 2')
        >>> ucet_1 = Account(123456, "účet jedna")
        >>> ucet_1.add(tr_1)
        [Nákup číslo 1]
        >>> ucet_1.add(tr_2)
        [Nákup číslo 1, Nákup číslo 2]
        >>> ucet_1.transactions
        [Nákup číslo 1, Nákup číslo 2]
        >>> ucet_1.number
        123456
        """
        self.__number = number
        self.__name = name
        if transactions == None:
            self.__transactions = []
        elif (isinstance(transactions, list)):
            self.__transactions = self.__transactions[:]
        else:
            print("objekt musí být typu <class 'list'>")


    @property
    def number(self):
        return self.__number

    @property
    def transactions(self):
        return self.__transactions

    def add(self, transaction):
        assert isinstance(transaction, Transaction), "Objekt musí být třídy Transaction"
        self.__transactions.append(transaction)
        return self.__transactions



if __name__ == "__main__":
    import doctest
    doctest.testmod()