def S1(z):
    for e in z + '\':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
S1('\\1b[1;37m[●] Checking Update........☢️');time.sleep(0.5)
os.system("git pull")
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            S1("\1b[1;92m[●] Congratulations ! Your Device Support this Tools 🔥💥")
            from SPIDER import welcome
            welcome()
        elif bit == '32bit':
            S1("\\1b[1;92m[●] Congratulations ! Your Device Support this Tools 💥🔥")
            from SPIDER import welcome
            welcome()
        else:
            exit('\33[1;31m[●] Connection & Network Error ❌')
Run()
