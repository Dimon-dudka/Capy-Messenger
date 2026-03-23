// Copyright 2026 Dudka Studio
#pragma once

#include "BaseLoggerMessage.h"


namespace TechLog
{
	enum class LogType : char
	{
		INFO = 1,
		WARNING = 2,
		ERROR = 3,
		FATAL = 4,
	};

	constexpr std::string_view MessageTypeToString(const LogType InType)
	{
		switch (InType)
		{
			case LogType::INFO:
				return "INFO";
			break;
			case LogType::WARNING:
				return "WARNING";
			break;
			case LogType::ERROR:
				return "ERROR";
			break;
			case LogType::FATAL:
				return "FATAL";
			break;
			default:
				return "Unknown MessageType";
		}
	}
}

class TechLogMessage final : public IBaseLoggerMessage{
public:
	explicit TechLogMessage(const std::string& InMessage,const TechLog::LogType InType) : Message(InMessage), LogType(InType) {}
	explicit TechLogMessage(std::string&& InMessage,const TechLog::LogType InType) : Message(std::move(InMessage)), LogType(InType) {}

	virtual ~TechLogMessage() = default;

	[[nodiscard]] virtual std::string ConvertToString() const override;

	#ifdef ENABLE_TESTS
	void SetLogType(TechLog::LogType InType);
	void SetMessage(const std::string& InMessage);
	#endif

	[[nodiscard]] std::string GetMessage() const;
	[[nodiscard]] TechLog::LogType GetLogType() const;

private:
	std::string Message;
	TechLog::LogType LogType;
};
