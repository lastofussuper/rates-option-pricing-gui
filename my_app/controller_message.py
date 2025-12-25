from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import os
import sys
import pandas as pd
import time

def info_message(title, message):
    messagebox.showinfo(title,message)


def error_message(title, message):
    messagebox.showerror(title, message)


def currency_popup(output_folder_path):
    significant_currencies_df_result =None
    table_window =tk.Toplevel()
    table_window.title('signficant currency & pricing methods & Assumptions')
    table_window.geometry('1000x400')

    columns =('Currency', 'Pricing Method', 'Assumptions')
    tree =ttk.Treeview(table_window,columns =columns, show ='headings')
    tree.heading('Currency', text='Currency')
    tree.heading('Pricing Method', text='Pricing Method')
    tree.heading('Assumptions', text='Assumptions')
    tree.pack(expand=True, fill='both')

    if getattr(sys,'frozen', False):
        current_folder =sys._MEIPASS
    else:
        current_folder =os.path.dirname(__file__)

    mapping_file_path =os.path.abspath(os.path.join(current_folder, '..', 'mapping_files', 'significant_currencies_mapping.csv'))

    if os.path.exists(mapping_file_path):
        default_significant_currencies =pd.read_csv(mapping_file_path).values.tolist()
    else:
        raise ValueError('signicant_currencies_mapping.csv file not found in mapping_files folder.')
    
    for currency, pricing_method, assumptions in default_significant_currencies:
        tree.insert('', tk.END, values=(currency, pricing_method, assumptions))

    def add_row():

        def save_row():
            currency =currency_var.get()
            pricing_method =pricing_method_var.get()
            assumptions =assumptions_var.get()

            if len(currency)==3 and currency.isupper():
                tree.insert('',tk.END, values =(currency, pricing_method, assumptions))
                add_row_window.destroy()
            else:
                error_message('Invalid Currency','Currency must be 3 capital letters.')

        add_row_window =tk.Toplevel(table_window)
        add_row_window.tile('Add Currency')
        add_row_window.geometry('500x200')

        tk.Label(add_row_window, text='Currency: 3 capital letters only').pack(pady=5)
        currency_var =tk.StringVar()
        currency_entry = ttk.Entry(add_row_window, textvariable =currency_var)
        currency_entry.pack(pady=5)

        tk.Label(add_row_window, text='Pricing Method: ').pack(pady=5)
        pricing_method_var =tk.StringVar(value ='risk_neutral')
        pricing_method_dropdown =ttk.Combobox(add_row_window,
                                              textvariable =pricing_method_var,
                                              values=['historical','risk_neutral'])
        pricing_method_dropdown.pack(pady=5)

        tk.Label(add_row_window, text='Assumptions: ').pack(pady=5)
        assumptions_var =tk.StringVar(value ='SN')
        assumptions_dropdown =ttk.Combobox(add_row_window,
                                           textvariable =assumptions_var,
                                           values =['SN','SV'])
        assumptions_dropdown.pack(pady=5)

        save_button =ttk.Button(add_row_window, text='Save', command =save_row)

        save_button.pack(pady=5)

    def delete_row():
        selected_row =tree.selection()
        if selected_row:
            tree.delete(selected_row)

        else:
            error_message('No Selection','Please select a row to delete.')
    
    def save_table():

        rows =[]
        for row_id in tree.get_children():
            rows.append(tree.item(row_id)['values'])
        significant_currencies_df_result =pd.DataFrame(rows, columns =['Currency','Pricing Method','Assumptions'])
        
        if default_significant_currencies == significant_currencies_df_result.values.tolist():
            info_message('No Changes','No changes made to significant currencies.')
            table_window.destroy()
            return None
        else:
            significant_currencies_df_result.to_csv(mapping_file_path,index=False)
            time_stamp =time.time().strftime('%Y%m%d_%H%M%S')
            file_name =f'significant_currencies_{time_stamp}.csv'
            significant_currencies_df_result.to_csv(os.path.join(output_folder_path,file_name), index =False)
            info_message('Saved','Significant currencies saved successfully.')
            table_window.destroy()
    
    add_button =ttk.Button(table_window, text='Add Row', command =add_row)
    add_button.pack(pady=5)

    delete_button =ttk.Button(table_window, text='Delete Row', command =delete_row)

    delete_button.pack(pady=5)

    save_button =ttk.Button(table_window, text='Save Table', command =save_table)
    save_button.pack(pady=5)

    table_window.wait_window()

    return significant_currencies_df_result
        

    

    
    




