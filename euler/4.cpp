
#include <stdio.h>
#include <iostream>
using namespace std;
int x;
int a;
int p = 0;
int ans0 = 0;
bool Palindromic(x, a){
  ans = ans0;
  p = x * a;
  if (string p == p[::-1] and p > ans)
    {
      ans = p;
      return ans;

    }
}

int
main ()
{
  a = 100;
  b = 100;
  while (ans < 10000)
    {
    cout << Palindromic(x, a);
    while (x<1000)
    {
        x +=1;
        cout<<Palindromic(x,a);
        while(a<1000){
            a+=1;
            cout<<Palindromic(x,a);
        }
        
    }
    
        
    }
  return 0;
}
