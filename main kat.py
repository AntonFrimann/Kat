from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.button import Button
import random
from API import getUrl

class AdoptCatApp(App):

        Catname=[ "Pasghetti", "Charles", "Whiskers", "Honey", "Boxers", "Killer", "Tiger", "House", "Doctor", "Jasper", "Gizmo", "Coco", "Kitty",
               "Nala", "Jasmine", "Ruby", "Gåstog", "Milo", "Buddy", "Geroge", "Oswell", "Toto", "Pumpkin", "Potato", "Turtle", "Tuttle", "Tutty", "Icecream",
               "James", "Jojo", "Pauline", "Paula", "Winston", "Winnie", "Bubbles", "Popcorn","Pickles", "Burger", "Chest", "Loppe", "Lollie", "Chester", "Doggy","Testikel", "Nixon", "Nixion",
                "AIDS", "Oldie", "Bear", "Lucifer", "Devil", "Chonkus"]
        random_name = random.choice(Catname)



        random_age = random.randint(1,18)

        Catbreeds=["Siamese", "American Bobtail", "Abyssinian", "American Curl", "American Shorthair", "American Wirehair",
                   "Balinese-Javanese","Bengal", "Birman", "Bombay", "British Shorthair", "Burmese", "Chartreux", "Exotic Shorthair",
                   "European Burmese"]
        random_breed = random.choice(Catbreeds)


        def build(self):
            layout = GridLayout(cols=3)
            layout.add_widget(AsyncImage(source=getUrl()))
            layout.add_widget(Label(text='[b]Name:[/b] {}\n[b]Age:[/b] {} years\n[b]Breed:[/b] {}'.format(random.choice(self.Catname), random.randint(1,18), random.choice(self.Catbreeds))))
            layout.add_widget(Button(text='Adopt', on_press=self.adopt_cat))

            layout.add_widget(AsyncImage(source=getUrl()))
            layout.add_widget(Label(text='[b]Name:[/b] {}\n[b]Age:[/b] {} years\n[b]Breed:[/b] {}'.format(random.choice(self.Catname), random.randint(1,18), random.choice(self.Catbreeds))))
            layout.add_widget(Button(text='Adopt', on_press=self.adopt_cat))

            layout.add_widget(AsyncImage(source=getUrl()))
            layout.add_widget(Label(text='[b]Name:[/b] {}\n[b]Age:[/b] {} years\n[b]Breed:[/b] {}'.format(random.choice(self.Catname), random.randint(1,18), random.choice(self.Catbreeds))))
            layout.add_widget(Button(text='Adopt', on_press=self.adopt_cat))



            return layout

        def adopt_cat(self, instance):
            print("Cat adopted!")

if __name__ == '__main__':
        AdoptCatApp().run()
