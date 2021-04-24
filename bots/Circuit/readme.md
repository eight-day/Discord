# Known Errors
* Error - _Check nested function_ not running due to invalid key [__Fixed__]
* Error - Invalid arguments in the cbot.run without token [__Fixed__]
* Error - Messy exception when !c purge is triggered [__Fixed__]

# Tasks/Future updates.
- [x] Check logging for any errors and fix them.
- [ ] Add in the ability to save logging to out.
- [ ] Make the break command fully functional.

# Side notes for developers.
Do not forget to update check to your need.

Be careful of what you allow others to execute...

Example:
- [x] Good:
```python
if command == "purge" and check(message, True):
	async for msg in channel.history(limit=limit):
		try:
			if check(msg, True):
				await msg.delete()
		except:
			continue
```
- [ ] Bad:
```python
if command == "purge" and check(message):
	async for msg in channel.history(limit=limit):
		try:
			if check(msg):
				await msg.delete()
		except:
			continue
```



# Plans
The following is nothing but things I plan to add on when I have the time.
1. Adding alias support.
1. Allowing the ability to change the prefix.
1. Adding more commands.
1. Getting the set properties to actually interact with the bot.
1. Getting other events in here and attached to the bot for whatever purpose.
1. Forking get-token and having it ran when no token is supplied automatically.
2.  ^ Branch of -> Allowing the token to be passed via argv


# Other
If you need to contact me about the following:

1. Adding things to the bot.
1. An error that has not been fixed.
1. A better way to do something.
1. CO-development

Feel free to message me on
[Instagram](https://instagram.com/notdoxxed)

Discord: 8 Day#0001
