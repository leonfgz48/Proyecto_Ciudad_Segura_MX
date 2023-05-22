"""Limpieza de datos

Script creado con la finalidad de contener funciones relacionadas con la 
limpieza de una base de datos. 

Este script se puede importar como módulo y contiene la siguiente función:
    
    *completitud - Regresa una tabla con el porcentaje de datos sin NA por variable
    *remove_stopwords - Elimina las stop words de un caracter. Regresa un string.
    
"""

#Importar liberias
import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('spanish'))

def completitud(df):
    comple=pd.DataFrame(df.isnull().sum())
    comple.reset_index(inplace=True)
    comple=comple.rename(columns={"index":"columna",0:"total"})
    comple["completitud"]=(1-comple["total"]/df.shape[0])*100
    comple=comple.sort_values(by="completitud",ascending=True)
    comple.reset_index(drop=True,inplace=True)
    return comple



def remove_stopwords(text):
    words = text.split()
    clean_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(clean_words)