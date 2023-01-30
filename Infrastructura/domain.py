class Jucator:
    """
    Clasa ce tine tipurile de jucatori
    """
    def __init__(self, nume,prenume,inaltime,post):
        """
        Initializatorul unui Jucator
        :param nume: string
        :param prenume: string
        :param inaltime: int
        :param post: string from a set of values
        """
        self.__nume = nume
        self.__prenume = prenume
        self.__inaltime = inaltime
        self.__post = post

    def get_nume(self):
        return self.__nume
    def get_prenume(self):
        return self.__prenume
    def get_inaltime(self):
        return self.__inaltime
    def get_post(self):
        return self.__post


    def set_inaltime(self, inaltime):
        """

        :param inaltime:  int
        :return:
        """
        self.__inaltime = inaltime

    def __str__(self):
        """
        Modul in care va fi printat un jucator
        :return:
        """
        return str(f"{self.__nume},{self.__prenume},{self.__inaltime},{self.__post}")

    def __eq__(self, other):
        """Returneaza true daca egale"""
        ok = True
        if self.__inaltime != other.__inaltime:
            ok = False
        if self.__nume != other.__nume:
            ok = False
        if self.__prenume != other.__prenume:
            ok = False
        if self.__post != other.__post:
            ok = False
        return ok


