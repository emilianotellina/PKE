from dataclasses import dataclass, field

from .context_profile import ContextProfile



@dataclass
class AgentProfile:


    name: str


    description: str = ""


    context_profile: ContextProfile = field(
        default_factory=ContextProfile
    )


    capabilities: list[str] = field(
        default_factory=list
    )


    metadata: dict = field(
        default_factory=dict
    )



    def has_capability(
        self,
        capability
    ):

        return capability in self.capabilities



    def to_dict(
        self
    ):

        return {

            "name":
                self.name,

            "description":
                self.description,

            "context_profile":
                self.context_profile.to_dict(),

            "capabilities":
                self.capabilities,

            "metadata":
                self.metadata

        }