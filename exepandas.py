import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

data = {'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
        'Idade': [25, 32, 30, 28, 45],
        'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Dentista']}
df1 = pd.DataFrame(data)

df1['Salario']= pd.Series([2000.00,1000.00, 2450.00, 1500.00], index=[0,1,3,4])



print(df1)