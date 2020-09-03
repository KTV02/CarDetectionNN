# -*- coding: utf-8  -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
import urllib
import requests
from pyvirtualdisplay import Display
from requests.exceptions import ConnectionError
#from PIL import Image
#import PIL
import random
import logging
from PIL import Image
from PIL import ImageFile
from io import BytesIO
import os
import re
import difflib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotVisibleException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
#class InstaBot:
#option.binary_location="" driver = webdriver.Chrome(chrome_options=options)
# coding=utf8

#init of number that counts total number of downloaded images
totalnumber=0
#all listings that have been visited by this programm
blacklist=[]
#alle Models die erkannt werden werden hier gespeichert
models=[]
#models=["Mitsubishi Galant 1992",  "Mitsubishi Grandis 2004", "Mitsubishi Galloper ", "Mitsubishi Outlander (CWO)", "Mitsubishi L200", "Mitsubishi Colt 1990", "Mitsubishi Carisma 1997", "Mitsubishi Space Wagon 1999", "Mitsubishi Space Star", "Mitsubishi Galloper", "Mitsubishi Sigma V6", "Mitsubishi 3000 GT", "Mitsubishi L200 (5)", "Mitsubishi Outlander", "Mitsubishi Space Gear", "Mitsubishi ASX ", "Nissan 370Z / 350Z", "Nissan Evalia / NV200", "Nissan GT-R", "Nissan Juke", "Nissan Leaf", "Nissan Micra", "Nissan Murano", "Nissan Navara", "Nissan Note", "Nissan Pathfinder", "Nissan Pixo", "Nissan Pulsar", "Nissan Qashqai", "Nissan X-Trail",  "Nissan Patrol", "Nissan Primera", "Nissan Micra", "Nissan Murano", "Nissan Almera", "Nissan Pathfinder", "Nissan Note", "Nissan Qashqai", "Nissan Skyline", "Nissan Sunny", "Nissan Terrano", "Nissan Maxima 1996", "Opel Rekord", "Nissan Micra (K13)", "Nissan Serena", "Nissan 370Z / 350Z", "Nissan Navara", "Nissan Pixo", "Nissan Cube",  "Nissan Pathfinder 1998", "Nissan Patrol 1992", "Nissan Juke", "Nissan X-Trail", "Nissan Vanette", "Nissan Kubistar Dci70", "Nissan Primastar", "Nissan Maxima", "Nissan Sunny 1990", "Nissan Terrano 1993", "Nissan Tiida 2008 2008", "Nissan Primastar 1.9", "Nissan Primera 1991", "Nissan GT-R", "Nissan Qashqai (J11)", "Nissan Pixo 1.0", "Nissan 350Z 2003", "Nissan Murano 2005", "Nissan Interstar ", "Nissan Tiida", "Nissan 100 NX", "Nissan Evalia (NV200/M20M)", "Nissan 350Z Coupé", "Nissan Almera Tino", "Nissan King Cab", "Nissan 300 ZX", "Nissan Armada", "Nissan Micra (K14)", "Nissan Quest", "Nissan Prairie", "Nissan Juke (F15)", "Nissan Urvan", "Nissan PickUp", "Nissan 370Z (Z34)", "Nissan Altima", "Nissan Kubistar", "Nissan Leaf (ZE0)", "Nissan Cabstar", "Nissan Almera 1995", "Nissan 200 SX", "Nissan 280 ZX", "Nissan X-Trail (T32) " , "Rolls-Royce Dawn", "Rolls-Royce Ghost", "Rolls-Royce Phantom", "Rolls-Royce Wraith",  "Honda Legend", "Rolls-Royce Wraith", "Rolls-Royce Corniche", "Rolls-Royce Dawn", "Rolls-Royce Phantom", "Rolls-Royce Silver Cloud", "Rolls-Royce Ghost", "Rolls-Royce Silver Shadow", "Rolls-Royce Drophead", "Rolls-Royce Seraph ",  "Seat Alhambra", "Seat Altea", "Seat Ateca", "Seat Exeo", "Seat Ibiza", "Seat Leon", "Seat Mii", "Seat Toledo",  "Seat Marbella", "Opel Rekord", "Seat Cordoba", "Seat Altea", "Seat Exeo",  "Seat Inca", "Seat Arosa", "Seat Alhambra", "Seat Cordoba 1996", "Seat Leon", "Seat Altea 2004", "Seat Altea Xl", "Seat Arosa 1998",  "Seat Toledo", "Seat Marbella ", "Seat Ibiza", "Seat Inca 1.9", "Seat Toledo (NH) ",  "Smart Forfour", "Smart Fortwo",  "Smart Brabus", "Smart Crossblade", "Smart Roadster", "BMW Roadster 1", "Smart Fortwo Cabrio (A453)", "Smart Fortwo (453)", "Smart Forfour ",  "SsangYong Actyon Sports", "SsangYong Korando", "SsangYong Rexton", "SsangYong Rodius", "SsangYong Tivoli", "SsangYong XLV",  "SsangYong Actyon Sports", "SsangYong Rexton", "SsangYong Rodius", "Ssangyong Kyron", "Ssangyong MUSSO", "SsangYong Tivoli", "SsangYong Tivoli", "Mahindra", "Ford C-Max 2004 ",  "Subaru BRZ", "Subaru Forester", "Subaru Impreza", "Subaru Levorg", "Subaru Outback", "Subaru WRX STI", "Subaru XV",  "Subaru Justy", "Opel Rekord", "Subaru Legacy", "Skoda Sedan", "Subaru Libero", "Subaru Tribeca", "Subaru Justy G3x", "Subaru Forester", "Subaru Outback", "Subaru Impreza (G4)", "Subaru Tribeca 2007", "Subaru Trezia", "Subaru SVX", "Subaru B9 Tribeca 2006", "Subaru Impreza", "Subaru Forester", "Subaru Legacy 1990 " , "Suzuki Baleno", "Suzuki Celerio", "Suzuki Ignis", "Suzuki Jimny", "Suzuki Swift", "Suzuki SX4", "Suzuki Vitara",  "Suzuki Vitara", "Suzuki Alto", "Suzuki Liana", "Suzuki Ignis", "Suzuki Grand Vitara", "Suzuki Kizashi", "Suzuki Splash", "Jeep Grand Cherokee 1993", "Suzuki Wagon R+", "Suzuki Samurai", "Suzuki Samurai De", "Suzuki SX4 S-Cross", "Suzuki Wagon R+ 1998", "Suzuki SX4", "Suzuki Baleno (EW)", "Suzuki Splash Auto", "Suzuki Vitara (2 / LY)", "Suzuki Liana 2002 2002", "Suzuki Swift (NZ)", "Suzuki Swift", "Suzuki Jimny", "Suzuki Alto 1997", "Suzuki Kizashi 2", "Suzuki Ignis", "Suzuki LJ 80", "Suzuki Celerio", "Suzuki Sj 410", "Suzuki Sj 413", "Suzuki Xl7", "Suzuki X-90 ",  "Tesla Model S", "Tesla Model X",   "Tesla Roadster", "Tesla Model 3", "Ferrari GTC4 Lusso",  "Peugeot 206", "Peugeot 308", "Ferrari F430", "Maserati GranTurismo", "Mercedes SLK 320", "Ferrari 288", "Ferrari Enzo", "Piaggio",  "Ferrari Testarossa", "Ferrari 599 GTO", "Ferrari GTC4 Lusso", "Ferrari Daytona", "BMW 3er",  "Ferrari 488 GTB", "Lotus Evora", "Bentley Continental", "Porsche 911 Turbo und Turbo S (991 II)", "Mitsubishi Eclipse", "Renault Spider", "Mazda MX-5 (ND)", "Ferrari 599 GTB", "Mercedes SLC / SLK", "Honda CR-Z", "Maserati Spyder", "Ferrari 458 Italia",  "VW Golf", "BMW 6er Cabriolet (F12)", "Jaguar XK",  "Porsche 718 Cayman",  "Audi A5", "VW Passat", "Ferrari 348", "Ferrari F50", "Ferrari LaFerrari", "Ferrari F430 2005", "Ferrari 360", "Ferrari 550", "Ferrari 456", "Ferrari 355", "Ferrari 488 Spider", "Aston Martin DB9", "Ferrari 612", "Ferrari 400", "Ferrari Scaglietti", "Ferrari 575", "Ferrari 365", "Ferrari 512", "Ferrari California 2009", "Ferrari 328", "BMW M6 635", "Mazda RX-7", "Lamborghini Murciélago 640", "Ferrari F40",  "Ferrari F12 Tdf", "Fiat Barchetta", "Ferrari 246", "Ferrari F12 Berlinetta", "Ferrari 458 Speciale", "Ferrari California", "Ferrari F355 1995", "Ferrari 308", "Ferrari FF", "Ferrari 412", "Ferrari Mondial ", "Mercedes A-Klasse", "BMW 2006", "Audi A1", "Audi A3", "Audi A4", "Audi A4 allroad", "Audi A5", "Audi A6", "Audi A6 allroad", "Audi A7", "Audi A8", "Audi Q2", "Audi Q3", "Audi Q5", "Audi Q7", "Audi R8", "Audi TT","NSU", "Audi QUATTRO", "Audi TTS","Audi 80",  "Audi Q7", "BMW 5er", "BMW X6",   "VW Polo", "BMW 3er", "VW Golf", "Audi TT", "Audi A6", "Audi A3", "Ford Fusion", "Audi 100", "Mercedes CL-Klasse", "Audi A7/S7 Sportback (4G)", "BMW X3", "Audi 80 Cabrio",  "Audi A8", "Audi A4",  "Audi A2", "Audi Cabriolet",    "Audi R8",  "Audi Cabriolet 1994", "Audi 50", "Audi Q1",  "Audi Coupé", "Audi A4 Avant (B8)", "Hyundai Coupe 1.6", "Audi A3 Dreitürer (8V)", "Audi A4 Limousine (B9)",  "Skoda Fabia", "Toyota Prius","BMW 6er", "Audi A2 2000", "Audi S4 2000", "Audi S6 1995", "Audi S8 1997", "Audi A6 allroad quattro (C7)", "Audi RS4 2000", "Audi V8 ", "Audi S5 2007", "Audi Q8", "Audi A5", "Audi Q3", "Audi RS6 Avant (C7/4G)", "Audi A1/S1 (8X)", "Audi A1", "Audi R8 Coupé (4S)", "Audi A5 Coupé (F5)", "Audi A6 Limousine (4G)", "Audi 200", "Audi S2", "Audi A8 (D4)", "Audi A7", "Audi 90", "Audi Q5 (8R)", "Audi V8", "Audi Allroad", "Audi Q5 ", "BMW 1er", "BMW 2er", "BMW 3er", "BMW 4er", "BMW 5er", "BMW 6er", "BMW 7er", "BMW i3", "BMW i8", "BMW X1", "BMW X3", "BMW X4", "BMW X5", "BMW X6", "BMW Z4", "BMW Z8",  "VW Touareg", "BMW X6", "BMW 1er", "BMW 3er", "Ford Taunus", "Audi 50", "Mercedes 190 Sl", "Alfa Romeo 166", "BMW M550 550d", "Mercedes 300 Se", "BMW M235 M235i",  "BMW Isetta", "Porsche Cayenne",  "BMW 7er (G11/G12)",  "Audi Q7", "BMW 2er", "BMW 5er",  "BMW 6er", "BMW X1 Neuwagen", "BMW X5 (F15)", "BMW 3er Limousine (F30)",  "BMW X5", "BMW 4er",    "BMW Z4", "BMW Z3",  "BMW 1600",   "Opel Olympia",  "Aston Martin V8 Vantage",   "Citroën DS", "BMW X3", "VW Golf", "BMW 650 650i", "Audi TT",   "BMW 2002", "Lancia Fulvia", "Saab 95", "Citroën DS3", "Mercedes 220 Coupé Se",  "Mercedes 220 Coupé Seb", "BMW 502", "Volvo Amazon", "MINI MINI Innocenti", "BMW 850", "BMW 7er", "BMW 700",  "BMW Z1", "BMW 6er Coupé (F13) ", "BMW X2", "BMW 840", "BMW 8er", "Porsche 911", "BMW Z8", "Porsche 968", "VW Tiguan", "Lexus LS 600h (XF40)", "Mercedes SLC / SLK", "Ford Mustang", "Toyota Supra ","Saab 9-3",  "Saab 9", "Saab 900", "Saab Kombi", "Saab 9-5", "Saab Cabrio","Mercedes 4matic", "dodge ram 2012", "dodge ram 1500 hemi", "Dodge RAM","dodge ram 250", "Dodge RAM 1500 crew cab laramie", "dodge durango", "dodge caliber", "dodge challenger srt8", "dodge ram 1500 laramie", "Dodge Challenger", "dodge ram 2500","Skoda Citigo", "Skoda Fabia", "Skoda Karoq", "Skoda Kodiaq", "Skoda Octavia", "Skoda Rapid", "Skoda Roomster", "Skoda Superb", "Skoda Yeti",  "Skoda Rapid Limousine (NH)", "Honda Accord", "Skoda Roomster (5J)", "Smart Crossblade", "Skoda Felicia", "Skoda Sedan","Skoda Yeti (5L)", "Skoda Greenline", "Skoda Octavia",  "Skoda Felicia 1996", "Skoda Fabia", "Skoda Yeti Outdoor", "Skoda Superb", "Skoda Favorit", "Skoda Fabia (3/NJ)", "Skoda Superb Limousine (3V)", "Skoda Octavia Limousine (5E) ","Mercedes A-Klasse", "Mercedes B-Klasse", "Mercedes C-Klasse", "Mercedes Citan", "Mercedes CL", "Mercedes CLA / CLA Shooting Brake", "Mercedes CLS", "Mercedes E-Klasse", "Mercedes G-Klasse", "Mercedes GL", "Mercedes GLA", "Mercedes GLC", "Mercedes GLE", "Mercedes GLK", "Mercedes GLS", "Mercedes M-Klasse", "Mercedes R-Klasse", "Mercedes S-Klasse", "Mercedes SL", "Mercedes SLC", "Mercedes SLK", "Mercedes SLS AMG", "Mercedes Sprinter", "Mercedes V-Klasse", "Mercedes Viano", "Mercedes Vito", "Mercedes-AMG GT", "Mercedes CE-Klasse","Mercedes 190",  "Mercedes CLK 500", "Mercedes-Maybach S-Klasse (X222)", "Mercedes CLS (C218)", "Mercedes Clc", "Mercedes R-Klasse", "Mercedes SLC / SLK", "Mercedes SLR", "Mercedes GLS (X166)",  "Mercedes GLS / GL", "Mercedes CLK 240", "Mercedes SLS AMG", "Mercedes-AMG CLS (C218/X218)", "Mercedes CLC 200", "Mercedes-AMG C-Klasse (W205/S205/C205/A205)", "Coupé Clc Sport", "Mercedes Clk", "Jaguar S-Type 1966", "Mercedes SL (R231)", "Mercedes SLC (R172)", " Gl 1500", "Mercedes ML 420", "Mercedes S-Klasse (W222)", "Mercedes CLC 350", "2005 Clk Amg", "Mercedes R 63 AMG", "Honda R 1", "Mercedes S-Klasse Cabriolet (A217)", "Mercedes GLK 280", "Mercedes E-Klasse", "2011 Cl Amg", "Fiat A 16", "Mercedes A-Klasse (W176)", "Mercedes GLK 350", "Mercedes B 170", "Mercedes GLC", "Ford B-Max", "Mercedes Amg", "Mercedes B-Klasse", "Mercedes A 150", "Mercedes A 170", "Mercedes A-Klasse", "Ford C-Max 2004", "Mercedes C 55 AMG", "Mercedes B-Klasse (W246)", "Mercedes ML 320", "Mercedes CLK 270", "Chevrolet G Tempomat", "Mercedes S-Klasse", "Mercedes G-Klasse", "Mercedes GLK 250", "Mercedes CL 500", "Mercedes R 280", "Mercedes R 320", "Mercedes CLC 180", "Mercedes SL", "Mercedes R 500", "Mercedes S 430", "Mercedes V-Klasse", "Mercedes CL 600", "Mercedes Vito", "Mercedes Vito", "Mercedes CLC 220", "Mercedes SLK 200", "Mercedes 190 Sl", "Mercedes CLS", "Mercedes Sprinter", "Mercedes CL-Klasse", "Mercedes Vaneo", "Mercedes ML 280", "Mercedes CLK 320", "Mercedes G-Klasse (W463)", "Mercedes CLK 280", "Mercedes CLK 220", "Mercedes SL 280", "Mercedes GLK 220", "Mercedes 350", "2005 Slk 55","BMW X6", "Mercedes C-Klasse", "Mercedes 300", "Saab 95", "Rover V6", "Saab 92", "Mercedes 220", "Mercedes 380 Sec", "Mercedes-AMG GT", "Mercedes Pullmann", "Mercedes Citan", "Mercedes ML 63 AMG", "Mercedes CLA / CLA Shooting Brake", "Mercedes 500 Sec", "Mercedes Youngtimer", "Mercedes GLC (X253)",  "Mercedes 240", "Mercedes 123", "Mercedes CLK 350", "Mercedes Citan Tourer", "Mercedes Viano", "Mercedes GLK 320", "Mercedes R 350", "Mercedes CL 63 AMG", "Mercedes M Klasse", "Mercedes ML 350", "Mercedes CLK 200", "Mercedes 600 Sec ",  "ford ka royal","Ford Focus Kombi ", "Ford 2008", "Volkswagen Cabrio", "Volkswagen Golf", "Volkswagen Polo ", "VW Amarok", "VW Beetle", "VW Bus / Transporter", "VW Caddy", "VW CC / Arteon", "VW Crafter", "VW e-up!", "VW Eos", "VW Fox", "VW Golf", "VW Jetta", "VW Lupo", "VW Passat", "VW Phaeton", "VW Polo", "VW Scirocco", "VW Sharan", "VW T-Roc", "VW Tiguan", "VW Touareg", "VW Touran", "VW up!", "Volkswagen Phaeton", "Volkswagen Eos", "Volkswagen Bora", "VW Golf 6 Cabriolet", "VW Jetta", "Volkswagen Passat CC", "VW Passat", "VW Polo", "VW Tiguan", "Bugatti", "Volkswagen Fox", "VW Golf 7 GTI", "Volkswagen Vento",         "Volkswagen Corrado",  "VW Amarok", "Volkswagen Crafter", "VW Golf", "Volkswagen Lupo", "Volkswagen Atlas", "Volkswagen Käfer", "VW Bus / Transporter", "Volkswagen Golf Plus", "Volkswagen Iltis", "Volkswagen LT 1", "Volkswagen Cross", "Volkswagen Karmann Ghia", "Volkswagen LT 2", "Volkswagen T1", "VW Beetle", "VW T6 Transporter", "Volkswagen Santana", "Volkswagen T2", "Volkswagen XL1", "Volkswagen Taigun", "VW up!", "Volkswagen T3", "Volkswagen Taro", "VW Passat Limousine (B8)", "Volkswagen T4 Multivan", "VW Touareg 2 (7P/7PH)", "VW Touran", "VW Polo (6R/6C)",  "Volkswagen T4 Caravelle", "Volkswagen T5 Dpf", "Skoda Octavia",  "Volkswagen T4 Dpf", "VW Sharan 2 (7N)", "Volkswagen Bora 1.6", "Volkswagen Corrado 16v", "VW Crafter", "VW Caddy", "VW T5 Multivan", "VW Scirocco (Typ 13)", "VW T5 Caravelle", "VW CC / Arteon", "Volkswagen Eos 2006", "Volkswagen Phaeton 2003", "VW Scirocco", "Volkswagen Vento ", "VW Touran 2 (5T)", "VW Sharan", "VW Touareg ", "Ford B-Max", "Ford C-Max", "Ford Ecosport", "Ford Edge", "Ford Fiesta", "Ford Focus", "Ford Fusion", "Ford Galaxy", "Ford Ka / Ka+", "Ford Kuga", "Ford Mondeo", "Ford Mustang", "Ford Ranger", "Ford S-Max", "Ford Tourneo Connect", "Ford Tourneo Courier", "Ford Tourneo Custom", "Ford Transit",  "Ford Taunus", "Ford Transit", "Ford Fusion", "Ford Puma", "Ford Focus", "Ford Fiesta", "Ford Mondeo", "Ford Capri", "Ford Escort", "Ford Cougar","Ford Flex", "Ford B-Max", "Ford Edge (CD539X)", "Ford Courier", "Ford Excursion", "Ford Explorer", "Ford Nugget", "Ford Ranger", "Ford Granada", "Ford C-Max / Grand C-Max", "Ford Sierra", "Ford Scorpio", "Ford Escape", "Ford Express", "Ford Expedition", "Ford B-Max", "Ford Orion", "Ford Tourneo Courier (JU2)", "Ford Thunderbird", "Ford Probe", "Ford Tourneo", "Ford Galaxy", "Ford Focus Schrägheck (Mk3)", "Ford F 150", "Ford Transit Connect", "Ford Windstar", "Ford Maverick", "Ford Kuga", "Ford Galaxy (WA6)", "Ford Transit 100", "Ford Windstar 1996", "Mercedes G-Klasse", "BMW 3er", "Ford Ka / Ka+",  "Opel Zafira / Zafira Tourer", "Ford Tourneo Connect", "Ford Mondeo Limousine (Mk5/BA7)", "Ford Escort 1.6", "Ford S-Max (WA6)", "Ford C-Max", "Ford Tourneo Connect (PJ2)", "Ford Transit", "Ford Cougar 1998", "Ford Courier 1996", "Ford S-Max", "Chevrolet Express Van 1997", "Ford Maverick 2001", "GMC Sierra 1500", "Ford Scorpio 1995", "Ford Focus Turnier (Mk3)", "Ford Fiesta Dreitürer (Mk7: JA8)", "Ford Puma 1.4", "Ford Probe 1991", "Ford Mondeo Turnier (4. Gen./BA7)", "Opel Meriva Opc", "Chevrolet Orlando", "Ford Fiesta Fünftürer (MK7/JA8)", "Mitsubishi Pajero", "Citroën C3 Picasso (SH)", "VW Sharan ", "Opel Adam", "Opel Ampera", "Opel Ampera-e", "Opel Astra", "Opel Cascada", "Opel Combo", "Opel Corsa", "Opel Crossland X", "Opel Grandland X", "Opel Insignia", "Opel Karl", "Opel Meriva", "Opel Mokka / Mokka X", "Opel Movano", "Opel Signum", "Opel Vivaro", "Opel Zafira", "Opel Zafira Tourer",  "Opel Kadett", "Opel Ascona", "Opel Omega", "Opel Vectra", "Renault Megane", "Opel Tigra", "Opel Agila", "Opel Movano", "Opel Antara", "Opel Signum", "Opel Calibra", "Opel Olympia", "Opel Senator", "Opel Manta", "Opel Campo", "Opel Combo", "Opel Diplomat", "Opel Meriva", "Opel Vivaro", "Chevrolet Corvette", "Opel Kadett 1970", "Opel Monterey", "Opel Rekord", "Opel GTC (Astra J)", "Opel Sintra", "Opel Ascona A", "Opel Monza", "Opel Commodore", "Opel Corsa", "Opel Speedster", "Opel Astra", "Opel Frontera", "Opel Agila ",   "Opel Movano Van", "Opel Calibra ", "Opel Omega A", "Opel Omega 1995", "Opel Combo (D)", "Opel Movano", "Opel Frontera 2.2", "Opel Zafira / Zafira Tourer", "Opel GT Roadster", "Opel Senator 24v", "Opel Sintra 16v", "Opel Vectra 1.6", "Opel Speedster 2.0", "Opel Insignia", "Opel Adam (A)", "Opel Tigra Twin Top", "Opel Cascada", "Opel Mokka X (J-A)", "Opel Meriva (B)"]

				
##        System.setProperty("webdriver.chrome.driver","G:\\chromedriver.exe");
#######################customize this are depending on computer##############
downloadPath="/media/hdd1/tools/carProject/carpictures/"
driverPath="/media/hdd1/tools/carProject/chromedriver"
projectFolder="/media/hdd1/tools/carProject/"
#############################################################################	



