#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    cin >> a;
    cin >> b;
    int lenA = a.size();
    int lenB = b.size();

    cout << lenA << ' ' << lenB << endl;
    cout << a+b << endl;
    char temp = a[0];
    a[0] = b[0];
    b[0] = temp;
    cout << a << ' ' << b;
    return 0;
}
