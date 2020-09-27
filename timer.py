from time import sleep, time, localtime, strftime

start_timer = time()

struct = localtime(start_timer)

print('Starting countdown at:' , strftime('%X' , struct))

i = 5
while i > -1:
    print(i)
    i -=1
    sleep(1)

end_timer = time()
difference = round(end_timer - start_timer)
print('✔✔ done counting ✔✔ ')    