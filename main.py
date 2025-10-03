import GeminiAI
import tkinter as tk
from tkinter import messagebox


def main():
    user_prompt = entry_field.get();
    print(f"Sending prompt to Gemini: '{user_prompt}'")
    
    # Call the function from the imported module
    gemini_response = GeminiAI.send_to_gemini(user_prompt)
    
    print("\n--- Gemini's Response ---")
    print(gemini_response)
    messagebox.showinfo("Gemini AI", f"{gemini_response}")
#if __name__ == "__main__":
    #while True:
        #main()
        
# Create the main window
root = tk.Tk()
root.title("Tkinter Input Example")
root.geometry("400x150") # Set initial window size

# Create a label
label = tk.Label(root, text="Enter your message:")
label.pack(pady=10) # Add some vertical padding

# Create a text input field (Entry widget)
entry_field = tk.Entry(root, width=50)
entry_field.pack(pady=5) # Add some vertical padding

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=main)
submit_button.pack(pady=10) # Add some vertical padding

# Start the Tkinter event loop
root.mainloop()
