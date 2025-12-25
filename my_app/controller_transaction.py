from tkinter import ttk

def transaction_data_frame(master, upload_command, load_command, dq_command):
    transaction_data_frame =ttk.LabelFrame(master,
                                      text='Transaction Data')
    transaction_data_frame.pack()
    


    transaction_data_upload_button =ttk.Button(transaction_data_frame,
                                               text='Upload Transaction Data',
                                               command =upload_command)
    transaction_data_upload_button.pack(pady=5)

    transaction_data_frame_load_button =ttk.Button(transaction_data_frame,
                                                  text='Load Transaction Data', 
                                                    command =load_command)
    transaction_data_frame_load_button.pack(pady=5)

    transaction_data_dq_button =ttk.Button(transaction_data_frame,
                                             text='Transaction Data Quality Check',
                                             command =dq_command)   
    transaction_data_dq_button.pack(pady=5)

    return transaction_data_frame