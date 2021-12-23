#Sources
#https://www.icex.es/icex/es/navegacion-principal/todos-nuestros-servicios/informacion-de-mercados/paises/navegacion-principal/el-pais/relaciones-bilaterales/index.html?idPais=US
#https://datacomex.comercio.es/Data/Index

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('imports_exports_dataset.csv').sort_values('year')

''' Data processing '''
#distribution exports/imports Spain-USA
df_e=df[(df['region']=='USA')&(df['Export/Import']=='E')][['year','euros']]
df_i=df[(df['region']=='USA')&(df['Export/Import']=='I')][['year','euros']]
#USA-Spain trade volume
df_trade_volume=df.pivot_table(values='euros',index='year',columns='region',aggfunc=[np.sum])
size_norm=3e+7
size=df_trade_volume.iloc[:,0]/size_norm
#years
years=df['year'].drop_duplicates().reset_index().iloc[:,1]
xpos=years
#ratio World-Spain trade volume to USA-Spain trade volume
ypos=df_trade_volume.iloc[:,0]/df_trade_volume.iloc[:,1]

    
''' Plot '''   
def draw_pie(dist, 
             xpos, 
             ypos, 
             size, 
             color_pie,
             label,
             ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10,8))

    # for incremental pie slices
    cumsum = np.cumsum(dist)
    cumsum = cumsum/ cumsum[-1]
    pie = [0] + cumsum.tolist()

    for r1, r2,c,lbl in zip(pie[:-1], pie[1:],color_pie,label):
        angles = np.linspace(2 * np.pi * r1, 2 * np.pi * r2)
        x = [0] + np.cos(angles).tolist()
        y = [0] + np.sin(angles).tolist()

        xy = np.column_stack([x, y])
        ax.scatter([xpos], [ypos], marker=xy, s=size,facecolor=c,label=lbl)
    return ax

fig, ax = plt.subplots(figsize=(16,8)) 
for i,y in years.items():
    dist_i=[df_e.iloc[i,1],df_i.iloc[i,1]]
    xpos_i=xpos.iloc[i]
    ypos_i=ypos.iloc[i]
    size_i=size.iloc[i]
    color_pie=['blue','red']
    if y!=2020:
        label=['_nolegend_','_nolegend_']
    else:
        label=['Exports','Imports']
    draw_pie(dist_i,xpos_i,ypos_i,size_i,color_pie, label,ax=ax)

#embellishment
plt.ylim(0.03, 0.06)
plt.yticks(ticks=[0.03,0.045,0.06])
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.suptitle('    Evolution of Spain foreign trade',fontsize=24,fontweight='bold')
plt.title('Imports and exports from and to US',fontsize=20,fontweight='normal')
plt.ylabel('% Total foreign trade in Spain\n',fontsize=16,color='black')
ax.legend(loc='upper center', 
          bbox_transform=fig.transFigure, 
          ncol=2,
          bbox_to_anchor=(0.5, 0.07),
          edgecolor='w')

vals = ax.get_yticks()
ax.set_yticklabels(['{:,.1%}'.format(x) for x in vals])
font_size=16
plt.rc('xtick', labelsize=font_size) 
plt.rc('ytick', labelsize=font_size) 
plt.rc('legend', fontsize=font_size)


