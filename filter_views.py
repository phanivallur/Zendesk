import sys
import json
import os
import AgentViews

i=0;
agents=[]

def createViewObject(input_json_data):
    x=AgentViews.ZDView()
    x.setRawTitle(input_json_data["raw_title"])
    x.setRestriction(input_json_data["restriction"])
    x.setDescription(input_json_data["description"])
    x.setTitle(input_json_data["title"])
    x.setUrl(input_json_data["url"])
    x.setHighlights(input_json_data["highlights"])
    x.setCreatedAt(input_json_data["created_at"])
    x.setUpdatedAt(input_json_data["updated_at"])
    x.setCountable(input_json_data["countable"])
    x.setActive(input_json_data["active"])
    x.setPosition(input_json_data["position"])
    x.setId(input_json_data["id"])
    
    update_zd_views(x)

    

for file in os.listdir("."):
    if file.endswith(".json"):
       agents.append(os.path.splitext(os.path.basename(file))[0])

for agent in agents:
    i=i+1
    with open(agent+".json") as file:
         agent_json_data=json.load(file)
    print(str(i)+"Data for agent: "+agent)
    for i in range(len(agent_json_data["views"])):
        if agent=='Phani':
           if str(agent_json_data["views"][i]["active"])=="True" and str(agent_json_data["views"][i]["raw_title"])=="Phani":
              #for key in agent_json_data["views"][i].keys():
                 # print(str(key))+" : "+str(agent_json_data["views"][i][key])
              createViewObject(agent_json_data["views"][i])
        else:
            if str(agent_json_data["views"][i]["active"])=="True":
               #for key in agent_json_data["views"][i].keys():
                   #print(str(key)+" : "+str(agent_json_data["views"][i][key]))
               createViewObject(agent_json_data["views"][i]])
    print("\n")

#print(agents)









"""with open('/var/tmp/Abhinav.json') as file:
     json_data=json.load(file)

for i in range(len(json_data["views"])):
    if str(json_data["views"][i]["active"])=="True":
       for key in json_data["views"][i].keys():
           print(str(key)+" : "+str(json_data["views"][i][key]))"""



