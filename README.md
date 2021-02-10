# python-data-structures
Sample work from Udacity's Data Structures &amp; Algorithms NanoDegree

# active_directory.py
See if a user exists in a group. A group may contain one or more group(s). I use a function to search a group for users. If there is a group within a group, I recursively call the function again to ssearch that group for users. 

Time complexity: O(n^2) because the is both a possible recursive call and a for loop nested in another for loop. 

Space Complexity: O(n).

# blockchain.py
Create a Blockchain as a linked list where each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. I also use a next pointer for each block in order to append and print the list. 

Time complexity: O(n) for print() because the method starts at the head and traverses the size of the linked list. O(1) for append because I use a tail pointer to add a new block to the end of the blockchain.

Space Complexity: O(n).

# file_recursion.py
Find all files with a given suffix nested under a directory. I traverse every file / folder in the given directory, and recursively call the find_files function if the "item" (file / folder) being traversed is a folder. 

Time complexity: O(n^2) because the can be a recursive call for every item in the directory.

Space Complexity: O(n).

# huffman_coding.py
Implement the loseless data compression algorithm Huffman Coding. I use a dictionary to store all of the characters and their frequency within a provided sentence. This is done in O(n) time. For the encoding part, I then use a min heap to store the characters and frequencies as nodes (for a tree). By uing a min heap, the sorting of the data occurs in O(nlogn) time. I iterate through all of the characters and their frequencies and create additional nodes that store the values of two min nodes at a time and point to those two nodes. This is done until there is only one node in the min heap, essentially creating a tree. I then create a tree by setting theat one node as the root of the tree. Side note: I created a Breadth First Search (using a queue) to print out the tree but it is not really used in this problem. The BFS would be O(V + E) where V is the number of vertices and E is the number of edges.

I then will traverse that tree to get an encoded value for each character and store that in a new dictionary. This is done using a Depth First Search (using a stack with state). Similiar to the BFS, this is done is O(V + E) time. I then combine those values to the original dictionary, resulting in a character: (frequency, encoded value). These two dictionaries could probably be combined to start with to save space but I would have to go back and make that change. I then take the original sentence and go through the dictionary to build out the encoded string for the sentence. Both steps with the dictionaries are done in O(n) time. 

For the last part of decoding the string, I traverse the tree based on the values of the encoded string. This is done sort of like a DFS but the route is dictated by 0's (left) or 1's (right). The min heap / tree is traversed until a string with the value is reached or there is no more nodes. Once a string is found, the process is repeated from the root. This is done n times with O(V + E) for the search time complexity. This should result in O((V + E) * n). 

Time complexity: O(nlogn). See above. 

Space Complexity: O(n).

# lru_cache.py
A Least Recently Used (LRU) Cache organizes items in order of use, allowing you to quickly identify which item hasn't been used for the longest amount of time. There is a tradeoff of space for time (more space used for quick access and updates). The set method has a time complexity of O(n) because if the cache is full, it will find the LRU item and remove it to make space for the new item. While it can get the item from the linked list in O(1) time, it will iterate through the dictionary to see which item is the LRU item. The get method is O(1) time. All of the methods for the linked list are O(1) (uses tail pointer) except for update and print which are both O(n) time. Update searches for a value in the list (potentially iterates the entire list) and print will iterate through all list nodes.

Time complexity: O(n) for get(), update() and print().

Space Complexity: O(n).

# union_and_intersection.py
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B. Take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. FOr the linked list, the append method takes O(1) time by using a tail pointer. The size and traverse functions both take O(n) time as they start at the head of the list and traverse to the end. The union function will combine all values in two linked lists into a new linked list, which takes O(n) time. The intersection function will find the values that exist in both lists and add to a new linked list, which takes O(n^2) time. FOr every element in one list, it will search through every element in the other list to find common values. 

Time complexity: O(n^2) for the instersection function as described above. 

Space Complexity: O(n).