##HELPER FUNCTIONS
#**************************************************************************************************************************************************
#image downloader#######################################################################

def getModels():
    global models
    asstring=""
    with open(projectFolder+"models.txt","r") as m:
        asstring=m.read()
    #print(asstring)
    models=asstring.split(",")




def stripUrls(listings):
    ids=[]
    for i in listings:
        if "?id=" in i:
            #if id is in url cut it and save it in list ids
            ids.append(i[51:60])
        else:
            listings.remove(i)
            
    return ids,listings
    

def getBlacklist():
    if os.path.isfile(projectFolder+'blacklist.txt'):
        global blacklist
        file=open(projectFolder+"blacklist.txt","r")
        alllines=file.readlines()
        for i in alllines:	
            blacklist.append(i)


def setBlacklist(ids):
    global blacklist
    #f=open("blacklist.txt","w")
    for i in ids:
        blacklist.append(i)
        with open(projectFolder+"blacklist.txt", "a") as myfile:
            myfile.write("\n")
            myfile.write(i)

def checkBlacklist(prelistings):
    global blacklist
    #set ids to ids of urls and listings to urls without "special litstings without ids"
    ids,listings=stripUrls(prelistings)
    setBlacklist(ids)
    print("number of listings before blacklist",len(listings))
    #check for every listening if its a "normal" listing with id in url
    for i in blacklist:
        #print("blacklist",i)
        #print("url",listings[1])
        
        #check for every id saved in blacklist if its in the list of ids
        #if the case the listing has already been visited because ids are unique
        if i in ids:
             print("Listing already visited")
             print("id=",i)
             for x in listings:
                 if i in x:
                     print("listings",x)
                     listings.remove(x)
    print("number of listings after blacklist",len(listings))
    sleep(30)
    return listings



