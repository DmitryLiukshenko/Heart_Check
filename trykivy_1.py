# внешний вид приложения описывается в том (единственном) экземпляре класса App, 
# у которого вызывается run(). 

from kivy.app import App

# Создадим класс-наследник App. В нём будет дописываться функционал приложения.
class MyApp(App):
   pass
#оваожывдодав
app = MyApp()
app.run()
