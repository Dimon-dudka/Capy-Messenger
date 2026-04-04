// Copyright 2026 Dudka Studio
#pragma once

#include <chrono>

class IBaseLoggerMessage{
public:
	virtual ~IBaseLoggerMessage() = default;

	[[nodiscard]] virtual std::string ConvertToString() const = 0;
	[[nodiscard]] std::time_t GetTime() const
	{
		return CreationTime;
	}
protected:
	IBaseLoggerMessage() : CreationTime(std::chrono::system_clock::to_time_t(std::chrono::system_clock::now())) {}

	std::time_t CreationTime;
};