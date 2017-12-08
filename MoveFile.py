import os
import shutil
import sys

#---
dr = sys.argv[1]; size = sys.argv[2]; subfolder = sys.argv[3]

files = [f for f in os.listdir(dr) if os.path.isfile(dr+"/"+f)]

chunks = [files[i:i + size] for i in range(0, len(files), size)]
for f in chunks[1]:
    shutil.move(dr+"/"+f, subfolder+"/"+f)