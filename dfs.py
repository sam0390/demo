import matplotlib.pyplot as plt
import networkx as nx

graph = {"Kudal":["Sawantwadi","Kankavli","Vengurla","Malvan"],
         "Sawantwadi":["Vengurla","Dodamarg","Kudal"],
         "Kankavli":["Malvan","Devgad","Kudal","Vaibhavwadi"],
         "Devgad":["Kankavli","Malvan","Vaibhavwadi"],
         "Malvan":["Kankavli","Kudal","Devgad","Vengurla"],
         "Vengurla":["Sawantwadi","Kudal","Malvan"],
         "Dodamarg":["Sawantwadi"],
         "Vaibhavwadi":["Kankavli"]   }
grp=nx.Graph(graph)
nx.draw(grp,with_labels=True,node_color="white",font_color="black")
plt.show()
visited=[]
print("The Path is :")
def dfs(node,visited,graph):
    if node not in visited: 
        print(node)
        visited.append(node)
        for i in graph[node]:
            dfs(i,visited,graph)
dfs("Kudal",visited,graph)
