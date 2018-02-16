import os
import hashlib

class File:
        def __init__(self, arg1, arg2):
                self.filename = arg1
                self.filelocation = arg2
		
        def get_cleaned_content(self):
                
#	        """open file and read lines"""
                os.chdir(self.filelocation)
#                print(os.getcwd())
                f = open(self.filename,'rb')
                filecontent = f.readlines()
#		
#                """Removing line breaks and spaces"""
                filecontent = [str(line).rstrip('\\n\'') for line in filecontent]
                filecontent = [str(line).lstrip('b\'') for line in filecontent]
#               
#                filecontent = ' '.join(filecontent).split() 
#                for line in filecontent:
#                    print(line)
                new_filecontent = []

                return filecontent
	
        def get_structured_content(self,old_content, delimiter, 
                                   no_column, excl_column, exclusions, ger_to_us_co):
                self.old_content = old_content
                self.delimiter = delimiter
                self.no_column = no_column
                self.excl_column = excl_column
                self.exclusions = exclusions
                self.ger_to_us_co = ger_to_us_co
                
                print("Start structuring")
		 
                new_content = []
                for line in old_content:
                        if self.exclusions not in line:
                                temp_line = str(line).split(self.delimiter)
                                if len(temp_line) == self.no_column:
                                        temp_line[self.ger_to_us_co] = temp_line[self.ger_to_us_co].replace('.','')
                                        temp_line[self.ger_to_us_co] = temp_line[self.ger_to_us_co].replace(',','.')
                                                
                                        i = 0
                                        for col in self.excl_column:
                                                t = col - i
                                                del temp_line[t]
                                                i = i + 1
                                               
                                        new_line = ';'.join(map(str, temp_line))
                                        new_line = new_line.replace('"','')
                                        new_line = new_line.encode("ascii", errors="ignore").decode()        
                                        new_content.append(new_line)
                print("Finish structuring")
                return new_content

        def add_hash(self,old_content):
                self.old_content = old_content
                new_content = []

                for line in old_content:
                        line_hash = hashlib.md5(line.encode('utf-8')).hexdigest()
                        new_line = line_hash + ";" + line
                        new_content.append(new_line)

                return new_content
