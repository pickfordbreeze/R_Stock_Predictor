import ipyvuetify as v
from ipywidgets import Output
import IPython.display




class home_page(object):
    def __init__(self):
        self.make_ux()
        self.show()

    def make_ux(self):
        self.but1 = v.Btn(class_='ma-2', children = ['but1'])
        self.but2 = v.Btn(class_='ma-2', children = ['but2'])
        self.but3 = v.Btn(class_='ma-2', children = ['but3'])
        self.but4 = v.Btn(class_='ma-2', children = ['but4'])

        self.layout = v.Html(children = [
            self.but1, self.but2, self.but3, self.but4
        ])

    def show(self):
        display(self.layout)

# b= home_page()
# display(b)