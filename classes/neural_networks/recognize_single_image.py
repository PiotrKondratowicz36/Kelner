import torch
import torchvision.transforms as transforms
import PIL.Image as Image

platestates = ['pusty', 'pelny']

model = torch.load('neural_networks/recognizeplate.pth')

mean = [0.7676, 0.7290, 0.6800]
std = [0.1982, 0.2108, 0.2328]

image_transforms = transforms.Compose([
    transforms.Resize((200, 200)),
    transforms.ToTensor(),
    transforms.Normalize(torch.Tensor(mean), torch.Tensor(std))
])


def classify(model, image_transforms, image_path, classes):
    model = model.eval()
    image = Image.open(image_path)
    image = image_transforms(image).float()
    image = image.unsqueeze(0)

    output = model(image)
    _, predicted = torch.max(output.data, 1)
    return f'Talerz jest {classes[predicted.item()]}'

# classify(model, image_transforms, 'neural_networks/testplates/zastawaikea.jpg', platestates)
