from dataclasses import dataclass
from typing import Any



@dataclass
class ContextCacheEntry:


    key: str

    context: Any



class ContextCache:


    def __init__(
        self
    ):

        self.entries = {}



    def _key(
        self,
        fingerprint,
        task,
        target,
        options
    ):

        return str(
            (
                fingerprint,
                task,
                target,
                options
            )
        )



    def get(
        self,
        fingerprint,
        task,
        target=None,
        options=None
    ):


        key = self._key(
            fingerprint,
            task,
            target,
            options
        )


        entry = self.entries.get(
            key
        )


        if entry is None:

            return None


        return entry.context



    def put(
        self,
        fingerprint,
        task,
        target,
        options,
        context
    ):


        key = self._key(
            fingerprint,
            task,
            target,
            options
        )


        self.entries[key] = ContextCacheEntry(

            key=key,

            context=context

        )



    def clear(
        self
    ):

        self.entries.clear()