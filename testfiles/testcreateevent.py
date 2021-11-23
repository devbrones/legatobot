from createevent import getListedEvents, createEvent, vartoarray

subject = "Svenska 1"
start = "2022-11-22T08:30:00+00:00"
finish = "2022-11-22T09:30:00+00:00"
classroom = "211"
teachers = "Hanna Åberg"
agenda = "Gud kommer att äta oss levande"

classes = vartoarray(subject, start, finish, classroom, teachers, agenda)
guildid = "879671396450578463"
#createEvent(guildid, classes)
a = getListedEvents(guildid)

