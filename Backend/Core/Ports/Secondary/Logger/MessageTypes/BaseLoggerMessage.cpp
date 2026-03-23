#include "BaseLoggerMessage.h"


std::tm BaseLogMessageHelpers::TimeHelpers::ConvertToUTCTime(const std::time_t& InTime){
	std::tm utcTimeStruct = {};

	if (InTime<0)
	{
		return utcTimeStruct;
	}

	gmtime_r(&InTime, &utcTimeStruct);

	return utcTimeStruct;
}

std::string BaseLogMessageHelpers::TimeHelpers::ConvertToString(const std::time_t& InTime, const char* InDateTimePattern){
	const std::tm utcTimeStruct = ConvertToUTCTime(InTime);

	std::ostringstream formattedTime;
	formattedTime << std::put_time(
		&utcTimeStruct,
		InDateTimePattern ? InDateTimePattern : "%Y-%m-%d %H:%M:%S"
	);

	return formattedTime.str();
}

std::time_t IBaseLoggerMessage::GetTime() const{
	return CreationTime;
}