import csv
import datetime


def introducere_categorii():
    while True:
        with open('categorii.txt', 'a', newline='') as file:
            file.write(f'{input("Adauga categoria: ")} \n')
            decizie = input("Doriti sa introduceti o alta categorie? (Y/N): ").lower()
            if decizie == 'n':
                break
    return True


def validare_data(data_limita):
    try:
        datetime.datetime.strptime(data_limita, '%d-%m-%Y %H:%M')
        return True
    except Exception:
        return False


def introducerea_taskurilor():
    while True:
        with open('taskuri.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',')

            task = input('Adauga un task: ')

            data_limita = input('Adauga o data limita: ')
            validarea_datei = validare_data(data_limita)

            while validarea_datei is False:
                print("Data nu are formatul corect")
                data_limita = input('Adaugati o noua data: ')
                validarea_datei = validare_data(data_limita)

                if validarea_datei is True:
                    break

            responsabil = input('Adauga persoana responsabila: ')
            categoria = input("Adauga categoria: ")

            with open('categorii.txt', 'r') as categorii_file:
                line = categorii_file.readlines()
            verificare = categoria.strip()
            new_list = [x.strip() for x in line]

            while verificare not in new_list:
                intr_categ = input('Categorie inexistenta. Reintrodu o alta categorie: ')
                if intr_categ:
                    categoria = intr_categ
                if intr_categ.strip() in new_list:
                    break
            csv_writer.writerow([task, data_limita, responsabil, categoria])
        decizie = input("Doriti sa introduceti un alt task? (Y/N): ").lower()
        print(decizie)
        if decizie == 'n':
            break

    return True


def sortare():
    with open('taskuri.csv', 'r') as file:
        rows = csv.reader(file, delimiter=',')
        li = []
        for row in rows:
            li.append(row)

        ordine = input('Alege ascendent/descendent A/D: ').lower()
        while ordine != 'a' and ordine != 'd':
            ordine = input('Eroare. Alege intre A/D - ascendent/decendent: ').lower()
            if ordine == 'a' or ordine == 'd':
                break

        decizie = int(input('Alege tipul de sortare dupa categorie:'
                            '1 - task\n'
                            '2 - data\n'
                            '3 - pers resp\n'
                            '4 - categorie\n'))
        while 1 > decizie > 4:
            decizie = int(input('Eroare. Introdu un numar de la 1 la 4: '))
            if 1 <= decizie <= 4:
                break

        if ordine == 'a':
            print(sorted(li, key=lambda x: x[decizie - 1]))
        elif ordine == 'd':
            print(sorted(li, key=lambda x: x[decizie - 1], reverse=True))


def filtrare():
    with open('taskuri.csv', 'r') as file:
        rows = csv.reader(file, delimiter=',')
        li = []
        for row in rows:
            li.append(row)

        decizie = int(input('Alege tipul de filtrare dupa categorie(1 - task /2 - data /3 - pers resp /4 - categorie): '))
        while 1 > decizie > 4:
            decizie = int(input('Eroare. Introdu un numar de la 1 la 4: '))
            if 1 <= decizie <= 4:
                break

        lista_filtrata = list(map(lambda x: x[decizie - 1], li))
        # print('Lista filtrata este: ', lista_filtrata)

        cuvant_filtrare = input('Alege un string deja utilizat dupa care sa se faca filtrarea listei: ')
        lista_ramasa = [item for item in lista_filtrata if cuvant_filtrare in item]

        return lista_ramasa

def new_task():
    with open('taskuri.csv', 'r', newline='') as file:
        rows = csv.reader(file, delimiter=',')
        lista = []
        for row in rows:
            lista.append(row)

    with open('taskuri.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        lista_taskuri = list(map(lambda x: x[0], lista))

        task_nou = input('Introduceti un nou task: ')
        while task_nou in lista_taskuri:
            task_nou = input('Task-ul se regaseste deja in lista. Introduceti un alt task: ')
            if task_nou not in lista_taskuri:
                break

        data_limita = input('Adauga o data limita: ')
        validarea_datei = validare_data(data_limita)

        while validarea_datei is False:
            print("Data nu are formatul corect")
            data_limita = input('Adaugati o noua data: ')
            validarea_datei = validare_data(data_limita)

            if validarea_datei is True:
                break

        responsabil = input('Adauga persoana responsabila: ')
        categoria = input("Adauga categoria: ")

        with open('categorii.txt', 'r') as categorii_file:
            line = categorii_file.readlines()
        verificare_categorie = categoria.strip()
        new_list = [x.strip() for x in line]

        while verificare_categorie not in new_list:
            intr_categ = input('Categorie inexistenta. Reintrodu o alta categorie: ')
            if intr_categ:
                categoria = intr_categ
            if intr_categ.strip() in new_list:
                break
        csv_writer.writerow([task_nou, data_limita, responsabil, categoria])
        file.close()
    return True

def editare():
    with open('taskuri.csv', 'r') as file:
        rows = csv.reader(file, delimiter=',')
        lista_csv = []
        for row in rows:
            lista_csv.append(row)
        file.close()

        for row in lista_csv:
            print(lista_csv.index(row), row)

        task_modificat = input('Ce task doriti sa modificati? ')

        for row in lista_csv:
            if task_modificat in row:
                decizie_task = input('Doriti sa modificati task-ul? (Y/N): ').lower()
                if decizie_task == 'y':
                    row[0] = input('Adaugati task-ul modificat: ')
                decizie_data = input('Doriti sa modificati data? (Y/N): ').lower()
                if decizie_data == 'y':
                    row[1] = input('Adauga data modificata: ')
                    validarea_datei = validare_data(row[1])
                    while validarea_datei is False:
                        print("Data nu are formatul corect")
                        data_limita = input('Adaugati o noua data: ')
                        validarea_datei = validare_data(data_limita)
                        if validarea_datei is True:
                            break
                decizie_persoana = input('Doriti sa modificati persoana responsabila? (Y/N): ').lower()
                if decizie_persoana == 'y':
                    row[2] = input('Introduceti numele persoanei responsabile: ')
                decizie_categorie = input('Doriti sa schimbati categoria (Y/N): ').lower()
                if decizie_categorie == 'y':
                    row[3] = input('Introduceti o alta categorie: ')
                    with open('categorii.txt', 'r') as categorii_file:
                        line = categorii_file.readlines()
                    verificare_categorie = row[3].strip()
                    new_list = [x.strip() for x in line]

                    while verificare_categorie not in new_list:
                        intr_categ = input('Categorie inexistenta. Reintrodu o alta categorie: ')
                        if intr_categ:
                            row[3] = intr_categ
                        if intr_categ.strip() in new_list:
                            break
        for row in lista_csv:
            print(row)
            with open('taskuri.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                for row in lista_csv:
                    csv_writer.writerow([row[0], row[1], row[2], row[3]])
    return True


def stergere_task():
    with open('taskuri.csv', 'r') as file:
        rows = csv.reader(file, delimiter=',')
        lista_csv = []
        for row in rows:
            lista_csv.append(row)
        file.close()

    for row in lista_csv:
        print(lista_csv.index(row), row)

    stergere = input('Introduceti ce task vreti sa stergeti: ')
    for row in lista_csv:
        if stergere in row:
            lista_csv.pop(lista_csv.index(row))

    for row in lista_csv:
        print(row)

    with open('taskuri.csv', 'w', newline='') as delete_file:
        csv_writer = csv.writer(delete_file, delimiter=',')
        for row in lista_csv:
            csv_writer.writerow([row[0], row[1], row[2], row[3]])

    return True


def meniu():
    with open('taskuri.csv', 'r') as file:
        rows = csv.reader(file, delimiter=',')
        li = []
        for row in rows:
            li.append(row)

        decizie = input('Alege o optiune:\n'
                        '1. Listare date\n'
                        '2. Sortare\n'
                        '3. Filtrare\n'
                        '4. Adauga un nou task\n'
                        '5. Editare detalii\n'
                        '6. Stergere task\n'
                        '(1/2/3/4/5/6)\n')

        if decizie == '1':
            print(sorted(li, key=lambda x: x[3]))
        elif decizie == '2':
            sortare()
        elif decizie == '3':
            print('Lista filtrata este: ', filtrare())
        elif decizie == '4':
            new_task()
        elif decizie == '5':
            editare()
        elif decizie == '6':
            stergere_task()

decizie_categorie = input('Doriti sa introduceti o noua categorie? (Y/N) ').lower()
if decizie_categorie == 'y':
    introducere_categorii()

decizie_task = input('Doriti sa introduceti un task? (Y/N) ').lower()
if decizie_task == 'y':
    introducerea_taskurilor()

meniu()
