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
queue=[]
print("The Path is :")
def bfs(node,visited,graph):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m)
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)  
bfs("Kudal",visited,graph)
