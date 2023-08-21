from recordbook.user_interface import AbstractInterface

class Telegram:
    def __init__(self, token):
        self.token = token
    
    def send_message(self, text):
        print(f"Send {text} to Telegram")
	

class TelegramOutput(AbstractInterface):
    def __init__(self, token) -> None:
        self.telegram_client = Telegram(token)
    
    def output(self, text: str, *args) -> None:
        self.telegram_client.send_message(text)
		

class Commands_Handler:
    def __init__(self, command_output: AbstractInterface):
        self.__output_processor = command_output
        
    def send_message(self, message) -> None:
        self.__output_processor.output(message)


if __name__ == "__main__":


    telegram_out = TelegramOutput("token")

    telegram_handler = Commands_Handler(telegram_out)
    telegram_handler.send_message("Hello guys")