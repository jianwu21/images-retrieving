import pickle
from sqlite3 import dbapi2 as sqlite
from get_data_set import train,test
from numpy import *

class Searcher(object):
    def __init__(self,db,voc):

        self.con = sqlite.connect(db)
        self.voc = voc

    def __del__(self):

        self.con.close()

    def candidates_from_imword(self,imword):

        # get a list of images containing imword
        im_ids = self.con.execute(
            "select distinct imid from imwords where wordid = %d" %imword
        ).fetchall()

        return [i[0] for i in im_ids if i[0] in range(len(train)+1)]

    def candidates_from_imhistogram(self,imwords):
        # get a list of images with similar words

        # get the word id
        words = imwords.nonzero()[0]

        # find the candidates
        candidates = []

        for word in words:
            c = self.candidates_from_imword(word)
            candidates += c

        tmp = [(w,candidates.count(w)) for w in set(candidates)]

        # sorting this candidates
        sorted_tmp = sorted(tmp,key=lambda d:d[1])
        sorted_tmp.reverse()

        # return sorted list and find the best matches
        return [w[0] for w in sorted_tmp]

    def get_imhistograms(self,imname):
        # return the histograms for the images

        im_id = self.con.execute(
            "select rowid from imlist where filename = '%s'" %imname).fetchone()

        s = self.con.execute(
            "select histogram from imhistograms where rowid = %d" %im_id).fetchone()

        return pickle.loads(str(s[0]))

    def query(self,imname):
        # find the best matching results

        h = self.get_imhistograms(imname)
        candidates = self.candidates_from_imhistogram(h)

        matches_score = []
        for candidate in candidates:
            cand_name = self.con.execute(
                "select filename from imlist where rowid = %d" %candidate).fetchone()

            cand_hist = self.get_imhistograms(cand_name)
            cand_dist = sqrt(sum((h-cand_hist)**2))
            matches_score.append((cand_dist,candidate))

        return [num[1] for num in sorted(matches_score)]
