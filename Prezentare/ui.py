import os

from Erori.erori import Muie


class UI:
    def __init__(self,service):
        """
        Initializatorul clasei de UI
        :param service:
        """
        self.__SERVICE = service

    def __afisare_ui(self):
        """
        Functia va afisa un text de tipul >>>
        :return:
        """
        print(">>>",end = "")

    def run_ui(self):
        os.system('cls')
        ok = True
        comenzi = {
            "adauga_jucator": self.__adaugare_jucator_ui,
            "modifica_inaltimea": self.__modificare_inaltime_ui,
            "echipa": self.__echipa_ui,
            "fisier": self.__fisier_ui

        }

        while ok:
            self.__afisare_ui()
            comanda  = input()
            if comanda == "" or comanda == "exit":
                ok = False
            else:
                comanda = comanda.strip()
                params = comanda.split()

                if params[0] not in comenzi:
                    print("Comanda invalida!")
                else:
                    try:
                        comenzi[params[0]](params[1:])
                    except Muie as err:
                        print(str(err))

    def __adaugare_jucator_ui(self, params):
        """
        :param params: numele, prenumele, inaltime, post
        :return:
        """
        if len(params)!=4:
            raise Muie("Numar de parametrii incorect, niciuna din campuri nu pot fi nule!")
        try:
            nume = params[0]
            prenume = params[1]
            inaltime = int(params[2])
            post = params[3]
        except ValueError:
            raise Muie("Parametrii invalizi!")
        self.__SERVICE.adaugare_jucator_service(nume,prenume,inaltime,post)

    def __modificare_inaltime_ui(self, params):
       """

       :param params: nume, prenume, inaltime
       :return:
       """
       if len(params)!=3:
           raise Muie("Numar de parametrii incorect!")
       try:
           nume = params[0]
           prenume = params[1]
           inaltime = int(params[2])
       except ValueError:
           raise Muie("Parametrii invalizi!")

       self.__SERVICE.modificare_inaltime_service(nume,prenume,inaltime)

    def __echipa_ui(self, params):
        """

        :param params:
        :return:
        """
        lista = self.__SERVICE.echipa_service()

        print("Prenume,Nume,Post,Inaltime")
        for element in lista:
            print(element)
    def __fisier_ui(self,params):
        """


        :param params: nume_fisier
        :return:
        """
        if len(params) != 1:
            raise Muie("Numar de parametrii incorect!")
        numar = self.__SERVICE.fisier_service(params[0])
        print(f"S-au adaugat {numar} persoane din fisier")