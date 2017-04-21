#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   JAMediaGlobals.py por:
#   Flavio Danesse <fdanesse@gmail.com>
#   CeibalJAM! - Uruguay

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os
import commands

import gi
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import GdkX11

if not os.path.exists(os.path.join(os.environ["HOME"], "JAMediaDatos")):
    os.mkdir(os.path.join(os.environ["HOME"], "JAMediaDatos"))
    os.chmod(os.path.join(os.environ["HOME"], "JAMediaDatos"), 0755)

# unificar directorios de JAMedia, JAMediaVideo y JAMediaImagenes
directorio_viejo = os.path.join(os.environ["HOME"], ".JAMediaDatos")
directorio_nuevo = os.path.join(os.environ["HOME"], "JAMediaDatos")
if os.path.exists(directorio_viejo):
    for elemento in os.listdir(directorio_viejo):
        commands.getoutput('mv %s %s' % (os.path.join(directorio_viejo,
            elemento), directorio_nuevo))
    commands.getoutput('rm -r %s' % (directorio_viejo))

# Directorios JAMedia
DIRECTORIO_MIS_ARCHIVOS = os.path.join(os.environ["HOME"],
    "JAMediaDatos", "MisArchivos")
DIRECTORIO_DATOS = os.path.join(os.environ["HOME"],
    "JAMediaDatos", "Datos")
if not os.path.exists(DIRECTORIO_MIS_ARCHIVOS):
    os.mkdir(DIRECTORIO_MIS_ARCHIVOS)
    os.chmod(DIRECTORIO_MIS_ARCHIVOS, 0755)
if not os.path.exists(DIRECTORIO_DATOS):
    os.mkdir(DIRECTORIO_DATOS)
    os.chmod(DIRECTORIO_DATOS, 0755)

# Directorio JAMediaTube
DIRECTORIO_YOUTUBE = os.path.join(os.environ["HOME"],
    "JAMediaDatos", "YoutubeVideos")
if not os.path.exists(DIRECTORIO_YOUTUBE):
    os.mkdir(DIRECTORIO_YOUTUBE)
    os.chmod(DIRECTORIO_YOUTUBE, 0755)

# Directorios JAMediaVideo
AUDIO_JAMEDIA_VIDEO = os.path.join(os.environ["HOME"],
    "JAMediaDatos", "Audio")
if not os.path.exists(AUDIO_JAMEDIA_VIDEO):
    os.mkdir(AUDIO_JAMEDIA_VIDEO)
    os.chmod(AUDIO_JAMEDIA_VIDEO, 0755)
VIDEO_JAMEDIA_VIDEO = os.path.join(os.environ["HOME"],
    "JAMediaDatos", "Videos")
if not os.path.exists(VIDEO_JAMEDIA_VIDEO):
    os.mkdir(VIDEO_JAMEDIA_VIDEO)
    os.chmod(VIDEO_JAMEDIA_VIDEO, 0755)
IMAGENES_JAMEDIA_VIDEO = os.path.join(os.environ["HOME"],
    "JAMediaDatos", "Fotos")
if not os.path.exists(IMAGENES_JAMEDIA_VIDEO):
    os.mkdir(IMAGENES_JAMEDIA_VIDEO)
    os.chmod(IMAGENES_JAMEDIA_VIDEO, 0755)

GRIS = Gdk.Color(60156, 60156, 60156)
AMARILLO = Gdk.Color(65000,65000,40275)
NARANJA = Gdk.Color(65000,26000,0)
BLANCO = Gdk.Color(65535, 65535, 65535)
NEGRO = Gdk.Color(0, 0, 0)

def get_pixels(centimetros):
    """ Recibe un tamaño centimetros y
    devuelve el tamaño en pixels que le corresponde,
    según tamaño del monitor que se está utilizando.
    
    # 1 px = 0.026458333 cm
    # 1 Pixel = 0.03 Centimetros = 0.01 Pulgadas. """

    screen = GdkX11.X11Screen()
    
    res_w = screen.width()
    res_h = screen.height()
    
    mm_w = screen.width_mm()
    mm_h = screen.height_mm()
    
    ancho = int (float(res_w) / float(mm_w) * 10.0 * centimetros)
    alto = int (float(res_h) / float(mm_h) * 10.0 * centimetros)
    
    return int(min([ancho, alto]))

def get_separador(draw = False, ancho = 0, expand = False):
    """ Devuelve un separador generico."""
    
    separador = Gtk.SeparatorToolItem()
    separador.props.draw = draw
    separador.set_size_request(ancho, -1)
    separador.set_expand(expand)
    return separador

def get_boton(archivo, flip = False,
    color = Gdk.Color(65000, 65000, 65000), rotacion = None, pixels = 0):
    """ Devuelve un toolbarbutton generico."""
    
    if not pixels:
        pixels = get_pixels(1)
        
    boton = Gtk.ToolButton()
    imagen = Gtk.Image()
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(archivo, pixels, pixels)
    if flip: pixbuf = pixbuf.flip(True)
    if rotacion: pixbuf = pixbuf.rotate_simple(rotacion)
    imagen.set_from_pixbuf(pixbuf)
    imagen.modify_bg(0, color)
    boton.set_icon_widget(imagen)
    imagen.show()
    boton.show()
    return boton

def get_togle_boton(archivo, flip = False,
    color = Gdk.Color(65000, 65000, 65000), pixels = 0):
    """ Devuelve un toolbarbutton generico."""
    
    if not pixels:
        pixels = get_pixels(1.5)
        
    boton = Gtk.ToggleToolButton()
    imagen = Gtk.Image()
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(archivo, pixels, pixels)
    if flip: pixbuf = pixbuf.flip(True)
    imagen.set_from_pixbuf(pixbuf)
    imagen.modify_bg(0, color)
    boton.set_icon_widget(imagen)
    imagen.show()
    boton.show()
    return boton

'''
Anotaciones para describir las clases de JAMedia:
    import pydoc
    import JAMediaObjects
    from JAMediaObjects.JAMediaReproductor import JAMediaReproductor

    pydoc.writedoc(JAMediaReproductor)'''
        