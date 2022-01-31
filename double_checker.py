import concurrent.futures
import json
import os


j = []
def double_checking(collection_name):
    with open('recipes_master/'+collection_name) as f:
        k=json.load(f)
        j=k['items']
        print(collection_name+","+str(len(j)))
        

files = os.listdir("recipes_master")
for file in files:
    double_checking(file)


#beetroot-recipes


# def writer():

 