def getsizes(uri):
    # get file size *and* image size (None if not known)
    file = urllib.urlopen(uri)
    size = file.headers.get("content-length")
    if size: 
        size = int(size)
    p = ImageFile.Parser()
    while True:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size, p.image.size
            break
    file.close()
    return(size, None)






##def deleteImages(path):
##    if os.path.exists(path):
##        im = Image.open(path)
##        width, height = im.size
##        im.close()
##        if im is not None and ((width<300) or (height<300)):
##            print("last image removed because too small")
##            os.remove(path)






    








def downloadImages(images,model,driver):
    for image in images:
        print(image.get_attribute("src"))
        # next 2 ifs check if image is really downloadable
        #try:
        if(True):
            if image.get_attribute("src") is not None:
                imageInfo=getsizes(image.get_attribute("src"))
                if len(imageInfo)>1:
                    #checks if dimensions of image are larger than 300x300
                    if (imageInfo[1][0]>300) and (imageInfo[1][1]>300):
                        modelpath=downloadPath+model.replace(" ", "")
                        #creates directory if not already there
                        if not os.path.exists(modelpath):
                            print("creating directory"+modelpath)
                            os.makedirs(modelpath)
                        path=modelpath+"/img"+str(countImages())+".jpg"
                        
                        print(image.get_attribute("src"))
                        #remove all images without link to src
                        if image.get_attribute("src"):
                            #remove all corrupted or unreadable links with e.g "data" 
                            if "http" in image.get_attribute("src"):
                                save_image(driver,image.get_attribute("src"),path)
                                #delete images that are too small -> deprecated because image size is cchecked before download in getsizes
                                #deleteImages(path)
                                sleep(0.5)
        #except:
            #print("Element is no longer attached to page so aborting download and trying different ad")
            
    #sleep(2)
    

