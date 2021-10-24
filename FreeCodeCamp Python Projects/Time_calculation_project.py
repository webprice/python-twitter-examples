def add_time(start_time,add_time,dayoftheweek='day'):
    split1=start_time.split(" ")
    split2=split1[0].split(":")
    split3=add_time.split(":")

    start_hours=int(split2[0])
    start_minutes=int(split2[1])
    start_zone=str(split1[1])

    add_start_hours = int(split3[0])
    add_start_minutes = int(split3[1])

    total_hours=int(add_start_hours+start_hours)
    total_minutes=int(add_start_minutes+start_minutes)

    dayoftheweek=dayoftheweek.lower()
    newzone=str()
    days_gone=int()
    newday=''
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    hours_list=['12','01','02','03','04','05','06','07','08','09','10','11']
    def switch(ampm):
        if ampm == 'AM':
            ampm = 'PM'
        else:
            ampm = 'AM'
        return ampm

#minutes counting
    if total_minutes>59:
        more_hours=total_minutes//60
        total_hours=more_hours+total_hours
        total_minutes=total_minutes%60
        #print("total_minutes,total_hours",total_minutes,total_hours)
    if total_minutes<10:
        total_minutes =f"0{total_minutes}"
        #print("total_minutes,type(total_minutes)",total_minutes,type(total_minutes))
    finish_minutes = int(total_minutes)
    #print("finish_minutes",finish_minutes)
    #print("totalhours",total_hours)
    #x = add_start_hours%12
    #result = start_hours + x
    result=total_hours
    if result>12:
        #print('resultt:', result)
        result= result%12
    #print('resultt:',result)
    if result == 0:
        result=12

    portals = total_hours//12
    portals_zones= portals%2
    if portals_zones==0 or portals_zones==2:
        newzone=start_zone
        #print("newzonnnn",newzone)
    if portals_zones==1:
        newzone=switch(start_zone)
        #print("newzone",newzone)
    if start_zone =='AM':
        days_gone=portals//2
    if start_zone =='PM':
        days_gone=(portals+1)//2

    daynumber=int()
    counter=int()
    for each in days_list:
        if each == dayoftheweek:
            daynumber = counter
        counter+=1
    dayposition=daynumber+(days_gone%7)
    #print("daypos",dayposition)
    if dayposition ==7:
        dayposition = dayposition%7
    newday = days_list[dayposition].capitalize()
    #print("day",{dayoftheweek},'is under this # in the list:',daynumber)
    #print("the new day is :",days_list[dayposition])

    if days_gone==0:
        if dayoftheweek != 'day':
            #print("good1")
            return f'{result}:{total_minutes} {newzone}, {newday}'
        return f'{result}:{total_minutes} {newzone}'

    if days_gone==1:
        if dayoftheweek != 'day':
            #print("good2")
            return f'{result}:{total_minutes} {newzone}, {newday} (next day)'
        return f'{result}:{total_minutes} {newzone} (next day)'

    if days_gone>1:
        if dayoftheweek != 'day':
            #print("good3")
            return f'{result}:{total_minutes} {newzone}, {newday} ({days_gone} days later)'
    return f'{result}:{total_minutes} {newzone} ({days_gone} days later)'
print(add_time("8:16 PM", "466:02", "tuesday"))
