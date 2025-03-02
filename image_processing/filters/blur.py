import cv2
import numpy as np

def apply_gaussian_blur(image, kernel_size=(5, 5), sigma=0):
    """
    Aplica um filtro de desfoque gaussiano a uma imagem.

    Args:
        image: A imagem a ser desfocada.
        kernel_size: O tamanho do kernel (largura, altura).
        sigma: O desvio padrão do kernel gaussiano.

    Returns:
        A imagem desfocada.
    """
    return cv2.GaussianBlur(image, kernel_size, sigma)

def apply_median_blur(image, kernel_size=5):
    """
    Aplica um filtro de desfoque mediano a uma imagem.

    Args:
        image: A imagem a ser desfocada.
        kernel_size: O tamanho do kernel (deve ser um número ímpar).

    Returns:
        A imagem desfocada.
    """
    return cv2.medianBlur(image, kernel_size)

def apply_bilateral_filter(image, diameter=9, sigma_color=75, sigma_space=75):
    """
    Aplica um filtro bilateral a uma imagem.

    Args:
        image: A imagem a ser filtrada.
        diameter: O diâmetro de cada pixel vizinho.
        sigma_color: O desvio padrão no espaço de cor.
        sigma_space: O desvio padrão no espaço de coordenadas.

    Returns:
        A imagem filtrada.
    """
    return cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)