from connect_priv_ import connect_do_stuff


with open("routers.txt", "r") as temp:
    r = temp.read().splitlines()


connect_do_stuff(r)

