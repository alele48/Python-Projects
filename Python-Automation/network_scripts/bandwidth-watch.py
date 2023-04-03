from netmiko import ConnectHandler
import re
import datetime
from time import sleep
import math

# converts bits to bytes
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

run = True


cisco = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.10',
    'username': 'netadmin',
    'password': '52RedRight!',
    'port' : 22,
    }



minute = 60
hour = 60 * 60

while run:
    net_connect = ConnectHandler(**cisco)
    f = open("network-interfaces.txt","r")

    for interfaces in f:
        interface = net_connect.send_command(f"show interfaces gigabitEthernet {interfaces}")
        # gets the date in Y/M/D H/M
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        # gets the input rate index
        input_rate_index = interface.find("input rate")
        # gets input rate text
        input_rate_text = interface[input_rate_index:]
        # end of input text
        input_end = input_rate_text.find("bit")

        input_rate = input_rate_text[0:input_end]
        ''' extracts numeric value from text '''
        input_num =""
        for i_num in input_rate: 
            if i_num.isdigit():
                input_num +=i_num

        # converts bits to bytes
        i_rate = convert_size(int(input_num))

        
        
        # gets the output rate index
        output_rate_index = interface.find("output rate")

        # gets text output
        output_rate_text = interface[output_rate_index:]
        # end of output rate text
        output_end = output_rate_text.find("bit")


        output_rate = output_rate_text[0:output_end]

        output_num =""
        for o_num in output_rate: 
            if o_num.isdigit():
                output_num +=o_num

        # converts bits to bytes
        o_rate = convert_size(int(output_num))
        
        print(f"Interface {interfaces}")
        print("@ " + date)
        print(f"Input Rate: {i_rate}")

        print(f"Output Rate: {o_rate}\n")

        with open("test-bandwidth.txt","a") as file:
           file.write(f"Interface {interfaces}\n")
           file.write(f"Date: {date}\n")
           file.write(f"Input Rate: {i_rate}\n")
           file.write(f"Output Rate: {o_rate}\n")
           file.write("\n")
           file = open("test-bandwidth.txt","r")
    sleep(hour*2)

'''
# gets the output rate text
output =interface[output_rate:877]
print(output)

print(f"Output: {output_rate}")
bit = output.find("bit")
print(f"bit:{bit}")


#output_num = re.findall(r'\d+',output_rate)
print(output[output_rate:bit])
#print(output[input_rate:output_rate].split(""))
'''

