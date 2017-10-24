from passlib.hash import sha256_crypt
salt = "password3"

pass1 = sha256_crypt.encrypt("password1")
pass2 = sha256_crypt.encrypt("password1")


saltpass1 = pass1 = salt
saltpass2 = pass2 = salt
newPass1 = sha256_crypt.encrypt(saltpass1)
newPass2 = sha256_crypt.encrypt(saltpass2)

print(newPass1)
print(newPass2)

print(sha256_crypt.verify("password1"+salt, newPass1))