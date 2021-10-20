import os
import sys

###############################################


top_dir = os.path.abspath('generated/Mercedes')
files = os.listdir( top_dir )

for index,item in enumerate(files):
    if os.path.isdir( os.path.join(top_dir,item) ):
       files.pop(index)

files.sort()

duplicates = []
last_index = None
for index,item in enumerate(files):

    last_index = index
    extension = ""
    if '.' in item:
        extension = '.' + item.split('.')[-1]
    old_file = os.path.join(top_dir,item)
    new_file = os.path.join(top_dir,'mercedes' + str(index) + extension  )
    while os.path.isfile(new_file):
          last_index += 1
          new_file = os.path.join(top_dir,str(last_index) + extension  )
    print( old_file + ' renamed to ' + new_file ) 
    os.rename(old_file,new_file)

###############################################
    

top_dir = os.path.abspath('generated/BMW')
files = os.listdir( top_dir )

for index,item in enumerate(files):
    if os.path.isdir( os.path.join(top_dir,item) ):
       files.pop(index)

files.sort()

duplicates = []
last_index = None
for index,item in enumerate(files):

    last_index = index
    extension = ""
    if '.' in item:
        extension = '.' + item.split('.')[-1]
    old_file = os.path.join(top_dir,item)
    new_file = os.path.join(top_dir,'bmw' + str(index) + extension  )
    while os.path.isfile(new_file):
          last_index += 1
          new_file = os.path.join(top_dir,str(last_index) + extension  )
    print( old_file + ' renamed to ' + new_file ) 
    os.rename(old_file,new_file)

###############################################


top_dir = os.path.abspath('generated/Audi')
files = os.listdir( top_dir )

for index,item in enumerate(files):
    if os.path.isdir( os.path.join(top_dir,item) ):
       files.pop(index)

files.sort()

duplicates = []
last_index = None
for index,item in enumerate(files):

    last_index = index
    extension = ""
    if '.' in item:
        extension = '.' + item.split('.')[-1]
    old_file = os.path.join(top_dir,item)
    new_file = os.path.join(top_dir,'audi' + str(index) + extension  )
    while os.path.isfile(new_file):
          last_index += 1
          new_file = os.path.join(top_dir,str(last_index) + extension  )
    print( old_file + ' renamed to ' + new_file ) 
    os.rename(old_file,new_file)
