# Circuit self bot written on a chromebook with slightly less..
# ..laziness than usual? Rip or claim this program all you want.
# Notice it's a simple program written by I(8 Day). That you can..
# Complete in your sleep with just abit of try....
# My faith runs soly in a docker and pure idk?
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
		_exit   # Closing the program and all of its children
	)
	from time import ctime, strftime
	from getpass import getpass # If you don't supply a token, you should atleast supply the login details.
except ImportError as Err:
	print(f"Module not found: {Err.name} | Install it and re-run.")
	exit()

cbot, token, prefix, sets, logs = (
	Client(),
	"", # Your token here if you dont wanna login each time.
	"!c ",
	{
		"deleted_logger": (False, []),
		"save_attachments": (False, []), # Not rec for accounts in many servers uwu.
		"allow_others": (False, [])
	},
	{
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
	def check(message: Message) -> bool:
		"""
		Do not use nonlocal unless you know it will not interfere.
		Using nonlocal with the below will cause errors and false positives.
		"""
		return message.author == cbot.user if not sets["others"] else (
			message.author in sets["allow_others"][1]
		)
	
	if content.startswith(prefix):
		if ( not sets["allow_others"] and not check(message) ): return
		if author not in sets["allow_others"][1]: return
		
		# Yes, I could've one lined the above, but it looked bad.
		command, *args = content.strip(prefix).split()
		if command == "purge":
			limit = int(args[0]) if args.__len__ >= 1 and args[0].isdigit() else None
			async for msg in channel.history(limit=limit):
				if check(msg):
					try: await msg.delete()
					except: continue
			await message.delete()
		if command == "logs":
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
			except IndexError:
				await message.edit("Error: no path supplied.")
				await message.edit(content)
			
			messages = []
			async for msg in channel.history(limit=None):
				if isinstance(msg.type, MessageType.default):
					messages.append(f"{msg.created_at} | {msg.author.name} > {msg.content}")
				if isinstance(msg.type, MessageType.call):
					messages.append(f"{msg.created_at} | {msg.author.name} > User called.")
			arguments["outdata"] = messages
			write_data(**arguments)
		if command == "break":
			if "nosave" in args:
				await channel.send("[+] Closed and didn't save.")
				_exit()
			await channel.send("[+] Closed and saved.")
			_exit()

if __name__ == "__main__":
	try:
		if token == "" or token is None:
			cbot.run(
				input("Username: "),
				getpass("Password: ")
			)
		else:
			cbot.run(token, bot=False)
	except Exception as Err:
		print("Error: " + str(Err))
		exit(1)
