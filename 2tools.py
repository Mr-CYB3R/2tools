#!/usr/bin/env python
#-*- coding: utf-8-*-

#Assalamualaikum
import os
from time import sleep

#warna
hijau = "\033[92m"
kuning = "\033[93m"
merah = "\033[91m"
putih = "\033[97m"

#darktools
print hijau+"Author : Mr.CYB3R"
print hijau+"name : tools installer\n\n"

#new
print "[1]. Install darktools"
print "[2]. Install Send SMS Gratis"

inp = raw_input("dipilih gayn:")
if inp == "1":
      print "sedang proses penginstallan"
      sleep (1)
      os.system ("git clone https://github.com/Zone-Xploiter//darktools")
      print " sudah ter install Ster"

if inp == "2":
      os.system ("git clone https://github.com/Zone-Xploiter/ngoding")
      sleep(2)
      print " sudah ter install Ster"

#enjoyy
