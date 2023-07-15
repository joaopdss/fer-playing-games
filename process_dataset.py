import os
import re
import cv2

def process_image(image):
	image = cv2.resize(image, (48, 48))
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	return image


path_dataset = r"C:\Users\devjo\Documents\Projects\fer-playing-games\dataset"
emotions = ["angry", "happy", "neutral", "sad", "surprise"]

if not os.path.isdir(path_dataset):
	os.makedirs(path_dataset)

	for emotion in emotions:
		os.makedirs(f"{path_dataset}/{emotion}")

folders = ["fer2013 train", "affectnet"]
path_fer = r"C:\Users\devjo\Documents\Projects\fer datasets"

for emotion in emotions:
	for folder in folders:
		for img_name in os.listdir(f"{path_fer}/{folder}/{emotion}/"):
			img = cv2.imread(f"{path_fer}/{folder}/{emotion}/{img_name}")
			img_processed = process_image(img)
			cv2.imwrite(f"{path_dataset}/{emotion}/{img_name}", img)

path_expw = r"C:\Users\devjo\Documents\Projects\fer datasets\ExpwCleaned"
names_imgs = ["angry_american", "angry_actor", "angry_black", "angry_boy", "angry_expression", "angry_face",
                "angry_girl", "angry_lady", "angry_man", "angry_people", "angry_woman", "amazed_family",
              "crying_actor", "crying_expression", "crying_face", "crying_girl", "crying_lady", "crying_man",
              "crying_people", "surprised_expression", "shocked_expression"]

for emotion in emotions:
	for img_name in os.listdir(path_expw):
		splits = re.split("_", img_name)
		if splits[0] in names_imgs and splits[1] in names_imgs:
			img = cv2.imread(f"{path_expw}/{img_name}")
			img_processed = process_image(img)
			cv2.imwrite(f"{path_dataset}/{emotion}/{img_name}", img)
