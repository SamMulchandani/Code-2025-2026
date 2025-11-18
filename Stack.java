import java.util.Arrays;
public class Stack{

    // Declare top variable and initialize to 0
    private int top = 0;
    // Declare length variable
    private int length;
    // Declare array variable to hold contents of stack
    private int[] arr;

    // Constructor when an integer for size of stack is passed
    public Stack(int length){
        // 1) Set the array instance variable to an empty array of provided length
        this.arr = new int[length];
        // 2) Set the length instance variable to provided length
        this.length = length;
    }
    // Constructor when an array is passed to input values of stack
    public Stack(int[] arr){
        // 1) Set the array instance variable to provided array
        this.arr = arr;
        // 2) Set the length instance variable to the length of the array provided
        this.length = arr.length;
    }

    // Pushes data onto the stack (if not full). Prints an error message if full
    public void push(int x){
        // Adds the passed integer to the top if not full and increments the top variable
        if(top < (length)){
            arr[top] = x;
            top++;
        } else{
            System.out.println("Cannot push; stack is full");
        }
    }

    // Pops data from the stack (if not empty). Prints an error message if empty
    // Returns the popped value
    public int pop(){
        // If not empty, returns the element at the top and decrements the top variable
        if(top > 0){
            top--;
            return arr[top];
        } else{
            System.out.println("Cannot pop; stack is empty");
            return -1;
        }
    }
    
    // Returns the top value of the stack without removing it
    public int peek(){
        if(top > 0){
            return arr[top - 1];
        } else{
            System.out.println("Cannot peek; stack is empty");
            return -1;
        }
    }

    // Returns True if the stack is empty (nothing pushed), False otherwise
    public boolean is_empty(){
        return (top == 0);
    }
    
    // Returns True if the stack is full (SIZE elements pushed), False otherwise
    public boolean is_full(){
        return (top == length);
    }

    // Resets the stack to empty
    public void clear(){
        top = 0;
    }

    // Returns the number of elements currently in the stack
    public int length(){
        return length;
    }

    // Returns a string containing all elements in the stack from top to bottom
    public String toString(){
        // 1) Creates a new array of length of current number of elements in the stack
        int[] list = new int[top];
        // 2) Reverses the order of the stack such that the top comes first
        for(int i = top - 1; i >= 0; i--){
            list[top - 1 - i] = arr[i];
        }
        return Arrays.toString(list);
    }

    public static void main(String[] args) {
        
        Stack stack = new Stack(10);

        System.out.println("Empty: " + stack.is_empty());
        System.out.println("Full: " + stack.is_full());
        
        // for(int i = 0; i < stack.length(); i++){
        //     stack.push((int)(Math.random() * 100));
        //     System.out.println(stack);
        // }
        
        stack.push(20);
        stack.push(30);
        stack.push(4);
        System.out.println(stack.peek());
        stack.push(2);
        stack.push(0);
        System.out.println(stack.pop());
        System.out.println(stack.peek());
        stack.clear();
        System.out.println(stack);
        
    }

}