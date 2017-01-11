import Indexing
import pickle
from get_data_set import train,test
import CodeBook_generation

'''
open the vocabulary file and
import the words histogram
'''
with open('bag_of_word.pkl','rb') as w:
    voc = pickle.load(w)

indx = Indexing.Indexer('test.db',voc)
indx.create_table()

'''
import the train and test files into the dataset
'''
# import train set
for i in range(len(train)):
    indx.add_to_index(train[i],voc.features[i],'train')

# import test set
indx.db_commit()
