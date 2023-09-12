# Chrome Volume Fix

## Description
This program addresses an issue with the volume on Google Chrome by adjusting the audio settings using the `pycaw` library.

## Usage
1. Ensure you have Python installed on your system.
2. Install the required library by running:
   ```
   pip install pycaw
   ```
3. Clone this repository using the following command:
   ```
   git clone https://github.com/mayankpatibandla/Chrome-Volume-Fix.git
   ```
4. Navigate to the directory:
   ```
   cd Chrome-Volume-Fix
   ```
5. Run the program by executing:
   ```
   python main.py
   ```

## Code Explanation
The provided Python script leverages the `pycaw` library to interact with the Windows Core Audio API. It iterates through all active audio sessions and identifies those associated with Google Chrome (`chrome.exe`). For each Chrome session, it adjusts the master volume to 100%.

## Requirements
- [Python](https://www.python.org/downloads/)
- [pycaw library](https://pypi.org/project/pycaw/)

## Disclaimer
This program is provided as-is, without any warranties or guarantees. Use at your own risk.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
[Mayank Patibandla](https://github.com/mayankpatibandla)

## Contributions
Contributions are welcome! If you find any issues or have suggestions, feel free to open an [issue](https://github.com/mayankpatibandla/Chrome-Volume-Fix/issues) or create a pull request.

---

## Adding to Windows Task Scheduler

To run the Chrome Volume Fix program automatically, you can utilize the Windows Task Scheduler. Follow these steps:

1. **Search for Task Scheduler** in the Windows search bar and open it.

2. In the right-hand panel, click **Create Task...**.

3. Give your task a name and description.
  
5. Select the **Triggers** tab.

6. Click **New...**. From the dropdown, select **On workstation unlock** (or any other trigger that suits your needs) and click **Ok**.

7. Select the **Actions** tab.

8. Click **New...**. From the dropdown, select **Start a program**.

9. Click **Browse...** and navigate to the location where your `pythonw.exe` is installed. Select the file and click **Open**.

10. Navigate to the location where you cloned this repository and copy the path to `main.py`.

11. Paste this path into the **Add arguments (optional):** field (you may need to surround the path in quotes).

12. Press **Ok** and then press **Ok** to complete creating the task.

The task is now scheduled to run on the specified triggers.
