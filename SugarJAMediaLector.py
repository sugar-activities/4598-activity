#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import commands

import gi
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject

import JAMediaLector
from JAMediaLector.JAMediaLector import JAMediaLector

from sugar3.activity import activity

import JAMediaObjects
import JAMediaObjects.JAMediaGlobales as G
JAMediaObjectsPath = JAMediaObjects.__path__[0]

class Ventana(activity.Activity):
    
    def __init__(self, handle):
        
        activity.Activity.__init__(self, handle, False)
        
        self.set_title("JAMediaLector")
        self.set_icon_from_file(os.path.join(JAMediaObjectsPath,
            "Iconos", "JAMediaLector.png"))
        self.set_resizable(True)
        self.set_size_request(640, 480)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(2)
        
        self.file_path = ""
        
        self.socket = Gtk.Socket()
        self.set_canvas(self.socket)
        self.jamedialector = JAMediaLector()
        self.socket.add_id(self.jamedialector.get_id())
        self.show_all()
        self.realize()
        
        self.connect("delete_event", self.delete_event)
        self.connect("destroy", self.salir)
        self.jamedialector.connect('salir', self.salir)
        
        GObject.idle_add(self.setup_init)
        
    def setup_init(self):
        self.jamedialector.setup_init()
        self.jamedialector.pack_standar()
        if self.file_path: self.jamedialector.abrir(self.file_path)
        
    def read_file(self, file_path):
        
        self.file_path = file_path
        
    def write_file(self, file_path):
        pass
    
    def delete_event(self, widget = None, event = None, data = None):
        self.salir()
        return False
    
    def salir(self, widget = None, senial = None):
        sys.exit(0)
    
if __name__ == "__main__":
    Ventana()
    Gtk.main()