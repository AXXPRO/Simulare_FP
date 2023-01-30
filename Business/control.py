import random

from Business.validare import Validator
from Erori.erori import Muie
from Infrastructura.domain import Jucator


class ServiceJucator:
    def __init__(self, repo):
        self.__REPO = repo

        self.__needed = ["Pivot", "Fundas", "Fundas", "Extrema", "Extrema"]

    def adaugare_jucator_service(self, nume,prenume,inaltime,post):
        """

        :param nume: string
        :param prenume: string
        :param inaltime: int
        :param post: string
        :return:
        """
        jucator = Jucator(nume,prenume,inaltime,post)
        valid = Validator(jucator)
        valid.is_valid()
        self.__REPO.adauga_jucator(jucator)

    def modificare_inaltime_service(self, nume,prenume, inaltime):
        """

        :param nume:  string
        :param prenume:  string
        :param inaltime:  int
        :return:
        """
        self.__lista = self.__REPO.get_all()

        for jucator in self.__lista:
            nume_jucator = jucator.get_nume()
            prenume_jucator = jucator.get_prenume()
            if nume == nume_jucator and prenume == prenume_jucator:

                self.__REPO.modifica_jucator(jucator,inaltime)

    def __is_needed(self,jucator):
        """
        Returneaza true daca e nevoie de acest tip de jucator
        :param jucator:
        :return:
        """

        if jucator.get_post() in self.__needed:
            indice = self.__needed.index(jucator.get_post())
            self.__needed.pop(indice)
            return True
        return False

    def echipa_service(self):
        """
        :return:
        """
        self.__needed = ["Pivot", "Fundas", "Fundas", "Extrema", "Extrema"]
        self.__lista = self.__REPO.get_all()
        self.__lista.sort(key = lambda x: x.get_inaltime(), reverse = True)
        self.__lista_returnat = []
        for jucator in self.__lista:
            if self.__is_needed(jucator):
                self.__lista_returnat.append(jucator)

        self.__lista_ordonata = [-1]* 5
        i_fundas = 0
        i_extrema = 3
        for elem in self.__lista_returnat:
            if elem.get_post() == "Pivot":
                self.__lista_ordonata[2] = f"{elem.get_prenume()},{elem.get_nume()},Pivot,{elem.get_inaltime()}"
            elif elem.get_post() == "Fundas":
                self.__lista_ordonata[i_fundas] = f"{elem.get_prenume()},{elem.get_nume()},Fundas,{elem.get_inaltime()}"
                i_fundas +=1
            else:
                self.__lista_ordonata[i_extrema] = f"{elem.get_prenume()},{elem.get_nume()},Extrema,{elem.get_inaltime()}"
                i_extrema +=1

        return  self.__lista_ordonata

    def __deja_exista(self,nume,prenume):
        """

        :param nume: nume din fisier
        :param prenume: prenume din fisier
        :return: True daca exita deja o persoana cu nume si prenume in fisier
        """

        self.__lista  = self.__REPO.get_all()

        for elem in self.__lista:
            if elem.get_nume() == nume and elem.get_prenume() == prenume:
                return True
        return False

    def __adaugare_jucator_random(self, nume, prenume):
        """
        :param nume:  numele stiut
        :param prenume:  prenumele stiut
        :return:
        """
        posturi = ["Fundas", "Extrema", "Pivot"]
        inaltime = random.randint(1,200)
        post = posturi[random.randint(0,2)]
        self.adaugare_jucator_service(nume,prenume,inaltime,post)

    def fisier_service(self, nume_fisier):
        """

        :param nume_fisier:
        :return: cati au fost adaugati
        """
        adaugati = 0
        try:
            f = open(nume_fisier, "r")
        except IOError:
            raise Muie("Fisier inexistent!\n")
        f.close()

        with open(nume_fisier, 'r') as fisier:
            linie = fisier.readline()
            while linie!= "":
                linie = linie.strip()
                params = linie.split()
                nume = params[0]
                prenume = params[1]
                if not self.__deja_exista(nume,prenume):
                    #ADAUGARE SI COUNTER ++
                    adaugati +=1
                    self.__adaugare_jucator_random(nume, prenume)





                linie = fisier.readline()
        return adaugati


