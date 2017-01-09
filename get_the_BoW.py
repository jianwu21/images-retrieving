import CodeBook_generation
import pickle
import os

'''get the train set and the test set'''
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

''' you know the pathes in train and test will be use for this experiment '''
voc_train = CodeBook_generation.Vocabulary('train')
voc_train.get_descriptors(train)
voc_train.train(400)

''' store the codebook as pkl file'''
with open('bag_of_word.pkl','wb') as f:
    pickle(voc_train,f)
    print 'vocabulary is:',voc_train.name,voc_train.nbr_words
