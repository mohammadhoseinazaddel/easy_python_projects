from datetime import datetime


def log_time(func):
    def wrapped_function(*args, **kwargs):
        start_time = datetime.now()
        result= func(*args, **kwargs) #main func
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print(
            f"total time : {hours}: {minutes}: {seconds}"
        )
        return result
    return  wrapped_function

# @log_time
# def pow2(num):
#     return num**2