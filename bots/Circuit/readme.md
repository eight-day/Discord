# Known Errors
* Error 0 - _Check nested function_ not running due to invalid key [__Fixed__]
* Error 1 - Invalid arguments in the cbot.run without token [__Fixed__]
* Error 2 - Messy exception when !c purge is triggered [__Pending__]

# Tasks/Future updates.
- [ ] Check logging for any errors and fix them.
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


# Other
If you need to contact me about the following:

1. Adding things to the bot.
1. An error that has not been fixed.
1. A better way to do something.
1. CO-development

Feel free to message me on
[Instagram](https://instagram.com/notdoxxed) or Discord: 8 Day#0001
