from tkinter import ttk
from tkinter import StringVar
from my_app.utils import validate_date
from my_app.controller_message import error_message
from tkinter import filedialog
import time
import os
def configuration_initialization(master, select_output_folder_wrap,
                                 currency_popup_wrap,
                                 config_wrap,
                                 config_completeness_check_wrap):
    configuration_frame =ttk.Frame(master,
                                   padding='10 10 10 10')
    configuration_frame.pack(pady=10)

    output_folder_label =ttk.Label(configuration_frame,
                                   text='Select the folder you want to generate outputs in:')
    output_folder_label.pack(pady=5)

    select_output_folder_button =ttk.Button(configuration_frame,
                                            text='Select Output Folder',
                                            command=select_output_folder_wrap)
    select_output_folder_button.pack(pady=5)

    #date entry
    date_label =ttk.Label(configuration_frame,
                          text ='Enter Date (dd-MMM-yyyy): 31-Dec-2025 as example')
    date_label.pack(pady=5)

    value_date =StringVar()
    value_date_entry =ttk.Entry(configuration_frame,
                                 textvariable =value_date)
    value_date_entry.pack(pady=5)

    def  validate_date_event(event= None):
        date_value =value_date.get()
        if validate_date(date_value):
            return True
        else:
            error_message('Invalid Date Format! Please enter date in dd-MMM-yyyy format, e.g., 31-Dec-2025')
    
    value_date_entry.bind('<FocusOut>', validate_date_event)
    value_date_entry.bind('<Return>', validate_date_event)

    #check significant_currency_list
    significant_currency_button =ttk.Button(configuration_frame,
                                             text='Select Significant Currencies',
                                             command=currency_popup_wrap)
    significant_currency_button.pack(pady=5)

    #stressed scenario configuration
    stressed_scenario_button =ttk.Button(configuration_frame,
                                         text ='load parrellel scenario configuration',
                                         command =config_wrap,)
    stressed_scenario_button.pack(pady=5)

    #configuration completeness check
    stressed_config_completness_check_button =ttk.Button(configuration_frame,
                                                         text='Configuration Completeness Check',
                                                         command =config_completeness_check_wrap
                                                         )
    stressed_config_completness_check_button.pack(pady=5)

    return {'value_date': value_date}

def select_output_folder(app):
    selected_folder =filedialog.askdirectory(title='Select Output Folder')
    time_stamp =time.time().strftime('%Y%m%d_%H%M%S')
    output_folder =os.path.join(selected_folder,f'output_{time_stamp}')
    os.makedirs(output_folder,exist_ok =True)
    output_folder =os.path.normpath(output_folder)
    
    app.output_folder_path =output_folder

    return  app.output_folder_path





            



