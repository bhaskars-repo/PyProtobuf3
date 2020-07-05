#
# @Author: Bhaskar S
# @Blog:   https: // www.polarsparc.com
# @Date:   04 Jul 2020
#

import Customer2_pb2
import Account2_pb2

account = Account2_pb2.Account2()
account.acct_no = "12345"
account.acct_type = Account2_pb2.SAVINGS
account.customer.first_name = "Bugs"
account.customer.last_name = "Bunny"
account.customer.email_id = "bugs.bunny@looney.us"
home = account.customer.phone_no.add()
home.number = "100-100-1000"
home.type = Customer2_pb2.MOBILE
mobile = account.customer.phone_no.add()
mobile.number = "100-100-1005"
mobile.type = Customer2_pb2.WORK

print("Account fields: %s" % account.ListFields())
print("Account data size: %s" % account.ByteSize())
print("Account: %s" % account)

data = account.SerializeToString()

account2 = Account2_pb2.Account2()
account2.ParseFromString(data)

print("Account deserialized: %s" % account2)
