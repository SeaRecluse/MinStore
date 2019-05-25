import matplotlib.pyplot as plt
 
def compute_iou(rec1, rec2):
    S_rec1 = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
    S_rec2 = (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])
 
    sum_area = S_rec1 + S_rec2
 
    left_line = max(rec1[1], rec2[1])
    right_line = min(rec1[3], rec2[3])
    top_line = max(rec1[0], rec2[0])
    bottom_line = min(rec1[2], rec2[2])
    
    if left_line >= right_line or top_line >= bottom_line:
        return 0
    else:
        w = right_line - left_line
        h = bottom_line - top_line
        r = plt.Rectangle((left_line,top_line),\
            w,\
            h,\
            linewidth=1,edgecolor='b',fill=True)
        ax.add_patch(r)

        intersect = w * h
        return float(intersect / (sum_area - intersect))
 
def test_iou(rect1,rect2):
    
    iou = compute_iou(rect1, rect2)
    return iou
    

fig = plt.figure()
ax = fig.add_subplot(111)
plt.rcParams['font.family'] = ['Times New Roman']
plt.xlabel("Pixel X")
plt.ylabel("Pixel Y")

if __name__ == "__main__":

    # (top, left, bottom, right)
    rect1 = [661, 27, 679, 47]
    rect2 = [662, 27, 682, 47]


    plt.xlim(min(rect1[1],rect1[3],rect2[1],rect2[3]) - 1,\
            max(rect1[1],rect1[3],rect2[1],rect2[3]) + 1)

    plt.ylim(min(rect1[0],rect1[2],rect2[0],rect2[2]) - 1,\
            max(rect1[0],rect1[2],rect2[0],rect2[2]) + 1)

    r = plt.Rectangle((rect1[1],rect1[0]),\
        rect1[3] - rect1[1],\
        rect1[2] - rect1[0],\
        linewidth=2,edgecolor='r',fill=False)
    ax.add_patch(r)

    r = plt.Rectangle((rect2[1],rect2[0]),\
        rect2[3] - rect2[1],\
        rect2[2] - rect2[0],\
        linewidth=2,edgecolor='g',fill=False)
    ax.add_patch(r)

    iou = test_iou(rect1,rect2)
    plt.title("IOU : " + str(iou))
    plt.show()