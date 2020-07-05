#
# @Author: Bhaskar S
# @Blog:   https: // www.polarsparc.com
# @Date:   04 Jul 2020
#

import CustomerAccount_pb2

account = CustomerAccount_pb2.Account()
account.acct_no = "12345"
account.acct_type = CustomerAccount_pb2.BROKERAGE
account.customer.first_name = "Bugs"
account.customer.last_name = "Bunny"
account.customer.email_id = "bugs.b@carrot.co"
account.customer.phone_no.append("100-100-1000")
account.customer.phone_no.append("100-100-1005")

print("Account fields: %s" % account.ListFields())
print("Account data size: %s" % account.ByteSize())
print("Account: %s" % account)

data = account.SerializeToString()

account2 = CustomerAccount_pb2.Account()
account2.ParseFromString(data)

print("Account deserialized: %s" % account2)
