from abc import abstractmethod, ABCMeta


class IPdf(metaclass=ABCMeta):

    @abstractmethod
    def sign(self, sign: str):
        pass
    
    @abstractmethod
    def compress(self, compress_quality: str):
        pass
    
    @abstractmethod
    def add_watermark(self, mark: str):
        pass