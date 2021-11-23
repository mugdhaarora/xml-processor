import os.path
import unittest
import pandas as pd
import sys
sys.path.append('../util')
import file_reader
import xml_parser_common
import xml.etree.ElementTree as et 


dirname = os.path.dirname(__file__)

def countFiles():
    path = dirname + 'data'
    file_type =  "**/*.xml"
    return file_reader.readFiles(path, file_type)

def validateRowCount():
    path = dirname + 'data'
    file_type =  "**/*.xml"
    df_error_cols = ["type", "process", "severity", "code","description","timestamp"]
    tree = et.parse(file_reader.readFiles(path, file_type)[0])
    root = tree.getroot()    
    df =  xml_parser_common.XML_parser(root, df_error_cols)
    return df[df.columns[0]].count()



class SimpleTest(unittest.TestCase):
   def test1(self):
      self.assertEqual(countFiles(), ['data\\002.xml', 'data\\003.xml'])

   def test2(self):
      self.assertEquals(validateRowCount(),2)
      
if __name__ == '__main__':
   unittest.main()

