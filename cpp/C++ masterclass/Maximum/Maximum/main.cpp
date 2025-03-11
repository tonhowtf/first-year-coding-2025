#include <iostream>

using namespace std;

int maximum(int a, int b)
{
	return a > b ? a : b;
}

int main()
{
	int a = 10, b = 20;

	cout << maximum(a, b) << endl;
	a = 30;
	b = 5;
	cout << maximum(a, b) << endl;

	return 0;
}



