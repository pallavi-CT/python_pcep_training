from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod

@dataclass
class Notification:
    recipient: str
    subject: str
    body: str
    sent_at: datetime = None
    priority: str = 'normal'


# abstract class - define a contract
class NotificationChannel(ABC):

    def __init__(self, name: str):
        self.name = name
        self._sent_count = 0

    def _pre_send_method(self, n: Notification) -> None:
        """override this in subclass for specific implementation"""
        pass

    @abstractmethod
    def send(self, notification: Notification) -> bool:
        """ abstract method. mandatory implementation"""
        ...

    def deliver(self, notification: Notification) -> bool:
        " template method"
        self._pre_send_method(notification)
        success = self.send(notification)
        if success:
            self._sent_count += 1
            notification.sent_at = datetime.date()
        
        return success

#implementation of abstract class
class EmailChannel(NotificationChannel):
    def __init__(self, smpt_host: str, from_addr: str):
        super().__init__('email')
        self.smtp_host = smpt_host
        self.from_addr = from_addr
    
    def _pre_send_method(self, n: Notification) -> None:
        if n.priority == 'critical':
            n.subject = '[URGENT] ' + n.subject
    
    def send(self, notification:Notification) -> bool:
        # smtplib.SMTP(self.smpt_host).sendmail(...)
        print(f' Email to {notification.recipient}: {notification.subject}')
        return True
    

