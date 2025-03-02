import cv2
import numpy as np

def apply_sharpen(image):
    """
    Aplica um filtro de nitidez a uma imagem.

    Args:
        image: A imagem a ser nitidada.

    Returns:
        A imagem nitidada.
    """
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

def apply_unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """
    Aplica um filtro de máscara de nitidez a uma imagem.

    Args:
        image: A imagem a ser nitidada.
        kernel_size: O tamanho do kernel (largura, altura).
        sigma: O desvio padrão do kernel gaussiano.
        amount: A quantidade de nitidez a ser aplicada.
        threshold: O limite para a máscara de nitidez.

    Returns:
        A imagem nitidada.
    """
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened