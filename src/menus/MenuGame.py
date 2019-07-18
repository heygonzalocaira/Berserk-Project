import wx

class Login(wx.Frame):


    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'Berserk', size=(500, 500))
        # Vertical sizer
        self.v_sizer = wx.BoxSizer(wx.VERTICAL)

        # Widget Creation

        # Create the button
        self.Solo = wx.Button(self, label="JugarSolo")
        self.Multiplayer= wx.Button(self, label="JugarMultiplayer")
        self.Opciones = wx.Button(self, label="Opciones")
        self.Salir = wx.Button(self, label="Salir")

        self.v_sizer.Add(self.Solo,wx.EXPAND,wx.ALIGN_RIGHT, 0)
        self.v_sizer.Add(((30, 30)))
        self.v_sizer.Add(self.Multiplayer,wx.EXPAND,wx.ALIGN_RIGHT, 0)
        self.v_sizer.Add(((30, 30)))
        self.v_sizer.Add(self.Opciones,wx.EXPAND, wx.ALIGN_RIGHT,0)
        self.v_sizer.Add(((30, 30)))
        self.v_sizer.Add(self.Salir,wx.EXPAND, wx.ALIGN_RIGHT,0)

        # Modificar acciones de cada button
        self.Solo.Bind(wx.EVT_BUTTON, self.OnSolo)
        self.Multiplayer.Bind(wx.EVT_BUTTON, self.OnMultiplayer)
        self.Opciones.Bind(wx.EVT_BUTTON, self.Options)
        self.Salir.Bind(wx.EVT_BUTTON, self.CloseWindows)


        # Add to the vertical sizer to create 3 rows


        # Set the sizer
        self.SetSizer(self.v_sizer)

    def OnSolo(self,event):
        pass


    def OnMultiplayer(self,event):
        pass

    def Options(self,event):
        pass

    def CloseWindows(self,event):
        self.Destroy()



if __name__=='__main__':
    app = wx.App()
    frame = Login(parent=None,id=-1)
    frame.Show()
    app.MainLoop()