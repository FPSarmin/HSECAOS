#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <iomanip>
#include <set>
#include <map>
#include <exception>
#include <vector>


using namespace std;

class Rational {
public:
    Rational(){
        numenator = 0;
        denominator = 1;
    }
    Rational(int new_numerator, int new_denominator){
        int tmp1 = abs(new_numerator);
        int tmp2 = abs(new_denominator);
        if (tmp2 == 0){
            throw invalid_argument("Invalid argument");
        }
        char sign = new_numerator * new_denominator >= 0 ? '+' : '-';
        int gcd = tmp1 != 0 ? GCD(tmp1, tmp2) : 0;
        while(gcd != 0 and gcd != 1){
            tmp1 /= gcd;
            tmp2 /= gcd;
            gcd = GCD(tmp1, tmp2);
        }
        if (sign == '-'){
            tmp1 = -abs(tmp1);
            tmp2 = abs(tmp2);
        }
        else{
            tmp1 = abs(tmp1);
            tmp2 = abs(tmp2);
        }
        this->numenator = tmp1;
        this->denominator = tmp1 != 0 ? tmp2 : 1;
    }

    int Numerator() const{
        return numenator;
    }
    int Denominator() const{
        return denominator;
    }
    bool operator==(const Rational& a) const{
        return this->numenator == a.numenator && this->denominator == a.denominator;
    }
    Rational operator+(const Rational& a) const{
        return Rational(this->numenator * a.denominator + a.numenator * this->denominator,
                        a.denominator * this->denominator);
    }
    Rational operator-(const Rational& a) const{
        return *this + Rational(-a.numenator, a.denominator);
    }
    Rational operator*(const Rational& a) const{
        Rational tmp1 = Rational(this->numenator, a.denominator);
        Rational tmp2 = Rational(a.numenator, this->denominator);
        return Rational(tmp1.numenator * tmp2.numenator, tmp1.denominator * tmp2.denominator);
    }
    friend bool operator<(const Rational& a, const Rational& b){
        return a.numenator / (double)a.denominator < b.numenator / (double)b.denominator;
    }
    friend bool operator>(const Rational& a, const Rational& b){
        return a.numenator / (double)a.denominator > b.numenator / (double)b.denominator;
    }
    Rational operator/(const Rational& a) const{
        if (a.numenator == 0){
            throw domain_error("Division by zero");
        }
        return *this * Rational(a.denominator, a.numenator);
    }
    friend ostream& operator<<(ostream& stream, const Rational& rational){
        stream << rational.Numerator() << '/' << rational.Denominator();
        return stream;
    }
    friend istream& operator>>(istream& istream1, Rational& rational){
        int tmp1 = 0, tmp2 = 0;
        char sign = 0;
        if (!(istream1 >> tmp1)) return istream1;
        if (!(istream1 >> sign))  return istream1;
        if (!(istream1 >> tmp2))  return istream1;
        if (sign == '/') rational = Rational(tmp1, tmp2);
        return istream1;
    }

private:
    int numenator = 0;
    int denominator = 1;
    int GCD(int a, int b) const {
        if (a < b){
            swap (a, b);
        }
        if (a % b == 0){
            return b;
        }
        return GCD(a % b, b);
    }
};

int main() {
    Rational a, b;
    char sign;
    try{
        cin >> a;
    }
    catch (invalid_argument& ex){
        cout << ex.what();
        return 0;
    }
    cin >> sign;
    try{
        cin >> b;
    }
    catch (invalid_argument& ex){
        cout << ex.what();
        return 0;
    }
    if (sign == '+'){
        cout << a + b;
    }
    else if (sign == '-'){
        cout << a - b;
    }
    else if(sign == '*'){
        cout << a * b;
    }
    else if(sign == '/'){
        try {
            cout << a / b;
        }
        catch (domain_error& ex){
            cout << ex.what();
        }
    }
}
