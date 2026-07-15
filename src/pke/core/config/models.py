from pydantic import BaseModel, Field


class ProjectConfig(BaseModel):

    name: str = "default"

    path: str = "."


class LoggingConfig(BaseModel):

    level: str = "INFO"

    file: str | None = None


class PluginConfig(BaseModel):

    enabled: list[str] = Field(
        default_factory=list
    )


class PKEConfig(BaseModel):

    project: ProjectConfig = ProjectConfig()

    logging: LoggingConfig = LoggingConfig()

    plugins: PluginConfig = PluginConfig()