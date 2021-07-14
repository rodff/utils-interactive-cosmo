'''
Interactive code to iteratively compute redshift or lookback time.

Remember to change the cosmology if you don't want to use Planck15 results.
'''

from time import sleep
from astropy.cosmology import Planck15, z_at_value
import astropy.units as u

quit = False 

print('\n')
print('\t (Using Planck15 cosmology) \n')

while(quit==False):

    print('---------------------------------------------------------------')
    print('Choose the input quantity and press Enter:')
    print('Redshift [z] \t Lookback time [t] \t Quit [q]')

    res = input()

    if(res=='z'):
        print('Type the redshift:')
        z = float(input())
        t = Planck15.lookback_time(z)
        print('Lookback Time: ',t.value)
        print('--------------------------------------------------------------- \n')
        sleep(1)

    elif(res=='t'):
        print('Type the lookback time:')
        t = float(input())
        z = z_at_value(Planck15.lookback_time, t * u.Gyr)
        print('Redshift: ',z)
        print('--------------------------------------------------------------- \n')
        sleep(1)

    elif(res=='q'):
        quit = True
        print('Bye!\n')

    else:
        print("The appropriate keys are 'z', 't' or 'q'.\n\n")
