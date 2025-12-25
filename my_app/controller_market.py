from tkinter import ttk

def market_data_frame(master, term_load_command, term_upload_command,term_dq_command,
                                vol_upload_command, vol_load_command, vol_dq_command,
                                ibors_upload_command, ibors_load_command, ibors_dq_command):
    market_data_frame =ttk.LabelFrame(master,
                                 text='Market Data',
                                )
    
    #term structure 
    term_structure_load_button =ttk.Button(market_data_frame,
                                            text='Load Term Structure Data',
                                            command =term_load_command)
    term_structure_load_button.pack(pady=5)

    term_structure_upload_button =ttk.Button(market_data_frame,
                                                text='Upload Term Structure Data',
                                                command =term_upload_command)
    term_structure_upload_button.pack(pady=5)

    term_structure_dq_button =ttk.Button(market_data_frame,
                                            text='Term Structure Data Quality Check',
                                            command =term_dq_command)
    term_structure_dq_button.pack(pady=5)
    #volatility surface
    vol_surface_upload_button =ttk.Button(market_data_frame,
                                           text='Upload Volatility Surface Data',
                                           command =vol_upload_command)
    vol_surface_upload_button.pack(pady=5)
    
    vol_surface_load_button =ttk.Button(market_data_frame,
                                            text='Load Volatility Surface Data',
                                            command =vol_load_command)
    vol_surface_load_button.pack(pady=5)

    vol_surface_dq_button =ttk.Button(market_data_frame,
                                         text='Volatility Surface Data Quality Check',
                                            command =vol_dq_command)
    vol_surface_dq_button.pack(pady=5)
    #ibors rates
    ibors_rates_upload_button =ttk.Button(market_data_frame,
                                            text='Upload IBORs Rates Data',
                                            command =ibors_upload_command)  
    ibors_rates_upload_button.pack(pady=5)

    ibors_rates_load_button =ttk.Button(market_data_frame,
                                          text='Load IBORs Rates Data',
                                            command =ibors_load_command)
    ibors_rates_load_button.pack(pady=5)

    ibors_rates_dq_button =ttk.Button(market_data_frame,
                                            text='IBORs Rates Data Quality Check',
                                                command =ibors_dq_command)
    ibors_rates_dq_button.pack(pady=5)
    
    market_data_frame.pack(padx =20, pady=10, fill='both',expand ='yes')

    return market_data_frame