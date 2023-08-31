#! /usr/bin/env python
# -*- coding: utf-8

'''
Name: dating.py(KNN algorithm)
Training and test dataset: dating.txt

Created on Feb 8, 2015

@author: Tao He
'''

__author__ = 'Tao He'

from numpy import array as nmarray
from matplotlib import pyplot as plt

LABEL_MAP = {
    'didntLike': 1,
    'smallDoses': 2,
    'largeDoses': 3,
}

ATTR_MAP = {
    1: 'Number of frequent flyer miles earned per year',
    2: 'Percentage of time spent playing video games',
    3: 'Liters of ice cream consumed per week',
}

def create_dataset(filename=None):
    ''' Return data group and labels.
    Get the data from file.
    If the filename is not specialed, return None.

    dataformat: flyerMiles, gameTime, icecream, label.
    '''

    def normalize_data(data=None):
        ''' Normalized dataset.
        Normalize all data to range 0-1.
        '''
        if data is None:
            return None
        for column in range(data[0].__len__()):
            max_val, min_val = max(data[:, column]), min(data[:, column])
            for row in range(data.__len__()):
                data[row][column] = (data[row][column]-min_val)/(max_val-min_val)
        return data

    if filename == None:
        return (None, None)
    group = []
    labels = []
    with open(filename, mode='r') as fp_data:
        for line in fp_data:
            group.append([float(num) for num in line[:-1].split('\t')[0:3]])
            labels.append(LABEL_MAP[line[:-1].split('\t')[3]])
    return normalize_data(nmarray(group)), labels

def draw_pic(group=None, labels=None, x=0, y=0):
    ''' Draw a subplot from data group.
    '''
    if group is None or labels is None:
        return None
    name = 'knn-dating'
    figure = plt.figure(num=name, dpi=100)
    ax_main = figure.add_subplot(1, 1, 1, xlabel=ATTR_MAP[x+1], ylabel=ATTR_MAP[y+1], title=name)
    ax_main.scatter(group[:, x], group[:, y],
                    s=15*nmarray(labels),
                    c=[[i/LABEL_MAP.__len__()] for i in labels])
    plt.show()
    ## plt.savefig('%s.png'%name, format='png', dpi=100)

def knn_classify(group, labels, attrs, ratio=0.5, item=0, k=3):
    ''' Return the type of item.
    knn classify function.
    '''

    def get_dist(i, j):
        ''' Return the distence of group[i] and group[j].
        '''
        dist = 0.0
        for attr in attrs:
            dist += (group[i][attr]-group[j][attr])*(group[i][attr]-group[j][attr])
        return dist

    length = group.__len__()
    distence = []
    for i in range(int(length*ratio), length):
        distence.append((i, get_dist(item, i)))
    cnt = {}
    distence.sort(key=lambda item: item[1])
    for i in range(k):
        label = labels[distence[i][0]]
        if label in cnt:
            cnt[label] += 1
        else:
            cnt[label] = 1
    return sorted(cnt.items(), key=lambda item: item[1], reverse=True)[0][0]

def knn():
    ''' KNN classify algorithm.
    '''
    data, labels = create_dataset('dating.txt')
    ratio, attr = 0.5, [0, 1, 2]
    cnt, cnt_correct = 0, 0
    length = data.__len__()
    for i in range(0, int(length*ratio)):
        cnt += 1
        knn_type = knn_classify(data, labels, attr, ratio, i, 3)
        # print('case[%d]: real: %d, knn: %d'%(i, labels[i], knn_type))
        if knn_type == labels[i]:
            cnt_correct += 1
    print('total: %d, correct: %d, correct ratio: %f'%(cnt, cnt_correct, cnt_correct/cnt))

if __name__ == '__main__':
    knn()

# vim: set sw=4, ts=4, fileencoding=utf-8


