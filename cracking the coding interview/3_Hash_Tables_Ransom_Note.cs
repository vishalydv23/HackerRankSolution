// A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

// Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

// Input Format

// The first line contains two space-separated integers describing the respective values of  (the number of words in the magazine) and  (the number of words in the ransom note). 
// The second line contains  space-separated strings denoting the words present in the magazine. 
// The third line contains  space-separated strings denoting the words present in the ransom note.

// Constraints

// .
// Each word consists of English alphabetic letters (i.e.,  to  and  to ).
// The words in the note and magazine are case-sensitive.
// Output Format

// Print Yes if he can use the magazine to create an untraceable replica of his ransom note; otherwise, print No.

// Sample Input 0

// 6 4
// give me one grand today night
// give one grand today
// Sample Output 0

// Yes



using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    public static Dictionary<string, int> GetWordCount(string[] magazine){
        Dictionary<string, int> wordFrequency = new Dictionary<string, int>();
        foreach(string word in magazine)
        {
            if(wordFrequency.ContainsKey(word)){
                wordFrequency[word]++;
            }else{
                wordFrequency.Add(word,1);
            }
        }
        return wordFrequency;
    }
    
    public static string MatchMagazineAndNote(string[] magazine, string[] ransom){
        Dictionary<string, int> magazineWordCount = GetWordCount(magazine);
        foreach(string word in ransom){
            if(magazineWordCount.ContainsKey(word)){
                if(magazineWordCount[word] > 1){
                    magazineWordCount[word]--;
                }else{
                    magazineWordCount.Remove(word);
                }
            }else{
                return "No";
            }
        }
        return "Yes";
    }
    
    static void Main(String[] args) {
        string[] tokens_m = Console.ReadLine().Split(' ');
        int m = Convert.ToInt32(tokens_m[0]);
        int n = Convert.ToInt32(tokens_m[1]);
        string[] magazine = Console.ReadLine().Split(' ');
        string[] ransom = Console.ReadLine().Split(' ');
        
        
        string answer = MatchMagazineAndNote(magazine, ransom);
        
        Console.WriteLine(answer);
        
    }
}