import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tarot_logic import TarotDeck
from data_loader import load_tarot_dict

class TarotApp:
    IMAGE_FOLDER_PATH = os.path.join(os.path.dirname(__file__), 'images')
    BACKGROUND_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'background.jpg')

    def __init__(self, root):
        self.root = root
        self.root.title("Mystical Tarot Reader App")

        # Load tarot card data
        self.data = load_tarot_dict()
        self.deck = TarotDeck(self.data)

        # Set up the background image
        self.background_image = Image.open(self.BACKGROUND_IMAGE_PATH)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        # Create and pack the UI elements
        self.create_widgets()

    def create_widgets(self):
        # Card image label
        self.image_label = tk.Label(self.root, bg='black')
        self.image_label.pack(pady=10)

        # Card description label
        self.description_label = tk.Label(self.root, text="", wraplength=400, bg='#1e1e1e', fg='white', font=("Helvetica", 14, "italic"))
        self.description_label.pack(pady=10)

        # Draw card button
        self.draw_button = tk.Button(self.root, text="Draw Card", command=self.draw_card, bg='#5c5c5c', fg='white', font=("Helvetica", 14, "bold"))
        self.draw_button.pack(pady=20)

    def _load_image(self, image_file):
        image_path = os.path.join(self.IMAGE_FOLDER_PATH, image_file)
        img = Image.open(image_path)
        img = img.resize((400, 600), Image.ANTIALIAS)  # Resize to fit the screen
        return ImageTk.PhotoImage(img)

    def draw_card(self):
        card_name, card_info = self.deck.draw_card()
        self.display_image(card_info[6])  # card_info[6] is the image path
        self.description_label.config(text=self.deck.interpret_card((card_name, card_info)))

    def display_image(self, image_path):
        if image_path:
            img = self._load_image(image_path)
            self.image_label.config(image=img)
            self.image_label.image = img
        else:
            messagebox.showinfo("Info", "No image found for this card.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TarotApp(root)
    root.mainloop()
