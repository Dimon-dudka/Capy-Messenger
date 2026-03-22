# Copyright 2025 Dudka Studio

import os
from enum import Enum
from .copyright import CopyrightChecker
from .python_format import BlackFormatter


class InspectionTypes(Enum):
    NONE = 0
    COPYRIGHT = 1
    PYTHON = 2


class InspectionActions(Enum):
    CHECK = 1
    FORMAT = 2


INSPECTION_MAP = {
    "1. Copyright": InspectionTypes.COPYRIGHT,
    "2. Python": InspectionTypes.PYTHON,
}

COPYRIGHT_MAP = {
    "1. Check copyright": InspectionActions.CHECK,
    "2. Format copyright": InspectionActions.FORMAT,
}

BLACK_FORMATTER_MAP = {
    "1. Check code-style": InspectionActions.CHECK,
    "2. Format code-style": InspectionActions.FORMAT,
}


class Inspector:
    __copyright_checker: CopyrightChecker
    __black_formatter: BlackFormatter

    COPYRIGHT_ACTIONS = {}
    BLACK_ACTIONS = {}

    def __init__(self):
        self.__copyright_checker = CopyrightChecker()
        self.__black_formatter = BlackFormatter()

        self.COPYRIGHT_ACTIONS[InspectionActions.CHECK] = (
            self.__copyright_checker.check_copyright
        )
        self.COPYRIGHT_ACTIONS[InspectionActions.FORMAT] = (
            self.__copyright_checker.format_copyright
        )

        self.BLACK_ACTIONS[InspectionActions.CHECK] = (
            self.__black_formatter.check_format
        )
        self.BLACK_ACTIONS[InspectionActions.FORMAT] = (
            self.__black_formatter.format_files
        )

        os.system("cls")
        self.__startup_module()

    def __startup_module(self):

        user_input = self.__process_menu(INSPECTION_MAP)

        selected_inspection_type = InspectionTypes.NONE
        for inspection_type in InspectionTypes:
            if inspection_type.value == user_input:
                selected_inspection_type = inspection_type
                break

        if selected_inspection_type.value == InspectionTypes.COPYRIGHT.value:
            user_input = self.__process_menu(COPYRIGHT_MAP)
            inspection_type = InspectionActions(user_input)
            action = self.COPYRIGHT_ACTIONS[inspection_type]
            os.system("cls")
            action()
        elif selected_inspection_type.value == InspectionTypes.PYTHON.value:
            user_input = self.__process_menu(BLACK_FORMATTER_MAP)
            inspection_type = InspectionActions(user_input)
            action = self.BLACK_ACTIONS[inspection_type]
            os.system("cls")
            action()

        print("\nEnter something to continue...")
        user_input = input()
        self.__startup_module()

    def __process_menu(self, input_dict: dict) -> int:
        user_input = -1
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.__print_inspection_type_menu(input_dict)

            user_input = self.__get_user_input(1, len(input_dict))
            if user_input != -1:
                break

        return user_input

    def __get_user_input(self, lower_bound: int, upper_bound: int) -> int:
        try:
            user_input = int(input())
        except ValueError:
            user_input = -1
        if user_input < lower_bound or user_input > upper_bound:
            return -1
        return user_input

    def __print_inspection_type_menu(self, menu_content: dict):
        for i in range(20):
            print("-", end="")

        print("\nCode Inspector")

        for i in range(20):
            print("-", end="")

        print("\n")

        for inspection in menu_content:
            print(inspection)

        print("")

        for i in range(20):
            print("-", end="")

        print("\nEnter your choice")

        for i in range(20):
            print("-", end="")

        print("\n")


def main():
    Inspector()


if __name__ == "__main__":
    main()
