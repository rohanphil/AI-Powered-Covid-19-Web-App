# AI-Powered-Covid-19-Web-App
Flask based web app with a pretrained VGG19 model that can detect the presence of a Covid-19 infection in a patient from X-ray scans of the lungs. 


# Dataset
The dataset consists of two very distinct classes that are trained with a basic CNN model on top of a pretained VGG19 model. The infected X-Ray images were taken from Dr. Joseph Cohen's
dataset, which seems to be the only such dataset available to the public at this moment in time. The link to the dataset is given below:

https://github.com/ieee8023/covid-chestxray-dataset

The covid-19 positive images were only 25 in number. Thus, 25 images of X-Rays of the lungs of patients who had not been infected with the coronavirus but that may have 
had other respiratory conditions was compiled. The very low number of images forces image augumentation techniques to increase accuracy.

Feel free to contact me at rohanphil98@gmail.com for the compiled dataset. The pretrained model however, is present in the model folder.

# Flask Application

The main.py file is the main executable file of the project. Run it as follows:

IN A WINDOWS OS

SET FLASK_APP=main.py
flask run

IN A LINUX ENVIORNMENT

export FLASK_APP=main.py
flask run

Navigate to the given ip and port and upload the test images to get predictions.

# Disclaimer
The results are by no means a conclusive standard for diagnosing covid-19. It is merely a tool to provide aid, should it be necessary. 
I will work on enhancing the model as and when I get access to more data as we try to fight this pandemic. Until then, stay home, stay safe.
