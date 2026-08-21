import glob, os

current_dir = 'd:/VSCode_code/data_practice/dataset'
valid_dir = 'd:/VSCode_code/data_practice/dataset/Rock_paper_scissors/valid'
train_dir = 'd:/VSCode_code/data_practice/dataset/Rock_paper_scissors/train'

file_train = open('d:/VSCode_code/data_practice/dataset/Rock_paper_scissors/train.txt', 'w')
file_test = open('d:/VSCode_code/data_practice/dataset/Rock_paper_scissors/valid.txt', 'w')

counter = 1

for pathAndFilename in glob.iglob(os.path.join(valid_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_test.write(f"data/rock-paper-scissors/valid/{title}.jpg\n")

for pathAndFilename in glob.iglob(os.path.join(train_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_train.write(f"data/rock-paper-scissors/train/{title}.jpg\n")