import Searcher
from  sqlite3 import dbapi2 as sqlite
from get_data_set import train,test
import pickle
from CodeBook_generation import *
import matplotlib.pyplot as plt


with open('bag_of_word.pkl') as w:
    voc = pickle.load(w)


w = Searcher.Searcher('test.db',voc)

test_in_train = random.choice(train,5)
con = sqlite.connect('test.db')
num = 1 
        
plt.figure(figsize=(8,8))
for imname in test_in_train:
    re = w.query(imname)[:6]
        
    list = con.execute(
        "select filename from imlist where rowid in %s" %(tuple(re),)).fetchall()
    
    list_name = [str(i[0]) for i in list]
    list_name.insert(0,imname)

    for i in list_name:
        plt.subplot(5,7,num)
        plt.imshow(cv2.imread(i,cv2.IMREAD_COLOR))
        plt.axis('off')
        num += 1

plt.show()
        
