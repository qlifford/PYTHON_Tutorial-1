class MailService:
    def _connect(self):
        return "Connecting to email server..."
        
    def _validate(self):
        return "Validating email..."
        
    def send_email(self, mail): 
        self._connect()       
        self._validate()       
        self._disconnect()    
        return f"Sending {mail}.."
           
    def _disconnect(self):
        return "Disconnecting from email server..."
        
email1 = MailService()
print(email1.send_email("New email"))