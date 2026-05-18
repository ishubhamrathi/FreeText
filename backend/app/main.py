import time

from hotkeys.listener import (
    HoldToTalkListener
)

from tray.service import (
    TrayService
)


running = True


def shutdown():

    global running

    print(
        "Shutting down"
    )

    running = False


def main():

    global running

    listener = (
        HoldToTalkListener()
    )

    listener.listen()

    tray = (
        TrayService(
            shutdown
        )
    )

    tray.run()

    print(
        "FreeText running"
    )

    print(
        "Use Win + Alt"
    )

    while running:

        time.sleep(
            1
        )

    listener.stop()

    tray.stop()


if __name__ == "__main__":

    main()