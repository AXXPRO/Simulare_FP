from Infrastructura.domain import Jucator


class JucatorRepoFisier:
    def __init__(self, path):
        """
        Initializatorul repoului din fisier

        """
        self.__lista = []
        self.__path = path

        self.__load_from_file()

    def get_all(self):
        """

        :return: lista cu toti jucatorii
        """
        self.__load_from_file()
        return self.__lista

    def modifica_jucator(self,jucator, inaltime):
        """

        :param jucator: jucatorul cui ii actualizam inaltimea
        :param inaltime:  inaltimea cu care actualizam
        :return:
        """
        self.__load_from_file()
        for j in self.__lista:
            if j == jucator:
                j.set_inaltime(inaltime)
        self.__store_to_file()

    def adauga_jucator(self,jucator):
        """
        Functia resposnabila pentru adaugarea de jucatori in aplicatie
        :return:
        jucator - obiect de tipul jucator
        """
        self.__load_from_file()
        self.__lista.append(jucator)
        self.__store_to_file()

    def empty(self):
        """
        Goleste lista de jcuatori
        :return:
        """
        self.__lista = []
        self.__store_to_file()
    def __load_from_file(self):
        self.__lista = []
        with open(self.__path, 'r') as fisier:
            linie = fisier.readline()
            while linie != "":
                linie = linie.strip()
                params = linie.split(',')
                jucator = Jucator(params[0], params[1], int(params[2]),params[3])
                self.__lista.append(jucator)
                linie = fisier.readline()

    def __store_to_file(self):
        """
        Va salva in fisier schimbarile
        :return:
        """
        with open(self.__path, 'w') as fisier:
            for jucator in self.__lista:
                fisier.write(str(jucator))
                fisier.write('\n')


