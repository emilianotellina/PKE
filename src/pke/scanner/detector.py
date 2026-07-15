from pathlib import Path


LANGUAGES = {
    ".py": "python",
    ".java": "java",
    ".kt": "kotlin",
    ".js": "javascript",
    ".ts": "typescript",
    ".cs": "csharp",
    ".go": "go",
    ".rs": "rust",
}


class LanguageDetector:


    def detect(self, path: Path):

        return LANGUAGES.get(
            path.suffix.lower(),
            "unknown"
        )