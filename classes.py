class Schedule:
    def __init__(self, module, session, description, date, day, start_time, end_time, duration, location, lecturer):
        self.module = module
        self.session = session
        self.description = description
        self.date = date
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.location = location
        self.lecturer = lecturer

class Module:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Location:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Lecturer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Session:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class Date:
    def __init__(self, id, day):
        self.id = id
        self.day = day

class Zone:
    def __init__(self, id, name):
        self.id = id
        self.name = name