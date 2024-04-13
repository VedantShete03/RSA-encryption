#include <iostream>
#include <cstdlib>
#include <bits/stdc++.h>
using namespace std;
// Function to compute modular exponentiation
long long powerMod(long long base, long long exponent, long long modulus) {
    long long result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = (result * base) % modulus;
        }
        base = (base * base) % modulus;
        exponent /= 2;
    }
    return result;
}

int main() {
    long long m, e, n;
    cout << "Enter values for m, e, and n: ";
    cin >> m >> e >> n;
    long long a = powerMod(m, e, n);
    cout << "Encrypted message = " << a << endl;

    return 0;
}
