#include <iostream>
#include <map>
#include <vector>
#include <sstream>
#include <string>
#include <utility>
#include <exception>

using namespace std;

template <typename key, typename value> value& GetRefStrict(map<key, value>& mi, key k){
    if (mi.count(k) != 0){
        value& result = mi[k];
        return result;
    }
    throw runtime_error("");
}

int main(){
    map<int, string> m = {{0, "value"}};
    string& item = GetRefStrict(m, 0);
    item = "newvalue";
    cout << m[0] << endl; // выведет newvalue

}
