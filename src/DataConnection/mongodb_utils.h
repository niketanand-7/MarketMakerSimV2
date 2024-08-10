#ifndef MONGODB_UTILS_H
#define MONGODB_UTILS_H

#include <string>
#include <mongocxx/client.hpp>

void printCollectionData(const std::string& dbName, const std::string& collectionName);

#endif