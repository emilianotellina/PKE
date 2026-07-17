import argparse

from pke.version import VERSION
from pke.core.config import ConfigManager
from pke.core.logging import LoggingManager
from pke.core.plugins import PluginManager
from pke.scanner import ProjectScanner
from pke.scanner import ProjectScanner
from pke.knowledge import KnowledgeGenerator
from pke.languages import (
    LanguageManager,
    create_default_registry
)

from pke.languages import LanguageAnalyzer

from pke.knowledge import (
    KnowledgePipeline
)
from pathlib import Path

from pke.parser.python_adapter import PythonAdapter
from pke.csr import CSRInspector


def main():

    parser = argparse.ArgumentParser(
        prog="pke"
    )


    parser.add_argument(
        "--version",
        action="store_true"
    )


    parser.add_argument(
        "command",
        nargs="?"
    )

    parser.add_argument(
       "path",
        nargs="?",
        default="."
    )

    


    args = parser.parse_args()



    if args.version:

        print(
            f"PKE {VERSION}"
        )

        return


    if args.command == "plugin":
        manager = PluginManager()
        print(
            "Installed plugins:"
        )
        for plugin in manager.registry.all():
            print(
                plugin.name,
                plugin.version
            )
        return

    if args.command == "scan":
        scanner = ProjectScanner()
        project = scanner.scan(
            args.path
        )


        print(
            f"Project: {project.name}"
        )


        print(
            f"Packages: {len(project.packages)}"
        )


        files = sum(
            len(p.files)
            for p in project.packages
        )


        print(
            f"Files: {files}"
        )
        return


    if args.command == "generate":

        scanner = ProjectScanner()


        project = scanner.scan(
            args.path
        )


        registry = create_default_registry()


        manager = LanguageManager(
            registry
        )


        analyzer = LanguageAnalyzer(
            manager
        )


        generator = KnowledgeGenerator(
            "knowledge"
        )


        pipeline = KnowledgePipeline(
            analyzer,
            generator
        )


        pipeline.execute(
            project
        )


        print(
            "Knowledge generated"
        )

        return

    if args.command == "inspect":

        path = Path(args.path)


        if not path.exists():

            print(
                f"File not found: {path}"
            )

            return


        source = path.read_text()


        graph = PythonAdapter().parse(
            source
        )


        inspector = CSRInspector(
            graph
        )


        print(
            inspector.inspect()
        )

        return

    logging = LoggingManager()
    logging.setup()



    logger = logging.get_logger(
        "pke"
    )


    config = ConfigManager()

    cfg = config.load()


    logger.info(
        "PKE started"
    )


    logger.info(
        f"Project: {cfg.project.name}"
    )



if __name__ == "__main__":
    main()