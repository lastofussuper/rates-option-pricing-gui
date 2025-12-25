from tkinter import ttk
import pandas as pd
from my_app.controller_initial_configuration import configuration_initialization, select_output_folder
from my_app.controller_upload import upload_data
from my_app.controller_transaction import transaction_data_frame
from my_app.controller_market import market_data_frame
from my_app.utils import read_file
from my_app.controller_message import error_message, info_message, currency_popup

class MyApp:
    def __init__(self,master):
        self.output_folder_path =None
        self.significant_currency= pd.DataFrame()
        self.df_paths =None
        self.input_dfs ={}



        self.master =master
        master.title('Rates Derivatives Pricing Engine')
        master.geometry('1200x800')

        #initial configuration frame
        self.initial_configuration_frame =configuration_initialization(
            master,
            select_output_folder_wrap =self.select_output_folder_wrap,
            
            currency_popup_wrap =self.currency_popup_wrap,
            config_wrap =self.configure_wrap,
            config_completeness_check_wrap=self.config_completeness_check_wrap,
        )
        self.value_date =self.initial_configuration_frame['value_date']
        #self.value_date =self.initial_configuration_frame.value_date

        # transaction data frame
        self.transaction_data_frame=transaction_data_frame(master,
                                                             upload_command =lambda: upload_data(self,df_type='transaction'),
                                                             load_command =lambda: self.load_df_wrap(df_type='transaction'),
                                                             dq_command =self.dq_wrap(df_type='transaction'))
        
        #market data frame
        self.market_data_frame =market_data_frame(master,
                                                  term_load_command= lambda: upload_data(self,df_type='term_structure'),
                                                  term_upload_command =lambda:self.load_df_wrap(df_type='term_structure'),
                                                  term_dq_command =self.dq_wrap(df_type='term_structure'),
                                                  vol_upload_command =lambda :upload_data(self,df_type='volatility_surface'),
                                                  vol_load_command =lambda: self.load_df_wrap(df_type='volatility_surface'),
                                                  vol_dq_command =self.dq_wrap(df_type='volatility_surface'),
                                                  ibors_upload_command =lambda :upload_data(self,df_type='ibors_rates'),
                                                  ibors_load_command =lambda:self.load_df_wrap(df_type='ibors_rates'),
                                                  ibors_dq_command =self.dq_wrap(df_type='ibors_rates'))

        self.transaction_data ={}

        self.transaction_data_preparation =ttk.Button(master,
                                                      text='run transaction data preprocessor',
                                                      command =self.transaction_data_preprocessor_wrap)
        self.transaction_data_preparation.pack()

        self.market_data_prepared ={}

        self.market_data_preparation =ttk.Button(master,
                                                  text='run market data preprocessor',
                                                  command =self.market_data_preprocessor_wrap)
        self.market_data_preparation.pack()

        self.run_model_button =ttk.Button(master,
                                          text='run model', 
                                            command =self.run_model)
        self.run_model_button.pack()


    def select_output_folder_wrap(self):
        if self.output_folder_path is None:
            select_output_folder(self)
            return self.output_folder_path
        else:
            error_message('Output folder already selected.')
            return self.output_folder_path
        
    def load_df_wrap(self,df_type):
        df_type =df_type
        
        self.df[f'df_{df_type}'] =read_file(self.df_paths)
        info_message(f'{df_type} data loaded successfully.')
        return self.df[f'df_{df_type}']
    def dq_wrap(self,df_type):
        df_type =df_type
        pass
         # skip this part as it is really sector specific..
         # nothing techinical here, 
        # pure inspired by experience of tackling wierd data from different source.
    def currency_popup_wrap(self):
        output_folder_path =self.output_folder_path
        self.significant_currency =currency_popup(output_folder_path)

        return self.significant_currency

    def configure_wrap(self):
        # it is only used to generate all stressed scnarios
        # no so important or technical
        # skip for now
        pass
    def config_completeness_check_wrap(self):
        # another data quality check
        # skip for now
        pass
    def transaction_data_preprocessor_wrap(self):
        
        # really sector specific
        #skip for now
        pass
    def market_data_preprocessor_wrap(self):
        # a function needed bcs in real life market data is messy
        # skip for now
        pass
    def run_model(self):
        pass
        # if self.output_folder_path:
        #    output_folder_path =self.output_folder_path
        # else:
        #       error_message('Please select output folder first.')
        #       return None
        # value_date =self.report_date.get()
