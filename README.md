# python-data-structures
Sample work from Udacity's Data Structures &amp; Algorithms NanoDegree

# active_directory.py
See if a user exists in a group. A group may contain one or more group(s). I use a function to search a group for users. If there is a group within a group, I recursively call the function again to ssearch that group for users. 

Time complexity: O(n^2) because the is both a possible recursive call and a for loop nested in another for loop. 

Space Complexity: O(n)

# blockchain.py
Create a Blockchain as a linked list where each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. I also use a next pointer for each block in order to append and print the list. 

Time complexity: O(n) for print() because the method starts at the head and traverses the size of the linked list. O(1) for append because I use a tail pointer to add a new block to the end of the blockchain.

Space Complexity: O(n)

# file_recursion.py

# huffman_coding.py

# lru_cache.py

# union_and_intersection.py
            
