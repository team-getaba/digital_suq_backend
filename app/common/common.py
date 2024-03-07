from dotenv import dotenv_values

get_env_values = dict(dotenv_values('.env'))


# env values 
HERE_WE_GO = get_env_values["HERE_WE_GO"]



# SMTP commons 
DEFAULT_FROM_EMAIL = 'profesornaoltena@gmail.com'
HOST_SMTP_SERVER = 'smtp.gmail.com'
HOST_SMTP_PORT = 587
HOST_SMTP_USERNAME = 'profesornaoltena@gmail.com'
HOST_SMTP_PASSWORD = 'lqqtyftdcvizlxox'  # https://myaccount.google.com/apppasswords.