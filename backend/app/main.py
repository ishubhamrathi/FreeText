from hotkeys.listener import (
    HoldToTalkListener
)


def main():

    listener = (
        HoldToTalkListener()
    )

    print(
        "Hold Win + Alt to speak"
    )

    listener.listen()


if __name__ == "__main__":
    main()