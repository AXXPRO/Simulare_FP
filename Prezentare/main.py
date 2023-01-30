from Business.control import ServiceJucator
from Infrastructura.repo import JucatorRepoFisier
from Prezentare.ui import UI


def main():
    """
    Aici incepe aplciatia
    :return:
    """
    repo = JucatorRepoFisier(r"jucatori.txt")
    service = ServiceJucator(repo)
    ui = UI(service)
    ui.run_ui()
if __name__ == '__main__':
    main()

