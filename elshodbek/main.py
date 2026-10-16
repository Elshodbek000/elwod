from xml.sax.handler import property_interning_dict

davlatlar={'AQSH': 'London','Rossiya': 'Moskva','O`zbekiston': 'Toshkent','Tojikiston': 'Dushanbe',
           'Qoraqalpog`iston': 'Bishkek','Portugaliya': 'CR7'}
for i in davlatlar:
    print(i)
for i in davlatlar.values():
    print(i)

son = input("Kalit so`zni kiriting:")
if son in davlatlar:
   print("Tog`ri")
else :
    print("Xato")

a={'olma','banan','olcha','nok','olxo`ri'}
print(a)
if 'olma' in a:
    print('olma')
if 'banan' in a:
    print('banan')
if 'olcha' in a:
    print('olcha')
if 'olxo`ri' in a:
        print('olxo`ri')
if 'nok' in a:
    print('nok')
for a in range(10):
    print(a+1,"-Tepada")
meva= {'nomi':'olma''banan','rangi':'qizil''sariq',
       'qayerdan olb kelinganligi':'Samarqand''Toshkent','tami':'shirin''zo`r',
       'sifati':'zor''yaxshi'}
for i in range(1,10):
    print(meva)
for i in meva.values():
    print(i)