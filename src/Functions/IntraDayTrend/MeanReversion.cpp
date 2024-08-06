#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;



/*
    @brief: Calculate the mean of the last window prices
    @param prevPrices: vector of current prices
    @param window: window size to calculate the mean
    @return: the mean of the last window prices
*/
double calculateMean(vector<double> prevPrices, double window){
    if (prevPrices.size() < window){
        return 0;
    }
    vector<double> subsetPrices(prevPrices.end() - window, prevPrices.end());

    double total = accumulate(subsetPrices.begin(), subsetPrices.end(), 0.0);

    return total / window;
}

/*
    @brief: Calculate the standard deviation of the last window prices
    @param prevPrices: vector of current prices
    @param window: window size to calculate the standard deviation
    @return: the standard deviation of the last window prices
*/
double standardDeviation(vector<double> prevPrices, double window){
    if (prevPrices.size() < window){
        return 0;
    }

    double mean = calculateMean(prevPrices, window);
    vector<double> subsetPrices(prevPrices.end() - window, prevPrices.end());
    double total = 0;
    for (int i = 0; i < subsetPrices.size(); i++){
        total += pow(subsetPrices[i] - mean, 2);
    }

    return sqrt(total / window);
}

/*
    @brief: Calculate z-score from the mean
    @param prevPrices: vector of current prices
    @param window: window size to calculate the deviation
    @return: the deviation from the mean
*/
double zScore(vector<double> prevPrices, double window, double currentPrice){
    if (prevPrices.size() < window){
        return 0;
    }

    double stdDev = standardDeviation(prevPrices, window);
    double mean = calculateMean(prevPrices, window);

    if (stdDev == 0){
        return 0;
    }
    return (currentPrice - mean) / stdDev;

}

/*
    @brief: Determine the trend direction based on the z-score
    @param prevPrices: vector of current prices
    @param window: window size to calculate the deviation
    @return: the trend direction based on the z-score
*/
string trendDirection(vector<double> prevPrices, double window, double curPrice){
    if (prevPrices.size() < window){
        return 0;
    }

    double mean = calculateMean(prevPrices, window);
    double stdDev = standardDeviation(prevPrices, window);
    double z = zScore(prevPrices, window, curPrice);

    if (z > 2){
        return  "bullish";
    } else if (z < -1){
        return "bearish";
    } else {
        return "neutral";
    }
}


int main() {
    vector<double> prices = {10.5, 11.2, 10.8, 11.5, 10.2, 10.9, 12.1, 11.8, 10.3, 11.0};
    double window = 5;
    double curPrice = 15.0;

    double mean = calculateMean(prices, window);
    double stdDev = standardDeviation(prices, window);
    double z = zScore(prices, window, curPrice);

    cout << "Mean: " << mean << endl;
    cout << "Standard Deviation: " << stdDev << endl;   
    cout << "Z-Score: " << z << endl;

    string trend = trendDirection(prices, window, curPrice);
    cout << "Trend Direction: " << trend << endl;

    return 0;
}