from abc import abstractmethod, ABCMeta


class IOnline(metaclass=ABCMeta):

    @abstractmethod
    def embebed(self, web: str):
        pass
    
    @abstractmethod
    def open_in_browser(self):
        pass