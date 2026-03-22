# Copyright 2025 Dudka Studio
import os
from .core_utils import *
from .git_usage import GitWorker


class BlackFormatter(CoreCommandExecutor):
    __git_worker: GitWorker

    def __init__(self):
        self.__git_worker = GitWorker()

    def check_format(self):
        project_dir = self.__git_worker.get_git_root_folder()

        if len(project_dir) == 0:
            raise ValueError("Git not found project directory")

        command = ["black", "--check", project_dir]
        result = self._execute_command(command)

        if result.returncode == 0:
            os.system("cls")
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.LOG,
                command=[],
                return_code=0,
                output_text=f"All files in project already black formatted",
            )
        elif result.returncode == 1:

            files_to_reformat = [
                line.split(" ")[-1].strip()
                for line in result.stderr.splitlines()
                if "would reformat" in line
            ]

            os.system("cls")
            for file in files_to_reformat:
                CoreLog.formatted_log(
                    log_type=CoreLog.LogType.LOG,
                    command=[],
                    return_code=0,
                    output_text=f"File with incorrect code style: {file}",
                )

        else:
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.LOG,
                command=[],
                return_code=0,
                output_text=f"Error by searching black format errors | stderr: {result.stderr} | stdout: {result.stdout}",
            )
            raise AssertionError(
                f"Error by searching black format errors | stderr: {result.stderr} | stdout: {result.stdout}"
            )

    def format_files(self):
        project_dir = self.__git_worker.get_git_root_folder()

        if len(project_dir) == 0:
            raise ValueError("Git not found project directory")

        command = ["black", "--quiet", project_dir]
        result = self._execute_command(command)

        # Formatted successfully
        if result.returncode == 0:
            os.system("cls")
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.LOG,
                command=[],
                return_code=0,
                output_text=f"All python files successfully formated",
            )
        # Some error occurred
        else:
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.LOG,
                command=[],
                return_code=1,
                output_text=f"Error by black formatting files | stderr: {result.stderr} | stdout: {result.stdout}",
            )
            raise AssertionError(
                f"Error by black formatting files | stderr: {result.stderr} | stdout: {result.stdout}"
            )
