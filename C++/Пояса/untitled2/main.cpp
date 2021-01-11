#include <iostream>
#include <iomanip>
#include <string>
#include <set>
#include <map>
#include <exception>

using namespace std;

void EnsureNextSymbolAndSkip(stringstream& stream, string& date){
    if (stream.peek() != '-'){
        throw runtime_error("Wrong date format: " + date);
    }
    stream.ignore(1);
}

void PrintSet(const set<string>& list){
    for (const auto& l : list){
        cout << l << endl;
    }
}


class Date {
public:
    Date (int new_year = 0, int new_month = 1, int new_day = 1){
        year = new_year;
        if (new_month > 12 || new_month < 1){
            throw runtime_error("Month value is invalid: " + to_string(new_month));
        }
        month = new_month;
        if (new_day > 31 || new_day < 1){
            throw runtime_error("Day value is invalid: " + to_string(new_day));
        }
        day = new_day;
    }
    int GetYear() const{
        return year;
    }
    int GetMonth() const{
        return month;
    }
    int GetDay() const {
        return day;
    }

    friend ostream& operator<<(ostream& stream, Date date){
        cout << setfill('0') << setw(4) << date.year << '-' << setw(2) << date.month << '-' << setw(2) << date.day;
        return stream;
    }

private:
    int year;
    int month;
    int day;
};

bool operator<(const Date& lhs, const Date& rhs){
    if (lhs.GetYear() == rhs.GetYear()){
        if (lhs.GetMonth() == rhs.GetMonth()){
            if (lhs.GetDay() == rhs.GetDay()){
                return false;
            }
            else return lhs.GetDay() < rhs.GetDay();
        }
        else return lhs.GetMonth() < rhs.GetMonth();
    }
    else return lhs.GetYear() < rhs.GetYear();
}

void ReadDate(string& str, Date& date){
    stringstream ss(str);
    int year = 0;
    int month = 0;
    int day = 0;
    if (!(ss >> year)) throw runtime_error("Wrong date format: " + str);
    EnsureNextSymbolAndSkip(ss, str);
    if (!(ss >> month)) throw runtime_error("Wrong date format: " + str);
    EnsureNextSymbolAndSkip(ss, str);
    if (!(ss >> day)) throw runtime_error("Wrong date format: " + str);
    date = Date(year, month, day);
    if (ss.peek() != EOF) throw runtime_error("Wrong date format: " + str);
}

class Database {
public:
    void AddEvent(const Date& date, const string& event){
        datebase[date].insert(event);
    }
    bool DeleteEvent(const Date& date, const string& event){
        if (datebase.count(date) != 0){
            if (datebase[date].count(event) != 0){
                datebase[date].erase(event);
                return true;
            }
        }
        return false;
    }
    int  DeleteDate(const Date& date){
        int n = datebase[date].size();
        datebase.erase(date);
        return n;
    }

    set <string> Find(const Date& date) const{
        set <string> value;
        if (datebase.count(date) > 0){
            value = datebase.at(date);
        }
        return value;
    }

    void Print() const{
        for (const auto& [key, value] : datebase){
            for (const string& item : value){
                cout << key << " " << item << endl;
            }
        }
    }

private:
    map<Date, set<string>> datebase;
};

int main() {
    Database db;

    string command;
    while (getline(cin, command)) {
        string tmp1, event, new_date;
        stringstream ss(command);
        Date date;
        ss >> tmp1;
        try{
            if (tmp1 == "Add"){
                ss >> new_date;
                ss >> event;
                ReadDate(new_date, date);
                db.AddEvent(date, event);
            }
            else if (tmp1 == "Del"){
                ss >> new_date;
                ReadDate(new_date, date);
                if ((ss >> event)){
                    if (db.DeleteEvent(date, event)){
                        cout << "Deleted successfully" << endl;
                    }
                    else{
                        cout << "Event not found" << endl;
                    }
                }
                else{
                    cout << "Deleted " << db.DeleteDate(date) << " events" << endl;
                }
            }
            else if (tmp1 == "Find"){
                ss >> new_date;
                ReadDate(new_date, date);
                PrintSet(db.Find(date));
            }
            else if (tmp1 == "Print"){
                db.Print();
            }
            else if (tmp1 == ""){

            }
            else{
                throw runtime_error("Unknown command: " + tmp1);
            }
        }
        catch (exception& ex){
            cout << ex.what() << endl;
            return 0;
        }
    }

    return 0;
}