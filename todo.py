from datetime import date
from enum import Enum
from uuid import uuid4


class Status(Enum):
    """ The Todo Statuses """
    NOT_STARTED = 0
    IN_PROGRESS =  1
    COMPLETED = 2


class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Item():
    __creation_date = date.today()
    __title = "empty"
    __status = Status.NOT_STARTED
    __priority = Priority.LOW
    __id = str(uuid4())
    __flag = False 
    __url = ""
    __due_date = date
    __icon = ""
    __state = False
    __notes = ""

    def __init__(self, title:str=None):
        if title is not None:
            self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value:str):
        self.__title = value

    @property
    def priority(self):
        return self.__priority.name
    
    @priority.setter
    def priority(self, value:Priority):
        self.__priority = value

    @property
    def creation_date(self):
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value

    @property
    def age(self):
        return self.__creation_date - date.today()
    
    @property
    def status(self):
        return self.__status.name
    @status.setter
    def status(self, value:Status):
        self.__status = value

    @property
    def id(self):
        return self.__id
    
    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, value:bool):
        self.__flag = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value:str):
        self.__url = value
    
    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value:date):
        self.__due_date = value
    
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, value:str):
        self.__icon = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value:bool):
        self.__state = value

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value:str):
        self.__value = value

class Todo():
    __todos = []

    def new_item(self, item:Item):
        self.__todos.append(item)
    
    @property
    def items(self)->list:
        return self.__todos

    def show(self):
        print("*"*80)
        for item in self.__todos:
            print(item.title, item.status, item.priority, item.age)
        
    @classmethod
    def show(cls):
        print("*"*80)
        for item in cls.__todos:
            print(item.title, item.status, item.priority, item.age, item.id)

    def remove_item(self, uuid):
        self.__todos.remote(uuid)

# i = Item("Get shopping")
# l = Todo()
# l.new_item(i)
# l.show()    
# l.remove_item()