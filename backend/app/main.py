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

    print(
        "\nStopping FreeText..."
    )

    running = False


def main():

    global running

    signal.signal(
        signal.SIGINT,
        shutdown
    )

    listener = (
        HoldToTalkListener()
    )

    listener.listen()

    print(
        "FreeText started"
    )

    print(
        "Hold Win + Alt"
    )

    while running:

        time.sleep(
            1
        )

    listener.stop()

    print(
        "Shutdown complete"
    )


if __name__ == "__main__":

    main()