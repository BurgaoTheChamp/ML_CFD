#include <iostream>

long double ReCalc(const long double &flowSpeed, const long double &viscosity, const long double &chordWidth, const long double &density){
    return (density*chordWidth*flowSpeed)/viscosity;
}

long double UCalc(const long double &reynolds, const long double &viscosity, const long double &chordWidth, const long double &density){
    return (reynolds*viscosity)/(density*chordWidth);
}

int main(){
    bool keep = true;

    while (keep)
    {
        int response;
        std::cout << "Do you wish to calculate the U or Re? (1/0)";
        std::cin >> response;

        if (response){
            long double reynolds, viscosity, chordWidth, density;

            std::cout << "Insert Reynolds number: ";
            std::cin >> reynolds;

            std::cout << "Insert chord width: ";
            std::cin >> chordWidth;

            std::cout << "Insert dynamic viscosity value: ";
            std::cin >> viscosity;

            std::cout << "Insert density value: ";
            std::cin >> density;

            std::cout << "The calculated flow speed value is " << UCalc(reynolds, viscosity, chordWidth, density) << std::endl;;
        }else{
            long double flowSpeed, viscosity, chordWidth, density;

            std::cout << "Insert flow speed value: ";
            std::cin >> flowSpeed;

            std::cout << "Insert chord width: ";
            std::cin >> chordWidth;

            std::cout << "Insert dynamic viscosity value: ";
            std::cin >> viscosity;

            std::cout << "Insert density value: ";
            std::cin >> density;

            std::cout << "The calculated Reynolds number is " << ReCalc(flowSpeed, viscosity, chordWidth, density) << std::endl;
        }

        std::cout << "Do you wish to do another one? (1/0)";
        std::cin >> keep;
    }
    
}