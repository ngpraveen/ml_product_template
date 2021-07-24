import gradio as gr
import sys


sys.path.insert(0, "../")

from app.app import make_prediction

def xyz(Sepal_Length, Sepal_Width, Petal_Length, Petal_Width):
    sl = float(Sepal_Length)
    sw = float(Sepal_Width)
    pl = float(Petal_Length)
    pw = float(Petal_Width)
    output = make_prediction(sl, sw, pl, pw)
    output = output.capitalize()
    return output 


Sepal_Length = gr.inputs.Slider(4.3, 7.9)
Sepal_Width = gr.inputs.Slider(2.0, 4.4)
Petal_Length = gr.inputs.Slider(1, 6.9)
Petal_Width = gr.inputs.Slider(0.1, 2.5)

'''
sl1 = 1.2
sw1 = 3.4
pl1 = 5.1
pw1 = 0.2
'''

#predict = make_prediction(sl1, sw1, pl1, pw1)

face = gr.Interface(fn=xyz, inputs=[Sepal_Length, Sepal_Width, Petal_Length, Petal_Width],
             outputs="text")
face.launch()
