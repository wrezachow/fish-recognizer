import sys
print(f"Python runtime: {sys.version}")
from fastai.vision.all import *
import gradio as gr

fish_types_labels = [
'Barramundi Fish',
'Bombay Duck Fish',
'Catla Fish',
'Hilsa Fish',
'Indian Featherback Fish',
'Mrigal Carp Fish',
'Pabda Catfish',
'Rohu Fish',
'Salmon Fish',
'Silver Pomfret'
]

model = None
load_error = None
try:
    # Force CPU to avoid CUDA dependency on Spaces
    model = load_learner('models/fish-recognizer-v8.pkl', cpu=True)
except Exception as e:
    load_error = str(e)
    print(f"\u26a0\ufe0f Failed to load learner: {load_error}")

def recognize_image(image):
  if model is None:
    # Surface a friendly error in the UI instead of 500 at startup
    raise gr.Error(f"Model failed to load: {load_error or 'unknown error'}")
  pred, idx, probs = model.predict(image)
  print(pred, probs)
  return dict(zip(fish_types_labels, map(float, probs)))


image = gr.Image(type="pil", label="Upload fish image")
label = gr.Label(num_top_classes=5)
examples = [
    'test_images/image1.jpg',
    'test_images/image2.jpg',
    'test_images/image3.jpg',
    'test_images/image4.jpeg'
    ]

demo = gr.Interface(
  fn=recognize_image,
  inputs=image,
  outputs=label,
  examples=examples,
  cache_examples=False,  # avoid calling predict at startup
)

demo.launch(inline=False)
