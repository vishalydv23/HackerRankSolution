// For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:

// The  value of every node in a node's left subtree is less than the data value of that node.
// The  value of every node in a node's right subtree is greater than the data value of that node.
// Given the root node of a binary tree, can you determine if it's also a binary search tree?

// Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a 
// boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

// Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.

// Input Format

// You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.




/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may 
want to write one or more helper functions.  

The Node struct is defined as follows:
   struct Node {
      int data;
      Node* left;
      Node* right;
   }
*/
   bool checkBST(Node* root, int minValue, int maxValue){
       if(root == NULL){
           return true;
       }
       if(root -> data < minValue || root -> data > maxValue){
           return false;
       }
       return(checkBST(root -> left, minValue, root -> data -1) && checkBST(root -> right, root -> data + 1, maxValue));
   } 

   bool checkBST(Node* root) {
      return checkBST(root,0,10000);
   }
