// A Juggling Algorith

// Instead of moving one by one, divide the array in different sets
// where number of sets is equal to GCD of n and d and move the elements within sets.
// If GCD is 1 as is for the above example array (n = 7 and d =2), then elements will be 
// moved within one set only, we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] 
// and finally store temp at the right place.

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {
    void leftRotate(int[] arr, int d, int n) 
    {
        int i, j, k, temp;
        for (i = 0; i < gcd(d, n); i++) 
        {
            /* move i-th values of blocks */
            temp = arr[i];
            j = i;
            while (1 != 0) 
            {
                k = j + d;
                if (k >= n) 
                    k = k - n;
                if (k == i) 
                    break;
                arr[j] = arr[k];
                j = k;
            }
            arr[j] = temp;
        }
    }
    
    /*Fuction to get gcd of a and b*/
    int gcd(int a, int b) 
    {
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }
    
    /* function to print an array */
    void printArray(int[] arr, int size) 
    {
        int i;
        for (i = 0; i < size; i++)
            Console.Write(arr[i] + " ");
    }
    
    static void Main(String[] args) {
        string[] tokens_n = Console.ReadLine().Split(' ');
        int n = Convert.ToInt32(tokens_n[0]);
        int d = Convert.ToInt32(tokens_n[1]);
        string[] a_temp = Console.ReadLine().Split(' ');
        int[] a = Array.ConvertAll(a_temp,Int32.Parse);
        
        Solution solution = new Solution();
        solution.leftRotate(a, d, n);
        solution.printArray(a, n);
        
    }
}
