# Copyright 2025 Dudka Studio
from .core_utils import *
from Tools.Format.git_usage import GitWorker


class RequirementsWorker(CoreCommandExecutor):
    __requirements_list = []
    __file_path = ""

    def __init__(self):
        git_worker = GitWorker()
        self.__file_path = (
            git_worker.get_git_root_folder() + "/Tools/Format/requirements.txt"
        )

        # get list of all requirements for current project
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                file_content = file.readlines()
                self.__requirements_list = [line.strip() for line in file_content]
        except Exception as ex:
            CoreLog.formatted_log(
                log_type=CoreLog.LogType.LOG,
                command=[],
                return_code=0,
                output_text=f"Error by opening file: {self.__file_path}. Exception: {ex}",
            )
            raise FileNotFoundError(
                f"Error by opening file: {self.__file_path}. Exception: {ex}"
            )

    # returns list of all not installed requirements
    def __check_requirements(self) -> List[str]:
        missing_requirements = []

        # check what requirement is not installed
        for requirement in self.__requirements_list:
            command = ["pip", "show", requirement.split("==")[0]]

            result = self._execute_command(command)

            if result.returncode != 0:
                missing_requirements.append(requirement)

        return missing_requirements

    # install all missing requirements
    def install_requirements(self):
        missing_requirements = self.__check_requirements()

        for requirement in missing_requirements:
            command = ["pip", "install", "--quiet", requirement]

            result = self._execute_command(command)

            if result.returncode != 0:
                CoreLog.formatted_log(
                    log_type=CoreLog.LogType.LOG,
                    command=[],
                    return_code=0,
                    output_text=f"Error by installing requirement: {requirement}",
                )
                raise FileExistsError("Error: Not all packages are installed")

        CoreLog.formatted_log(
            log_type=CoreLog.LogType.LOG,
            command=[],
            return_code=0,
            output_text=f"All packages successfully installed",
        )
