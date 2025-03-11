#include <iostream>

using namespace std;

int main()
{
	char oper;
	float num1 = 0, num2 = 0;

	cout << "Input operator (+ - * /): ";
	cin >> oper;

	cout << "Input num1: ";
	cin >> num1;

	cout << "Input num2: ";
	cin >> num2;

	switch (oper)
	{
	case '+':
		cout << "Result: " << (num1 + num2) << "\n\n";
		break;
	case '-':
		cout << "Result: " << (num1 - num2) << "\n\n";
		break;
	case '*':
		cout << "Result: " << (num1 * num2) << "\n\n";
	case '/':
		cout << "Result: " << (num1 / num2) << "\n\n";
		break;
	default:
		cout << "Invalid operator!\n\n";
	}

	return 0;
}