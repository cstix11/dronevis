import os
import random
import shutil


dogdir = 'C:/Users/sherlc/Documents/Coding/TensorFlow/workspace/dronevis/images/dogs'
imgdir = 'C:/Users/sherlc/Documents/Coding/TensorFlow/workspace/dronevis/images'

i = 1  # Image index storage
sample = random.sample(os.listdir(dogdir), 250)
for name in sample:
    shutil.move(dogdir+'/'+name, imgdir+'/'+name)
    os.rename(imgdir+'/'+name, imgdir+'/dog'+str(i)+'.jpg')
    i += 1

civ_vehicle = []
heli = []
military_vehicle = []
person = []
police_vehicle = []

for img in os.listdir(imgdir+'/all'):
    prefix = img[:4]
    if prefix == 'civ_':
        civ_vehicle.append(img)
    elif prefix == 'heli':
        heli.append(img)
    elif prefix == 'mili':
        military_vehicle.append(img)
    elif prefix == 'pers':
        person.append(img)
    elif prefix == 'poli':
        person.append(img)

c = 1
for civ in civ_vehicle:
    shutil.move(imgdir+'/all/'+civ, imgdir+'/'+civ)
    os.rename(imgdir+'/'+civ, imgdir+'/civ_vehicle'+str(c)+'.png')
    c += 1

h = 1
for hel in heli:
    shutil.move(imgdir+'/all/'+hel, imgdir+'/'+hel)
    os.rename(imgdir + '/' + hel, imgdir + '/heli' + str(h) + '.png')
    h += 1

m = 1
for mil in military_vehicle:
    shutil.move(imgdir+'/all/'+mil, imgdir+'/'+mil)
    os.rename(imgdir + '/' + mil, imgdir + '/military_vehicle' + str(m) + '.png')
    m += 1

p = 1
for per in person:
    shutil.move(imgdir+'/all/'+per, imgdir+'/'+per)
    os.rename(imgdir + '/' + per, imgdir + '/person' + str(p) + '.png')
    p += 1

po = 1
for pol in police_vehicle:
    shutil.move(imgdir+'/all/'+pol, imgdir+'/'+pol)
    os.rename(imgdir + '/' + pol, imgdir + '/police_vehicle' + str(po) + '.png')
    po += 1

