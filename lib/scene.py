from abc import ABC, abstractmethod


class Scene(ABC):
    @abstractmethod
    def on_input(key):
        pass

    @abstractmethod
    def render(term):
        pass
