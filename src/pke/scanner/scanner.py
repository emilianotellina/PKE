from pathlib import Path

from pke.knowledge import (
    Project,
    Package,
    SourceFile
)

from .filters import DEFAULT_EXCLUDES
from .detector import LanguageDetector



class ProjectScanner:


    def __init__(self):

        self.detector = LanguageDetector()



    def scan(self, root):

        root = Path(root)

        root = root.resolve()

        project = Project(
            name=root.name,
            path=str(root)
        )


        packages = {}


        for file in root.rglob("*"):


            if not file.is_file():
                continue


            if any(
                part in DEFAULT_EXCLUDES
                for part in file.parts
            ):
                continue


            language = self.detector.detect(file)


            source = SourceFile(
                name=file.name,
                path=str(file),
                language=language
            )


            package_path = (
                file.parent
                .relative_to(root)
            )


            package_name = str(
                package_path
            )


            if package_name not in packages:

                packages[package_name] = Package(
                    name=package_name,
                    path=str(
                        file.parent
                    )
                )


            packages[package_name].files.append(
                source
            )


        project.packages = list(
            packages.values()
        )


        return project