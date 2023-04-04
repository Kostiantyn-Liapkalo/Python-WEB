from collections import UserDict
from pathlib import Path
import pickle


class AbstractPresenter:
    def get_note(self):
        raise NotImplementedError
    
    def get_notes_by_tag(self):
        raise NotImplementedError
    
    def get_all(self):
        raise NotImplementedError



class NoteBook(UserDict, AbstractPresenter):

    def add_note(self, note):
        self.data.update({note.title: note})

    def get_note(self, title):
        note = self.data.get(title, None)
        return note

    def delete_note(self, title):
        deleted = self.data.pop(title)
        return deleted

    def get_notes_by_tag(self, tag):
        notes_list = self.data.values()
        notes = list(filter(lambda x: x.tag == tag, notes_list))
        return notes
    
    def get_all(self):
        notes_list = list(self.data.values())
        return notes_list

    def save_data_to_file(self):
        with open('notes_data.bin', 'wb') as file:
            pickle.dump(self.data, file)

    def retrieve_data_from_file(self):
            path = Path('notes_data.bin')
            if path.exists():
                with open('notes_data.bin', 'rb') as file:
                    is_file_empty = not bool(file.read()) 
                    if is_file_empty:
                        return
                    else:
                        file.seek(0)
                        deserialized = pickle.load(file)
                        self.data = deserialized 


class Note:
    def __init__(self):
        self._title = None
        self._tag = None
        self._text = None

    @property
    def title(self):
        return self._title
    
    @property
    def tag(self):
        return self._tag
    
    @property
    def text(self):
        return self._text

    @title.setter
    def title(self, title, note_book):
        if_exists = note_book.get_note(title)
        if if_exists:
            raise ValueError(f"Note with title {title} already exists")
        elif title == '':
            raise ValueError("Value should not be empty")
        elif len(title) > 20:
            raise ValueError("Title should not exceed 20 characters")
        else:
            self._title = title

    @tag.setter
    def tag(self, tag):
        if tag == '':
            raise ValueError("Value should not be empty")
        elif len(tag) > 20:
            raise ValueError("Title should not exceed 20 characters")
        else:
            self._tag = tag

    @text.setter
    def text(self, text):
        if text == '':
            raise ValueError("Value should not be empty")
        if len(text) > 250:
            raise ValueError("Title should not exceed 250 characters")
        else:
            self._text = text



class Tag:
    def __init__(self, value):
        self.value = value

class Title:
    def __init__(self, value):
        self.value = value

class Content:
    def __init__(self, value):
        self.value = value
