import matplotlib.pyplot as plot
import pandas as pd

description = ('Country', ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
dataset = [   ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ':']),
              ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
              ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
              ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
              ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
              ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93', ': ', '96 ']),
              ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
              ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
              ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
              ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
              ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
              ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
              ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
              ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
              ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
              ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
              ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
              ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
              ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
              ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99', '98 ']),
              ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
              ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
              ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
              ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
              ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
              ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82 ']),
              ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
              ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
              ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
              ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
              ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
              ('RO', ['47 ', '54 ', '58 ', '61 ', '68 ', '72 ', '76 ', '81 ', '84 ']),
              ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
              ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
              ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
              ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
              ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84', '88 ']),
              ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
              ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']), ]

# salvare date csv
description2 = list(description)
value = [an for an in description[1]]
value2 =[]
value2.append(description2[0])
description_csv = value2 + value

b = dict(dataset)
data_set_final = []
for key, val in b.items():
    data_set_final.append([key] + val)


df = pd.DataFrame(data_set_final, columns=description_csv)
df.to_csv('date.csv', index=0)

# inlocuire valori nule cu 0
df = pd.read_csv('date.csv')

df.replace(': ', 0, inplace=True)
df.replace(':', 0, inplace=True)
print(df)

# calcul medie pe fiecare tara, adugare coloana in tabelul format
df.set_index('Country').transpose().to_csv('date2.csv')
df = pd.read_csv('date2.csv')
mean_value =list(df.describe().loc['mean'])
mean_value[0] = 'Mean'

description_csv.append(mean_value[0])
del mean_value[0]
print(len(data_set_final))
print(len(mean_value))

for element1, element2 in zip(mean_value, data_set_final):
    element2.append(element1)

print(data_set_final)
print(mean_value)

df = pd.DataFrame(data_set_final, columns=description_csv)
df.to_csv('date3.csv', index=0)
df.set_index('Country').transpose().to_csv('date4.csv')

df = pd.read_csv('date4.csv')

# afisati informatii referitoare la date cu ajutorul functiei describe
print(df.describe())

# grafic tip scatter pentru primele 2 tari
df.plot(kind='scatter', x='AL', y='AT')
plot.show()

# histograma a datelor pentru romanaia
df['RO'].plot(kind='hist')
plot.show()