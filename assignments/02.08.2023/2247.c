<<<<<<< HEAD
class Solution {
public:
    int sumOfMultiples(int n) {
       int sum = 0 ;
       for (int i = 1 ; i <= n  ; i++){
           if (i%3 == 0 || i%5 == 0 || i%7 == 0 ){
               sum+=(i);
           }
       }
       return sum;
    }
=======
class Solution {
public:
    int sumOfMultiples(int n) {
       int sum = 0 ;
       for (int i = 1 ; i <= n  ; i++){
           if (i%3 == 0 || i%5 == 0 || i%7 == 0 ){
               sum+=(i);
           }
       }
       return sum;
    }
>>>>>>> 8df968f400e5a2c4fc6d763f4a351e4e2b545a92
};