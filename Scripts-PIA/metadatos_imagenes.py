# -*- encoding: utf-8 -*-
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os
import argparse


def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin/60.0 + Nsec/3600.0))
        Lng = Wmult * (Wdeg + (Wmin/60.0 + Wsec/3600.0))
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def printMeta(x):
    ruta = x
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("[+] Metadata for file: %s " %(name))
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                print ("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

descrip = """ El parametro principal -metadata usa como argumento la ruta de las imagenes
ejemplo: -metadata c:imagenes/facebook"""

