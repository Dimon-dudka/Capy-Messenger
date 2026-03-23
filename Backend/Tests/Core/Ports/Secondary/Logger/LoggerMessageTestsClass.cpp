// Copyright 2026 Dudka Studio

#include "LoggerMessageTestsClass.h"

void LoggerMessageTestsClass::SetUp(){
	TechLogMessageImpl = std::make_unique<TechLogMessage>(TechLogMessageText ,TechLog::LogType::INFO);

	Test::SetUp();
}

void LoggerMessageTestsClass::TearDown(){
	Test::TearDown();
}
