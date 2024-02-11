
class Template:
    def verify_email(verification_code):
        email_verification_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GebreKoo Verification</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f1f1f1;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}

        .logo {{
            max-width: 100%;
            margin-bottom: 20px;
            border-radius: 10px;
        }}

        .header {{
            font-size: 24px;
            font-weight: bold;
            color: #6500ff;
            margin-bottom: 20px;
        }}

        .verification-code {{
            font-size: 28px;
            font-weight: bold;
            background-color: #6500ff;
            color: #ffffff;
            padding: 15px 30px;
            border-radius: 10px;
            border: 2px solid #4c00b2;
            margin-bottom: 30px;
        }}

        .instructions {{
            font-size: 16px;
            color: #555555;
            margin-bottom: 30px;
        }}
 
        .footer {{
            font-size: 14px;
            color: #777777;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <img src="https://as2.ftcdn.net/v2/jpg/05/63/04/73/1000_F_563047379_abTUQzC9kapV6Y2ax1EcpQ176OuFypmx.jpg" alt="Zemare Music Logo" class="logo">
        <div class="header">Email Verification Code</div>
        <div class="verification-code">{verification_code}</div>
        <div class="instructions">
            Thank you for signing up with GebreKoo. To complete your registration, please use the above verification code.
            <br>
            
        </div>
       <center class="instructions">
           Big Thanks Naol Tena <br> cofounders and CEO
           </center>
        <div class="footer">
            GebreKoo | © 2024 All rights reserved.
        </div>
    </div>
</body>
</html>
"""

        return email_verification_template

    def verify_user(user_name):
        temp = f"""<h1>welcome {user_name} to GebreKoo </h1>"""
        return temp
