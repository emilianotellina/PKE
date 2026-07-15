from pathlib import Path

from pke.scanner import ProjectScanner


def test_scan():

    scanner = ProjectScanner()

    files = scanner.scan(Path("."))

    assert len(files) > 0