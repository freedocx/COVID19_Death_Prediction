def autolabelint(ax,rects,fsize,col):
    for rect in rects:
        ax.text(rect.get_x() + rect.get_width()/2 , rect.get_height(),'%d' % int(rect.get_height()),ha='center', va='bottom', fontweight='bold', color=col, fontsize= ((fsize[1]+fsize[0])/2) + 3)
def autolabelfloat(ax,rects,fsize,col):
    for rect in rects:
        ax.text(rect.get_x() + rect.get_width()/2,rect.get_height() ,'%s' % str(round(rect.get_height(),2)),ha='center',va='bottom',fontweight='bold', color=col,fontsize=((fsize[1]+fsize[0])/2) + 3)
def autolabelpercent(ax,rects,fsize,col):
    for rect in rects:
        ax.text(rect.get_x() + rect.get_width()/2,rect.get_height(),'%s' % ('%' + str(round(rect.get_height(),2))), ha='center', va='bottom',fontweight='bold',color=col,fontsize=((fsize[1]+fsize[0])/2) + 3)