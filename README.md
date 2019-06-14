# sentence-annotation-tool
A sentence-level annotation tool written in TKinter. 
The tool is used to manually annotate open-ended survey comments provided by University students. 
The tool supports a two-level annotation scheme where each sentence is labelled with two types of annotations, namely type of sentiment and type of feedback, respectively. 
The sentiment label can either be positive or negative while each sentence is assigned to one and only one sentiment label. 
In contrast to the sentiment label, the feedback label is both multi-label (10 different values instead of two) 
and multi-class (a sentence can be assigned to more than one feedback label).  

# Requirements
* Anaconda (Python 3.6), pandas==0.23.0, scikit-learn==0.19.1, scipy==1.1.0, nltk==3.3


* Install dependencies `pip install -r requirements.txt`


# Data format 

* **Input file** should be formated as a CSV file with a header line. You should place the CSV file under the data folder. The CSV file should include the following headers:
`CSV_ID,DEPARTMENT,SURVEY_ID,AOS_TYPE,CODE,QUESTION_PROMPT,QUESTION_RESPONSE,QUESTION_RESPONDED`

* **SQLite** annotations are stored into an SQLite db. The db consists of only one table with the following attributes:

        | **Attribute** | **Data Type** |   
        | id | text |
        | comment_id | text |
        | department | text |
        | survey_id | text |
        | aos_typ | text |
        | code | text |
        | question | text |
        | comment | text |
        | sentence | text |
        | comment_created | text |
        | feedback_categories | text |
        | sentiment_category | text |
        | is_multi_label | Boolean |
        | annotator_name | text |
        
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
    

 