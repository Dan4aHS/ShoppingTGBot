import cv2
from pyzbar.pyzbar import decode


async def get_qr_data(file_path: str) -> str:
    qcd = cv2.QRCodeDetector()
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    ret, qr_image = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    qr_text = decode(qr_image)
    if len(qr_text) != 0:
        return str(qr_text[0].data)[2:-1]
    return ''
