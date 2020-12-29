# Enable Me
### Steps to use Website for Visually Impaired user:
Enable talkback on your Android Phone by going to settings.
Open URL http://enableme.herokuapp.com/
Navigate as blind user using talkback
Go to Blind icon which has alt text for Blind Flow
You can record your voice here. Which in turn calls Base64->Speech2Text to build your profile. [Note: This does not work because chrome does not allow recording on websites without security certificate]
You can see profile on http://enableme.herokuapp.com/profile
Currently it'll show simple message: your profile 


### Steps to use Google Action "Enable Me":
Say "Ok Google, Talk to Enable Me".
For first time user authentication flow will be triggered. Allow the permissions [These will be used later for session management]
Once you are in, Bot will tell a bit about itself.
Now say "I would like to build profile" or some variant of it [ Bot can classify and identify what user is trying to say]
Bot will ask series of questions to build your profile, answer them. [for experience years at the end is necessary to say, like 5 years]
You can also build your profile by saying "Here's quick summary about me. My name is ......, I work at ...... and have experience of ..... . Currently I am living in .......". [This summary is converted from speech to text and sent to sentient NER api to extract details]
You can search for jobs by saying, "Show me jobs" or "new jobs in Pune[location can vary]". This will trigger job search flow.
It'll fetch data from dummy db and start showing jobs.
you can say "next job" or "next" to hear next job advertisement.
you can say at any point on job search flow "apply for job" and your application will be sent.
