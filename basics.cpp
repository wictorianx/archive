#include <cmath>		// for math like min()
#include <stdio.h>
#include <iostream>
using namespace std;		// to use commands from library
int
main ()
{
  cout << "hello world";
std:cout << "\they\n";		// this is also a possible use
  string ensar = "pro";
  cout << ensar.length ();	// \t does a tab distance space and \n goes to new line
  int num;
  ensar[0] = 'K';		//p is replaced with k
  //cin>> num;// requests input
  cout << ensar;
  cout << ensar[1];
  cout << ensar[ensar.length () - 1];
  const char wictorian = 5;	//const can't be changed, gives error when overwritten
/* double is for floats
char is a single letyer a character of a string
bool is boolean
*/
  string param1;
  string param2;
  cout << "requesting string";
  cin >> param1;
  cout << "requesting string";
  cin >> param2;
  int param0;
  cout << "requestingninteger";
  cin >> param0;
  cout << param1 + param2;
  if (sqrt (param0) == round (sqrt (param0)))
    {
      cout << param0;
      cout << "is a full square";
    }

  else if (round (param0) == param0)
    {
      cout << param0;
      cout << "is a integer";

    }

  else
    {
      cout << param0;
      cout << "is neigther an integer nor a full square";
    }

// min(), max(), sqrt(), round()
// boolean = false, false is 0 and true is 1
// min chooses the smallest, max instead chooses the biggest
int i;
  for (i = 0; i <= 10; i++)
    {
      cout << i;
      while ((i * 2) % 2 == 0)
	{
	  cout << i;
	cout << "is am even number";
	    
	}
    }


  return 0;











}
