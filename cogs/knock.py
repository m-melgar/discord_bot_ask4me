import os, sys, discord
from discord.ext import commands
import persistqueue

# Only if you want to use variables that are in the config.py file.
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config


# Here we name the cog and create a new class for the cog.
class Meeting_Handler(commands.Cog, name="knock"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.command(name="knock")
    async def knock(self, context):
        """
        Knocks the door, if:
            if door is open: moves teacher and command author to the meeting room
            if door is closed: waits til teacher approval to move teacher and command author to the meeting room
            if teacher is outside: sends an stored message
        """
        if config.DOOR_STATUS == 'open':
            # move teacher & author
            embed = discord.Embed(
                title="door is open",
                description=f"**{context.message.author}** you are now move to the meeting room",
                color=config.success
            )
            await context.send(embed=embed)
            await context.author.move_to(self.bot.get_channel(config.MEETING_ROOM_ID))

        if config.DOOR_STATUS == 'close':
            q = persistqueue.UniqueQ(config.DB_PATH)
            q.put(context.message.author.id)
            embed = discord.Embed(
                title="door is closed",
                description=f"**{context.message.author}** you have been put in the waiting queue at position {q.size}"
                            f"\nfriendly reminder that your position in queue is unique",
                color=config.success
            )
            await context.send(embed=embed)

        if config.DOOR_STATUS == 'out':
            embed = discord.Embed(
                title="OUT OF DISCORD",
                description=config.TEACHER_OUTSIDE_MESSAGE,
                color=config.warning
            )
            await context.send(embed=embed)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Meeting_Handler(bot))
