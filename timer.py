import pygetwindow as pg
import time
import asyncio
import discord
from discord.ext import commands
from discord.ui import Button, View
from PIL import ImageGrab
import keyboard
import pyautogui
import pydirectinput as di


bot_token = "YOUR_TOKEN"

intents = discord.Intents.all()
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)



# Global variale to store the value entered for Update Money function

money = 0




def tfs(output_file):
    # Capture a fullscreen screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot to the specified output file
    screenshot.save(output_file)


def press_z_key():
    keyboard.press('z')
    time.sleep(0.1)  # Convert milliseconds to seconds
    keyboard.release('z')


def press_u_key():
    keyboard.press('u')
    time.sleep(0.1)  # Convert milliseconds to seconds
    keyboard.release('u')


def press_p_key():
    keyboard.press('p')
    time.sleep(0.1)  # Convert milliseconds to seconds
    keyboard.release('p')


def press_o_key():
    keyboard.press('o')
    time.sleep(0.1)  # Convert milliseconds to seconds
    keyboard.release('o')


def press_k_key():
    keyboard.press('k')
    time.sleep(0.1)  # Convert milliseconds to seconds
    keyboard.release('k')


def press_i_key():
    keyboard.press('i')
    time.sleep(0.1)  # Convert milliseconds to seconds
    keyboard.release('i')


def press_j_key():
    keyboard.press('j')
    time.sleep(0.1)  # Convert milliseconds to seconds
    keyboard.release('j')


def press_l_key():
    keyboard.press('l')
    time.sleep(0.1)  # Convert milliseconds to seconds
    keyboard.release('l')


def end_timer():
    tasks = asyncio.all_tasks()
    for task in tasks:
        task.cancel()


def switchToGTA():
    def timeout_function():
        start_time = time.time()
        order = pg.getAllTitles()
        while("" in order):
            order.remove("")
        index = 0
        for i in range(len(order)):
            if order[i] == "Grand Theft Auto V":
                index = i
                break
        while time.time() - start_time < 7:  # Adjust the timeout value as needed (7 seconds in this case)
            current_window_title = pyautogui.getActiveWindowTitle()
            if current_window_title == "Grand Theft Auto V":
                print(f"Switched to window with title: {current_window_title}")
                return True  # Return True if successfully switched
            time.sleep(0.1)
            di.keyDown('alt')
            for j in range(index):
                di.keyDown('tab')
                di.keyUp('tab')
            di.keyUp('alt')
            index += 1
        return False  # Return False if timed outo

    while not timeout_function():  # Loop until the switch is successful
        print("Switching to GTA timed out. Trying again...")
        time.sleep(1)  # Wait for 1 second before retrying


def take_screenshot(filename):
    # Find the "Grand Theft Auto V" window
    window_title_to_find = "Grand Theft Auto V"
    window = pg.getWindowsWithTitle(window_title_to_find)[0]

    # Get the window's position and size
    window_left = window.left
    window_top = window.top
    window_width = window.width
    window_height = window.height

    # Capture the screenshot of the window
    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot.save(filename)




@bot.command()
async def p(ctx):
    press_p_key()
    tfs("tfs.png")
    await ctx.send(file=discord.File("tfs.png"))


@bot.command()
async def u(ctx):
    press_u_key()
    tfs("tfs.png")
    await ctx.send(file=discord.File("tfs.png"))


@bot.command()
async def o(ctx):
    press_o_key()
    tfs("tfs.png")
    await ctx.send(file=discord.File("tfs.png"))


@bot.command()
async def i(ctx):
    press_i_key()
    tfs("tfs.png")
    await ctx.send(file=discord.File("tfs.png"))


@bot.command()
async def k(ctx):
    press_k_key()
    tfs("tfs.png")
    await ctx.send(file=discord.File("tfs.png"))


@bot.command()
async def l(ctx):
    press_l_key()
    tfs("tfs.png")
    await ctx.send(file=discord.File("tfs.png"))


@bot.command()
async def j(ctx):
    press_j_key()
    tfs("tfs.png")
    await ctx.send(file=discord.File("tfs.png"))


@bot.command()
async def z(ctx):
    switchToGTA()
    press_z_key()  # Press 'z' key automatically
    print("PRESSED")
    take_screenshot("screenshot.png")
    print("SCREENSHOT")
    await ctx.send(file=discord.File("screenshot.png"))


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def update_money(ctx, new_amount: int):
    global money
    money = new_amount
    await ctx.send(f'Money updated! New amount: ${money:,}')
    return money

@bot.command()
async def initialize_104(ctx):
    switchToGTA()
    order = [101, 98, 98, 98, 102, 102, 102, 102, 102, 101, 96, 98, 98, 98, 98, 98, 98, 101,
             101, 96, 98, 98, 98, 98, 98, 98, 98, 101, 101, 101, 98, 98, 98, 101, 98, 98, 98, 98]
    for i in range(len(order)):
        di.keyDown(order[i])
        await asyncio.sleep(0.1)
        di.keyUp(order[i])
        await asyncio.sleep(0.2)
        if i == 9:
            await asyncio.sleep(15)
    di.press('m')
    await asyncio.sleep(1)
    di.press('down')
    await asyncio.sleep(0.1)
    di.press('enter')
    await asyncio.sleep(0.1)
    di.press('enter')
    await asyncio.sleep(0.1)
    di.press('enter')

    await ctx.send('READY')
    await ctx.send('TYPE IN !START')


@bot.command()
async def initialize_87(ctx):
    switchToGTA()
    order = ['o', 'p', 'u', 'k', 'k', 'k', 'l', 'l', 'l', 'l', 'l', 'u', 'o', 'k', 'k', 'k', 'k', 'k', 'k',
             'u', 'u', 'o', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'u', 'u', 'u', 'k', 'k', 'k', 'u', 'k', 'k', 'k', 'k']
    for i in range(len(order)):
        keyboard.press(order[i])
        await asyncio.sleep(0.2)
        keyboard.release(order[i])
        await asyncio.sleep(0.2)
        if i == 11:
            await asyncio.sleep(15)
    di.press('m')
    await asyncio.sleep(1)
    di.press('down')
    await asyncio.sleep(0.2)
    di.press('enter')
    await asyncio.sleep(0.2)
    di.press('enter')
    await asyncio.sleep(0.2)
    di.press('enter')

    await ctx.send('READY')
    await ctx.send('TYPE IN !START')


@bot.command()
async def test(ctx):
    await ctx.send("The bot is online")


@bot.command()
async def delete_all(ctx):
    try:
        # Delete all messages in the channel
        await ctx.channel.purge(limit=None)
    except discord.Forbidden:
        await ctx.send("I don't have the permission to delete messages in this channel.")

@bot.command()
async def start(ctx):
    total_seconds = 30 * 60 + 52  # Initial 30 minutes
    await start_timer(ctx, total_seconds)



@bot.command()
async def start_timer(ctx, total_seconds):
    switchToGTA()
    press_z_key()  # Press 'z' key automatically
    take_screenshot("screenshot.png")
    await ctx.send(file=discord.File("screenshot.png"))
    await ctx.send('INITIAL AMOUNT')
    press_u_key()
    pyautogui.keyDown('num5')
    await asyncio.sleep(0.1)
    pyautogui.keyUp('num5')
    
    
    count = 0
    while True:

        # Function to update the remaining time in the channel
        async def update_remaining_time():
            nonlocal total_seconds

            while total_seconds > 0:
                await asyncio.sleep(1)
                elapsed_time = time.time() - start_time  # Calculate the elapsed time
                remaining_time = total_seconds - \
                    int(elapsed_time)  # Calculate remaining time
                if remaining_time <= 0:
                    break
                minutes, secs = divmod(remaining_time, 60)
                remaining_time_str = f"Time remaining: {minutes:02d}:{secs:02d}"

                # Edit the previous message with the new time
                await previous_message.edit(content=remaining_time_str)

            # If the loop ends, send "Time's up!" message
            await ctx.send("Time's up!")

        count += 1
        await ctx.send(f'第{count}次')
        await ctx.send(f'${money:,}')

        start_time = time.time()  # Get the current time as the starting point

        # Send initial remaining time message
        minutes, secs = divmod(total_seconds, 60)
        remaining_time_str = f"Time remaining: {minutes:02d}:{secs:02d}"
        previous_message = await ctx.send(remaining_time_str)

        # Run the update_remaining_time task in the background
        update_task = asyncio.create_task(update_remaining_time())

        # Loop to simulate 105 seconds delay and other actions
        for i in range(105):
            await asyncio.sleep(1)
            print(i + 1)

        press_z_key()  # Press 'z' key automatically
        print("PRESSED")
        take_screenshot("screenshot.png")
        print("SCREENSHOT")
        await ctx.send(file=discord.File("screenshot.png"))

        # Calculate money at the end of each loop
        money += 2491280
        await ctx.send(f'${money:,}')

        # Wait for the update_remaining_time task to complete
        await update_task

        # Calculate the remaining time accurately after the loop
        elapsed_time = time.time() - start_time

        # Wait for 30 minutes before the next loop
        await asyncio.sleep(total_seconds - int(elapsed_time))




@bot.command()
async def end_timer(ctx):
    # Function to end the timer
    end_timer()

class MyView(View):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

    @discord.ui.button(label="Initialize 104", style=discord.ButtonStyle.green)
    async def init_104(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.ctx.send("Initializing 104...")
        switchToGTA()
        order = [101, 98, 98, 98, 102, 102, 102, 102, 102, 101, 96, 98, 98, 98, 98, 98, 98, 101,
                101, 96, 98, 98, 98, 98, 98, 98, 98, 101, 101, 101, 98, 98, 98, 101, 98, 98, 98, 98]
        for i in range(len(order)):
            di.keyDown(order[i])
            await asyncio.sleep(0.1)
            di.keyUp(order[i])
            await asyncio.sleep(0.2)
            if i == 9:
                await asyncio.sleep(15)
        di.press('m')
        await asyncio.sleep(1)
        di.press('down')
        await asyncio.sleep(0.1)
        di.press('enter')
        await asyncio.sleep(0.1)
        di.press('enter')
        await asyncio.sleep(0.1)
        di.press('enter')

        await self.ctx.send('READY')
        await self.ctx.send('TYPE IN !START')
        

    @discord.ui.button(label="Initialize 87", style=discord.ButtonStyle.green)
    async def init_87(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.ctx.send("Initializing 87...")
        switchToGTA()
        order = ['o', 'p', 'u', 'k', 'k', 'k', 'l', 'l', 'l', 'l', 'l', 'u', 'o', 'k', 'k', 'k', 'k', 'k', 'k',
                'u', 'u', 'o', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'u', 'u', 'u', 'k', 'k', 'k', 'u', 'k', 'k', 'k', 'k']
        for i in range(len(order)):
            keyboard.press(order[i])
            await asyncio.sleep(0.1)
            keyboard.release(order[i])
            await asyncio.sleep(0.2)
            if i == 11:
                    await asyncio.sleep(15)
        di.press('m')
        await asyncio.sleep(1)
        di.press('down')
        await asyncio.sleep(0.1)
        di.press('enter')
        await asyncio.sleep(0.1)
        di.press('enter')
        await asyncio.sleep(0.1)
        di.press('enter')

        await self.ctx.send('READY')
        await self.ctx.send('TYPE IN !START')
        

    @discord.ui.button(label="Test", style=discord.ButtonStyle.primary)
    async def test(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.ctx.send("The bot is online")

    @discord.ui.button(label="Capture Screenshot (Z)", style=discord.ButtonStyle.primary)
    async def capture_z(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.ctx.send("Taking a screenshot...")
        switchToGTA()
        press_z_key()  # Press 'z' key automatically
        print("PRESSED")
        take_screenshot("screenshot.png")
        print("SCREENSHOT")
        await self.ctx.send(file=discord.File("screenshot.png"))
        


    @discord.ui.button(label="Delete All", style=discord.ButtonStyle.primary)
    async def deleteAll(self, button: discord.ui.Button, interaction: discord.Interaction):
        try:
        # Delete all messages in the channel
            await self.ctx.channel.purge(limit=None)
        except discord.Forbidden:
            await self.ctx.send("I don't have the permission to delete messages in this channel.")
    
    @discord.ui.button(label="Start!", style=discord.ButtonStyle.primary)
    async def startall(self, button: discord.ui.Button, interaction: discord.Interaction):
        total_seconds = 30 * 60 + 52  # Initial 30 minutes
        await start_timer(self.ctx, total_seconds)

    @discord.ui.button(label="Update Money", style=discord.ButtonStyle.green)
    async def update_money(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.ctx.send("Please enter the new amount of money:")
        try:
            message = await bot.wait_for('message', timeout=30.0, check=lambda m: m.author == self.ctx.author and m.channel == self.ctx.channel)
            new_amount = int(message.content)
            global money
            money = new_amount
            await self.ctx.send(f'Money updated! New amount: ${money:,}')
        except asyncio.TimeoutError:
            await self.ctx.send('You took too long to respond!')

    @discord.ui.button(label="Show Money", style=discord.ButtonStyle.primary)
    async def show_money(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.ctx.send(f'Current Money: {money:,}')
    

        



@bot.command()
async def board(ctx):
    # Send the interactive message with buttons using the custom view
    view = MyView(ctx)
    message = await ctx.send("Use the buttons below to interact with the board commands.", view=view)

    # Wait for the user's response and add the view to the message interaction
    interaction = await bot.wait_for("message_action", check=lambda i: i.user == ctx.author and i.message.id == message.id)
    view.message = interaction.message
    await interaction.respond(type=6, view=view)

@bot.command()
async def show_money(ctx):
    await ctx.send(f'Current Money: {money:,}')


if __name__ == "__main__":
    bot.run(bot_token)
