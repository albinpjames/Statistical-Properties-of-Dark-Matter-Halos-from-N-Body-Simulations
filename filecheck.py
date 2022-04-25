import numpy as np
import math

from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
'''Redshifts to be computed'''
redshifts = ["5.000","3.000","0.250","0.200","0.100"]
#redshifts = ["5.000"]
'''Prameters from the simulation'''
type, cosmo, intcont, sf, ef = 'base', 'c000', 'ph000', 0, 33
#type, cosmo, intcont, sf, ef = 'small', 'c000', 'ph3000', 0, 0

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def onebyone(clm1, redshift):
   print("Status: Reading the files")
   
   global halo_mass
   data = []
   for i in range(sf,ef+1): 
    
      print("Procesing file", i)
      try:
        if i < 10:
            file = str('AbacusSummit Public Data Access/AbacusSummit_' + type + '_' + cosmo +'_' + intcont + '/halos/z' + redshift + '/halo_info/halo_info_00' + str(i) + '.asdf')
        else:   
            file = str('AbacusSummit Public Data Access/AbacusSummit_' + type + '_' + cosmo +'_' + intcont + '/halos/z' + redshift +  '/halo_info/halo_info_0' + str(i) + '.asdf')
        cat = CompaSOHaloCatalog(file, cleaned=False)
        num_halos = len(cat.halos)
        num = np.array(cat.halos['N'])
        print(len(num))
        for i in range (num_halos):
            data.append(num[i])
        del cat
      except Exception as e:
         print(e)
    
   return data

for j, redshift in enumerate(redshifts):
   print(redshift)
   N = onebyone('N', redshift)
   del N