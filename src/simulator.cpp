#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <ctime>
#include <chrono>
#include <cmath>
#include "../include/OrderBook/OrderBook.h"

using namespace std;
using namespace std::chrono;

int main(){
    OrderBook orderBook();
    dayOrder = orderBook.getOrder();

    // Get trading time stamps that are after the first 30 minutes
    auto tradingTimeStamps = orderBook.getTradingTimeStamps();
    int startIndex = tradingTimeStamps.size() > 30 ? 30: 0;
    tradingTimeStamps.erase(tradingTimeStamps.begin(), tradingTimeStamps.begin() + startIndex);


    auto start = high_resolution_clock::now();
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);
    cout << "Time taken by function: "
         << duration.count() << " microseconds" << endl;
    return 0;
}