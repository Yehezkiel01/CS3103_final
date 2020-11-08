/*
sudo apt-get install libssl-dev
g++ -o verify verify.cpp -lcrypto
./verify
*/

#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <openssl/sha.h>

using namespace std;

// ref: stackoverflow.com/a/10632725
string sha256(const string str)
{
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    stringstream ss;
    
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, str.c_str(), str.size());
    SHA256_Final(hash, &sha256);
    
    for(int i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        ss << hex << setw(2) << setfill('0') << (int)hash[i];
    }
    
    return ss.str();
}

int main() {
    string input;
    cout << "Enter the flag below:" << endl;
    cout << "password=";
    cin >> input;
    
    if (sha256(input) == "a11ebaa2e2d01d936da0fafec00baa40fdb08a8dd74fb13d2c0bb7b64cff9ec7") {
        cout << "\nCorrect! You've solved it!" << endl;
    } else {
        cout << "\nIncorrect. Please try again." << endl;
    }
    
    return 0;
}
