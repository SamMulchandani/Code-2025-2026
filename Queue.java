public class Queue{

    private int head = 0;
    private int tail = 0;
    private int[] arr;

    public Queue(){
        // Initialize head and tail indices
        // Initialize storage list/array
    }

    public String toString(){
        // Iterate through queue from head
        // to tail and create a String
        // representation to return
    }

    // Adds data to the tail of the queue
    // Prints out error message if queue is full
    public void enqueue(int data){
        // 1) Check if queue is full
        //   1a) Print error and break
        // 2) Add data to index tail
        // 3) Increment tail index by one
    }
    public void add(int data){
        // Call enqueue method
    }

    // Removes and returns the data at the head
    // Prints out error message if queue is empty
    public int dequeue(){
        // 1) Check if queue is empty
        //   1a) Print error and break
        // 2) Store element at head index
        // 3) Increment head index
        // 4) Return stored element at old head
    }
    public int remove(){
        // Call dequeue method
    }

    public int peek(){}
    public int get_head(){}

    public int size(){}

    public boolean isEmpty(){}

    public boolean isFull(){}

    public void clear(){}

}