import pickle

class AccountError(Exception): pass

class NoFilenameError(AccountError): pass

class SaveError(AccountError): pass

class LoadError(AccountError): pass

class Transaction:

    def __init__(self, amount, date, currency="EUR", eur_conversion_rate=1, description=None):
        """
        Třída Transaction uchovává transakce

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
        Třída Account uchovává číslo účtu, jeho jméno a přidružené transakce třídy Transaction

        >>> tr_1 = Transaction(350, "2022-03-01", "CZK", 25, "Nákup číslo 1")
        >>> tr_2 = Transaction(1560, "2018-03-01", "EUR", 1, "Nákup číslo 2")
        >>> tr_1.amount, tr_1.currency, tr_1.date, tr_1.description
        (350, 'CZK', '2022-03-01', 'Nákup číslo 1')
        >>> tr_2.amount, tr_2.currency, tr_2.date, tr_2.description
        (1560, 'EUR', '2018-03-01', 'Nákup číslo 2')
        >>> ucet_1 = Account(123456, "účet jedna")
        >>> ucet_1.apply(tr_1)
        [Nákup číslo 1]
        >>> ucet_1.apply(tr_2)
        [Nákup číslo 1, Nákup číslo 2]
        >>> ucet_1.transactions
        [Nákup číslo 1, Nákup číslo 2]
        >>> ucet_1.number
        123456
        >>> len(ucet_1)
        2
        >>> ucet_1.balance
        10310.0
        >>> ucet_1.save()
        123456.acc
        Soubor 123456.acc uložen
        >>> ucet_2 = Account(987654, "účet dva")
        >>> ucet_2.load('123456.acc')
        Soubor 123456.acc načten
        >>> tr_3 = Transaction(500, "2022-04-01", "DOL", 2, "Nákup číslo 3")
        >>> ucet_2.apply(tr_3)
        [Nákup číslo 1, Nákup číslo 2, Nákup číslo 3]
        >>> ucet_2.number
        987654
        >>> ucet_2.save()
        987654.acc
        Soubor 987654.acc uložen
        >>> ucet_2.name
        'účet dva'
        """
        assert len(name) >= 4, "Jméno musí mít minimálně 4 znaky"
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
    def name(self):
        return self.__name

    @property
    def transactions(self):
        return self.__transactions

    def __len__(self):
        return len(self.transactions)

    def _balance(self):
        _bal = 0
        for transaction in self.transactions:
            _bal += float(transaction.eur)
        return _bal

    @property
    def balance(self):
        return self._balance()

    def set_name(self, name):
        assert len(name) >= 4, "Jméno musí mít minimálně 4 znaky"
        self.__name = name

    def apply(self, transaction):
        assert isinstance(transaction, Transaction), "Objekt musí být třídy Transaction"
        self.__transactions.append(transaction)
        return self.__transactions

    def save(self):
        _filename = str(self.number) + ".acc"
        print(_filename)

        fh = None
        try:
            data = self.transactions
            fh = open(_filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()
                print(f"Soubor {_filename} uložen")

    def load(self, filename=None):
        if filename is not None:
            assert filename.lower().endswith(".acc"), "Soubor musí mít příponu *.acc"
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None
        try:
            fh = open(self.filename, "rb")
            data = pickle.load(fh)
            self.__transactions = data
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()
                print(f"Soubor {self.filename} načten")


if __name__ == "__main__":
    import doctest
    doctest.testmod()