import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def drewROC(P_Name,N_Name,isDistance,tabThreshold):
    x = []
    y = []
    trueCompareList = []
    falseCompareList = []
    with open(P_Name,"rb") as f:
        scoreList = f.readlines()
        for score in scoreList:
            if score:
                trueCompareList.append(float(score.decode().split(" ")[1]))
    with open(N_Name,"rb") as f:
        scoreList = f.readlines()
        for score in scoreList:
            if score:
                falseCompareList.append(float(score.decode().split(" ")[1]))

    tsLen = len(trueCompareList)
    fsLen = len(falseCompareList)
    
    xy_coordinate = ""
    fristTh = True
    for threshold in range(0,10001):
        threshold = float(threshold/10000)
        ts_count = 0
        fs_count = 0
        if isDistance:
            for ts in trueCompareList:
                if ts >= threshold:
                    ts_count += 1

            for fs in falseCompareList:
                if fs >= threshold:
                    fs_count += 1

            fpr_score = float(fs_count/fsLen)
            tpr_score = float(ts_count/tsLen)

            if fpr_score <= tabThreshold:
                if fristTh:
                    x_label = str(round((100*fpr_score),2)) + '%'
                    y_label = str(round((100*tpr_score),2))  + '%'
                    hit_threshold = threshold        
                elif x[-1] > tabThreshold:
                    if (x[-1] - tabThreshold )\
                        / (tabThreshold - fpr_score)> 10:
                        x_label = str(round((100*fpr_score),2)) + '%'
                        y_label = str(round((100*tpr_score),2))  + '%'  
                    else:
                        x_label = str(round((100*x[-1]),2)) + '%'
                        y_label = str(round((100*y[-1]),2))  + '%'
                    hit_threshold = threshold 
                xy_coordinate = "(" + x_label + "," + y_label + "," + str(hit_threshold) + ")"

        else:
            for ts in trueCompareList:
                if ts <= threshold:
                    ts_count += 1

            for fs in falseCompareList:
                if fs <= threshold:
                    fs_count += 1

            fpr_score = float(fs_count/fsLen)
            tpr_score = float(ts_count/tsLen)

            if fpr_score >= tabThreshold:
                if fristTh:
                    x_label = str(round((100*fpr_score),2)) + '%'
                    y_label = str(round((100*tpr_score),2))  + '%'
                    hit_threshold = threshold                 
                elif x[-1] < tabThreshold:
                    if (tabThreshold - x[-1])\
                        / (fpr_score - tabThreshold)> 10:
                        x_label = str(round((100*fpr_score),2)) + '%'
                        y_label = str(round((100*tpr_score),2))  + '%'
                    else:
                        x_label = str(round((100*x[-1]),2)) + '%'
                        y_label = str(round((100*y[-1]),2))  + '%'
                    hit_threshold = threshold 
                xy_coordinate = "(" + x_label + "," + y_label + "," + str(hit_threshold) + ")"
        
        x.append(fpr_score)
        y.append(tpr_score)
        fristTh = False

    p, = plt.plot(x,y,'-',linewidth=1)

    return p,xy_coordinate


def to_percent(temp, position):
    return str(round((100*temp),3)) + '%'


def getROC(record_path,p_list,coordinate_list):
    for filename in os.listdir(record_path):
        isDistance = False
        if "v3" in filename:
            isDistance = True

        txt_list = os.listdir(record_path + filename)
        P_Name = record_path + filename + "/" + txt_list[1]
        N_Name = record_path + filename + "/" + txt_list[0]

        p,coordinate = drewROC(P_Name,N_Name,isDistance,tabThreshold)
        p_list.append(p)
        coordinate_list.append(filename + ":" + coordinate)

    return p_list,coordinate_list
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
plt.figure()
plt.rcParams['font.family'] = ['Times New Roman']
plt.title("ROC")
plt.xlabel("FPR")
plt.ylabel("TPR")
plt.xlim(0,0.0011) #默认FPR: 0 ~ 1.0%
plt.ylim(0.50,1.0001) #默认TPR: 50.0 ~ 100.0%
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
tabThreshold = 0.001 #默认记录的阈值 0.10%
record_path_pre = "./leagcy/"#之前的ROC测试数据
record_path_now = "./testROC/" #当前ROC测试的数据
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
p_list = []
coordinate_list = []

#绘制之前
# record_path = record_path_pre
# p_list,coordinate_list = getROC(record_path,p_list,coordinate_list)

#绘制当前
tabThreshold = 0.001
record_path = record_path_now
p_list,coordinate_list = getROC(record_path,p_list,coordinate_list)

plt.legend(p_list,coordinate_list,loc = 0,fontsize = "large")
plt.show()