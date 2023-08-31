#! /usr/bin/env python
# -*- coding: utf-8

'''
Name: handwriting.py (KNN classify algorithm)
Training and test dataset: handwriting.zip

Created on Feb 8, 2015

@author: Tao He
'''

__author__ = 'Tao He'

from os import listdir
from os.path import sep as SYS_SEPARATOR

def create_dataset(dirname=None):
    ''' Return all handwriting digits files under dir dirname.
    '''
    if dirname == None:
        return (None, None)
    files = listdir(dirname)
    group = []
    labels = []
    for file in files:
        labels.append(int(file[0]))
        mat = []
        with open(dirname+SYS_SEPARATOR+file, mode='r') as fp_data:
            for line in fp_data:
                mat.append([int(num) for num in line[:-1]])
        group.append(mat)
    return group, labels

def knn_classify(sample, labels, case, k=3):
    ''' Return the type of item.
    knn classify function.
    '''
    def get_dist(u, v):
        ''' Return the distence of group[i] and group[j].
        '''
        row = u.__len__()
        column = u[0].__len__()
        dist = 0
        for r in range(row):
            for c in range(column):
                dist += abs(u[r][c]-v[r][c])
        return dist

    length = sample.__len__()
    distence = []
    for i in range(length):
        distence.append((i, get_dist(case, sample[i])))
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
    ''' KNN algorithm.
    '''
    sample, sample_labels = create_dataset('trainingDigits')
    cases, cases_labels = create_dataset('testDigits')
    cnt, cnt_correct = 0, 0
    for case in cases:
        knn_type = knn_classify(sample, sample_labels, case, 3)
        print('case[%d]: real: %d, knn: %d'%(cnt, cases_labels[cnt], knn_type))
        if knn_type == cases_labels[cnt]:
            cnt_correct += 1
        cnt += 1
    print('total: %d, correct: %d, correct ratio: %f'%(cnt, cnt_correct, cnt_correct/cnt))

if __name__ == '__main__':
    knn()

# vim: set sw=4, ts=4, fileencoding=utf-8


