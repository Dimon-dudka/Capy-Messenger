# Copyright 2026 Dudka Studio
import subprocess
from enum import Enum
from subprocess import CompletedProcess
from typing import List


class CoreCommandExecutor:

    def _execute_command(self, command_args: List) -> CompletedProcess:
        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=command_args,
            return_code=0,
            output_text="",
        )

        try:
            result = subprocess.run(
                command_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
        except subprocess.CalledProcessError:
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.ERROR,
                command=command_args,
                return_code=result.returncode,
                output_text=result.stderr,
            )
            return result

        CoreLog.formatted_log(
            log_type=CoreLog.LogType.SUCCESS,
            command=command_args,
            return_code=0,
            output_text=result.stdout,
        )
        return result


class CoreLog:
    class LogType(Enum):
        INFO = 0
        ERROR = 1
        SUCCESS = 2
        LOG = 4

    @staticmethod
    def formatted_log(log_type: LogType, command: List, return_code, output_text):
        output_str = ""
        git_command_str = " ".join(command)

        if log_type == CoreLog.LogType.INFO:
            output_str = f"{output_text}"
        elif log_type == CoreLog.LogType.ERROR:
            output_str = f"Error by executing command: {git_command_str}. Return code: {return_code}. Output: {output_text}"
        elif log_type == CoreLog.LogType.SUCCESS:
            output_str = f"Success by executing command: {git_command_str}"
        elif log_type == CoreLog.LogType.LOG:
            output_str = "Log:"
            if len(git_command_str) != 0:
                output_str = f"{output_str} executing command: {git_command_str} "
            if len(output_str) != 0:
                output_str = f"{output_str} {output_text}"

        if len(output_str) != 0:
            print(output_str)
