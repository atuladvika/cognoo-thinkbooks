# Draw the Exercise 1.7 grids (Q 1 and Q 2) into assets/ch1/. Run from igcse-addmath: python3 _class/figs_ch1_ex7.py
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from matplotlib import font_manager as fm
fm.fontManager.addfont('fonts/Poppins-Regular.ttf'); fm.fontManager.addfont('fonts/Poppins-Italic.ttf')
plt.rcParams['font.family']='Poppins'
NAVY='#1e436d'; BB=dict(facecolor='white',edgecolor='none',pad=.6)
def grid(name, xs, ys, lab, lx, ly):
    fig,ax=plt.subplots(figsize=(3.2,3.2),dpi=400)
    ax.set_xlim(-6.6,6.9); ax.set_ylim(-6.6,6.9); ax.set_aspect('equal'); ax.axis('off')
    for v in range(-6,7):
        ax.plot([v,v],[-6,6],color='#cfdbe0',lw=.5,zorder=0); ax.plot([-6,6],[v,v],color='#cfdbe0',lw=.5,zorder=0)
    ax.annotate('',xy=(6.8,0),xytext=(-6.3,0),arrowprops=dict(arrowstyle='-|>',color=NAVY,lw=.9,mutation_scale=8))
    ax.annotate('',xy=(0,6.8),xytext=(0,-6.3),arrowprops=dict(arrowstyle='-|>',color=NAVY,lw=.9,mutation_scale=8))
    ax.plot(xs,ys,color='#007ea2',lw=1.6,solid_capstyle='round',zorder=3)
    for v in (-6,-4,-2,2,4,6):
        ax.plot([v,v],[-.15,.15],color=NAVY,lw=.8); ax.plot([-.15,.15],[v,v],color=NAVY,lw=.8)
        ax.text(v,-.45,str(v).replace('-','−'),ha='center',va='top',fontsize=6.5,color=NAVY,zorder=2)
        ax.text(-.3,v,str(v).replace('-','−'),ha='right',va='center',fontsize=6.5,color=NAVY,zorder=2)
    ax.text(-.25,-.3,'O',ha='right',va='top',fontsize=6.5,style='italic',color=NAVY)
    ax.text(6.85,-.3,'x',ha='center',va='top',fontsize=7,style='italic',color=NAVY)
    ax.text(.3,6.8,'y',ha='left',va='center',fontsize=7,style='italic',color=NAVY)
    ax.text(lx,ly,lab,fontsize=7.5,color='#007ea2')
    fig.savefig(f'assets/ch1/{name}.png',bbox_inches='tight',pad_inches=0.02,facecolor='white'); plt.close(fig)
x=np.linspace(-5,5,50); grid('ex7_q1',x,0.5*x-0.5,'f',5.15,2.05)
x=np.linspace(-4,5,400); grid('ex7_q2',x,np.sqrt(x+4),'g',5.15,3.0)
