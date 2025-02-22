#include <iostream>

using namespace std;

#define LAST_MONTH 12

int main()
{
	const int screenMaxXPos = 80;
	int x = screenMaxXPos;

	const int lastMonth = LAST_MONTH;
	

	int currentMonth = LAST_MONTH;

	if (currentMonth == lastMonth)
	{
		cout << "December!\n";
	}

	return 0;
}