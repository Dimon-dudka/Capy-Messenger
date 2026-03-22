# Copyright 2026 Dudka Studio
import os
import re
from typing import List
from enum import Enum
from .core_utils import CoreLog
from .git_usage import GitWorker

COPYRIGHT_LINE = "Copyright 2026 Dudka Studio"


class FileTypes(Enum):
    PYTHON = 0
    CPP_SOURCE = 1
    CPP_HEADER = 2


ALLOWED_FILE_EXTENSIONS = {FileTypes.PYTHON: "py",
                           FileTypes.CPP_SOURCE: "cpp",
                           FileTypes.CPP_HEADER: "h",
                           }

EXTENSION_PER_TYPE = {"py": FileTypes.PYTHON,
                      "cpp": FileTypes.CPP_SOURCE,
                      "h": FileTypes.CPP_HEADER,
                      }

LANGUAGE_COMMENTS_FORMAT = {"py": r"#.*$",
                            "cpp": r"//.*$",
                            "h": r"//.*$",
                            }

LANGUAGE_COPYRIGHT_LINE = {"py": f"# {COPYRIGHT_LINE}\n",
                           "cpp": f"// {COPYRIGHT_LINE}\n",
                           "h": f"// {COPYRIGHT_LINE}\n",
                           }

COPYRIGHT_PATTERNS = {FileTypes.PYTHON: r"# " + re.escape(COPYRIGHT_LINE) + r"$",
                      FileTypes.CPP_SOURCE: r"// " + re.escape(COPYRIGHT_LINE) + r"$",
                      FileTypes.CPP_HEADER: r"// " + re.escape(COPYRIGHT_LINE) + r"$",
                      }


class CopyrightChecker:
    __git_worker: GitWorker

    def __init__(self):
        self.__git_worker = GitWorker()

    def check_copyright(self):
        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=[],
            return_code=0,
            output_text=f"Check copyright started",
        )

        wrong_copyright_files_lst = self.__get_wrong_copyright_files()

        os.system("cls")
        if len(wrong_copyright_files_lst) == 0:
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.INFO,
                command=[],
                return_code=0,
                output_text=f"No copyright errors found",
            )
            return

        for file_path in wrong_copyright_files_lst:
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.INFO,
                command=[],
                return_code=0,
                output_text=f"Incorrect copyright found in file: {file_path}",
            )

    def format_copyright(self):
        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=[],
            return_code=0,
            output_text="Format copyright started",
        )
        wrong_copyright_files_lst = self.__get_wrong_copyright_files()

        formated_files = 0
        for file_path in wrong_copyright_files_lst:
            file_content = []
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.readlines()
            except Exception as ex:
                CoreLog.formatted_log(
                    log_type=CoreLog.LogType.LOG,
                    command=[],
                    return_code=0,
                    output_text=f"Error by opening file: {file_path}. Exception: {ex}",
                )
                continue

            file_ext = self.__get_file_extension(file_path)
            copyright_line = LANGUAGE_COPYRIGHT_LINE.get(file_ext)

            index = 0
            for i in file_content:
                if len(i.strip()) == 0:
                    index += 1
                else:
                    break

            file_content = file_content[index:]

            if file_content and re.search(
                LANGUAGE_COMMENTS_FORMAT.get(file_ext), file_content[0]
            ):
                file_content[0] = copyright_line
            else:
                file_content.insert(0, copyright_line)

            new_file_content = "".join(file_content)

            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(new_file_content)
            except Exception as ex:
                CoreLog.formatted_log(
                    log_type=CoreLog.LogType.LOG,
                    command=[],
                    return_code=0,
                    output_text=f"Error by writing file: {file_path}. Exception: {ex}",
                )
                return
            formated_files += 1

        os.system("cls")
        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=[],
            return_code=0,
            output_text=f"Successfully formated copyright in {formated_files} files",
        )

    def __get_wrong_copyright_files(self) -> List[str]:
        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=[],
            return_code=0,
            output_text=f"Get wrong copyright files",
        )

        git_project_files = self.__git_worker.get_files_in_repo()

        project_files_allowed = [
            file
            for file in git_project_files
            if any(
                file.endswith(ALLOWED_FILE_EXTENSIONS[ext])
                for ext in ALLOWED_FILE_EXTENSIONS
            )
        ]

        project_source_dir = self.__git_worker.get_git_root_folder()
        project_files_with_full_paths = [
            project_source_dir + "/" + path for path in project_files_allowed
        ]

        wrong_copyright_files = []

        for file_path in project_files_with_full_paths:
            first_line = ""
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    first_line = file.readline().strip()
            except Exception as ex:
                CoreLog.formatted_log(
                    log_type=CoreLog.LogType.LOG,
                    command=[],
                    return_code=0,
                    output_text=f"Error by opening file: {file_path} . Exception: {ex}",
                )

            file_ext = self.__get_file_extension(file_path)

            if file_ext in EXTENSION_PER_TYPE:
                file_type = EXTENSION_PER_TYPE[file_ext]
                copyright_pattern = COPYRIGHT_PATTERNS.get(file_type)

                if copyright_pattern and not re.match(copyright_pattern, first_line):
                    wrong_copyright_files.append(file_path)
            else:
                CoreLog.formatted_log(
                    log_type=CoreLog.LogType.LOG,
                    command=[],
                    return_code=0,
                    output_text=f"Unknown file extension: {file_ext} for file: {file_path}",
                )

        return wrong_copyright_files

    def __get_file_extension(self, file_path: str) -> str:
        if len(file_path) == 0:
            return ""
        return file_path.rsplit(".", 1)[-1]
