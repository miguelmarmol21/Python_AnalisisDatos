import pandas as pd 

#Organizaer los datos

tabla1=pd.read_csv("./data/empleados.csv")

from data.comidas import comidas
tabla2=pd.DataFrame(comidas,columns=['nombrePlato','precioUnitario'])


from data.medicos import crearMedicos
medicos=crearMedicos()
tabla3=pd.DataFrame(medicos)

'''print(tabla1)
print("\n")
print(tabla2)
print("\n")
print(tabla3)'''

#Como mostrar los primeros registros indicando la cantidad dentro del head(cantidad)

'''tabla1Modicada=tabla1.head(50)
print(tabla1Modicada)'''


#Como mostrar los ultimos registros indicando la cantidad dentro del tail(cantidad)

'''tabla1Modicada=tabla1.tail(50)
print(tabla1Modicada)'''

#Como mostrar un campo especifico

'''tabla1Modicada=tabla1['salario']
print(tabla1Modicada)'''

#Como mostrar varios campos especificos

'''tabla1Modicada=tabla1[['nombres','salario']].head(10)
print(tabla1Modicada)'''


