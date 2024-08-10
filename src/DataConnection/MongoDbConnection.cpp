#include "mongodb_utils.hpp"
#include <iostream>
#include <bsoncxx/json.hpp>
#include <mongocxx/instance.hpp>

void printCollectionData(const std::string& dbName, const std::string& collectionName)
{
    mongocxx::instance inst{};
    const auto uri = mongocxx::uri{"mongodb://localhost:27017/"};
    mongocxx::client client{uri};

    auto db = client[dbName];
    auto collection = db[collectionName];

    auto cursor = collection.find({});
    for (const auto& doc : cursor) {
        std::cout << bsoncxx::to_json(doc) << std::endl;
    }
}

int main()
{
    printCollectionData("day_stock_data", "intraday");
    return 0;
}