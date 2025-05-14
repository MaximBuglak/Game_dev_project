#include <iostream>
#include <cstdlib>
#include <ctime>
#include <clocale> // Для setlocale
using namespace std;

int main() {
    setlocale(LC_ALL, "RUS"); // Включаем поддержку русских символов

    srand(time(0));
    int number = rand() % 100 + 1;
    int guess;

    cout << "Угадай число от 1 до 100:\n";

    do {
        cout << "Твой вариант: ";
        cin >> guess;

        if (guess > number)
            cout << "Меньше!\n";
        else if (guess < number)
            cout << "Больше!\n";
        else
            cout << "Ты угадал!\n";

    } while (guess != number);

    return 0;
}
