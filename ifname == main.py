#todo if__name__==__main__: (this statemement can be imported or run standalone)
# functions and classes in this module can be reused
# without the main block of code existing
#todo ex.library - import library for functionality
#   when running library directly displays a help page

def fav_food(food):
    print(f"My favorite food is {food}")
def main():
    fav_food("pizza")
    fav_food("ice cream")
    fav_food("pasta")
    print("Done!")

if __name__ == "__main__":
    main()