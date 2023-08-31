import time
rq_time=time.ctime()
rules={
    "hi" :"hey",
    "how are you" :"I am fine",
    "what is your name" :"My name is bot01",
    "what is your birth year" :"2023",
    "what is the time now":"The time is "+rq_time,
}
while True:
    questions=input()

    if (questions=="bye"):
        print("see ya...")
        break
    else:
        print(rules[questions])