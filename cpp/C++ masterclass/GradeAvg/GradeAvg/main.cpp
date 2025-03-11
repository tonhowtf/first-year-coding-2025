#include <limits>
#include <iostream>

using namespace std;

int main()
{
	float grade1 = 0, grade2 = 0, avg = 0;
		

	cout << "Enter your first grade: ";
	cin >> grade1;

	if (cin.fail()) {
		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		cout << "Invalid input!\n";
		return -1;
	}

	cout << "Enter your second grade: ";
	cin >> grade2;
	
	if (cin.fail()) {
		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		cout << "Invalid input!\n";
		return -1;
	}

	avg = (grade1 + grade2) / 2;
	cout << "Average: " << avg << endl;

	

	if (avg >= 6) {
		cout << "Congratulations! You passed!\n"; 
		
	}
	else {
		cout << "Sorry, you failed!\n";
	}
}