import pynstagram
import random, os
path = r"/folder/subfolder/with/pics/"
random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
print ("Uploading:")
print(random_filename)

with pynstagram.client('xxx', 'xxx') as client:
    client.upload(path+random_filename, '#bot #bulk #instagram')

print ("Deleting:")
print(random_filename)
os.remove(path+random_filename)
