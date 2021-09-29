import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--dset', type=str, default='VH_channel/samples_list_2018.txt')
args = parser.parse_args()


with open(args.dset,'r') as datasets:
    ds_ = datasets.readlines()

for d_ in ds_:
    d_ = d_.strip('\r\n')
    filename = d_.replace('/','_')[1:]
    filename = 'VH_channel/{}.txt'.format(filename)
    os.system('dasgoclient --query "file dataset={}" > {}'.format(d_, filename))
