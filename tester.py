import json
l=set((1,3))
p=list([1,3,4])
l.add(tuple(p))
print(l)

j=set([])
with open('Type_of_food/Breakfast.json') as f:
        k=json.load(f)
        for r in range(1):
            
            k[r]["juju"]="dccdc"
            print(k[r]["juju"])
     
            
             