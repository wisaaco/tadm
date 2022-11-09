"""
penguin.py

Description:
    Primera entrega de ejercicios.
    
Author:
    Joan Pont (jponte98@gmail.com)
"""

import pandas as pd
import numpy as np
from palmerpenguins import load_penguins

def pretty_printing(i):
    print("-"*100)
    print(f'EJERCICIO {i}')
    print("-"*100)
    print("\n\n")


def main():
    """Resolución de 6 cuestiones sobre el dataset de pinguinos"""

    ######################################################################################
    # EJERCICIO 1
    ###################################################################################### 

    pretty_printing(1)

    # Cargamos la librería
    penguins = load_penguins()
    # Guardamos las dimensiones del dataset
    dimensiones = penguins.shape
    # Imprimimos el número de observaciones
    print(f'Número de observaciones: {dimensiones[0]} \n')
    # Imprimimos su información
    print(f'Tipo de dato de las columnas:') 
    print(f'\n {penguins.info()} \n')
    # Vemos las columnas que tienen valores NA
    print(f'Las columnas con valores NA son: \n {penguins.columns[penguins.isna().any()]}\n')


    ######################################################################################
    # EJERCICIO 2
    ###################################################################################### 

    pretty_printing(2)

    # Eliminamos las observaciones NA
    penguins = penguins.dropna()
    # Comprobamos que no hay ninguna columna con algún valor NA
    print(f'Comprobamos que no hay columnas con valores NA: \n {penguins.isna().any()} \n')

    ######################################################################################
    # EJERCICIO 3
    ###################################################################################### 

    pretty_printing(3)

    # Encontramos los individuos por sexo agrupando con la función groupby() y usando la función count()
    print(f"Individuos por sexo: \n {penguins.groupby('sex').sex.count()} \n ")
    # Encontramos la longitud media del pico por sexo agrupando con la función groupby() y usando la función mean()
    print(f"Longitud media del pico según el sexo: \n {penguins.groupby('sex').bill_length_mm.mean()} \n")

    ######################################################################################
    # EJERCICIO 4
    ###################################################################################### 

    pretty_printing(4)

    # Añadimos la columna usando la función insert()
    penguins.insert(loc = penguins.shape[1], 
                    column="bill_area", 
                    value = penguins["bill_length_mm"]*penguins["bill_depth_mm"])
    
    # Imprimimos las primeras observaciones para comprobar que se ha añadido correctamente
    print(f'\n {penguins.head()} \n')

    ######################################################################################
    # EJERCICIO 5
    ###################################################################################### 

    pretty_printing(5)

    # Agrupamos por sexo y especie y tomamos los grupos
    rows_grouped = penguins.groupby(["sex", "species"]).groups
    
    # Guardamos las filas de las observaciones que tengan sexo femenino por cada una de las especies. 
    # Usamos la función concatenate de numpy
    selected_information = np.concatenate((rows_grouped[('female', 'Adelie')].values, rows_grouped[('female', 'Chinstrap')].values, rows_grouped[('female', 'Gentoo')].values))
    
    # Creamos un nuevo dataframe seleccionando solamente las filas encontradas en el paso anterior
    penguins_5 = penguins.loc[selected_information]

    # Comprobamos que efectivamente obtenemos la información referente al sexo femenino
    print(f'Información sexo femenino: \n {penguins_5.head()} \n')

    # Podemos obtener también información estadística con la función describe
    print(f'Información estadística: \n {penguins_5.describe()} \n')
    
    ######################################################################################
    # EJERCICIO 5.1
    ###################################################################################### 

    pretty_printing(5.1)

    # Aprovechamos el dataframe del ejercicio anterior para calcular la longitud 
    # media del pico según la especie.

    print(f"Longitud media del pico femenino según la especie: \n {penguins_5.groupby('species').bill_length_mm.mean()} \n")

    ######################################################################################
    # EJERCICIO 6
    ###################################################################################### 

    pretty_printing(6)

    # Modificamos la fila body_mass_g modificando sus unidades
    penguins.body_mass_g = penguins.body_mass_g/1000
    #Renombramos la fila body_mass_g con la función rename()
    penguins = penguins.rename(columns = {"body_mass_g": "body_mass_kg"})
    # Imprimimos las primeras observaciones para comprobar que el funcionamiento es correcto
    print(f'\n {penguins.head()}')

if __name__ == '__main__':
    main()