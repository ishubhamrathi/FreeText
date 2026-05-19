import time

import sounddevice as sd

from path_setup import add_app_to_path


add_app_to_path()

import config.settings as settings

settings.LIVE_PROCESS_INTERVAL = settings.LIVE_STRIDE_SECONDS

from streaming.service import (
    StreamService
)


service = StreamService()

service.start()


def callback(
    indata,
    frames,
    time_info,
    status
):

    service.append_audio(
        indata
    )


with sd.InputStream(
    samplerate=16000,
    channels=1,
    callback=callback
):

    print(
        "Speak for testing..."
    )

    time.sleep(20)

service.stop()
