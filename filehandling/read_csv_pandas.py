import hashlib
import pandas
import numpy

class ReadCsvPandas:
    def __init__(self, arg1, arg2):
        self.filename = arg1
        self.filelocation = arg2

    def get_pandas_content(self,skiplines,excl_columns,delimiter, add_column, subject_column):
            self.skiplines = skiplines
            self.excl_columns = excl_columns
            self.delimiter = delimiter
            self.add_column = add_column
            self.subject_column = subject_column

            fileloc=self.filelocation+self.filename

            content = pandas.read_csv(fileloc, encoding = "ISO-8859-1",header=None, sep=self.delimiter,
                                      skiprows=range(0,self.skiplines))
            if add_column:
                print('Merging columns requested')
                content[subject_column] = content[add_column] + " - " + content[subject_column]

            content = content.drop(content.columns[self.excl_columns], axis=1)




            return content

    def add_hash_pandas(self, content, length):
        self.content = content
        self.length = length

        # make df row a string
        # read string line by line and hash the line
        x = content.to_string(header=False, index=False, index_names=False).split('\n')

        # write hash into a list
        hash_list = []
        for line in x:
            line_hash = hashlib.md5(line.encode('utf-8')).hexdigest()
            hash_list.append(line_hash)

        # add list as new column
        content.insert(loc=0, column=length, value=hash_list)

        return content

    def ger_to_us(self,content, ger_to_us_col):
        self.content = content
        self.ger_to_us_col = ger_to_us_col

 #       print(self.ger_to_us_col)
        #
        i = 0
        while i < len(content):
            val = content.ix[i,self.ger_to_us_col]
            val =val.replace('.','')
            val = val.replace(',','.')
            content.ix[i, self.ger_to_us_col] = val
#            print(content.ix[i, self.ger_to_us_col])
            i = i + 1
        return content