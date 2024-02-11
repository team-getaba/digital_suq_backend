from dotenv import dotenv_values

get_env_values = dict(dotenv_values('.env'))


# env values 
res_env = get_env_values["HERE_WE_GO"]



# SMTP commons 
sender_email = 'profesornaoltena@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'profesornaoltena@gmail.com'

# https://myaccount.google.com/apppasswords.
smtp_password = 'lqqtyftdcvizlxox'  