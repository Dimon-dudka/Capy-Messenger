// Copyright 2026 Dudka Studio
#pragma once

#include "Logger/Interfaces/BaseLoggerMessage.h"
#include "Logger/MessageTypes/TechLogMessage.h"
#include "Logger/Utils/LoggerUtils.h"
#include <gtest/gtest.h>

namespace TimeTestHelpers
{
	static bool tm_equals(const std::tm& a, const std::tm& b) {
		return a.tm_sec == b.tm_sec &&
			   a.tm_min == b.tm_min &&
			   a.tm_hour == b.tm_hour &&
			   a.tm_mday == b.tm_mday &&
			   a.tm_mon == b.tm_mon &&
			   a.tm_year == b.tm_year;
	}
}

class LoggerMessageTestsClass : public testing::Test {
protected:
	virtual void SetUp() override;
	virtual void TearDown() override;

	std::unique_ptr<IBaseLoggerMessage> TechLogMessageImpl;
	static constexpr const char* TechLogMessageText = "Test TechLogMessage";
};


#pragma region BaseLogMessageHelperFunctionsTests
// ConvertToUTCTime Tests
TEST_F(LoggerMessageTestsClass,ConvertToUTCTime_EpochTest)
{
	constexpr std::time_t time = 0;
	const std::tm result = BaseLogMessageHelpers::TimeHelpers::ConvertToUTCTime(time);

	std::tm expected = {};
	expected.tm_sec = 0;
	expected.tm_min = 0;
	expected.tm_hour = 0;
	expected.tm_mday = 1;
	expected.tm_mon = 0;   // January
	expected.tm_year = 70;  // 1900 + 70 = 1970

	EXPECT_TRUE(TimeTestHelpers::tm_equals(result, expected));
}

TEST_F(LoggerMessageTestsClass,ConvertToUTCTime_SpecificDateTest)
{
	std::tm tm_specific = {};
	tm_specific.tm_year = 2023 - 1900;
	tm_specific.tm_mon = 11;      // December
	tm_specific.tm_mday = 31;
	tm_specific.tm_hour = 23;
	tm_specific.tm_min = 59;
	tm_specific.tm_sec = 59;
	tm_specific.tm_isdst = 0;     // UTC has no DST

	constexpr std::time_t t_known = 1704067199;

	const std::tm result = BaseLogMessageHelpers::TimeHelpers::ConvertToUTCTime(t_known);

	std::tm expected = {};
	expected.tm_sec = 59;
	expected.tm_min = 59;
	expected.tm_hour = 23;
	expected.tm_mday = 31;
	expected.tm_mon = 11;
	expected.tm_year = 2023 - 1900;

	EXPECT_TRUE(TimeTestHelpers::tm_equals(result, expected));
}

// ConvertToString Tests
TEST_F(LoggerMessageTestsClass,ConvertToString_DefaultFormat)
{
	constexpr std::time_t time = 0;
	const std::string result =  BaseLogMessageHelpers::TimeHelpers::ConvertToString(time);
	EXPECT_EQ(result, "1970-01-01 00:00:00");
}

TEST_F(LoggerMessageTestsClass,ConvertToString_CustomFormat)
{
	constexpr std::time_t time = 0;
	const std::string result =  BaseLogMessageHelpers::TimeHelpers::ConvertToString(time, "%Y/%m/%d");
	EXPECT_EQ(result, "1970/01/01");
}

TEST_F(LoggerMessageTestsClass,ConvertToString_SpecificDate)
{
	constexpr std::time_t time = 1704067199;
	const std::string result = BaseLogMessageHelpers::TimeHelpers::ConvertToString(time, "%Y-%m-%d %H:%M:%S");
	EXPECT_EQ(result, "2023-12-31 23:59:59");
}

TEST_F(LoggerMessageTestsClass, ConvertToString_EmptyFormat) {
	constexpr std::time_t time = 0;
	const std::string result = BaseLogMessageHelpers::TimeHelpers::ConvertToString(time, "");
	EXPECT_TRUE(result.empty());
}

