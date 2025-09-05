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
        int key = (int) (Math.random() * 101);

        System.out.println(Arrays.toString(list));
        System.out.println("Key: " + key);
        System.out.println(linearSearch(list, key));
    }
}
