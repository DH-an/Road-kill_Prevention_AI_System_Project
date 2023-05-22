import glob
import os
import cv2

classes = {'inermis':1,'scrofa':2,'procyonoides':3,
                   'sibiricus':4,'vulgaris':5, 'pygargus':6,'sibirica':7,
                   'coreanus':8}

new_class = {}
for k, v in classes.items():
    new_class[v] = k


image_path_list = glob.glob(os.path.join("./test/dram/data/train","*.png"))
txt_path_list = glob.glob(os.path.join("./test/dram/label/train","*.txt"))
count = 0
for i in image_path_list:
    image = cv2.imread(i)
    #cv2.imshow('test',image)
    a = i.split('\\',1)[1]
    txtname = a.split('.',1)[0]+'.txt'
    print(txtname)

    with open("./test/dram/label/train/{}".format(txtname), "r") as f:
        txtfile = f.readlines()

    for bbox_info in txtfile:
        print(bbox_info.split())
        bbox = bbox_info.split()
        x1 = int(float(bbox[1]))
        y1 = int(float(bbox[2]))
        x2 = int(float(bbox[3]))
        y2 = int(float(bbox[4]))
        label_number = int(bbox[0])
        cv2.rectangle(image,(x1, y1),(x2, y2),(255, 255, 255), 2)
        cv2.putText(image,'{}'.format(new_class[label_number]), (x1,y2), cv2.FONT_HERSHEY_COMPLEX, 5,(255,255,255), 3)
    cv2.imshow("{}".format(a),image)
    cv2.moveWindow("{}".format(a), 0, 0)
    cv2.waitKey()
    cv2.destroyAllWindows()
    if cv2.waitKey() == ord('q'):
        exit()
