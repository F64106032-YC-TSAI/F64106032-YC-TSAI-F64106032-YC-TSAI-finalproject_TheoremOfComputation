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




    def is_going_to_basketball(self, event):
        text = event.message.text
        return text.lower() == "basketball"
    def on_enter_basketball(self, event):
        print("I'm entering basketball")

        reply_token = event.reply_token
        send_text_message(reply_token, "basketball enter")
        
    def on_exit_basketball(self, evevt):
        print("Leaving basketball state")


    def is_going_to_baseball(self, event):
        text = event.message.text
        return text.lower() == "baseball"
    def on_enter_baseball(self, event):
        print("I'm entering baseball")

        reply_token = event.reply_token
        send_text_message(reply_token, "baseball enter")
        
    def on_exit_baseball(self, evevt):
        print("Leaving baseball state")


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

    def is_going_to_basketball_player_Durant(self, event):
        text = event.message.text
        return text == "Durant"
    def on_enter_basketball_player_Durant(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "basketball_player enter")
        img_url = "https://media.gettyimages.com/id/1433160669/photo/kevin-durant-of-the-brooklyn-nets-takes-a-shot-during-a-preseason-game-against-the-milwaukee.jpg?s=612x612&w=gi&k=20&c=sG_tWPo72JboJ2Bj06W9EWasAqpG0IgcGFEmJYGHwU8="
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_basketball_player_Durant(self, event):
        print("Leaving player state")

    def is_going_to_basketball_player_Harden(self, event):
        text = event.message.text
        return text == "Harden"
    def on_enter_basketball_player_Harden(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "basketball_player enter")
        img_url = "https://cdn.vox-cdn.com/thumbor/B1vVXbY84ciIIvmryxmxh2HZSzc=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/23521928/1240634978.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_basketball_player_Harden(self, event):
        print("Leaving player state")

    def is_going_to_basketball_player_Irving(self, event):
        text = event.message.text
        return text == "Irving"
    def on_enter_basketball_player_Irving(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "basketball_player enter")
        img_url = "https://media.npr.org/assets/img/2022/04/29/gettyimages-1393854580-4585b9878a2e69e7206c9a999e80e74d22d0b9b8.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_basketball_player_Irving(self, event):
        print("Leaving player state")

    def is_going_to_basketball_player_Curry(self, event):
        text = event.message.text
        return text == "Curry"
    def on_enter_basketball_player_Curry(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "basketball_player enter")
        img_url = "https://media.bleacherreport.com/image/upload/x_19,y_32,w_2948,h_1961,c_crop/v1637080168/ukf6gnhncdcsf1ssct74.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_basketball_player_Curry(self, event):
        print("Leaving player state")

    def is_going_to_basketball_player_George(self, event):
        text = event.message.text
        return text == "George"
    def on_enter_basketball_player_George(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "basketball_player enter")
        img_url = "https://www.si.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTkzNTg3NTA4NjgyOTU4MzIw/usatsi_19338145_168390270_lowres.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_basketball_player_George(self, event):
        print("Leaving player state")



    def is_going_to_baseball_player_Betts(self, event):
        text = event.message.text
        return text == "Betts"
    def on_enter_baseball_player_Betts(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "baseball_player enter")
        img_url = "https://fivethirtyeight.com/wp-content/uploads/2022/06/GettyImages-1400184240-4x3-1.jpg?w=917"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_baseball_player_Betts(self, event):
        print("Leaving player state")

    def is_going_to_baseball_player_Judge(self, event):
        text = event.message.text
        return text == "Judge"
    def on_enter_baseball_player_Judge(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "baseball_player enter")
        img_url = "https://images.chinatimes.com/newsphoto/2022-10-01/656/20221001000835.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_baseball_player_Judge(self, event):
        print("Leaving player state")

    def is_going_to_baseball_player_Stanton(self, event):
        text = event.message.text
        return text == "Stanton"
    def on_enter_baseball_player_Stanton(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "baseball_player enter")
        img_url = "https://cdn.vox-cdn.com/thumbor/zFSdPbJM0tJ-DJlbQ4dMQggOvSI=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/22750858/1234119746.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_baseball_player_Stanton(self, event):
        print("Leaving player state")

    def is_going_to_baseball_player_Harper(self, event):
        text = event.message.text
        return text == "Harper"
    def on_enter_baseball_player_Harper(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "baseball_player enter")
        img_url = "https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2022/05/04/0/16932906.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_baseball_player_Harper(self, event):
        print("Leaving player state")

    def is_going_to_baseball_player_Cole(self, event):
        text = event.message.text
        return text == "Cole"
    def on_enter_baseball_player_Cole(self, event):
        print("I'm entering player")

        reply_token = event.reply_token
        #send_text_message(reply_token, "baseball_player enter")
        img_url = "https://nypost.com/wp-content/uploads/sites/2/2022/06/Tigers-Yankees-Baseball-1.jpg"
        send_image_url(reply_token, img_url)
        self.go_back_user(event)   #state trigger要打
    
    def on_exit_baseball_player_Cole(self, event):
        print("Leaving player state")
    
    

    



    
