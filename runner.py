import imghdr

from Getting import find_file_with_ext
from Emailiy import send_mail

# user can edit information
# ***********************************************************************
contact = ['rahulkumark72@gmail.com', 'kumarpratyush456@gmail.com'] #
Email_Address = "rahulkumark72@gmail.com"
Email_Password = "rahul@234"

subject = 'Automation task completed'
content = "file attached..."

user_dir = 'C:\\Users\\DELL\\Desktop\\Full_Automation\\'
file_extension = ".py"
zip_name = "automation"
# ****************************************************************************

if __name__ == "__main__":
    zip_file_name = find_file_with_ext(user_dir, file_extension, zip_name)
    with open(zip_file_name, 'rb') as zp:
        file_data = zp.read()
        file_type = imghdr.what(zp.name)
        file_name = zp.name
    new_file_name = file_name.split("\\")[-1]
    send_mail(Email_Address, Email_Password, contact, subject, content, new_file_name, file_data)