from tkinter import filedialog


def upload_data(app,df_type):
    file_paths =filedialog.askopenfilenames(title =f'Please select {df_type} data file(s) to upload',
                                            filetypes =[('csv files','*.csv'),
                                                        ('excel files','*.xlsx;*.xls'),
                                                        ('excel binary files','*.xlsb')])
    if file_paths:
        app.df_paths =list(file_paths)
        print(f'{df_type} data file(s) uploaded successfully: {app.df_paths}')
        return app.df_paths
    else:
        print(f'No {df_type} data file(s) selected.')
        return None 