def save_image(driver, img_url,path):
    
    with open(path, "wb") as handle:
        try:
            response = requests.get(img_url, stream=True)
        except ConnectionError as e:    # This is the correct syntax
            print(e)
            response = "No response"
        
        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)



#total number of images downloaded  -> calculates Filenames
def countImages():
    global totalnumber
    totalnumber=totalnumber+1
    if totalnumber%100==0:
	f=open(projectFolder+"imagecounter.txt","w")
	f.write(str(totalnumber))
    return totalnumber

def setCounter(counter):
    global totalnumber
    totalnumber=counter
    return totalnumber




def formatTitle(title):
    title=title.lower()
    title=title.replace(" ","")
    if "benz" in title:
        title=title.replace("benz","")
    if "-" in title:
        title=title.replace("-"," ")
    if "volkswagen" in title:
        title=title.replace("volkswagen","vw")
#####COMMENTED OUT BECAUSE RASPBERY CANT DECODE  OE as german utf 8 character  
 # if "citr n" in title:
    #    title=title.replace("citr n","citroen")
    return title
########################################################################################


#alle links speichern die auf eine anzeige zeigen
def setListings(driver):
    #dieser link ist in jedem link der auf eine anzeige zeigt vorhanden, daher werden diese herausgefiltert
    sleep(3)
    listings=[]
    prelistings=driver.find_elements_by_xpath("//*[contains(@href, 'https://suchen.mobile.de/fahrzeuge/details.html')]")
    for i in prelistings:
        listings.append(str(i.get_attribute("href"))+"\n") #do i need \n???????????????????????

    listings=checkBlacklist(listings)
    return listings


   

