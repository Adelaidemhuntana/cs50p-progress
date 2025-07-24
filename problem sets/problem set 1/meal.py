def main():
    time = input("What time is it? ")         # this must ask the user what ttime it is
    time_float = convert(time)                  # convert the time that the user inputs into a decimal

    if 7.0 <= time_float <= 8.0:                # If the time is between 7:00 and 8:00 print "breakfast time"
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:            # If the time is between 12:00 and 13:00 print "lunch time"
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:            # If the time is between 18:00 and 19:00 print "dinner time"
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")           # Split the time into hours and minutes from "7:00" into ["7" , "30"]
    return int(hours) + int(minutes) / 60      # Convert to decimal hours 7.5

if __name__ == "__main__":                     
    main()                                     #call main function 