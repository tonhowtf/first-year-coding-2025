#include <queue>
#include <iostream>

using namespace std;

/*
1. for
2. while
3. do while

4. go to

*/

int main() 
{
	const string pass("HER");

	for (char a = 'A'; a <= 'Z'; ++a)
	{
		for (char b = 'A'; b <= 'Z'; ++b) 
		{
			for (char c = 'A'; c <= 'Z'; ++c) 
			{
				const string tempPass({ a, b, c });
				cout << tempPass << endl;
				if (tempPass == pass)
				{
					cout << "\n\n\nPassword found: " << tempPass << "\n\n\n";
					goto END;
				}
			}
		}
	}
	END:
	return 0;
}