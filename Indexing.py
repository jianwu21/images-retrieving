import pickle
from sqlite3 import dbapi2 as sqlite

class Indexer(object):
    def __init__(self,db,voc):
        self.con = sqlite.connect(db)
        self.voc = voc

    def __del__(self):
        self.con.close()

    def db_commit(self):
        self.con.commit()

    def create_table(self):
        self.con.execute('create table imlist(filename,category,tr_or_te)')
        self.con.execute('create table imwords(imid,wordid,word,vocname)')
        self.con.execute('create table imhistograms(imid,histogram,vocname)')
        self.db_commit

    '''Addimg images'''
    def add_to_index(self,imname,des,tr_or_te):
        if self.is_indexed(imname):
            return
        print('indexing',imname)

        '''get the imid'''
        imid = self.get_id(imname,tr_or_te)

        ''' get the words '''
        imwords = self.voc.project(des)
        nbr_words = imwords.shape[0]

        #link each word to the Image
        for i in range(nbr_words):
            word = imwords[i]

            # insert the wordid and word
            if word != 0:
                self.con.execute('insert into imwords(imid,wordid,word,vocname) values(?,?,?,?)',
                                 (imid,i,word,self.voc.name))

        # store word histogram for image
        # use pickle to encode Numpy arrays as strings
        self.con.execute('insert into imhistograms(imid,histogram,vocname) values(?,?,?)',
                         (imid,pickle.dumps(imwords),self.voc.name))

    def is_indexed(self,imname):
        im = self.con.execute(
            "select rowid from imlist where filename= '%s'" %imname).fetchone()

        return im != None

    def get_id(self,imname,tr_or_te):
        '''get an entry id  and add if not present. '''

        cur = self.con.execute(
            "select rowid from imlist where filename = '%s'" %imname)

        res = cur.fetchone()
        if res == None:
            cur = self.con.execute(
                "insert into imlist(filename,category,tr_or_te) values (?,?,?)",
                (imname,imname.split('/')[1],tr_or_te)
            )
            return cur.lastrowid
        else:
            return res[0]
