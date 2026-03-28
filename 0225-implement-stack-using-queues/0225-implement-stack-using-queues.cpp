class MyStack {
private:
    
    int q1[100], q2[100];
    int f1, r1, f2, r2;

public:
    MyStack() {
        f1 = r1 = 0;
        f2 = r2 = 0;
    }
    
  
    bool isEmptyQ1() {
        return f1 == r1;
    }
    
    void pushQ2(int x) {
        q2[r2++] = x;
    }
    
    void pushQ1(int x) {
        q1[r1++] = x;
    }
    
    int popQ1() {
        return q1[f1++];
    }
    
    int frontQ1() {
        return q1[f1];
    }
    
    void push(int x) {
        
        pushQ2(x);
       
        while (f1 < r1) {
            q2[r2++] = q1[f1++];
        }
        
        f1 = 0; r1 = 0;
        for (int i = f2; i < r2; i++) {
            q1[r1++] = q2[i];
        }
        
        f2 = r2 = 0;
    }
    
    int pop() {
        return popQ1();
    }
    
    int top() {
        return frontQ1();
    }
    
    bool empty() {
        return isEmptyQ1();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */