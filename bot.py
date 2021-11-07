import discord

class EveryBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as { self.user } (ID: { self.user.id })')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content == 'Ping!':
            await message.author.send('Pong!')

if __name__ == '__main__':
    token_file = open('token', 'r')
    token      = token_file.read()
    token_file.close()
    client     = EveryBot()
    client.run(token)