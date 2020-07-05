#
# @Author: Bhaskar S
# @Blog:   https: // www.polarsparc.com
# @Date:   04 Jul 2020
#

import Customer_pb2

customer = Customer_pb2.Customer()
customer.first_name = "Wile E"
customer.last_name = "Coyote"
customer.phone_no.append("200-101-2001")
customer.phone_no.append("201-102-2002")

print("Customer fields: %s" % customer.ListFields())
print("Customer data size: %s" % customer.ByteSize())
print("Customer: %s" % customer)

with open('/tmp/customer.bin', 'wb') as bf:
    bf.write(customer.SerializeToString())

print("Customer object serialized to /tmp/customer.bin")
