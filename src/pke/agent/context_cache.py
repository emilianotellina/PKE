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



    def _normalize_options(
        self,
        options
    ):


        if options is None:

            return ()



        if isinstance(
            options,
            dict
        ):

            return tuple(

                sorted(

                    (

                        str(key),

                        self._normalize_value(value)

                    )

                    for key, value

                    in options.items()

                )

            )


        return self._normalize_value(
            options
        )



    def _normalize_value(
        self,
        value
    ):


        if hasattr(
            value,
            "name"
        ):

            return value.name



        if isinstance(
            value,
            dict
        ):

            return tuple(

                sorted(

                    (

                        str(key),

                        self._normalize_value(val)

                    )

                    for key, val

                    in value.items()

                )

            )


        if isinstance(
            value,
            list
        ):

            return tuple(

                self._normalize_value(item)

                for item

                in value

            )


        return str(
            value
        )



    def _key(
        self,
        fingerprint,
        task,
        target,
        options
    ):


        normalized_options = self._normalize_options(
            options
        )


        return str(

            (

                fingerprint,

                task,

                target,

                normalized_options

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