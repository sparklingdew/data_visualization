import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1.inset_locator import inset_axes 

'''Dataset'''
# column 1: load in N
# column 2: time in s
# all other columns: strain in microstrains. Column names are sensor location in mm.
df=pd.read_csv('mechanical_test_dataset.csv')
load=df['load']
strain=df.iloc[:,2:]
time_points=np.arange(0,load.size)
tmax=df['seconds'].iloc[-1]
# dmax: distance to last sensor 
dmax=float(df.columns[-1])

'''Plot'''
fig, (ax1, ax2) = plt.subplots(2,sharex=True, 
                                figsize=[7, 5],
                               gridspec_kw={'height_ratios':[1,3]})
fig.suptitle('Strain profile during loading-unloading',fontsize=12, fontweight='bold')

ax1.plot(time_points,load)
ax1.set( ylabel='load (kN)')
ax1.set_ylim([-50,100])
ax1.xaxis.set_ticks_position('none') 
ax1.tick_params(axis='y', which='major', labelsize=8)   
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.spines["bottom"].set_visible(False)
    
im=ax2.imshow(strain.T, cmap='rainbow',vmin=-2500,vmax=2500,
              aspect='auto',interpolation=None)
ax2.set(xlabel='time (s)',ylabel='sensor location (mm)')
ax2.set_xticks(np.arange(0,df.shape[0]*1.01, 
                         step=df.shape[0]/4))
ax2.set_xticklabels(np.arange(0,round(tmax*1.01),step=round(tmax/4)))
ax2.set_yticks(np.arange(0,df.shape[1]*1.01, 
                         step=df.shape[1]/4))
ax2.set_yticklabels(np.arange(0,dmax*1.01,
                              step=round(dmax/4,2)).astype('f2'))
ax2.tick_params(axis='both', which='major', labelsize=8) 
axins = inset_axes(ax2, # here using axis of the lowest plot
               width="2%",  # width = 2% of parent_bbox width
               height="100%",  # height 
               loc='lower left',
               bbox_to_anchor=(1.02, 0.0, 1, 1),
               bbox_transform=ax2.transAxes,
               borderpad=0,
               )
cbar=fig.colorbar(im, cax=axins)
cbar.set_label('strain (\u03BCstrain)')
plt.savefig('strain_profile_vs_time.png',bbox_inches='tight',dpi=500)



