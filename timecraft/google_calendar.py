from datetime import datetime, timedelta
import pytz

class Scheduler:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def schedule_event(self, title, duration=60, priority_list=None, constraints=None):
        # Simplified scheduling logic for now (just returns a fixed date/time)
        event_time = datetime.now(pytz.UTC) + timedelta(days=1)
        return event_time.strftime('%Y-%m-%d %H:%M:%S %Z')

    def __repr__(self):
        return f"Scheduler(participants={self.participants})"
