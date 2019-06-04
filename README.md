# data_classification_with_python
classifying data  with machine learning tools


Description
After making some research, I realized this task is a machine learning problem, 
more specifically a classification problem. In this kind of problems, a set of data has to be labeled. 
From the labeled data, the machine learns the labeling “rules” and implements them to classify unlabeled data. 
I received a Train file, labeled, from which the machine learn, and a Test file which the algorithm has to label. 

Methods
I believe that the way to solve this classification problem is using a supervised learning algorithm.
The Train dataset file has ~1400 labeled rows, while the Test dataset file has ~700 unlabeled rows. 
I split the Train file into two files- ‘Train_1000.csv’ with ~1000 random rows from original Train file, and ‘TrainValidation400.csv’ 
with 400 rows from original Train file.
Supervised learning algorithms are useful when a train labeled dataset is available. 
The algorithm I used learns the pattern from the Train_1000 file and will label the 400 rows from TrainValidation file. 
This allows check each supervised algorithm accuracy before implementing it on the real target- the Test dataset. 
(Attached “files_splitting.py” python file I wrote to easily and randomly split the Train dataset to Train_1000 
and TrainValidation csv files). 
I am aware there are library functions to split data frame to Train-Validation-Test data frames but this time I decided 
to keep it simple with my data splitting script.
The file “validation.py” has validation code, which runs the labeled 1000 train samples as “train” and the other 400 labeled data as “test”, 
as if they were not labeled. It allows us to compare the algorithm prediction to the real 400 rows labels. 
This comparison can be seen in “validation.csv”.
There is a variety of classification algorithms which can be used for this task. I chose Naive Bayes algorithm.  Ideally, I would run a few relevant algorithms on the 1000 train rows and implement on 400 validation rows, check accuracy level for each algorithm and choose the best one.
The real Test: I ran the Naïve Bayes algorithm with all Train dataset supplied as Train, and with Test Dataset as Test. 
The code is in “classification.py” and the file “classification.csv” has Test row ID and matching predicted label.

Difficulties / Limitation
Some limitation to accuracy of these algorithms may be:
Missing data in some rows in either Train or Test datasets.
Inaccurate data in either Train or Test datasets. 
Train data is too specific and does not cover all the relevant cases.
Train data is too small.
Suggestions for further studies
Splitting the Train labeled data to “Train” and “Validation” files. 
This way allows us to test and run the algorithms on “Validation” which is actually already known and labeled .
By doing this you can give score to each algorithm and each Train data size . 
Doing this can help the analyst improve his work by making the following decisions:
Set optimal Train data size to get good validation score.
Choose best algorithm for labeling a certain set of data.
