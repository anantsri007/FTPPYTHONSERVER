from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Step 1: Create an authorizer to manage users and permissions
authorizer = DummyAuthorizer()

# Ensure the FTP home directory exists
ftp_home = "/FTPServerPath"
if not os.path.exists(ftp_home):
    os.makedirs(ftp_home)

# Step 2: Add a user (username: user1, password: 123456, home directory: /FTPServerPath)
# Permissions: "elradfmw" (full access: read, write, delete, list)
authorizer.add_user("user1", "123456", ftp_home, perm="elradfmw")

# Step 3: Optional: Add an anonymous user (read-only)
# authorizer.add_anonymous("/path_to_anonymous_directory")

# Step 4: Create an FTP handler instance and link it to the authorizer
handler = FTPHandler
handler.authorizer = authorizer

# Step 5: Create an FTP server instance listening on the specific IP and port 2121
server = FTPServer(("192.168.239.124", 2121), handler)

# Step 6: Start the FTP server
print("FTP server started on all interfaces at port 2121...")
server.serve_forever()




