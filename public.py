# 一些公有的数值与函数
dx=15
border=600
px=30

maxlife=600
cent=150
edge=140
# 格点坐标转化为画布坐标
def posToMap(pos):
    x=15+30*pos[0]
    y=15+30*pos[1]
    return (x,y)
#画布坐标转化为格点坐标
def mapToPos(map_xy):
    px=(map_xy[0]-15)//30
    py=(map_xy[1]-15)//30
    return (px,py)

def inBox(map_xy):
    barriers=[]
    for c in range(1,18,4):
        for r in range(1,18,4):
            barriers.append((c,r))
    if map_xy[0]>=15 and map_xy[0]<=555 and \
        map_xy[1]>=15 and map_xy[1]<=555 and \
            mapToPos(map_xy) not in barriers:
        return True
    else :
        return False