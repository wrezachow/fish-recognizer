# south-asian-fish-recognition
Recognizes 10 different types of fishes that can be found in south asia:

| Image | Name |
|:------:|:-----|
| <img src="docs/fishies/Hilsa.jpg" width="160"/> | **Hilsa Fish** |
| <img src="docs/fishies/Rohu.png" width="160"/> | **Rohu Fish** |
| <img src="docs/fishies/Catla.jpeg" width="160"/> | **Catla Fish** |
| <img src="docs/fishies/Barramundi.jpeg" width="160"/> | **Barramundi Fish** |
| <img src="docs/fishies/Mrigal.jpeg" width="160"/> | **Mrigal Carp Fish** |
| <img src="docs/fishies/Indian Featherback.jpg" width="160"/> | **Indian Featherback Fish** |
| <img src="docs/fishies/Salmon.jpeg" width="160"/> | **Salmon Fish** |
| <img src="docs/fishies/Pabda.jpg" width="160"/> | **Pabda Catfish** |
| <img src="docs/fishies/Silver Pomfret.jpg" width="160"/> | **Silver Pomfret** |
| <img src="docs/fishies/Bombay Duck.jpeg" width="160"/> | **Bombay Duck Fish** |

# Why did I make this?
I created South Asian Fish Recognition to solve a real problem I face at the local bazaar when buying fish. I wanted to know the fish’s name beforehand and check if the fish fits my taste before buying. This would help because I wouldn't end up purchasing something I didn't like. <br/>

# Preparing Data
Data was collected from DuckDuckGo<br/>
DataLoader was set up using the fast.ai DataBlock API<br/>
fast.ai provided default data augumentation which operates in GPU. more details in 'notebooks/data_prepare.ipynb' <br/>
# Data Training
### Model Benchmark
| Model         | Avg. Accuracy (%) |    Avg. Training Time   | Confusion Matrix |
| :------------ | :---------------: | :---------------------: | :------: |
| **ResNet-34** |     **98.58**     | **≈ 1 min 6 s / epoch** | <img src="docs/confusion_matrix/resnet34.png"> |
| **ResNet-50** |       94.42       |   ≈ 1 min 11 s / epoch  | <img src="docs/confusion_matrix/resnet50.png"> |
| **AlexNet**   |       94.02       |   ≈ 1 min 2 s / epoch  | <img src="docs/confusion_matrix/alexnet.png" width="298" height="310"> |

### Chosen Model - Resnet-34
Resnet-34 had the highest accuracy among the three and although it did have a higher average time than Alexnet, the tradeoff for a higher average accuracy makes it worth it. 

# Data Cleaning
Cleaned Data using fast.ai's ImageClassifierCleaner. <br/>
The dataset initially had 3,772 images and after cleanning it reduced to 3,415.<br/>

# Deploying the model
I deployed the model with HuggingFace Spaces Gradio App. The implementation is in the 'deployment' folder. It can also be found [here](https://huggingface.co/spaces/wrezachow/south-asian-fish-recognition) <br/>
<img src = "deployment/thumbnail.png">
<br/>

# API integration wit GitHub pages
deployed the model [here](https://github.com/wrezachow/south-asian-fish-recognition) in GitHub Pages Website. 
I used LLMs to generate some of the HTML and CSS for better visuals when uploading photos.
You can view the scripts in 'docs' part of the repo.

### Home page

