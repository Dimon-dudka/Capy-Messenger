// Copyright 2026 Dudka Studio
#pragma once

#include <chrono>
#include <string>

namespace BaseLogMessageHelpers
{
	namespace TimeHelpers
	{
		[[nodiscard]] std::tm ConvertToUTCTime(const std::time_t& InTime);
		[[nodiscard]] std::string ConvertToString(const std::time_t& InTime,const char* InDateTimePattern = "%Y-%m-%d %H:%M:%S");
	}
}

class IBaseLoggerMessage{
public:
	virtual ~IBaseLoggerMessage() = default;

	[[nodiscard]] virtual std::string ConvertToString() const = 0;
	[[nodiscard]] std::time_t GetTime() const;
protected:
	IBaseLoggerMessage() : CreationTime(std::chrono::system_clock::to_time_t(std::chrono::system_clock::now())) {}

	std::time_t CreationTime;
};