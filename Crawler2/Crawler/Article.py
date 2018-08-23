class Article():
    SEP = ";"
    
    def __init__(self, a_id, title, imgurl, text, emoji):
        self.a_id = a_id
        self.title = title
        self.imgurl = imgurl
        self.text = text
        self.emoji = ""
    
    def __str__(self):
        return (str(self.a_id) + self.SEP + self.emoji + self.SEP + self.title + self.SEP + self.imgurl + self.SEP + self.text)    
    
    def get_as_list(self):
        return [str(self.a_id),self.emoji,self.title,self.imgurl,self.text]