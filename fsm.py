from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def init(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "lobby"

    def on_enter_state1(self, event):
        print("I'm entering lobby")

        reply_token = event.reply_token
        send_text_message(reply_token, "lobby enter")
        self.state1()

    def on_exit_state1(self):
        print("Leaving lobby state")


    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "soccer"

    def on_enter_state2(self, event):
        print("I'm entering soccer")

        reply_token = event.reply_token
        send_text_message(reply_token, "soccer enter")

    def on_exit_state2(self):
        print("Leaving soccer state")


    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "Messi"

    def on_enter_state3(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        img_url = "https://cdn.britannica.com/34/212134-050-A7289400/Lionel-Messi-2018.jpg"
        send_image_url(reply_token, img_url)
        self.state2()   #state trigger要打

    def on_exit_state3(self):
        print("Leaving player state")

