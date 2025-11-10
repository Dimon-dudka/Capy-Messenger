#include "nlohmann/json.hpp"
#include <iostream>

int main()
{
	std::cout << "Hello, World!" << std::endl;

	nlohmann::json j;
	std::cout << j.size();

	return 0;
}
