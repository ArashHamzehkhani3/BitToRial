import Rial
import emoji
import Bit

def main():
    print("Welcome to my program")
    bit_price=Bit.get_bit()
    Rial_price=Rial.get_rial()
    print(emoji.emojize("₿:"),bit_price * Rial_price)
    print(emoji.emojize(":grinning_face_with_big_eyes:"))


    




main()