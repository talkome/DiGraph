 DiGraph
 ======

 this project represents an infrastructure of 
 algorithms for creating of directional weighted positive graph 
* implement Python, base on NetworkX library

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
 - Create an empty stack S’ and do DFS traversal of a graph. In DFS traversal,
 - after calling DFS for adjacent vertices of a vertex, 
 - push the vertex to stack.
 - Reverse directions of all arcs to obtain the transpose graph.
 - One by one pop a vertex from S while S is not empty.
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
 * Complexity: O(|V|+|E|) + O(|V|) = O(|V|+|E|)
 * running BFS and then start pass from the src node, in every iteration we select the 
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
 
 ## How to run 
 * Click the green Clone or Download button on the right. 
 * Click the Download ZIP button. 
 * Open the project on your computer 
 * run tests classes on MyTest folder

 ## Sources
- https://www.geeksforgeeks.org/strongly-connected-components/
- https://www.geeksforgeeks.org/iterative-depth-first-traversal/


