from abc import ABC, abstractmethod
from threading import Thread


class AbstractProtocol(ABC):

    def __init__(self, queue):
        self.test_finished = False
        self.queue = queue

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def send_message(self, message , ):
        pass

    @abstractmethod
    def receive_message(self):
        pass

    def send_receiver_ready(self):
        self.queue.put("RECEIVER_READY")

    def send_sender_finished(self):
        self.queue.put("END_TEST")

