import shutil
import os


def merge(inputPath, outputPath):
    if type(inputPath) is str:
        inputPath = [inputPath]
    elif type(inputPath) is list:
        pass
    else:
        raise TypeError("inputPath must be a string or a list of strings")

    os.makedirs(outputPath, exist_ok=True)
    os.makedirs(os.path.join(outputPath, "images"), exist_ok=True)
    os.makedirs(os.path.join(outputPath, "labels"), exist_ok=True)

    for root in inputPath:
        for path in os.listdir(root):
            for file in os.listdir(os.path.join(root, path)):
                if file.endswith(".txt"):
                    shutil.copy(
                        os.path.join(root, path, file),
                        os.path.join(outputPath, path, file),
                    )
                elif (
                    file.endswith(".jpg")
                    or file.endswith(".jpeg")
                    or file.endswith(".png")
                ):
                    shutil.copy(
                        os.path.join(root, path, file),
                        os.path.join(outputPath, path, file),
                    )
                else:
                    pass


path = os.getcwd()

merge(
    [
        os.path.join(path, "dataset", "train"),
        os.path.join(path, "dataset", "train-1"),
    ],
    os.path.join(path, "dataset", "train-merged"),
)

merge(
    [
        os.path.join(path, "dataset", "val"),
        os.path.join(path, "dataset", "val-1"),
    ],
    os.path.join(path, "dataset", "val-merged"),
)
