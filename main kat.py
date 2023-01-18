from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

from API import getUrls

class AdoptCatApp(App):

    def build(self):
        layout = GridLayout(cols=3)
        layout.add_widget(Image(source='cat1.jpg'))
        layout.add_widget(Label(text='[b]Name:[/b] Whiskers\n[b]Age:[/b] 2 years\n[b]Breed:[/b] Siamese'))
        layout.add_widget(Button(text='Adopt', on_press=self.adopt_cat))

        layout.add_widget(Image(source='cat2.jpg'))
        layout.add_widget(Label(text='[b]Name:[/b] Mittens\n[b]Age:[/b] 1 year\n[b]Breed:[/b] Maine Coon'))
        layout.add_widget(Button(text='Adopt', on_press=self.adopt_cat))

        layout.add_widget(Image(source='cat3.jpg'))
        layout.add_widget(Label(text='[b]Name:[/b] snuske\n[b]Age:[/b]  year\n[b]Breed:[/b] Calico'))
        layout.add_widget(Button(text='Adopt', on_press=self.adopt_cat))

        return layout

    def adopt_cat(self, instance):
        print("Cat adopted!")

if __name__ == '__main__':
    AdoptCatApp().run()
