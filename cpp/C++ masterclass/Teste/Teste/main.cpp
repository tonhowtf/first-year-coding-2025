#include <iostream>

using namespace std;

enum class Months : uint8_t {
	January = 1,
	February,
	March,
	April,
	May,
	June,
	July,
	August,
	September,
	October,
	November,
	December
};

int main()
{
	Months currentMonth = Months::December;

	cout << sizeof(Months) << endl;
	cout << "Number: " << static_cast<int>(currentMonth) << endl;
	if (currentMonth == Months::January) {
		cout << "January!" << endl;
	}
	else if (currentMonth == Months::February) {
		cout << "February!" << endl;
	}
	else if (currentMonth == Months::March) {
		cout << "March!" << endl;
	}
	else if (currentMonth == Months::April) {
		cout << "April" << endl;
	}
	else if (currentMonth == Months::May) {
		cout << "May!" << endl;
	}
	else if (currentMonth == Months::July) {
		cout << "July!" << endl;
	}
	else if (currentMonth == Months::August) {
		cout << "August!" << endl;
	}
	else if (currentMonth == Months::September) {
		cout << "September!" << endl;
	}
	else if (currentMonth == Months::October) {
		cout << "October!" << endl;
	}
	else if (currentMonth == Months::November) {
		cout << "November!" << endl;
	}
	else if (currentMonth == Months::December) {
		cout << "December!" << endl;
	}

	return 0;
}