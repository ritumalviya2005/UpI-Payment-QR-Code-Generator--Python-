import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID = ")

# Create payment URLs
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&acu=INR&tn=Payment'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cu=INR&tn=Payment'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&cu=INR&tn=Payment'

# to Create QR Codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Show QR Codes 👇
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

# for Save QR codes
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')