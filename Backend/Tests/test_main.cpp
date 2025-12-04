#include <gtest/gtest.h>

TEST(MyTests, simpleCheck)
{
	EXPECT_EQ(2 + 2, 4);
	std::cout << "Hello Tests!" << std::endl;
}

int main(int argc, char** argv)
{
	testing::InitGoogleTest(&argc, argv);

	return RUN_ALL_TESTS();
}