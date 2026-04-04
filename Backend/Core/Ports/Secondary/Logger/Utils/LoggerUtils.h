// Copyright 2026 Dudka Studio

#pragma once

#include <ctime>
#include <string>

namespace BaseLogMessageHelpers::TimeHelpers
{
	[[nodiscard]]  std::tm ConvertToUTCTime(const std::time_t& InTime);

	[[nodiscard]] std::string ConvertToString(const std::time_t& InTime,const char* InDateTimePattern = "%Y-%m-%d %H:%M:%S");
}