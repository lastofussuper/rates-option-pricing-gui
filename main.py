import tkinter as tk
from my_app.gui import MyApp
import logging
def main():
    logging.basicConfig(level =logging.INFO,
                        format ='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('staring the application')

    root =tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ =='__main__':
    main()