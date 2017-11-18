// A linked list is said to contain a cycle if any node is visited more than once while traversing the list.

// Complete the function provided in the editor below. It has one parameter: a pointer to a Node object named that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a cycle in the list. If there is a cycle, return true; otherwise, return false.

// Note: If the list is empty,  will be null.

// Input Format

// Our hidden code checker passes the appropriate argument to your function. You are not responsible for reading any input from stdin.

// Output Format

// If the list contains a cycle, your function must return true. If the list does not contain a cycle, it must return false. The binary integer corresponding to the boolean value returned by your function is printed to stdout by our hidden code checker.

/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    // Complete this function
    // Do not write the main method
    Node* tortoise = head;
    Node* hare = head;
    while(hare !=NULL && hare->next !=NULL){
        tortoise = tortoise->next;
        hare = hare->next->next;
        if(tortoise == hare){
            return true;
        }
    }
    return false;
}
