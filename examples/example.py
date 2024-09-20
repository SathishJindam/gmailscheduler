from gmailscheduler import Scheduler, Participant

# Create a scheduler instance
scheduler = Scheduler()

# Add participants
scheduler.add_participant(Participant("sathishjindam98@gmail.com", timezone="Europe/London", availability="weekdays 10am-4pm"))

# Schedule an event (this will also add it to Google Calendar)
# Add your credentials.json file here
event_time = scheduler.schedule_event(
    title="Team Sync",
    duration=30,
    priority_list=[ "sathishjindam98@gmail.com"]
)

print(f"Suggested Event Time: {event_time}")
