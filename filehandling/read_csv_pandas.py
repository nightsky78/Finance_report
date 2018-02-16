import os
import pandas

class read_csv_pandas:
    def __init__(self, arg1, arg2):
        self.filename = arg2
        self.filelocation = arg1

    def get_pandas_content(self):
                fileloc=self.filelocation+self.filename
                print(fileloc)
                content = pandas.read_csv(fileloc, encoding = "ISO-8859-1")

                select(content, )