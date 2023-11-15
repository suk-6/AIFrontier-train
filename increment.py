import cv2
import numpy as np
import os
from tqdm import tqdm


def brightness(image, alpha=1.5, beta=10):
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted


def whiteBalance(image):
    blueCoefficient = np.random.uniform(0.5, 1.5)
    redCoefficient = np.random.uniform(0.5, 1.5)
    image[:, :, 0] = np.clip(image[:, :, 0] * blueCoefficient, 0, 255)
    image[:, :, 2] = np.clip(image[:, :, 2] * redCoefficient, 0, 255)
    return image


def augment(inputDir, outputDir, brightnessAlpha=1.5, brightnessBeta=10):
    imageDir = os.path.join(inputDir, "images")
    labelDir = os.path.join(inputDir, "labels")

    for filename in tqdm(os.listdir(imageDir)):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            imagePath = os.path.join(imageDir, filename)
            image = cv2.imread(imagePath)

            labelPath = os.path.join(
                labelDir,
                filename.replace(".jpg", ".txt")
                .replace(".jpeg", ".txt")
                .replace(".png", ".txt"),
            )
            with open(labelPath, "r") as labelFile:
                labelData = labelFile.read().strip()

            augmentedImage = brightness(
                image, alpha=brightnessAlpha, beta=brightnessBeta
            )
            augmentedImage = whiteBalance(augmentedImage)

            outputImageDir = os.path.join(outputDir, "images")
            outputLabelDir = os.path.join(outputDir, "labels")

            os.makedirs(outputImageDir, exist_ok=True)
            os.makedirs(outputLabelDir, exist_ok=True)

            filename = f"{filename.split('.')[0]}-augmented.{filename.split('.')[-1]}"
            outputImagePath = os.path.join(outputImageDir, filename)
            outputLabelPath = os.path.join(
                outputLabelDir,
                filename.replace(".jpg", ".txt")
                .replace(".jpeg", ".txt")
                .replace(".png", ".txt"),
            )

            cv2.imwrite(outputImagePath, augmentedImage)

            with open(outputLabelPath, "w") as labelFile:
                labelFile.write(labelData)


augment("dataset/train", "dataset/train-1")
augment("dataset/val", "dataset/val-1")
