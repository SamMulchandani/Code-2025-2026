//Generate random data
//Generate random key

// 1) Initialize start variable at index 0,
// 1) Initialize end variable at index of length - 1

// 2) While start < end:
    // 3) Intialize mid variable as (start + end) divided by two
    // 4) Check if element at index of mid variable is key
    //  4a) Return mid 
    // 5) Else:
    //  5a) If key is greater than element at index of mid:
    //      5a) start variable = mid + 1
    //  5b) If key is less than element at index of mid:
    //      5b) end variable = mid
// 6) If start > end, key not found and:
//  6a) Return -1

import java.util.Arrays;

public class BinarySearch {
    public static int binarySearch(int[] list, int key){
        int start = 0;
        int end = list.length - 1;

        while(start <= end){
            int mid = (start + end) / 2;
            if(list[mid] == key) return mid;
            else if(key > list[mid])
                start = mid + 1;
            else if (key < list[mid])
                end = mid;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] list = new int[30];
        for(int i = 0; i < list.length; i++){
            list[i] = (int) (Math.random() * 101);
        }
        Arrays.sort(list);
        int key = (int) (Math.random() * 101);

        System.out.println(Arrays.toString(list));
        System.out.println("Key: " + key);
        System.out.println(binarySearch(list, key));
    }
}
