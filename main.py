import os

dir_path = os.path.dirname(os.path.realpath(__file__))

os.system(f"start \"\" cmd /k \"python3 {os.getcwd()}/Subscriber.py & color 04\"")
os.system(f"start \"\" cmd /k \"python3 {os.getcwd()}/Publisher.py & color 04\"")

exit()