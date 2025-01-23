
def generate_flag():
    return "".join((x+y)[::-1] for x,y in zip("}0_w__0{S"[::-1], "SMnw10nyu"))

print(generate_flag())