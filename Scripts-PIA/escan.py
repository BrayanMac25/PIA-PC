import nmap
import pandas as pd

def Escaneo(begin, end, target):
    scanner = nmap.PortScanner()
    datos=[]
    for i in range (begin, end+1):
        res = scanner.scan(target,str(i))
        datos.append(type(res))
        for x,y in res.items():
            datos.append([x,y])
        res = res['scan'][target]['tcp'][i]['state']
        datos.append(f'por {i} is {res}.')
    df_datos = pd.DataFrame(datos)
    df_datos.to_csv('Escaneo.txt')




















