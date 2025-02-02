/*
    1. Receber 2 notas
    2. Somar as duas notas, dividir por 2 para obter a média
    3. Mostrar a média
    4. Se media for >= 6 (aprovado)
    5. Caso contrário (reprovado)

    int
    string
*/

#include <iostream>

using namespace std;

int main()
{
    float grade1 = 0, grade2 = 0, avg =0;

    cout << "Enter your first grade: ";
    cin >> grade1;

    if (cin.fail()) {
        cin.clear(); // limpa os flags de erro
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // limpa o buffer
        cout << "invalid input!\n";
        return -1;

    }

    cout << "Enter your second grade: ";
    cin >> grade2;

    if (cin.fail()) {
        cin.clear(); // limpa os flags de erro
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // limpa o buffer
        cout << "invalid input!\n";
        return -1;

    }

    avg = (grade1 + grade2) / 2;
    cout << "Avarage: " << avg << endl;

    if (avg >= 6){
        cout << "Congratulations! You passed!\n";
    } else{
        cout << "You, failed!\n";
    }

    return 0;

}
