//Generate some random data

//Prompt user for search key

//Linear search algorithm

// 1) Initialize a current index variable to 0
// 2) Check if element at the current index matches key
//   2a) Return current index since key found
// 3) If element at current index does not match key, then increment current index to next element
// 4) Repeat from step 2 while index is less than length of list
// 5) If key not found, return -1
import java.util.Arrays;
import java.util.Scanner;
public class LinearSearch{
    public static int linearSearch(int[] array, int key){
        for(int i = 0; i < array.length; i++){
            if(array[i]==key)
                return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] list = new int[30];
        for(int i = 0; i < list.length; i++){
            list[i] = (int) (Math.random() * 101);
        }
        System.out.println(Arrays.toString(list) + "\n");

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter key:");
        int key = Integer.parseInt(scanner.nextLine());
        System.out.println();
        scanner.close();

        int search = linearSearch(list, key);

        System.out.println("Key: " + key);
        if(search == -1) System.out.println("Key not found");
        else System.out.println("Index: " + search);
    }
}
