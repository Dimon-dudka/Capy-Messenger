// Copyright 2026 Dudka Studio

#pragma once

#include <exception>
#include <sstream>
#include <string>

class BaseFormattedException;

#define THROW_FORMATTED_EXCEPTION(msg) throw BaseFormattedException(__FILE__, __FUNCTION__, __LINE__, msg)

class BaseFormattedException : public std::exception
{
public:
	explicit BaseFormattedException(const char* InFile, const char* InFunctionName,const int InCodeLineNumber, const char* InMessage = nullptr)
	{
		constexpr std::string_view defaultMessage = "No message was provided for this exception";
		constexpr std::string_view defaultFile = "UnknownFile";
		constexpr std::string_view defaultFunction = "UnknownFunction";

		const std::string_view file = InFile ? InFile : defaultFile;
		const std::string_view function = InFunctionName ? InFunctionName : defaultFunction;
		const std::string_view message = InMessage ? InMessage : defaultMessage;

		std::ostringstream oss;
		oss << "Exception at ["
			<< file
			<< "::"
			<< function
			<< ":"
			<< InCodeLineNumber
			<< "] - "
			<< message;

		Message = oss.str();
	}

	[[nodiscard]] inline virtual const char* what() const noexcept override final
	{
		return Message.c_str();
	}

private:
	std::string Message;
};