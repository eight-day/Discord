# Circuit self bot written on a chromebook with slightly less..
# ..laziness than usual? Rip or claim this program all you want.
# Notice it's a simple program written by I(8 Day). That you can..
# Complete in your sleep with just abit of try....
# Anyways cya nerds
try:
	import discord, time, colorama
except ImportError as Err:
	print(f"Module not found: {Err.name}, so install it nerd.")

cbot, token, prefix, sets, logs = (
	discord.Client(),
	"YOUR DISCORD TOKEN HERE NERD",
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

@cbot.event
async def on_message(message: discord.Message) -> None:
	#Add your own stuff here nerd, don't constantly ask me to.
	#Understand the base working of it and edit based on that.
	
	content, author, channel, embeds, attachments = (
		message.content,
		message.author,
		message.channel,
		message.embeds,
		message.attachments
	)
	def check(message: discord.Message) -> bool:
		if not sets["allow_others"]:
			return True if (message.author == cbot.user) else False
		else:
			return True
	
	if content.startswith(prefix):
		if ( not sets["allow_others"] and not check(message) ): return
		if author not in sets["allow_others"][1]: return
		
		# Yes, I could've one lined the above, but it looked bad.
		await message.delete()
		command, *args = content.strip(prefix).split()
		if command == "purge":
			limit = int(args[0]) if args.__len__ >= 1 and args[0].isdigit() else None
			async for msg in channel.history(limit=limit):
				if check(msg):
					try: await msg.delete()
					except: continue
		if command == "logs":
			if args.__len__ != 
