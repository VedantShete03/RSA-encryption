#include <iostream>
#include <cstdlib>
#include <bits/stdc++.h>
using namespace std;
// Function to compute modular exponentiation
long long powerMod(long long base, long long exponent, long long modulus) {
    long long result = 1;
    base = base % modulus;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = (result * base) % modulus;
        }
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

// Function to compute modular inverse using Extended Euclidean Algorithm
long long modInverse(long long a, long long m) {
    long long m0 = m, t, q;
    long long x0 = 0, x1 = 1;
    if (m == 1) return 0;
    while (a > 1) {
        q = a / m;
        t = m;
        m = a % m;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    if (x1 < 0) x1 += m0;
    return x1;
}

int main() {
    long long p, q, e;
    long long encryptedMessage;
    cout << "Enter values for p, q, and e: ";
    cin >> p >> q >> e >>encryptedMessage;
    long long N = p * q;
    long long phiN = (p - 1) * (q - 1);
    long long d = modInverse(e, phiN);
    long long decryptedMessage = powerMod(encryptedMessage, d, N);
    cout << "Decrypted message: " << decryptedMessage << endl;
    return 0;
}
