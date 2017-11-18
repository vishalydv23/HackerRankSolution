// A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the 
// front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added 
// to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

// A basic queue has the following operations:

// Enqueue: add a new element to the end of the queue.
// Dequeue: remove the element from the front of the queue and return it.
// In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

// 1 x: Enqueue element  into the end of the queue.
// 2: Dequeue the element at the front of the queue.
// 3: Print the element at the front of the queue.
// Input Format

// The first line contains a single integer, , denoting the number of queries. 
// Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. 
// All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , 
// denoting the value to be enqueued.

// Output Format

// For each query of type , print the value of the element at the front of the queue on a new line.

using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    
    public static Stack<int> newOnTop = new Stack<int>();
    public static Stack<int> oldOnTop = new Stack<int>();
    
    public static void Push(int value){
        newOnTop.Push(value);
    }
    public static void Pop(){
        if(oldOnTop.Count <=0 ){
            while(newOnTop.Count <= 0){
                oldOnTop.Push(newOnTop.Peek());
                newOnTop.Pop();
            }
        }
        oldOnTop.Pop();
    }
    public static int Display(){
        if(oldOnTop.Count <=0 ){
            while(newOnTop.Count <= 0){
                oldOnTop.Push(newOnTop.Peek());
                newOnTop.Pop();
            }
        }
        return oldOnTop.Peek();
    }
    
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int input = Int32.Parse(Console.ReadLine());
        
        for(int i = 0; i < input;i++){
            string[] operations = Console.ReadLine().Split(' ');
            int type = Convert.ToInt32(operations[0]);
            
            if(type == 1){
                int value = Convert.ToInt32(operations[1]);
                Push(value);
            }else if(type == 2){
                Pop();
            }else if(type == 3){
                Console.WriteLine(Display());
            }
        }
    }
}
