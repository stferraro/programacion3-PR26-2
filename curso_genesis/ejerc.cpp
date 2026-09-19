#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    double peso, estatura, imc;
    cout << "Introduce tu peso en kg: ";
    cin >> peso;
    cout << "Introduce tu estatura en metros: ";
    cin >> estatura;
    imc = peso/(estatura*estatura);

    printf("Tu indice de masa corporal es %.2f\n", imc);
    return 0;
}

