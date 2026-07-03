# Priority scale: 1 (lowest) to 5 (highest)
PRIORITIES = {
    1: ("Low", "Minor issue, no urgency. Workaround exists; can wait."),
    2: ("Normal", "Standard request. Should be handled in normal queue."),
    3: ("Medium", "Affects work but system still usable. Fix within a few days."),
    4: ("High", "Major impact on user or business. Needs attention soon."),
    5: ("Critical", "System down or security/data risk. Fix immediately."),
}

# Status lifecycle: 1 to 5
STATUSES = {
    1: ("Open", "New ticket, not yet reviewed or assigned."),
    2: ("In Progress", "Team is actively working on it."),
    3: ("Pending", "Waiting on user info, approval, or another team."),
    4: ("Resolved", "Fix applied; waiting for user confirmation."),
    5: ("Closed", "Issue confirmed fixed; ticket is complete."),
}
