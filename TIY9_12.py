from TIY9_12b import User
from TIY9_12b import Admin, Privileges

priv = ["can add post", "can delete post", "can edit post", "can ban user", "can unban user", "can change username"]
ad = Admin("Ethan", "Passino", "EthanPassino", "2/6/03", 17, "M", priv)
ad.privileges.show_privileges()
