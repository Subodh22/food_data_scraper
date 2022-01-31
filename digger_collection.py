##this digs all the recipes collection

from os import name
import requests
import json
 
 

 
 



def write_json(new_data,filename):
   
    with open("recipes_master/"+filename,"a") as file : 
        file.write(new_data+'\n')
 




def collection_digger(collection_name):
    m=""
    for i in range(1,10):
        url="https://www.bbcgoodfood.com/api/lists/posts/list/"+str(collection_name)+"/items?page="+str(i)
        
        response = requests.get(url)
        if(response.status_code!=200):
            break
         
        rubish_recipe =    json.dumps(response.json()["items"])
        
        rubish_recipe = rubish_recipe[1:-1] 
        print(rubish_recipe)
        if(i==1):
            m=rubish_recipe
        else:
            m=m+","+rubish_recipe
    
       
    m =  '{"items":['+m+']}'
    
    json_name=collection_name+".json"
 
    write_json(m,json_name)

def name_cleaner(x):
    x=x.lower()
    x=x.replace("'","")
    x=x.replace(" ","-")
    return x
collection_digger("quick-veggie-recipes")
def collection_selector():
    with open('jj.json') as g:
        p=json.load(g)
        
        for i in range(len(p["collections"])):
            urls=name_cleaner(p["collections"][i]["title"])
            collection_digger(urls)
            
            

     
# collection_selector()