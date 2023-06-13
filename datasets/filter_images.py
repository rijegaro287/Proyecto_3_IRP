import os
import shutil
import csv


if(os.path.exists('dataset')):
    shutil.rmtree('./dataset')
    
if(os.path.exists('dataset.csv')):
    os.remove('dataset.csv')

os.mkdir('dataset')

label_by_class = {'no_leaf': 0}

images_data = [['file_name', 'label']]

current_label = 1
image_count = 0
for folder in os.scandir('.'):
    if folder.is_dir() and folder.name != 'dataset':
        print(folder.name)
        folder_path = os.path.join('.', folder.name)
        for filename in os.scandir(folder_path):
            
            if(folder.name == 'Background_without_leaves'):
                images_data.append([f'no_leaf_{image_count}.jpg', label_by_class['no_leaf']])
            else:
                plant_type = folder.name.split('___')[0]
                plant_state = 'healthy' if folder.name.split('___')[1] == 'healthy' else 'diseased' 
                
                file_name = f'{plant_type}_{plant_state}'
                if file_name not in label_by_class: 
                    label_by_class[file_name] = current_label
                    current_label += 1
                
                images_data.append([f'{file_name}_{image_count}.jpg', label_by_class[file_name]])
            
            shutil.copyfile(filename.path, os.path.join('dataset', images_data[-1][0]))
            image_count += 1
            
with open('dataset.csv', 'x', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(images_data)

            
print(image_count)
print(label_by_class)
