import unittest

from Business.control import ServiceJucator
from Business.validare import Validator
from Erori.erori import Muie
from Infrastructura.domain import Jucator
from Infrastructura.repo import JucatorRepoFisier


class TestDomain(unittest.TestCase):
    def setUp(self):
        self.__nume = "Marc"
        self.__prenume = "George"
        self.__inaltime = 121
        self.__post = "Pivot"
    def tearDown(self):
        pass

    def testEqual(self):
        """
        Testeaza egalitatea
        :return:
        """
        jucator1 = Jucator(self.__nume, self.__prenume, self.__inaltime, self.__post)
        jucator2 = Jucator(self.__nume, self.__prenume, self.__inaltime, self.__post)
        jucator3 = Jucator("Belga", "DAm", self.__inaltime, self.__post)

        self.assertEqual(jucator1, jucator2)

        self.assertNotEqual(jucator1,jucator3)

    def testGetter(self):
        """
        Testeaza daca functiile de get fucntioneaza
        :return:
        """
        jucator = Jucator(self.__nume,self.__prenume,self.__inaltime,self.__post)
        self.assertEqual(jucator.get_nume(),self.__nume)
        self.assertEqual(jucator.get_prenume(), self.__prenume)
        self.assertEqual(jucator.get_inaltime(), self.__inaltime)
        self.assertEqual(jucator.get_post(), self.__post)
    def testSetter(self):
        """
        Testeaza functiile de set
        :return:
        """
        jucator = Jucator(self.__nume, self.__prenume, self.__inaltime, self.__post)
        jucator.set_inaltime(130)
        self.assertEqual(jucator.get_inaltime(),130)

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.__jucator = Jucator("a","b",123,"Pivot")
        self.__jucator_rau = Jucator("a", "b",-312,"Atac")
    def tearDown(self):
        pass
    def testValid(self):
        valid = Validator(self.__jucator)
        valid.is_valid()

        valid = Validator(self.__jucator_rau)

        self.assertRaises(Muie, valid.is_valid)

class TestService(unittest.TestCase):
    def setUp(self):
        self.__path = r"jucatori_test.txt"
        self.__REPO = JucatorRepoFisier(self.__path)
        self.__SERVICE = ServiceJucator(self.__REPO)
        self.__jucator1 = Jucator("Messi","George",192,"Fundas")
        self.__jucator2 = Jucator("Ronaldo","Ronaldinio",120,"Pivot")
        self.__jucator_de_adaugat = Jucator("Adauga", "George", 192, "Fundas")
    def tearDown(self):
        self.__REPO.empty()
        self.__REPO.adauga_jucator(self.__jucator1)
        self.__REPO.adauga_jucator(self.__jucator2)
    def testModificare(self):
        self.__inaltime = 1
        self.__SERVICE.modificare_inaltime_service("Messi","George", 2)

        self.__lista = self.__REPO.get_all()

        for juc in self.__lista:
            if juc.get_nume() == "Messi":
                self.assertEqual(juc.get_inaltime(), 2)
    def testAdaugare(self):
        self.__SERVICE.adaugare_jucator_service(self.__jucator_de_adaugat.get_nume(),self.__jucator_de_adaugat.get_prenume(),self.__jucator_de_adaugat.get_inaltime(),self.__jucator_de_adaugat.get_post())
        self.__lista = self.__REPO.get_all()
        self.assertEqual(len(self.__lista), 3)


class TestRepo(unittest.TestCase):
    def setUp(self):
        self.__path = r"jucatori_test.txt"
        self.__REPO = JucatorRepoFisier(self.__path)
        self.__jucator1 = Jucator("Messi","George",192,"Fundas")
        self.__jucator2 = Jucator("Ronaldo","Ronaldinio",120,"Pivot")
    def testModifica(self):
        self.__inaltime = 1
        self.__REPO.modifica_jucator(self.__jucator1, self.__inaltime)
        self.__lista = self.__REPO.get_all()

        for juc in self.__lista:
            if juc.get_nume() == "Messi":
                self.assertEqual(juc.get_inaltime(), 1)
    def tearDown(self):
        self.__REPO.empty()
        self.__REPO.adauga_jucator(self.__jucator1)
        self.__REPO.adauga_jucator(self.__jucator2)
    def testLoad(self):
        """
        testeaza ca incarca bine din fisier
        :return:

        """
        self.__lista = self.__REPO.get_all()
        self.assertEqual(2, len(self.__lista))
    def testStore(self):
        """
        Testeaza stocarea in fisier
        :return:
        """
        self.__jucator3 = Jucator("Cristina", "Neagu", 175, "Pivot")
        self.__REPO.adauga_jucator(self.__jucator3)
        self.__lista = self.__REPO.get_all()
        self.assertEqual(len(self.__lista),3)

