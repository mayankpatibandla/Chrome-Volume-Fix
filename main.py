from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


def main():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == "chrome.exe":
            session._ctl.QueryInterface(ISimpleAudioVolume).SetMasterVolume(1.0, None)


if __name__ == "__main__":
    main()
