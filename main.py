"""A very nice main module!"""
import importlib
from pathlib import Path

from shutil import copyfile


year = 2021
day = 5


def _pre_processing(year: int, day: int):
    """Check whether the appropriate files exist and create them if needed."""
    print("test")

    data_dir_path = Path(f"data")
    if not data_dir_path.exists():
        data_dir_path.mkdir(parents=True)
        print(f"The input will be stored in: {data_dir_path}/{day}.input")

    solution_dir_path = Path(f"src")
    solution_path = Path("src/day{:02d}.py".format(day))
    if not solution_dir_path.exists():
        solution_dir_path.mkdir(parents=True)

    if not solution_path.exists():
        copyfile("templates/src.py", solution_path)
        print(f"A solution template has been created in: {solution_path}")

    test_dir_path = Path(f"tests")
    test_path = Path("tests/test_day{:02d}.py".format(day))
    if not test_dir_path.exists():
        test_dir_path.mkdir(parents=True)

    if not test_path.exists():
        copyfile("templates/test.py", test_path)
        print(f"A test template has been created in: {test_path}")
        print("⚠️ YOU NEED TO MODIFY THE IMPORTS IN THE TEST FILE! ⚠️")


def main() -> None:

    _pre_processing(year, day)

    runner_str = "src.day{:02d}".format(day)
    runner = importlib.import_module(runner_str)
    runner.run(year, day)


main()
