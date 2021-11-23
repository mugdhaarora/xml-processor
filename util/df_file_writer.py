import openpyxl
import pandas as pd

def writeToFile(result_err_df, result_msg_df, result_rules_df, fileName): 
    with pd.ExcelWriter(fileName,engine="openpyxl") as writer :
        result_err_df.to_excel(writer,sheet_name='Errors', index = False)   
        result_msg_df.to_excel(writer,sheet_name='Message', index = False)
        result_rules_df.to_excel(writer,sheet_name='Rules', index = False)
