from path_setup import add_app_to_path

add_app_to_path()

from history.tag_service import (
    TagService
)


service = TagService()

service.update_tags(
    1,
    "meeting,idea"
)

print(
    "Tags updated"
)