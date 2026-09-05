# --- r mode - read only ---
with open('pfs-64.txt', 'r') as file:
    print("Read mode:")
    print(file.read())

    file.seek(0)
    print(file.readline())

    file.seek(0)
    print(file.readlines())


# --- w mode - write ---
# It creates the file if it doesn't exist.
# It overrides the previous content.
with open('pfs-64.txt', 'w') as file:
    file.write('We are learning python full stack at Codegnan')


# --- a mode - append ---
# It adds new content at the end.
with open('pfs-64.txt', 'a') as file:
    file.write(
        ' . And the technologies are python, flask, mysql, '
        'html, css, bootstrap, javascript, reactjs'
    )


# --- a+ mode - append + read ---
with open('mysql.txt', 'a+') as file:
    file.write('. It can be used with python for the backend')

    file.seek(0)
    print("\na+ mode:")
    print(file.read())


# --- r+ mode - read + write ---
with open('mysql.txt', 'r+') as file:
    print("\nr+ mode:")
    print(file.read())

    # After read(), cursor is at the end
    file.write('. If we learn PostgreSQL, then it will be more useful')


# --- w+ mode - write + read ---
# It removes previous content first.
with open('mysql.txt', 'w+') as file:
    file.write('Learning mysql itself is not that useful')

    file.seek(0)
    print("\nw+ mode:")
    print(file.read())