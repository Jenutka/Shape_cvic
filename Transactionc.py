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

if __name__ == "__main__":
    import doctest

    doctest.testmod()