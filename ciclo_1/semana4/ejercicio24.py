# libreria pandas
import pandas as pd

'''
s = pd.Series([7,5,8])
print(s)
'''

'''
s = pd.Series([7,9,3], index=['Ene','Feb','Mar'])
print(s)
'''

# utilizando diccionarios

d = { 'Ene': 7, 'Feb': 6, 'Mar': 9}

'''
s = pd.Series(d)
print(s)
'''

'''
s = pd.Series(d, index=['Abr','Mar','Feb','Ene'], dtype = int)
print(s)
'''

# utilizando un escalar

s = pd.Series(7,index=['Ene','Feb','Mar'])
print(s) 
