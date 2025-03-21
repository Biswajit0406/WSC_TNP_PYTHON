# import os
# import time
#
#
# class Screenshot:
#     @staticmethod
#     def take_screenshot(driver, name="Screenshot"):
#         """Capture a screenshot and save it with a timestamp in the specified directory."""
#
#         # Define absolute screenshot directory path
#         screenshot_dir = r"C:\Users\KIIT\PycharmProjects\pythonProject6\Screenshot"
#
#         # Ensure the screenshots directory exists
#         os.makedirs(screenshot_dir, exist_ok=True)
#
#         # Generate timestamped filename
#         timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
#         filename = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
#
#         # Save the screenshot
#         driver.save_screenshot(filename)
#         print(f"Screenshot saved at: {filename}")
#
#         return filename  # Return the screenshot path for pytest-html report attachment
