import Indexing
import pickle

'''
open the vocabulary file and
import the words histogram
'''
with open('bag_of_word.pkl') as w:
    voc = pickle.load(w)

index = Indexer('test.db',voc)
index.create_table()

'''
import the train and test files into the dataset
'''

# import train set
for i in range(len(train)):
    indx.add_to_index(train[i],voc.features[i],'train')

# import test set
for i in range(len(test)):
    indx.add_to_index(test[i],voc_test.features[i],'test')

indx.db_commit()
