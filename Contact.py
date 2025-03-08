from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
api_key = "your_hubspot_api_key"
client = HubSpot(api_key=api_key)
new_contact = SimplePublicObjectInput(
properties={
"email": "test@example.com",
"firstname": "John",
"lastname": "Doe",
"phone": "+1 234 567 890",
"company": "Tech Corp"
}
)
response = client.crm.contacts.basic_api.create(new_contact)
