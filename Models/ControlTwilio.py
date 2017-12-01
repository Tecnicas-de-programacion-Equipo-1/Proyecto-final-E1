from Models.JsonTwilio import JsonTwilio
from twilio.rest import Client

class ControlTwilio():
    class Constants:
        env_file = "Env-example/env_example"

    def __init__(self):
        env_variables = JsonTwilio.open_json_file(self.Constants.env_file)
        if env_variables is None:
            return

        account_sid = env_variables.get("account_sid", None)
        auth_token = env_variables.get("auth_token", None)
        self.__twilio_phone = env_variables.get("twilio_phone", None)

        self.client = Client(account_sid, auth_token)
        self.phone = env_variables.get("phone", None)
        self.message = env_variables.get("msg", None)

    def send_message(self):
        self.client.messages.create(to=self.phone, from_= self.__twilio_phone, body=self.message)
        print("Mensaje enviado")
