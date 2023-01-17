import os
from delphivcl import *

class Form1(Form):

    def __init__(self, owner):
        self.EFilm = None
        self.BtnSearch = None
        self.ListBox1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Interfaz.pydfm"))

    def BtnSearchClick(self, Sender):
        self.ListBox1.Items.Add(self.EFilm.Text)
        self.EFilm.Text = ""
        txt = self.EFilm.Text
        print(str(txt))

def main():
    Application.Initialize()
    Application.Title = 'ProyectoSSII'
    MainForm = Form1(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()