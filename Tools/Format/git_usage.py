# Copyright 2025 Dudka Studio

from .core_utils import *


class GitWorker(CoreCommandExecutor):

    def __init__(self):
        # check the git status
        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=[],
            return_code=0,
            output_text="Checking out git status",
        )
        git_command = ["git", "--version"]

        if not self._execute_command(git_command):
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.LOG,
                command=[],
                return_code=0,
                output_text="Git not found!",
            )

    def get_git_root_folder(self) -> str:
        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=[],
            return_code=0,
            output_text=f"Get git root repo folder",
        )
        git_command = ["git", "rev-parse", "--show-toplevel"]
        result = self._execute_command(git_command)

        if result.returncode == 0:
            return result.stdout.strip()

        return ""

    def get_files_in_repo(self) -> List[str]:

        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=[],
            return_code=0,
            output_text=f"Get files in repo",
        )

        root_folder = self.get_git_root_folder()

        if len(root_folder) == 0:
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.LOG,
                command=[],
                return_code=0,
                output_text=f"No git root folder found, continue with abstract path",
            )
            root_folder = "."

        git_command = ["git", "-C", root_folder, "ls-files"]

        result = self._execute_command(git_command)

        if result.returncode != 0:
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.LOG,
                command=[],
                return_code=0,
                output_text=f"No files in git repo found!",
            )
            return []

        git_output = result.stdout.strip()
        files_in_project_lst = git_output.split(sep="\n")
        return files_in_project_lst
