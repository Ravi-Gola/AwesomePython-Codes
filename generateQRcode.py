""" for generate QR code of any thing """
# import qrcode
# img = qrcode.make("ravi is a good boy")
# img.save("myQR.jpg")

"""for read qr code content without scan it"""
# import cv2
# d = cv2.QRCodeDetector()
# val,_,_= d.detectAndDecode(cv2.imread("myQR.jpg"))
# print("Decoded text is: ", val)