# Lead Generator - CrewAI Crew

## 🚀 Overview

This crew uses a team of specialized AI agents to research, identify, and engage decision-makers with personalized emails, ultimately driving high-quality leads to your business through your service.

## ✨ Key Features

- **Researching Potential Leads**: The crew investigates companies that could become potential leads, saving you time and ensuring you're targeting the right prospects.
- **Identifying Decision-Makers**: They pinpoint the key individuals within those companies who have the authority to make decisions, ensuring your message reaches the right person.
- **Crafting Personalized Emails**: They create tailored emails that highlight specific pain points and explain how your service can solve them, increasing engagement and conversion rates.

## 🔍 Use Cases

This crew is ideal for:

- Businesses looking to generate high-quality leads through targeted, personalized outreach.

## 🛠️ Requirements

- CrewAI version: 0.121.0
- API Keys needed:
  - Gemini Key: To obtain a Gemini API key, sign into Google AI Studio with a Google account, click "Get API Key" from the left-hand menu, and select "Create API key in new project" to generate and copy the key.
  - Hunter.IO Key: To obtain a Hunter.io API key, create a free account on Hunter.io, log in, navigate to the "API" section in your dashboard, and copy or generate your unique API key.
  - SerperDev Key: To obtain a Serper.dev API key, sign up for a free account at serper.dev, verify your email, log in, navigate to the "API Keys" section in your dashboard, and generate or copy your unique API key.
- Additional dependencies: 
  - Pydantic version: >=2.11.5

## 📊 Example Output

[Include a brief description of what the output looks like. If appropriate, include a screenshot or example of the output.]

```
[
  {
        "mail_id": "mike.frank@companyb.com",
        "recipient_name": "Mike Frank",
        "subject_line": "Streamlining Operations at Company B with AI Agents",
        "email_body": "Dear Mr. Frank,\n\nMy name is [Your Name] from [Your Company], where we build AI agents and apps focused on improving business processes and operational efficiency.\n\nGiven your role as Executive Vice President, Chief Operating Officer at Company B, you are at the forefront of managing the day-to-day complexities of providing administrative and clinical support services, especially as the company experiences rapid growth.\n\nFast growth in healthcare services naturally increases the volume and intricacy of operational tasks – from managing administrative workflows to supporting clinical processes. This is where AI agents can make a significant impact.\n\nOur AI solutions can be tailored to automate repetitive administrative tasks, improve data processing speed and accuracy, optimize resource allocation, and provide consistent support across your operations. This not only enhances efficiency but also allows your teams to handle increased demand more effectively.\n\nI'd be keen to show you how AI agents could specifically benefit Company B's operational framework, helping to streamline processes and support your continued expansion. Would you have 15-20 minutes for a call next week?\n\nSincerely,\n\n[Your Name]\n[Your Title]\n[Your Company]\n[Your Website]\n[Your Phone Number (Optional)]"
},
  .
  .
  .
]
```

## Credits

Thanks to CrewAI for an amazing framework and OpenAI for the Model

Built with ❤️ by Kartavya AI (https://kartavyatech.com)

## 📝 License

MIT License