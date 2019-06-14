# sentence-annotation-tool
A sentence-level annotation tool written in TKinter. 
The tool is used to manually annotate open-ended survey comments provided by University students. 
The tool supports a two-level annotation scheme where each sentence is labelled with two types of annotations, namely type of sentiment and type of feedback, respectively. 
The sentiment label can either be positive or negative while each sentence is assigned to one and only one sentiment label. 
In contrast to the sentiment label, the feedback label is both multi-label (10 different values instead of two) 
and multi-class (a sentence can be assigned to more than one feedback label).  

# Requirements
* Anaconda (Python 3.6)

* pandas==0.23.0
* scikit-learn==0.19.1
* scipy==1.1.0
* nltk==3.3


* Run

`pip install -r requirements.txt`



