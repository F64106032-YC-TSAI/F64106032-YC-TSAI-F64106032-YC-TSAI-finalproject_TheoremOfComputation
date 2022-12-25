from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url


class TocMachine(GraphMachine):
    def init(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    
    #def is_going_back_to_lobby(self, event):
    #    text = event.message.text
    #    return text.lower() == "back to lobby"
    
    def is_going_to_lobby(self, event):
        text = event.message.text
        return text.lower() == "lobby"
    def on_enter_lobby(self, event):
        print("I'm entering lobby")

        reply_token = event.reply_token
        send_text_message(reply_token, "lobby enter")
        #lobby 現在state在lobby不動?
    def on_exit_lobby(self, event):
        print("Leaving lobby state")


    def is_going_to_soccer(self, event):
        text = event.message.text
        return text.lower() == "soccer"
    def on_enter_soccer(self, event):
        print("I'm entering soccer")

        reply_token = event.reply_token
        send_text_message(reply_token, "soccer enter")
        
    def on_exit_soccer(self, evevt):
        print("Leaving soccer state")


    def is_going_to_soccer_player_Messi(self, event):
        text = event.message.text
        return text == "Messi"
    def on_enter_soccer_player_Messi(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "soccer_player enter")
        img_url = "https://cdn.britannica.com/34/212134-050-A7289400/Lionel-Messi-2018.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_soccer_player_Messi(self, event):
        print("Leaving player state")

    def is_going_to_soccer_player_Neymar(self, event):
        text = event.message.text
        return text == "Neymar"
    def on_enter_soccer_player_Neymar(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "soccer_player enter")
        img_url = "https://extratimetalk.com/wp-content/uploads/2021/06/gettyimages-1324132723-594x594-1.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_soccer_player_Neymar(self, event):
        print("Leaving player state")

    
    def is_going_to_soccer_player_Pogba(self, event):
        text = event.message.text
        return text == "Pogba"
    def on_enter_soccer_player_Pogba(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "soccer_player enter")
        img_url = "https://www.fussball.com/wp-content/uploads/2018/10/Paul-Pogba-1.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_soccer_player_Pogba(self, event):
        print("Leaving player state")

    def is_going_to_soccer_player_Mbappe(self, event):
        text = event.message.text
        return text == "Mbappe"
    def on_enter_soccer_player_Mbappe(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "soccer_player enter")
        img_url = "https://media.gq.com.tw/photos/6393137aac07f8003c9a04ee/3:2/w_1617,h_1078,c_limit/11.png"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_soccer_player_Mbappe(self, event):
        print("Leaving player state")

    def is_going_to_soccer_player_Ronaldo(self, event):
        text = event.message.text
        return text == "Ronaldo"
    def on_enter_soccer_player_Ronaldo(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "soccer_player enter")
        img_url = "https://i.pinimg.com/originals/2d/d1/a2/2dd1a247bd4e7c83de7daa7c2e30a724.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_soccer_player_Ronaldo(self, event):
        print("Leaving player state")

    def is_going_to_soccer_player_Modric(self, event):
        text = event.message.text
        return text == "Modric"
    def on_enter_soccer_player_Modric(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "soccer_player enter")
        img_url = "https://assets.laliga.com/assets/201807/w_900x700_11220327636669413755947180.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_soccer_player_Modric(self, event):
        print("Leaving player state")
    

    



    
