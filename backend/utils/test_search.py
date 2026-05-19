from path_setup import add_app_to_path


add_app_to_path()

from history.search_service import (
    SearchService
)


service = SearchService()

results = service.search(
    "FreeText"
)

for item in results:

    print(
        item
    )
