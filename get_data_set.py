import os

'''
90%  as the train set
'''
train = []
test = []

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def get_dirlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if not f.endswith('.DS_Store')]

for files in get_dirlist('data/'):
    train_num = int(round(0.8 *  len(get_imlist(files))))
    train += get_imlist(files)[:train_num]
    test += get_imlist(files)[train_num:]


