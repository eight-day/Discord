# Circuit self bot written on a chromebook with slightly less..
# ..laziness than usual? Rip or claim this program all you want.
# Notice it's a simple program written by I(8 Day). That you can..
# Complete in your sleep with just abit of try....
# My faith runs soly in a docker and pure idk?
# I'm not adding any YAYA features to this as its just a simple bot.
# Anyways cya nerds
try:
	from discord import (
		Client, 
		MessageType,
		Message
	)
	from os import (
		path,   # For file based operations
		getenv, # If you have your token in an ENV use this. getenv(ENV_NAME)
		system, # Executing commands
		_exit   # https://man7.org/linux/man-pages/man2/_exit.2.html
	)
	from time import ctime, strftime
	from threading import Thread
except ImportError as Err:
	print(f"Module not found: {Err.name} | Install it and re-run.")
	exit()

cbot, token, prefix, sets, logs = (
	Client(),				# discord.Client object init.
	"", 					# Token
	"!c ",					# Prefix
	{					# Settings
		"deleted_logger": (False, []),  
		"save_attachments": (False, []),# Not rec for accounts in many servers uwu.
		"allow_others": (False, [])
	},
	{					# Logs
		"deleted_messages": [],
		"executed_commands":[],
		"failed_commands":  [],
		"other_events":     [],
		"changes":          []
	}
)

def write_data(outdata: list, outpath: str, overwrite = False, append = False) -> bool:
	try:
		if path.isfile(outpath) and overwrite: desc = open(outpath, "w")
		elif path.isfile(outpath) and append: desc = open(outpath, "a")
		else: desc = open(outpath, "w")
		desc.writelines(outdata)
		return True
	except:
		return False

@cbot.event
async def on_message(message: Message) -> None:
	#Add your own stuff here nerd, don't constantly ask me to.
	#Understand the base working of it and edit based on that.
	
	content, author, channel, embeds, attachments = (
		message.content,
		message.author,
		message.channel,
		message.embeds,
		message.attachments
	)
	def check(message: Message, is_self=False) -> bool:
		"""
		Do not use nonlocal unless you know it will not interfere.
		Using nonlocal with the below will cause errors and false positives.
		"""
		if is_self:
			message.author == cbot.user
		if sets["allow_others"] and message.author in sets["allow_others"][1]:
			return True
		return message.author == cbot.user
	
	if content.startswith(prefix) and check(message):
		# Here is where you need to focus if you plan to add anything.
		# Be aware of what you allow others to do.
		command, *args = content.strip(prefix).split()
		if command == "purge":
			if message.author != cbot.user:
				return
			limit = int(args[0]) if len(args) >= 1 and args[0].isdigit() else None
			async for msg in channel.history(limit=limit):
				if check(msg):
					try: await msg.delete()
					except: continue
		if command == "log":
			try:
				arguments = {
					"overwrite": "--overwrite" in args or "-a" in args,
					"append": "--append" in args or "-a" in args,
					"outpath": (
						(f"{channel}-{ctime()}.log") if "-o" not in args else (
							args[args.index("-o") + 1])
					),
					"outdata": [] # Uses writelines
				}
				await message.delete()
				async for msg in channel.history(limit=None):
					if isinstance(type(msg.type), type(MessageType.default)):
						arguments["outdata"].append(
							f"[{msg.creation_date}] {msg.author} - {msg.content}\n"
						)
					if isinstance(type(msg.type), type(MessageType.call)):
						arguments["outdata"].append(
							f"[{msg.creation_data}] {msg.author} - Called.\n"
						)
				Thread(target=write_data, kwargs=arguments).start() # Use a thread so we dont interrupt the eLoop

			except IndexError:
				await message.edit("Error: no path supplied.")
				await message.edit(content)
			async for msg in channel.history(limit=None):
				if isinstance(type(msg.type), type(MessageType.default)):
					arguments["outdata"].append(
						f"[{msg.creation_date}] {msg.author} - {msg.content}\n"
					)
				if isinstance(type(msg.type), type(MessageType.default)):
					arguments["outdata"].append(
						f"[{msg.creation_data}] {msg.author} - Called.\n"
					)
			write_data(**arguments)
		if command == "break":
			if "nosave" in args:
				await channel.send("[+] Closed and didn't save.")
				_exit()
			await channel.send("[+] Closed and saved.")
			_exit()
		if command == "set" and len(args) == 2:
			if args[0] in sets and args[1].lower() in ("true", "false"):
				sets[args[0]][0] = True if args[1].lower() == "true" else False
				await message.edit(content=f'Option: {args[0]} set to {str(sets[args[0]][0])}.')
			else:
				if args[0] not in sets:
					await message.edit(content=f"{args[0]} Does not exist.")
				else:
					await message.edit(content=f"Invalid setting for {args[0]}.")

if __name__ == "__main__":
	try:
		if token == "" or token is None:
			print("[!] No token supplied.")
			_exit(1)
		else:
			cbot.run(token, bot=False)
	except Exception as Err:
		print("Error: " + str(Err))
		exit(1)
