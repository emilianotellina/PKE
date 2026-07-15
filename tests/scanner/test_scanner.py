from pathlib import Path

from pke.scanner import ProjectScanner


def test_scanner_returns_project():


    scanner = ProjectScanner()


    project = scanner.scan(
        Path(".")
    )


    assert project.name

    assert project.packages is not None



def test_files_are_detected():


    scanner = ProjectScanner()


    project = scanner.scan(
        Path(".")
    )


    total = sum(
        len(p.files)
        for p in project.packages
    )


    assert total > 0