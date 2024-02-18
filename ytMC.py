import pytchat
import pydirectinput
import time

VIDEO_ID = "ID"  # Replace with the ID of your YouTube video

def read_youtube_chat(video_id):
    chat = pytchat.create(video_id=video_id)

    while chat.is_alive():
        try:
            for c in chat.get().sync_items():
                message = c.message
                print(f"Received message: {message}")

                # Control Minecraft based on the chat message
                control_minecraft(message.lower())  # Convert to lowercase

        except Exception as e:
            print(f"An error occurred: {e}")

def control_minecraft(command):
    if "mouse left" in command:
        move_mouse(-500, 0)  # Adjust the values as needed
    elif "mouse right" in command:
        move_mouse(500, 0)  # Adjust the values as needed
    elif "mouse up" in command:
        look_up_down(-500)  # Adjust the values as needed
    elif "mouse down" in command:
        look_up_down(500)  # Adjust the values as needed
    elif "break" in command:
        left_click()
    elif "place" in command:
        right_click()
    elif command.isdigit() and 1 <= int(command) <= 10:
        select_inventory_slot(int(command))
    elif command.lower() == "q":
        drop_item()
    elif command.lower() == "jump":
        run_jump()
    elif command in ["w", "a", "s", "d"]:
        pydirectinput.keyDown(command)
        time.sleep(0.5)  # Adjust the duration as needed
        pydirectinput.keyUp(command)
    else:
        print(f"Unknown command: {command}")

def move_mouse(delta_x, delta_y):
    pydirectinput.moveRel(delta_x, delta_y)
    print(f"Moving mouse by ({delta_x}, {delta_y})")

def look_up_down(delta_y):
    pydirectinput.moveRel(0, delta_y)
    print(f"Looking up/down by {delta_y}")

def run_jump():
    pydirectinput.keyDown("w")  # Hold down sprint key
    jump()  # Perform the jump action
    pydirectinput.keyUp("w")  # Release sprint key
    print("Running Jump!")

def jump():
    pydirectinput.press("space")
    print("Jumping!")

def left_click():
    pydirectinput.mouseDown(button='left')
    time.sleep(1)  # Adjust the duration as needed
    pydirectinput.mouseUp(button='left')

def right_click():
    pydirectinput.mouseDown(button='right')
    time.sleep(1)  # Adjust the duration as needed
    pydirectinput.mouseUp(button='right')

def select_inventory_slot(slot_number):
    pydirectinput.press(str(slot_number))

def drop_item():
    pydirectinput.press("q")

# Replace "YOUR_VIDEO_ID" with the actual ID of your YouTube video
read_youtube_chat(VIDEO_ID)
