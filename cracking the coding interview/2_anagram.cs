using System.IO;
using System;

class Program
{
    static void Main()
    {
        string af = Console.ReadLine(); // first string is read
        string bf = Console.ReadLine(); // second string is read
        
        int[] counts = new int[26]; // An int array that will store the caharater count
        char a = 'a'; //character a will be kept as a point of reference

        char[] charArray = af.ToCharArray();

        for (int i = 0; i < charArray.Length; i++) { // This adds up to the int array for each character
            counts[charArray[i] - a]++;
        }

        charArray = bf.ToCharArray();
        
        for (int i = 0; i < charArray.Length; i++) { // similar characters from second arra are reduced
            counts[charArray[i] - a]--;
        }

        int sum = 0;
        for (int i = 0; i < counts.Length ; i++){
            sum += Math.Abs(counts[i]);
        }

        Console.Write(sum);
    }
}