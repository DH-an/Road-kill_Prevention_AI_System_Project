import json
import osg
import os

file_path = "./test.json"

dir_path = "C:\\Users\\user\\Desktop\\gony\\2.Validation\\label\\VL_04.다람쥐"

classes = {'inermis':1,'scrofa':2,'procyonoides':3,
                   'sibiricus':4,'vulgaris':5, 'pygargus':6,'sibirica':7,
                   'coreanus':8}

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            #print(file_path)

            with open(file_path, "r", encoding='UTF-8') as json_file:
                json_data = json.load(json_file)

                #print(json_data)
                #print(json_data["images"])
                print(json_data["annotations"])
                a = json_data["images"][0]
                print(a)

                #for i in a:
                name = a['file_name']
                #print(name.split('.',1)[0])
                #txtname = name.split('.',1)[0]+'.txt'
                split = name.split('.')
                txt_name = split[0] + '.' + split[1] + '.txt'
                height = a['height']
                width = a['width']

                x_scale = float(640) / float(a['width'])
                y_scale = float(640) / float(a['height'])

                for j in json_data['annotations']:
                    print(j['bbox'][0][0])
                    print(j['category_name'])
                    obc = j['category_name']
                    label = classes[obc]
                    
                    x1 = j['bbox'][0][0]
                    y1 = j['bbox'][0][1]
                    x2 = j['bbox'][1][0]
                    y2 = j['bbox'][1][1]
                    
                    yolox = round(((x1 + x2) / 2) * x_scale, 6)
                    yoloy = round(((y1 + y2) / 2) * y_scale, 6)
                    yolow = round((x2 - x1) * x_scale, 6)
                    yoloh = round((y2 - y1) * y_scale, 6)
                    
                    os.makedirs(f"./daram_resized/labels", exist_ok=True)

                    with open(f"./daram_resized/labels/{txt_name}", "a", encoding='UTF-8') as f:
                        f.write(f"{label} {yolox} {yoloy} {yolow} {yoloh} \n")




