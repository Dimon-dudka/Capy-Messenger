# Copyright 2025 Dudka Studio
from .requirements_worker import RequirementsWorker


def main():
    requirements_worker = RequirementsWorker()
    requirements_worker.install_requirements()


if __name__ == "__main__":
    main()
