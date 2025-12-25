import re
from my_app.params import report_date_format
#from pyxlsb import open_workbook
import logging

def validate_date(date_value):
    if bool(re.match(report_date_format, date_value)):
        return True
    else:
        return False
    

def data_quality_check(df,df_type):
    # skip this part as it is really sector specific..
    # nothing techinical here, 
    # pure inspired by experience of tackling wierd data from different source.
    df
    df_type
    pass

def read_file(file_paths):
    if len(file_paths)==1:
        file_path =file_paths[0]
        if file_path.endswith('.csv'):
            import pandas as pd
            df =pd.read_csv(file_path)
            return df
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            import pandas as pd
            df =pd.read_excel(file_path)
            return df
        elif file_path.endswith('.xlsb'):
            # with open_workbook(file_path) as wb:
            #     with wb.get_sheet(1) as sheet:
            #         df =[row for row in sheet.rows()]
            #         return df
            pass  # skip for now
                    
        else:
            raise ValueError('Unsupported file format. Please upload a CSV or Excel file.')
    else:
        dfs ={}
        for file_path in file_paths:
            logging.info(f'Reading file: {file_path}')
            file_name =re.search(r'[^\\/\]+(?=\.\w]+$)',file_path).group()
            if file_path.endswith('.csv'):
                import pandas as pd
                df =pd.read_csv(file_path)
                dfs[file_name] =df
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                import pandas as pd
                df =pd.read_excel(file_path)
                dfs[file_name] =df
            elif file_path.endswith('.xlsb'):
                # with open_workbook(file_path) as wb:
                #     with wb.get_sheet(1) as sheet:
                #         df =[row for row in sheet.rows()]
                #         dfs[file_name] =df
                pass  # skip for now
            else:
                raise ValueError('Unsupported file format. Please upload a CSV or Excel file.')
            
        return dfs
    
            

