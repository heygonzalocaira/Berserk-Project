import wx
from utils import *
import webbrowser

class Login(wx.Frame):


    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Berserk', size=(500, 500))
        self.h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.h2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.h3_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Vertical sizer
        self.v_sizer = wx.BoxSizer(wx.VERTICAL)

        # Widget Creation
        # Create the static text widget and set the text
        self.text = wx.StaticText(self, label="Username:")
        # Create the Edit Field (or TextCtrl)
        self.edit = wx.TextCtrl(self, size=wx.Size(150, -1))
        # Create the static text widget and set the text
        self.password = wx.StaticText(self, label="Password: ")
        # Create the Edit Field (or TextCtrl)
        self.edit_pass = wx.TextCtrl(self, size=wx.Size(150, -1))

        # Create the button
        self.Ingresar = wx.Button(self, label="Ingresar")
        self.Registrarse = wx.Button(self, label="Registrarse")

        # Add to horizontal sizer
        # add the static text to the sizer, tell it not to resize
        self.h_sizer.Add(self.text, 0, )
        self.h_sizer.Add(self.edit, 1)

        self.h2_sizer.Add(self.password, 0, )
        self.h2_sizer.Add(self.edit_pass, 1)

        self.h3_sizer.Add(self.Ingresar, 0)
        self.h3_sizer.Add(((30, 30)))
        self.h3_sizer.Add(self.Registrarse, 0)

        self.Ingresar.Bind(wx.EVT_BUTTON, self.OnAutenticate)
        self.Registrarse.Bind(wx.EVT_BUTTON, self.OnRegister)

        # Add to the vertical sizer to create 3 rows
        self.v_sizer.Add(self.h_sizer, 0)
        self.v_sizer.Add(self.h2_sizer, 0)
        self.v_sizer.Add(self.h3_sizer, 0)
        # Add button underneath

        # Set the sizer
        self.SetSizer(self.v_sizer)

    def OnAutenticate(self,event):
        username = self.edit.GetValue()
        password = self.edit_pass.GetValue()
        if autenticate(username,password):
            print("Pasar al siguiente Menu, eliminar este")
        else:
            wx.MessageBox("Usuario o Contraseña incorrecta","Info", wx.OK)


    def OnRegister(self,event):
        webbrowser.open_new("https://pypi.python.org/pypi")

    def closewindow(self,event):
        self.Destroy()



if __name__=='__main__':
    app = wx.App()
    frame = Login(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

