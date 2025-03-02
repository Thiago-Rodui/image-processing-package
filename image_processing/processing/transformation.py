import cv2
import numpy as np

def resize_image(image, size):
    """
    Redimensiona uma imagem para um tamanho especificado.

    Args:
        image: A imagem a ser redimensionada.
        size: Uma tupla (largura, altura) especificando o novo tamanho.

    Returns:
        A imagem redimensionada.
    """
    return cv2.resize(image, size)

def rotate_image(image, angle):
    """
    Rotaciona uma imagem por um ângulo especificado.

    Args:
        image: A imagem a ser rotacionada.
        angle: O ângulo de rotação em graus.

    Returns:
        A imagem rotacionada.
    """
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def flip_image(image, flip_code):
    """
    Espelha uma imagem horizontalmente, verticalmente ou ambas.

    Args:
        image: A imagem a ser espelhada.
        flip_code: Código de espelhamento (0 para vertical, 1 para horizontal, -1 para ambos).

    Returns:
        A imagem espelhada.
    """
    return cv2.flip(image, flip_code)