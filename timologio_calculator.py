# timologio_calculator.py
# Created by: Dimitrios Ioannidis
# Created on: 04.06.2014
# Updated on: -
# Copyright:  2014

'''
This scrpt calculates the values that must be filled in a 'TIMOLOGIO PAROXHS YPHRESIWN'.
The amount of money that is being paid is needed.

'''

print 'The script has started...\n'

def TC(bank_amount, FPA_value = 0.23):
    b = bank_amount
    a = (100./80) * b
    par = 0.2 * a
    fpa = FPA_value * a
    t = a + fpa
    p = b + fpa
    return a, par, fpa, t, p

bank_v = eval(raw_input('Amount of money: '))

if bank_v > 0:
    aksia, parakrathsh, poso_fpa, oliko, pliroteo = TC(bank_v)

    print '\nFor an amount of %.3f: \n\nPOSO PARAKRATHSHS: %.3f\n\nAKSIA: %.3f\n\nPOSO FPA: %.3f\n\nOLIKO: %.3f\n\nPLHRWTEO: %.3f\n\n' %(bank_v, parakrathsh,\
    aksia, poso_fpa, oliko, pliroteo)

    print 65* '-' + '\n\tEND OF PROCESSING - THE SCRIPT HAS RUN SUCCESSFULLY\n' + 65*'-'
else:
    print 'ATTENTION: Give a valid amount!!!'




