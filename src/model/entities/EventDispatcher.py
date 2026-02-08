from .Trigger import Trigger
from .Event import Event

class EventDispatcher:
    def __init__(self):
        self.listeners: dict[str, list[Trigger]] = {}

    def register(self, trigger: Trigger):
        self.listeners.setdefault(trigger.event_type, []).append(trigger)

    def dispatch(self, event: Event, engine):
        for trigger in self.listeners.get(event.type, []):
            if trigger.condition(event):
                trigger.effect(event, engine)
