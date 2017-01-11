import CodeBook_generation
import pickle
import os
from get_data_set import train,test


''' you know the pathes in train and test will be use for this experiment '''
voc_train = CodeBook_generation.Vocabulary('train')
voc_train.get_descriptors(train)
voc_train.train(400)

''' store the codebook as pkl file'''
with open('bag_of_word.pkl','wb') as f:
    pickle.dump(voc_train,f)
    print 'vocabulary is:',voc_train.name,voc_train.nbr_words
