// Copyright 2026 Dudka Studio

#pragma once

#include "BaseFormattedException.h"
#include <gtest/gtest.h>

class BaseFormattedExceptionTestsClass : public testing::Test {
protected:
	virtual void SetUp() override
	{
		Test::SetUp();
	}

	virtual void TearDown() override
	{
		Test::TearDown();
	}
};

TEST_F(BaseFormattedExceptionTestsClass, FormatsMessageCorrectly)
{
	const char* file = "TEST_F.cpp";
	const char* function = "TestFunction";
	int line = 42;
	const char* message = "Something went wrong";

	const BaseFormattedException ex(file, function, line, message);

	const std::string result = ex.what();

	EXPECT_NE(result.find("TEST_F.cpp"), std::string::npos);
	EXPECT_NE(result.find("TestFunction"), std::string::npos);
	EXPECT_NE(result.find("42"), std::string::npos);
	EXPECT_NE(result.find("Something went wrong"), std::string::npos);
}

TEST_F(BaseFormattedExceptionTestsClass, UsesDefaultMessageWhenNullptr)
{
	const BaseFormattedException ex("file.cpp", "Func", 10, nullptr);

	const std::string result = ex.what();

	EXPECT_NE(result.find("No message was provided"), std::string::npos);
}

TEST_F(BaseFormattedExceptionTestsClass, UsesDefaultFileWhenNullptr)
{
	const BaseFormattedException ex(nullptr, "Func", 10, "Error");

	const std::string result = ex.what();

	EXPECT_NE(result.find("UnknownFile"), std::string::npos);
}

TEST_F(BaseFormattedExceptionTestsClass, UsesDefaultFunctionWhenNullptr)
{
	const BaseFormattedException ex("file.cpp", nullptr, 10, "Error");

	const std::string result = ex.what();

	EXPECT_NE(result.find("UnknownFunction"), std::string::npos);
}

TEST_F(BaseFormattedExceptionTestsClass, ContainsExpectedFormatStructure)
{
	const BaseFormattedException ex("file.cpp", "Func", 99, "Error");

	const std::string result = ex.what();

	EXPECT_TRUE(result.find("Exception at [") == 0);
	EXPECT_NE(result.find("file.cpp::Func:99"), std::string::npos);
	EXPECT_NE(result.find(" - Error"), std::string::npos);
}

TEST_F(BaseFormattedExceptionTestsClass, ThrowMacroThrowsException)
{
	EXPECT_THROW({
		THROW_FORMATTED_EXCEPTION("Macro error");
	}, BaseFormattedException);
}

TEST_F(BaseFormattedExceptionTestsClass, ThrowMacroFormatsMessage)
{
	try
	{
		THROW_FORMATTED_EXCEPTION("Macro TEST_F");
	}
	catch (const BaseFormattedException& ex)
	{
		const std::string result = ex.what();

		EXPECT_NE(result.find("Macro TEST_F"), std::string::npos);
		EXPECT_NE(result.find(__FILE__), std::string::npos);
	}
}

TEST_F(BaseFormattedExceptionTestsClass, WhatIsStable)
{
	const BaseFormattedException ex("file.cpp", "Func", 1, "Error");

	const char* first = ex.what();
	const char* second = ex.what();

	EXPECT_STREQ(first, second);
}