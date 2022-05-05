import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from openpyxl.chart import BarChart, Reference
from matplotlib import pyplot as plt
import numpy as np





class MyGrid(FloatLayout):

    statlist = [0, 0, 0, 0] # lista som representerar antalet tryck på respektive gubbe



    angry = ObjectProperty(None)
    langry = ObjectProperty(None)
    lhappy = ObjectProperty(None)
    happy = ObjectProperty(None)
    show_graph = ObjectProperty(None)






    def knapp_tryck(self,instance):

        print(self.statlist)

        if instance == self.angry:
            self.statlist[0] += 1

        elif instance == self.langry:
            self.statlist[1] += 1

        elif instance == self.lhappy:
            self.statlist[2] += 1
        else:
            self.statlist[3] += 1

        if instance == self.show_graph:
            plt.show()

        angryornot = ['Angry', 'Langry', 'Lhappy', 'Happy']
        pos = np.arange(len(angryornot))
        plt.bar(pos,self.statlist,color='grey',edgecolor='black')
        plt.xticks(pos,angryornot)
        plt.title('Responsee',fontsize=20)
        plt.legend()













class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()




