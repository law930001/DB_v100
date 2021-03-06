import os
from os import listdir
from os.path import isfile, join
import json


def from_json():

    root = "/root/Storage/datasets/TBrain/train/"

    for json_file in listdir(root + 'json/'):
        print(json_file)
        with open(root + 'json/' + json_file) as file:
            data = json.load(file)
            with open(root + 'train_gts/' + json_file.replace('.json', '.jpg.txt'), 'w') as gt_file:
                for shapes in data['shapes']:
                    shapes['label'] = 'null' if shapes['label'] == '' else shapes['label']
                    data = ','.join(str(int(x)) + ',' + str(int(y)) for x, y in shapes['points']) + ',' + shapes['label'] + '\n'
                    gt_file.write(data)
        # break

def make_list_txt():

    root = "/root/Storage/datasets/TBrain/train/"

    with open(root + 'train_list.txt', 'w') as file:
        for i in range(1,4566):
            file.write('img_{}.jpg\n'.format(i))

def make_gt_txt():
    root = "/root/Storage/datasets/ICDAR2017/test/test_gts/"
    dirs = listdir(root)
    for file in dirs:
        print(root + file.lstrip('gt_').rstrip('.txt') + '.jpg.txt')
        os.rename(root + file, root + file.lstrip('gt_').rstrip('.txt') + '.jpg.txt')


def rename_result():
    root = "/root/Storage/DB_v100/results/"
    dirs = listdir(root)
    for file in dirs:

        result = 'res_img_' + file.split('_')[2].split('.')[0].zfill(5) + '.txt'

        print(result)
        os.rename(root + file, root + result)

if __name__ == '__main__':
    # from_json()
    make_list_txt()
    # make_gt_txt()
    # rename_result()

    print("finish")
