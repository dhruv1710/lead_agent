from pydantic import BaseModel
class Email(BaseModel):
    email: str
    name: str
    subject: str
    body: str

class Contact(BaseModel):
    company: str
    full_name: str
    title: str
    linkedin_url: str
    email: str

class Company(BaseModel):
    name: str
    website: str
    description: str
    reason: str    

class Companies(BaseModel):
    companies: list[Company]

class Contacts(BaseModel):
    contacts: list[Contact]

class Emails(BaseModel):
    emails: list[Email]