def log_time(application, issuekey, time):
    jira = application.jira
    try:
        jira.add_worklog(issuekey, timeSpent=time, reduceBy=time)
    except Exception:
        jira.add_worklog(issuekey, timeSpent=time)
