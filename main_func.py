import pandas as pd
import os
import xml.etree.ElementTree as et 
import util.xml_parser_common as xparser
import util.df_file_writer as file_writer
import util.file_reader as file_reader

file_name = "result/xmlparser.xlsx"
file_type =  "**/*.xml"
df_error_cols = ["type", "process", "severity", "code","description","timestamp"]
df_rules_cols = ["guid","ID","Description","Timestamp","Severity","Override","AllowOverride"]
df_messages_cols=["Timestamp","Source","Number","Description"]

def main():
    # specifying the file path
    dirname = os.path.dirname(__file__)
    path = dirname + 'data/'
    all_files = file_reader.readFiles(path, file_type)

    #define the Result Dataframe and columns for Dataframe
    result_err_df=pd.DataFrame(columns=df_error_cols)
    result_rules_df=pd.DataFrame(columns=df_rules_cols)
    result_msg_df=pd.DataFrame(columns=df_messages_cols)

    #runnning for all xml files in the data folder
    for f in all_files:
        tree = et.parse(f)
        root = tree.getroot()
    
        if root.find('Nuula').find('Errors') != None:
                r_error=root.find('Nuula').find('Errors')
                result_err_df=result_err_df.append(xparser.XML_parser(r_error, df_error_cols))    
        else:  
                print('No Error Table in',f) 
                
        if root.find('DataExtract900jer').find('Rules') != None:
                r_rules=root.find('DataExtract900jer').find('Rules')
                result_rules_df=result_rules_df.append(xparser.XML_parser(r_rules, df_rules_cols))
        else:
                print('No Rules Table in',f)

        if root.find('DataExtract900jer').find('Messages') != None:
                r_messages=root.find('DataExtract900jer').find('Messages')    
                result_msg_df=result_msg_df.append(xparser.XML_parser(r_messages, df_messages_cols))
        else:
                print('No Messages Table in',f)

    file_writer.writeToFile(result_err_df, result_msg_df, result_rules_df, file_name)    

if __name__ == "__main__":
    main()






    





