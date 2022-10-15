import pymongo
import gridfs


class mongoDBManage():

    def __init__(self):
        self.myclient = pymongo.MongoClient("localhost", 27017)
        self.db = self.myclient.mydatabase
        self.fs = gridfs.GridFS(self.db)

    def Create_DB(self, mydb):
        """
        Enter database name as a parameter mydb
        """
        self.mydb = self.myclient[mydb]

        return self.mydb

    def Create_collection(self, collection):

        self.mycol = self.mydb[collection]
        return self.mycol

    def Insert_to_collection(self, dictionary):
        """This
        takes a dictionary as input to insert into column"""

        self.x = self.mycol.insert_one(dictionary)
        return self.x

    def Find_colum(self):
        self.xy = self.mycol.find()
        for x in self.xy:
            print(x)

    def Query(self, myquery):
        """myquery asks for a dictionary"""
        self.mydoc = self.mycol.find(myquery)
        return self.mydoc

    def Sort(self):
        self.mydoc = self.mycol.find().sort("name")
        for x in self.mydoc:
            print(x)

    def Delete_query(self, todelete):
        """
        todelete: recieves a key-value dictoinary to be deleted
        """
        self.todelet = self.mycol.delete_one(todelete)

        return self.todelet

    def Put_File(self, ar=None, name=None):
        self.a = self.fs.put(ar, filename=name)
        return self.a

    def Get_file(self):
        print(self.fs.get(self.a).read())

    def DeletAll(self):
        self.xy = self.mycol.find()
        for x in self.xy:
            self.mycol.delete_many(x)


mydict = {"name": "John", "address": "Highway 37"}

check = mongoDBManage()
check.Create_DB('Mydatabase')
check.Create_collection('Customers')
# check.Insert_to_collection(mydict)
check.Put_File(b"", "beeebee")
