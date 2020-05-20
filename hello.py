import os
def check_ping(host):
    hostname = host
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
        return pingstatus
    else:
        pingstatus = "Network Error"
        return pingstatus

    return pingstatus

host=input()
print(check_ping(host))