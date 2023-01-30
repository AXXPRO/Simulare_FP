from Erori.erori import Muie


class Validator:
    def __init__(self, jucator):
        """
        Clasa ce va valida un jucator
        """
        self.__jucator = jucator
        self.__roluri = ["Fundas", "Pivot", "Extrema"]
    def is_valid(self):
        """

        :return: True daca jucator e Valid
        """
        err = ""

        inaltime = self.__jucator.get_inaltime()
        if inaltime <=0:
            err+="Inaltime invalida!\n"
        post = self.__jucator.get_post()
        if post not in self.__roluri:
            err+="Post invalid!\n"
        if err !="":
            raise Muie(err)


