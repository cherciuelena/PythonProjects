import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = ['https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/',
        'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-21-ianuarie-ora-13-00/',
        'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-22-ianuarie-ora-13-00/',
        'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-23-ianuarie-ora-13-00/',
        'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-24-ianuarie-ora-13-00/',
        'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-25-ianuarie-ora-13-00/'
        ]
main_header = []
main_dataset = []

for url in urls:
    req = requests.get(url)
    link = BeautifulSoup(req.text, 'html.parser')

    if url == urls[0]:
        main = link.find_all('div', attrs={'class': 'entry-content'})
        header_list = []
        dataset = []

        for obj in main:
            for table_index in obj.find_all('table'):
                for table_trs in table_index.find_all('tr'):
                    td_list = []

                    for index, td in enumerate(table_trs.find_all('td')):
                        td_list.append(td.get_text())

                    dataset.append(td_list)

        del dataset[45:]
        for lista in dataset:
            del lista[3:]
        del dataset[0]
        del dataset[-1][-1]
        dataset[-1].insert(0,'')

        main_dataset = dataset

    if url in urls[1:6]:
        main = link.find_all('div', attrs={'class': 'entry-content'})
        header_list = []
        dataset = []

        for obj in main:
            for table_index in obj.find_all('table'):
                for table_trs in table_index.find_all('tr'):
                    td_list = []
                    for index, td in enumerate(table_trs.find_all('td')):
                        td_list.append(td.get_text())

                    dataset.append(td_list)

        if url != urls[2]:
            del dataset[45:]
            for lista in dataset[0:-1]:
                del lista[3:]
                del lista[0:2]
            del dataset[0]
            del dataset[-1][0]
        else:
            del dataset[43]
            del dataset [45:]
            for lista in dataset[0:-1]:
                del lista[3:]
                del lista[0:2]
            del dataset[0]
            del dataset[-1][0]


        for i,j in zip(main_dataset,dataset):
            i.append(j[0])


main_header= ['NR CRT', 'JUDET', '20.01','21.01','22.01','23.01','24.01','25.01']

df = pd.DataFrame(main_dataset, columns=main_header)
print(df)
df.to_excel("Covid.xlsx", header=main_header, index=0)