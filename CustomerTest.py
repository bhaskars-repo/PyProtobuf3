#
# @Author: Bhaskar S
# @Blog:   https: // www.polarsparc.com
# @Date:   04 Jul 2020
#

import Customer_pb2

customer = Customer_pb2.Customer()
customer.first_name = "Bugs"
customer.last_name = "Bunny"
customer.email_id = "bugs.b@carrot.co"
customer.phone_no.append("100-100-1000")
customer.phone_no.append("100-100-1005")

print("Customer fields: %s" % customer.ListFields())
print("Customer data size: %s" % customer.ByteSize())
print("Customer: %s" % customer)

data = customer.SerializeToString()

customer2 = Customer_pb2.Customer()
customer2.ParseFromString(data)

print("Customer deserialized: %s" % customer2)
