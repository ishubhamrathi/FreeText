import signal
import time

from hotkeys.listener import (
    HoldToTalkListener
)


running = True


def shutdown(
    signum,
    frame
):

    global running

    running = False


def main():

    listener = (
        HoldToTalkListener()
    )

    listener.listen()

    print(
        "Hold Win + Alt"
    )

    listener.controller \
        .streaming \
        .debug_ui \
        .overlay \
        .run()


if __name__ == "__main__":

    main()