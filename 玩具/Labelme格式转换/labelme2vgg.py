import json
import glob
import os

transformerPath = "./vggJson/"
pic_path = "./picFile/"
pic_list = os.listdir(pic_path)
filelist = glob.glob("./labelmeJson/*.json")
filelist.sort()

def get_x(shape, index):
    shape = shape[index]
    points = shape["points"]
    x_list = []
    for i in range(len(points)):
        x_list.append(points[i][0])
    return x_list

def get_y(shape, index):
    shape = shape[index]
    points = shape["points"]
    y_list = []
    for i in range(len(points)):
        y_list.append(points[i][1])
    return y_list

def resolveJson(pathSource,picPath):
    via_annotator = []

    file = open(pathSource, "rb")
    fileJson = json.load(file)
    flag = fileJson["flags"]
    shape = fileJson["shapes"]
    LineColor = fileJson["lineColor"]
    FileColor = fileJson["fillColor"]
    ImagePath = os.path.splitext(picPath)[0] + ".jpg"
    ImageData = fileJson["imageData"]
    size = os.path.getsize(pic_path + ImagePath)
    
    vgg_annotator = {}
    vgg_annotator["fileref"] = ""
    vgg_annotator["size"] = size
    vgg_annotator["filename"] = ImagePath
    vgg_annotator["base64_img_data"]=""
    vgg_annotator["file_attributes"]={}
    regionObject = {}

    for i in range(len(shape)):
        indexRegion = {}
        indexRegion["region_attributes"] = {}
        indexRegion["region_attributes"]["name"] = shape[i]["label"]
        shape_attribute = {}
        shape_attribute["all_points_x"] = get_x(shape,i)
        shape_attribute["all_points_y"] = get_y(shape,i)
 
        shape_attribute["name"] = shape[i]["label"]
        indexRegion["shape_attributes"] = shape_attribute
        regionObject[str(i)]=indexRegion

    vgg_annotator["regions"] = regionObject
    via_annotator.append(vgg_annotator)

    return via_annotator

for i in range(len(filelist)):
    res = resolveJson(filelist[i],pic_list[i])
    json_str = json.dumps(res)
    
    print(os.path.splitext(pic_list[i])[0] + ".json")

    with open(transformerPath + os.path.splitext(pic_list[i])[0] + ".json", 'w') as json_file:
        json_file.write(json_str)