TEST_F(LoggerMessageTestsClass, ConvertToUTCTime_NegativeTime) {
	// -1 second from epoch = 1969-12-31 23:59:59 UTC
	constexpr std::time_t time = -1;
	const std::tm result = BaseLogMessageHelpers::TimeHelpers::ConvertToUTCTime(time);

	EXPECT_TRUE(TimeTestHelpers::tm_equals(result, {}));
}

#pragma endregion BaseLogMessageHelperFunctionsTests

#pragma region TechLogHelperFunctionsTests

TEST_F(LoggerMessageTestsClass, MessageTypeToString_Info)
{
	EXPECT_EQ(TechLog::MessageTypeToString(TechLog::LogType::INFO), "INFO");
}

TEST_F(LoggerMessageTestsClass, MessageTypeToString_Unknown)
{
	constexpr auto invalid = static_cast<TechLog::LogType>(999);
	EXPECT_EQ(TechLog::MessageTypeToString(invalid), "Unknown MessageType");
}


#pragma endregion TechLogHelperFunctionsTests

#pragma region TechLogMessageFunctionsTests

TEST_F(LoggerMessageTestsClass, TechLogMessage_Should_Create_Message_Successfully)
{
	ASSERT_NE(TechLogMessageImpl, nullptr);
}

TEST_F(LoggerMessageTestsClass, TechLogMessage_ConvertToString_Should_Contain_Message_Text)
{
	const std::string result = TechLogMessageImpl->ConvertToString();

	EXPECT_NE(result.find(TechLogMessageText), std::string::npos);
}

TEST_F(LoggerMessageTestsClass, TechLogMessage_ConvertToString_Should_Contain_Info_Type)
{
	const std::string result = TechLogMessageImpl->ConvertToString();

	EXPECT_NE(result.find(TechLog::MessageTypeToString(TechLog::LogType::INFO)), std::string::npos);
}

TEST_F(LoggerMessageTestsClass, TechLogMessage_Should_Handle_All_LogTypes)
{
	const std::vector<std::pair<TechLog::LogType, std::string>> cases = {
		{TechLog::LogType::INFO, "INFO"},
		{TechLog::LogType::WARNING, "WARNING"},
		{TechLog::LogType::ERROR, "ERROR"},
		{TechLog::LogType::FATAL, "FATAL"}
	};

	for (const auto& [type, expectedString] : cases)
	{
		const TechLogMessage log(TechLogMessageText, type);
		const std::string result = log.ConvertToString();

		EXPECT_NE(result.find(expectedString), std::string::npos)
			<< "Failed for type: " << expectedString;
	}
}

TEST_F(LoggerMessageTestsClass,  TechLogMessage_Should_Support_MoveConstructor)
{
	std::string msg = "MoveTest";

	const TechLogMessage log(std::move(msg), TechLog::LogType::WARNING);

	const std::string result = log.ConvertToString();

	EXPECT_NE(result.find("MoveTest"), std::string::npos);
}

TEST_F(LoggerMessageTestsClass, TechLogMessage_Should_Initialize_Correctly)
{
	const auto impl = static_cast<TechLogMessage*>(TechLogMessageImpl.get());
	ASSERT_NE(impl, nullptr);

	EXPECT_EQ(impl->GetMessage(), "Test TechLogMessage");
	EXPECT_EQ(impl->GetLogType(), TechLog::LogType::INFO);
}

TEST_F(LoggerMessageTestsClass, TechLogMessage_Should_Set_Creation_Time)
{
	const auto impl = static_cast<TechLogMessage*>(TechLogMessageImpl.get());
	ASSERT_NE(impl, nullptr);

	const std::time_t now = std::time(nullptr);
	const std::time_t creationTime = impl->GetTime();

	EXPECT_LE(creationTime, now);
}

#pragma endregion TechLogMessageFunctionsTests
