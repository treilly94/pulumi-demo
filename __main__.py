"""An Azure Python Pulumi program"""

import pulumi
from pulumi_azure import core, storage

config = pulumi.Config()

# Create an Azure Resource Group
resource_group = core.ResourceGroup('sportsdrink-{}'.format(pulumi.get_stack()))

# Create an Azure resource (Storage Account)
account = storage.Account('storage',
                          # The location for the storage account will be derived automatically from the resource group.
                          resource_group_name=resource_group.name,
                          account_tier='Standard',
                          account_replication_type='LRS')

# Export the connection string for the storage account
pulumi.export('connection_string', account.primary_connection_string)
