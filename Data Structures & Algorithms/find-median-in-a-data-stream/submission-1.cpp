class MedianFinder {
    priority_queue<int> left;
    priority_queue<int> right;

public:
    MedianFinder() {
    }
    
    void addNum(int num) {
        if (this->left.size() == this->right.size()){
            this->left.push(num);
            int z = this->left.top(); this->left.pop();
            this->right.push(-z);
        }
        if (this->left.size() < this->right.size()){
            this->right.push(-num);
            int z = -this->right.top(); this->right.pop();
            this->left.push(z);
        }
    }
    
    double findMedian() {
        cout << this->left.size() << " " << this->right.size() << '\n';
        int r = -(this->right.top());
        if (this->left.size() == this->right.size()) {
            int l = this->left.top();
            return ((double)l + r)/ 2;
        }

        return (double)r;
    }
};