#get all listings of one page 
def pageListings(links,driver):
    model=""
    print("number of listings on current page",len(links))
    
    for i in range(len(links)):
        #currentlisting=driver.find_element_by_xpath(listings[i])
       # driver.execute_script("arguments[0].scrollIntoView();", currentlisting)
        currentlisting=links[i]
        #driver.execute_script("arguments[0].scrollIntoView();", currentlisting)
        ############################################################
        #catch connection aborted error of driver.get
        try:
            driver.get(currentlisting)
        except requests.exceptions.ConnectionError as e:
            pass
        except Exception as e:
            randomtime = random.randint(1,5)
            time.sleep(randomtime)
            continue
        
        #sleep(2)
        #driver.find_element_by_xpath("//span[@class="image-enlarge-display u-text-white u-pull-right"]").click()
        #images= driver.find_elements_by_xpath("//img[@class="cycle-slide"]")
        
        # need to remove benz and - and volkswagen to vw
        
        images = driver.find_elements_by_tag_name("img") #get all immages of page     ->> remove bad images
        #get model name by copying title of listing
        title=driver.find_element_by_id("rbt-ad-title").get_attribute("textContent")
        #remove whitespaces and transform to lower case Ich bin cool--> ichbincool
        print("titel der anzeige: "+title)
        title=formatTitle(title)
        print("edited title",title)
        
        
        modelsInTitle=[]
        for i in models:
            #strip whitespaces and transform to lowercase to compare the title of ad to list of saved carmodels
            i=i.lower()
            i=i.replace(" ","")
	    i.decode('latin1').encode('utf-8')
            if i in title.decode('latin1').encode('utf-8'):
		 #append possible match 
                modelsInTitle.append(i)
        print(modelsInTitle,"all possible model matches based on title")
        #decide wich of the possible matches is closest to adtitille
        mostSimilarModels=difflib.get_close_matches(title,modelsInTitle,cutoff=0.2)
        #ignore ad if no matching model found
        if(len(mostSimilarModels)>0):
            model=mostSimilarModels[0]
            print("erkanntes model: "+model)
            print("Number of available pictures",len(images))
            downloadImages(images,model,driver)
        #if no match found create/add txt datei mit titel der anzeige zum debuggen des problems/ hinzufügen des models
        else:
            with open(projectFolder+"noMatches.txt", "a") as f:
                f.write("\n"+ title)
            
        driver.get("https://suchen.mobile.de/fahrzeuge/search.html?dam=0&isSearchRequest=true&sfmr=false&vc=Car")
        sleep(2)
        


def getNumberOfPages(driver):
    #scroll to "nächste seite" button next to number of pages
    nextPage=driver.find_element_by_xpath("//*[@title='Zur nächsten Seite']")
    actions = ActionChains(driver)
   # actions.move_to_element(nextPage).perform()
    pagenumbers=driver.find_elements_by_xpath("//*[contains(@title,'Gehe zu Seite ')]")
    numbers=[]
    for i in pagenumbers:
        fracture= i.get_attribute("title").split() #split Description of button that points to different pages at whitespaces -> element that points to highest page number is total number of pages
        number=int(fracture[len(fracture)-1]) #get Number of pages by selecting last element
        #get the page number auf die das jeweilige WebElement zeigt und füge sie der Liste hinzu
        numbers.append(number)
        #die höchste nummer dieser liste ist die gesamtanzahl der gefundenen Seiten
    numberOfPages=max(numbers)
    print("number of pages",numberOfPages)
    return numberOfPages




        
    
def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
   # counter=0
    getBlacklist()
    if os.path.isfile(projectFolder+'imagecounter.txt'):
	f=open(projectFolder+"imagecounter.txt")
	counter=f.read()
	print("start naming images at: ",counter)
	setCounter(int(counter))
    getModels()
    options = Options()
    options.headless = True
    # driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver') #driverPath
    driver=webdriver.Firefox(options=options,executable_path='/usr/local/bin/geckodriver')
    driver.implicitly_wait(3) #wait 10 seconds when doing a find_element before carrying on
    #display = Display(visible=0, size=(800, 600))
    #display.start()
    print("saving pid")
    pid=str(os.getpid())
    f=open(projectFolder+"pid.txt","w")
    f.write(pid)
    f.close()
    driver.get("https://suchen.mobile.de/fahrzeuge/search.html?dam=0&isSearchRequest=true&sfmr=false&vc=Car")
    sleep(0.5)
    listings=setListings(driver)
    cookie="/html/body/div/div[1]/div[2]/div[2]/div"
    
    
    numberOfPages=getNumberOfPages(driver)
    #show all 1.6M results for cars
    

        
    for i in range(numberOfPages):
        driver.get("https://suchen.mobile.de/fahrzeuge/search.html?damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&pageNumber="+str(i)+"&scopeId=C")
        sleep(1)
        listings=setListings(driver)
        pageListings(listings,driver)
    
    sleep(2)
main()
            
            

#need to check if there are multiple hits with title of listing
# ---> golf und golf V könnte zu problemen führen

#mercedes-benz vs mercedes benz oder mercedes ist unterschiedlich

#removed benz
       
             
#bmw 3er vs 318d
#vw oder volkswagen

#citrön
#maybe instead of instant download first gather multiple arrays with links to images -> every array is one model
#need to desperately work on efficiency


##SORT MODEL FILE ALPHABETICLY
