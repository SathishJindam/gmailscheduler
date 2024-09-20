import unittest
from gmailscheduler import Scheduler, Participant

class TestGmailScheduler(unittest.TestCase):
    def test_add_participant(self):
        scheduler = Scheduler()
        participant = Participant("Alice", timezone="America/New_York")
        scheduler.add_participant(participant)
        self.assertIn(participant, scheduler.participants)

    def test_schedule_event(self):
        scheduler = Scheduler()
        scheduler.add_participant(Participant("Alice", timezone="UTC"))
        event_time = scheduler.schedule_event(title="Meeting")
if __name__ == '__main__':
    unittest.main()
