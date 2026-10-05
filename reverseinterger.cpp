class Solution {
public:
    int reverse(int x) {
        long long answer=0;
        while(x!=0){
        int digit= x%10;
        answer = answer * 10 + digit;
        x=x/10;
        }
     return answer;
    }
   

};