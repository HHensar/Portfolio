# Easy Image Model – Python Library
**Source Code** [github.com/HHensar/easy_image_model](https://github.com/HHensar/easy_image_model)

## How It Works
You organize your images into folders (one folder per category), and the library handles all the preprocessing automatically. No need to manually resize images, normalize pixel values, or write custom data loaders. Just point it at your data and train.

## Key Features
- Automatic image preprocessing (resizing, normalization)
- Batch training support for faster convergence
- Customizable hidden layers and input dimensions
- Save/load model weights as JSON
- Works with most common image formats (JPG, PNG, BMP, GIF, TIFF)
- Returns probability scores for all categories

## Installation
```bash
pip install easy-image-model
```

## Example Usage

```python
from easy_image_model import create_model, train_model_batch_folders, evaluate_model

# Define your categories
categories = ['Eagles', 'Penguins', 'Owls', 'Others']

# Create a model with 3 hidden layers
model = create_model([512, 256, 128], categories, img_size=224)

# Train on organized folders
folder_paths = {
    'Eagles': 'dataset/Eagles',
    'Penguins': 'dataset/Penguins',
    'Owls': 'dataset/Owls',
    'Others': 'dataset/Others'
}
model = train_model_batch_folders(model, folder_paths, batch_size=4, epochs=5)

# Evaluate a new image
result = evaluate_model(model, 'test_images/test1.jpg')
print(result)  # {'Eagles': 0.87, 'Penguins': 0.05, 'Owls': 0.23, 'Others': 0.1}
```

## Use Cases
The main goal was to make image classification as simple as possible. Instead of dealing with PyTorch's complexity, you just organize images into folders and call a few functions. Returns as JSON, for easy use.

## Technical Stack
Built on PyTorch with a focus on simplicity and ease of use. Released under MIT License. Requires Python 3.9+. Default image input size is 224x224 pixels, but this can be configured based on your dataset requirements.
