# Study Dijkstra's Algorithm and Practice these questions thoroughly

1. [Find Minimum Time to Reach Last Room I](3341-Find-Minimum-Time-to-Reach–Last-Room-I.py)
   - Basic Dijkstra implementation with single cost per move
   - Uses priority queue (heapq) to find shortest path
   - Time complexity: O(E log V) where E is number of edges and V is number of vertices

2. [Find Minimum Time to Reach Last Room II](3342-Find-Minimum-Time-to-Reach-Last-Room-II.py) 
   - Advanced Dijkstra with alternating move costs (1 and 2)
   - Uses state-based Dijkstra with parity tracking
   - Time complexity: O(2E log V) due to two possible states per vertex
