import pyprowl


def push_prowl(app_name, event, description):
    #TODO prowlapi setzen
    prowl_api = ""
    p = pyprowl.Prowl(prowl_api)
    try:
        p.verify_key()
        print("Prowl API key successfully verified!")
    except Exception as e:
        print("Error verifying Prowl API key: {}".format(e))
        exit()

    try:
        p.notify(event=event, description=description,
                 priority=0, url='http://www.example.com',
                 # apiKey='uncomment and add API KEY here if different',
                 appName=app_name)
        print("Notification successfully sent to Prowl!")
    except Exception as e:
        print("Error sending notification to Prowl: {}".format(e))
