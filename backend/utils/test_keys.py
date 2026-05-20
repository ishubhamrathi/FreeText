from path_setup import (
    add_app_to_path
)

add_app_to_path()

from ai.key_store import (
    KeyStore
)


store = (
    KeyStore()
)

store.save(
    "openai",
    "demo-key"
)

print(
    store.get(
        "openai"
    )
)