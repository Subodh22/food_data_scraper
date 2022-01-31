import concurrent.futures 
from recipe_scrapers import scrape_me
import recipe_scrapers
import json

from pathlib import Path
import os


glo_col="" 
    
def name_cleaner(x):
    x=x.lower()
    x=x.replace("'","")
    x=x.replace(" ","-")
    return x

def starter(collection_name):
    e=[]
    j= []
    
    global glo_col
    glo_col=collection_name
    with open('Type_of_food/'+collection_name+".json") as f:
        k=json.load(f)
        for r in range(len(k)):
            j.append(k[r])
            
             
     
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(golden_scrape,j)

    
def golden_scrape(recipe_object):
    yy=recipe_object["title"]
    clean_rec=name_cleaner(yy)
    print(clean_rec)
    scraper = scrape_me('https://www.bbcgoodfood.com/recipes/'+clean_rec+'/')
   
    
    
    recipe_object["act_time"]=scraper.total_time()
    recipe_object["act_yields"]=scraper.yields()
    recipe_object["act_ingredients"]=scraper.ingredients()
    recipe_object["act_instructions"]=scraper.instructions()
    recipe_object["act_image"]=scraper.image()
    
    
    recipe_object["act_nutrients"]=scraper.nutrients()
     
    recipe_saver( recipe_object,yy ,glo_col)
    

def recipe_saver(d,r_name,collection_name):
    print(collection_name)
    Path("type_of_food_recipes/"+collection_name).mkdir(parents=True, exist_ok=True)

    with open("type_of_food_recipes/"+collection_name+"/"+r_name+".json","w") as l:
       json.dump(d,l)

files = os.listdir("Type_of_food")
for file in files:
    u=str(file).split(".")
    u=u[0]
    
    starter(u)