import datetime


def validator(cnp):
    """
    :param cnp: CNP-ul introdus de la tastatura
    :return: CNP-ul valid
    """
    while len(cnp) != 13 or cnp.isdigit() is False:
        cnp = input('Reintrodu CNP-ul: ')
    return cnp


def validare_sex(cnp):
    """
    :param cnp: CNP-ul introdus
    :return: sexul corespunzator CNP-ului
    """
    if int(cnp[0]) in range(1, 10):
        return True
    return False


def validare_data_nastere(cnp):
    data_nastere = cnp[1:7]
    try:
        datetime.datetime.strptime(data_nastere, '%y%m%d')
        return True
    except Exception:
        return False


def validare_judet(cnp):
    judet = int(cnp[7:9])
    if judet < 47 or judet in [51, 52]:
        return True
    return False


def validare_numar(cnp):
    numar = int(cnp[9:12])
    if numar in range(1, 1000):
        return True
    return False


def validator_control(cnp):
    const = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    cifra_control = int(cnp[-1])

    """Varianta 1 - finala"""
    cifre_integer_cnp = list(map(int, cnp))

    """Varianta 2"""
    # cifre_cnp = list(cnp)
    # cifre_integer_cnp = [int(cifra) for cifra in cifre_cnp]
    # print(cifre_integer_cnp)

    """Varianta 3"""
    # cifre_cnp = list(cnp)
    # cifre_integer_cnp = []
    # for cifra in cifre_cnp:
    #     cifre_integer_cnp.append(int(cifra))

    product = list(map(lambda x, y: x * y, const, cifre_integer_cnp))

    if sum(product) % 11 == cifra_control or (sum(product) % 11 == 10 and cifra_control == 1):
        return True
    return False


def validator_cnp(cnp):
    if validare_sex(cnp) and validare_data_nastere(cnp) and validare_judet(cnp) and validare_numar(
            cnp) and validator_control(cnp):
        return 'Valid'
    return 'Invalid'


variabila_cnp = validator(input('Intrdocuceti CNP-ul: '))
print(validator_cnp(variabila_cnp))
