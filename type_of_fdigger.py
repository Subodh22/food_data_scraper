##this digs all the recipes collection

from os import name
import requests
import json
 

def write_json(new_data,filename):
   
    with open("Type_of_food/"+filename,"a") as file : 
       json.dump(new_data,file)
 
def collection_digger(collection_name):
    x=str(name_cleaner(collection_name))
    m=""
    limiter=24
    for i in range(1,3):
        if(i==1):
            url="https://search.api.immediate.co.uk/v4/search?search="+x+"&tab=recipes&sort=-relevance&limit="+str(limiter)+"&offset=48&sitekey=bbcgoodfood"
        else:
            
            url="https://search.api.immediate.co.uk/v4/search?search="+x+"&tab=recipes&sort=-relevance&limit="+str(limiter)+"&offset=48&sitekey=bbcgoodfood"
      
        response = requests.get(url)
        if(response.status_code!=200):
            break
        
        
        rubish_recipe =response.json()["data"]["results"] 
        limiter= response.json()["pagination"]["total"]
        rubish_recipe = rubish_recipe[1:-1] 
        # print(rubish_recipe)
        print(i)
        if(i!=1):
            m= rubish_recipe
    
       
    
    
    json_name=collection_name+".json"
 
    write_json(m,json_name)

def name_cleaner(x):
    x=x.lower()
    x=x.replace("'","")
    x=x.replace(" ","-")
    return x
collection_digger("Dinner")

            

     
# collection_selector()