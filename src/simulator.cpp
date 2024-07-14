#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <ctime>
#include <chrono>
#include <cmath>

using namespace std;
using namespace std::chrono;

int main(){
    auto start = high_resolution_clock::now();
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);
    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;
    return 0;
}