// Copyright 2026 Dudka Studio

#include "TechLogMessage.h"
#include "Logger/Utils/LoggerUtils.h"

std::string TechLogMessage::ConvertToString() const{
	std::ostringstream result;

	if(Message.empty())
	{
		return "";
	}

	// time setup
	result << "[" <<BaseLogMessageHelpers::TimeHelpers::ConvertToString(CreationTime) << "]" << "\t";
	result << "[" << TechLog::MessageTypeToString(LogType) << "]" << "\t";
	result << Message << std::endl;

	return result.str();
}
#ifdef ENABLE_TESTS
void TechLogMessage::SetLogType(TechLog::LogType InType){
	LogType = InType;
}

void TechLogMessage::SetMessage(const std::string& InMessage){
	Message = InMessage;
}
#endif

std::string TechLogMessage::GetMessage() const{
	return Message;
}

TechLog::LogType TechLogMessage::GetLogType() const{
	return LogType;
}
