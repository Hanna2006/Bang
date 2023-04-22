# BME - 2.hét, labor: Kettő meg három
egyik = int(input('Írj be egy számot... '))
másik  = int(input('Írj be még egy számot... '))
print('Az összegük: ', egyik + másik, '.', sep='')

# BME - 2.hét, labor: Sztringek különleges karakterekkel
print ('A print', "(\'hello')",  'kiírja, hogy "hello",',  '\nés kezd egy új sort. \nA', ("\\t"),  'karaktert tabulátornak nevezzük.', '\nA következő 8-cal osztható sorszámú oszlopra lehet ugrani vele.')

# BME - 2.hét, labor: A tartály
from cmath import sqrt
import math
from os import sep
print('Tartály festése')
tartaly_magassaga = float(input('Milyen magas a tartály?'))
tartaly_atmeroje = float(input('Mekkora a tartály átmérője?'))
sugar = tartaly_atmeroje/2
felulet = ((2 * sugar**2 * math.pi) + (tartaly_magassaga * 2 * sugar * math.pi)) 
festek_mennyiseg = felulet/2
print(festek_mennyiseg, 'doboz festék kell.')

# BME - Kör területe és kerülete
import math
sugar = float(input('Mekkora a kör sugara?'))
print('A kör sugara: ', sugar, '.', sep='')
kerület = 2 * sugar * math.pi
terület = sugar**2 * math.pi
print('Kerület: ', kerület, '.', sep='')
print('Terület: ', terület, '.', sep='')

# BME - 2.hét, labor: Szakasz hossza
import math
x_1 = int(input('Mi az egyik pont x koordinátája?'))
y_1 = int(input('Mi az egyik pont y koordinátája?'))
x_2 = int(input('Mi a másik pont x koordinátája?'))
y_2 = int(input('Mi a másik pont y koordinátája?'))
if x_1 > x_2:
    a = x_1 - x_2
else: 
    a = x_2 - x_1
if y_1 > y_2:
    b = y_1 - y_2
else: 
    b = y_2 - y_1
szakasz_hossza = math.sqrt(a**2 + b**2)
print('A két pont közé húzott egyenes szakasz hossza: ', szakasz_hossza, '.', sep='')

