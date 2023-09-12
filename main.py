from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


def main():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process.name() == "chrome.exe":
                volume.SetMasterVolume(1, None)


if __name__ == "__main__":
    main()
