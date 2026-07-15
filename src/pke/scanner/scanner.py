from pathlib import Path

from .models import ProjectFile

from .filters import DEFAULT_EXCLUDES


class ProjectScanner:

    def scan(
        self,
        root
    ):

        root = Path(root)

        files = []

        for file in root.rglob("*"):

            if not file.is_file():
                continue

            if any(
                part in DEFAULT_EXCLUDES
                for part in file.parts
            ):
                continue

            files.append(

                ProjectFile(
                    path=file,
                    extension=file.suffix,
                    size=file.stat().st_size
                )

            )

        return files