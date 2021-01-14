 DiGraph
 ======

 this project represents an infrastructure of 
 algorithms for creating of directional weighted positive graph 
* implement on Python, base on NetworkX library

 ## node_data 
 This class represents the set of operations applicable on a 
 vertex in a directed weighted positive graph.
 * every node contain: unique key, tag, weight, location point on the graph and info
 
 ## DiGraph
 This class represents a directed weighted positive graph. 
 * the graph's nodes saved in dictionary
 * Contains a dictionary of all the nodes connected from
 * Contains a dictionary of all the nodes connected to.

 ## GraphAlgo
 This interface represents a Directed Positive Weighted Graph Theory algorithms including:
 0. init(graph)
 1. shortestPath
 2. Save as json file 
 3. Load from json file
 4. Connected Components 
 5. plot graph 
 6. algorithms: DFS, Dijkstra
 
 ## Save as json file  
 * Let's save the graph we are working on as json file.
 * usually the graph will be saved in the data package in our project 
   
 ## Load from json file
 * Let's create a new graph from a json file.
  
 ## Connected Components
 - Create an empty stack S’ and do DFS traversal of a graph. 
 - In DFS traversal,after calling DFS for adjacent vertices of a vertex, push the vertex to stack.
 - reverse the insertions direction in the stack 
 - Reverse directions of all arcs to obtain the transpose graph.
 - One by one pop a vertex from S while S is not empty.
 - activate DFS on the transpose graph 
 * Complexity:  
    * takes O(|V| + |E|) for a graph represented using adjacency list.
    * Reversing a graph also takes O(|V| + |E|) time. 
    * For reversing the graph, we simple traverse all adjacency lists.

 ## Connected Component
 * Finds the Strongly Connected Component(SCC) that node id is a part of.
 * Complexity: O(|V|+|E|) + O(|V|) = O(|V|+|E|)
 * running Connected Components and return list that contain given node id
  
 ## The Shortest Path
* Returns the length of the shortest path between src to dest, and the shortest path between src to dest 
   as an ordered List of nodes: src--> n1--> n2--> ... -> dest 
* using Dijkstra algorithm we find the distance of the shortest path to each vertex from the source vertex 
   then return the distance of the target vertex.
 * base on the dijkstra result we will set the new vertices weights, 
   and For each vertex we will select the neighbor with the lowest 
   weight and thus we will create the cheapest route
 * Complexity: O(|E|log|V| + |V|) in worst case performance
 * running Dijkstra and then start pass from the src node, in every iteration we select the 
 node with the minimal distance and move to it until we reach the destination vertex.
   
## Plot Graph
* Draws the graph we are working on beautifully
* If the nodes have a position, the nodes will be placed there, 
  Otherwise, they will be placed in a random but elegant manner.
* Base on Matplotlib library
 
 ## DFS Algorithm
 * an algorithm for traversing or searching tree or graph data structures.
 - Created a stack of nodes and visited array.
 - Insert the root in the stack.
 - Run a loop till the stack is not empty.
 - Pop the element from the stack and print the element.
 - For every adjacent and unvisited node of current node, mark the node and insert it in the stack.
 * Complexity: O(|V| + |E|) in the worst case

  ## Dijkstra Algorithm
  * A famous algorithm for finding the shortest paths in a weighted positive graph.
  * Put the given vertex in the priority queue,
      priority queue sort the vertices by they tags value, 
      for each vertex we sum the current vertex's tag with his connected edge's weight, 
      each time we poll vertex with the minimal value in the priority queue 
      we go over all its neighbors, select the neighbor with the minimal value and put it in the priority queue
      mark all the vertex we passed,
      if there is a path with a minimal weight we will discover it and select this path
      each vertex we finished passing out of the priority queue
  * Complexity: O(|E|log|V| + |V|)
  
  Runtime Comparations
====================
## Graph no pos 

| G_10_80_0            | Python | java | NetworkX |
| :--------- | ----------: | :----------: | :----------: |
| shortest path        | 0.0001 | 5 | 2.656 |
| connected component  | 6.994 | 51 | 9.201 |
| connected components | 7.7201 | 48 | 9.201 |
| G_100_800_0 
| shortest path        | 0.0025| 4 | 4.9723|
| connected component  | 0.00071 | 48 | 1.5484 |
| connected components | 0.00076 | 32 | 1.5484 |
| G_1000_8000_0       
| shortest path        | 0.08245 | 10 | 7.9673 |
| connected component  | 0.0039 | 75 | 6.8919 |
| connected components | 0.003738 | 73 | 6.8919 |
| G_10000_80000_0      
| shortest path        | 7.64449 | 58 | 0.00012 |
| connected component  | 0.0573	| 193 | 1.0853 | 
| connected components | 0.05754| 189	| 1.0853 | 
| G_20000_160000_0     
| shortest path | 32.259799	| 56	| 0.0002812 |
| connected component 	| 0.1195588	| 188	| 1.3542 |
| connected components	| 0.1076574	| 182	|1.3542|
| G_30000_240000_0     
|shortest path 	|93.2501444	|79	|0.00025468	|
|connected component 	|0.181145047	|255	|1.389299723	|
|connected components	|0.18190369	|274	|1.389299723	|

## Graph on circle 

| G_10_80_1 | Python | java | NetworkX |
| :--------- | ----------: | :----------: | :----------: |		
|shortest path 	|7.08282	|6	|1.487059|
|connected component| 	3.84071	|44	|9.3060007|
|connected components	|4.3028001	|43	|9.3060007|
|G_100_800_1			
|shortest path 	|0.001246	|4	|2.55473|
|connected component 	|0.0003487	|37	|8.44399|
|connected components	|0.0003899	|34	|8.44399|
|G_1000_8000_1			
|shortest path 	|0.08029	|10	|5.7134|
|connected component 	|0.003356229	|72	|6.602000212|
|connected components	|0.00363	|63	|6.602000212|
|G_10000_80000_1			
|shortest path 	|7.3867	|46	|0.00014271|
|connected component 	|0.0472731	|166	|1.11510016|
|connected components	|0.0447415	|158	|1.11510016|
|G_20000_160000_1			
|shortest path 	|30.66032524	|41	|0.00024091|
|connected component 	|0.1211118	|191	|1.5159999|
|connected components	|0.1095079	|181	|1.5159999|
|G_30000_240000_1			
|shortest path 	|90.6683008	|55	|0.0002582|
|connected component 	|0.180592	|277	|0.181647052|
|connected components	|0.181647052	|263	|0.181647052 |
 
 ## How to run 
 * Click the green Clone or Download button on the right. 
 * Click the Download ZIP button. 
 * Open the project on your computer 
 * run tests classes on MyTest folder

 ## Sources
- https://www.geeksforgeeks.org/strongly-connected-components/
- https://www.geeksforgeeks.org/iterative-depth-first-traversal/


