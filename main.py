import discord, os
from discord.ext import commands, tasks
from discord.ui import Button, View, Select, Modal
import math
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from questions import computing, religious_education
import random
import cmath
import asyncio
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from flask import Flask
from threading import Thread



app = Flask('')

def run():
    app.run(host="0.0.0.0", port=8080)

@app.route('/')
def home():
    return "hi :) under development"

t2 = Thread(target=run)
t2.start()

uri = "mongodb+srv://CoinBot:coinbot123@coinbot.nqsluqc.mongodb.net/CoinBot?retryWrites=true&w=majority"

mongo_client = MongoClient(uri)
data_link = mongo_client.StudyBot
mongo_link = data_link.UserData

load = mongo_link.find_one({"_id": ObjectId("664110ab0baf6ec9ea4e2cc9")})
db = dict(load)

mongo_link.insert_one({})
async def discordinput(ctx, check=None, msg=None, timetoquit=300):
  if check==None:
    def check(m):
      return m.author == ctx.author
  if msg!=None:
    await ctx.reply(msg)
  if timetoquit==None:
    timetoquit=300
  try:
    prompt = await bot.wait_for('message', check=check, timeout=timetoquit)
    return prompt.content.lower()
  except asyncio.TimeoutError:
    return await ctx.reply("Took too long, cancelling...")

def plot_triangle(side_lengths, angles_degrees):
    # if os.path.exists("plot.png"):
    #   os.remove("plot.png")

    # Convert angles to radians
    angles_radians = np.radians(angles_degrees)

    # Coordinates of the vertices
    A = (0, 0)
    B = (side_lengths[0], 0)
    C = (side_lengths[1] * np.cos(angles_radians[0]), side_lengths[1] * np.sin(angles_radians[0]))

    # Plot triangle
    plt.plot([A[0], B[0]], [A[1], B[1]], 'k-')  # Side AB
    plt.plot([B[0], C[0]], [B[1], C[1]], 'k-')  # Side BC
    plt.plot([C[0], A[0]], [C[1], A[1]], 'k-')  # Side CA

    # Label sides
    plt.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2, f'{side_lengths[2]}', horizontalalignment='center', verticalalignment='bottom')
    plt.text((B[0] + C[0]) / 2, (B[1] + C[1]) / 2, f'{side_lengths[0]}', horizontalalignment='right', verticalalignment='top')
    plt.text((C[0] + A[0]) / 2, (C[1] + A[1]) / 2, f'{side_lengths[1]}', horizontalalignment='left', verticalalignment='top')

    plt.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2, f'C', horizontalalignment='center', verticalalignment='top', fontsize=16, weight='bold')
    plt.text((B[0] + C[0]) / 2, (B[1] + C[1]) / 2, f'B', horizontalalignment='left', verticalalignment='bottom', fontsize=16, weight='bold')
    plt.text((C[0] + A[0]) / 2, (C[1] + A[1]) / 2, f'A', horizontalalignment='right', verticalalignment='bottom', fontsize=16, weight='bold')

    # Label angles
    plt.text(B[0]*0.96666, B[1], f'{angles_degrees[2]}°', verticalalignment='bottom', horizontalalignment='right')
    plt.text(C[0], C[1]*0.9, f'{angles_degrees[1]}°', verticalalignment='top', horizontalalignment='left')
    plt.text(A[0]+(C[1]/30), A[1]+(B[0]/30), f'{angles_degrees[0]}°', verticalalignment='bottom', horizontalalignment='left')

    # Label points with larger font size
    plt.text(A[0], A[1], 'X', verticalalignment='bottom', horizontalalignment='right', fontsize=16, weight='bold')
    plt.text(B[0], B[1], 'Z', verticalalignment='bottom', horizontalalignment='left', fontsize=16, weight='bold')
    plt.text(C[0], C[1], 'Y', verticalalignment='bottom', horizontalalignment='right', fontsize=16, weight='bold')

    #print(A, B, C)

    plt.axis('off')
    plt.grid(False)
    plt.savefig("memory/plot.png")
    plt.clf()

def trig(a = None, b = None, c = None, X = None, Y = None, Z = None):
  if a is not None and b is not None and c is not None:
    X = math.degrees(math.acos( (a**2 + c**2 - b**2)/(2*a*c) ))
    Y = math.degrees(math.acos( (a**2 + b**2 - c**2)/(2*a*b) ))
    Z = math.degrees(math.acos( (b**2 + c**2 - a**2)/(2*b*c) ))
    return a, b, c, X, Y, Z

  # ANGLES IN A TRIANGLE
  if X is None and Y is not None and Z is not None:
    X = 180 - (Y + Z)
  elif Y is None and X is not None and Z is not None:
    Y = 180 - (X + Z)
  elif Z is None and X is not None and Y is not None:
    Z = 180 - (Y + X)

  if Y == 90:
    if a is None and b is not None and c is not None:
      a = ((c**2)-(b**2))**(1/2)
    elif b is None and a is not None and c is not None:
      b = ((c**2)-(a**2))**(1/2)
    elif c is None and a is not None and b is not None:
      c = ((a**2)+(b**2))**(1/2)

  # COSINE RULE
  # solve for side
  if a is None:
    if b is not None and c is not None and Z is not None:
      a = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(math.radians(Z)))
  if b is None:
    if a is not None and c is not None and X is not None:
      b = math.sqrt(a**2 + c**2 - 2*a*c*math.cos(math.radians(X)))
  if c is None:
    if a is not None and b is not None and Y is not None:
      c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(Y)))

  # SINE RULE
  if a is not None and Z is not None:
    if b is None and X is not None:
      b = (a/math.sin(math.radians(Z)))*math.sin(math.radians(X))
    elif X is None and b is not None:
      X = math.degrees(math.asin((math.sin(math.radians(Z))/a)*b))

    if c is None and Y is not None:
      c = (a/math.sin(math.radians(Z)))*math.sin(math.radians(Y))
    elif Y is None and c is not None:
      Y = math.degrees(math.asin((math.sin(math.radians(Z))/a)*c))

  if b is not None and X is not None:
    if a is None and Z is not None:
      a = (b/math.sin(math.radians(X)))*math.sin(math.radians(Z))
    elif Z is None and a is not None:
      Z = math.degrees(math.asin((math.sin(math.radians(X))/b)*a))

    if c is None and Y is not None:
      c = (b/math.sin(math.radians(X)))*math.sin(math.radians(Y))
    elif Y is None and c is not None:
      Y = math.degrees(math.asin((math.sin(math.radians(X))/b)*c))

  if c is not None and Y is not None:
    if a is None and Z is not None:
      a = (c/math.sin(math.radians(Y)))*math.sin(math.radians(Z))
    elif Z is None and a is not None:
      Z = math.degrees(math.asin((math.sin(math.radians(Y))/c)*a))

    if b is None and X is not None:
      b = (c/math.sin(math.radians(Y)))*math.sin(math.radians(X))
    elif X is None and b is not None:
      X = math.degrees(math.asin((math.sin(math.radians(Y))/c)*b))
  return a, b, c, X, Y, Z

def start(a = None, b = None, c = None, X = None, Y = None, Z = None):
  for i in range(5):
    a, b, c, X, Y, Z = trig(a, b, c, X, Y, Z)

  if a is not None and b is not None and c is not None:
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return round(a, 2), round(b, 2), round(c, 2), round(X, 2), round(Y, 2), round(Z, 2), round(area, 2), round(s*2, 2)
  else:
    return a, b, c, X, Y, Z, None, None

TOKEN = os.environ['secret_token']

bot = commands.Bot(command_prefix=["!","."], intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
  print(f'{bot.user} is now running.')

@bot.command(name = "help")
async def help(ctx):
  text = """**!trig** - Triangle calculator, run !trig for more
**!test** - creates a test you can do for a subject, see subjects at !test
**!quadratic** - solves a quadratic equation, inputs at !quadratic
**!analyse** - add data and it will give you graphs and means, !analyse formore"""
  embed = discord.Embed(title = "Commands", description = text)
  await ctx.reply(embed = embed)

@bot.command(name = "trig")
async def trig_command(ctx, *args):
  if len(args) == 0:
    embed = discord.Embed(title = "**Advanced Trignometry**",
                         description = "This command can be used to solve difficult trignometry problems using sine and cosine rules and can help find the area of a triangle which base/height cannot be calculated easily.\n\nUsage: `!trig a=0 b=0 c=0 X=0 Y=0 Z=0`\nHere only enter the values that are given to you such as `!trig a=12 b=5 X=30` and here there MUST be 1 side given and in total at least 3 values.")
    file = discord.File("memory/trigimage.png", filename="trigimage.png")
    embed.set_image(url="attachment://trigimage.png")
    await ctx.reply(embed = embed, file = file)
  else:
    await ctx.message.add_reaction("<a:loading:1225144141806178437>")
    inputstr = str(' '.join(args))
    inputstr = inputstr.replace("A", "a").replace("B", "b").replace("C", "c").replace("x", "X").replace("y", "Y").replace("z", "Z")
    a, b, c, X, Y, Z, area, perimeter = eval(f"start({inputstr})")
    answer = f"""Sides
a = {a} units
b = {b} units
c = {c} units

Angles
X = {X}°
Y = {Y}°
Z = {Z}°

Area: {area} units²
Perimeter: {perimeter} units²"""

    side_lengths = [b, a, c]
    angles_degrees = [X, Y, Z]
    try:
      plot_triangle(side_lengths, angles_degrees)
      file = discord.File("memory/plot.png", filename="plot.png")

      embed = discord.Embed(title = "**Advanced Trignometry**",
                           description = answer)
      embed.set_footer(text = "NOTE: There may be more possible solutions. This is just the first one.")
      embed.set_image(url="attachment://plot.png")
      await ctx.reply(embed = embed, file = file)
    except:
      embed = discord.Embed(title = "**Advanced Trignometry**",
         description = answer)
      embed.set_footer(text = "NOTE: There may be more possible solutions. This is just the first one.")
      await ctx.reply(embed = embed)
    # if a is not None and b is not None and c is not None:
    #   s = (a+b+c)/2
    #   area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    #   embed = discord.Embed(title = "**Advanced Trignometry**",
    #                        description = f"a = {a}\nb = {b}\nc = {c}\nX = {X}\nY = {Y}\nZ = {Z}\nArea = {area}\nPerimeter = {s*2}")
    #   await ctx.reply(embed = embed)
    # else:
    #   await ctx.reply("Invalid values")


@bot.command(name = "quadratic", aliases = ["quad"])
async def quadratic(ctx, *args):
  if len(args) > 0:
    a = int(args[0])
    b = int(args[1])
    c = int(args[2])
    answers = []
    d = (b**2) - (4*a*c)
    ans1 = str((-b-cmath.sqrt(d))/(2*a)).replace("(", "").replace(")", "").replace("+0j", "")
    ans2 = str((-b+cmath.sqrt(d))/(2*a)).replace("(", "").replace(")", "").replace("+0j", "")
    answers.append(ans1)
    answers.append(ans2)
    embed = discord.Embed(title = "**Advanced Quadratics**",
                         description = f'{a}x²{"+" if b>0 else ""}{b}x{"+" if c>0 else ""}{c}\n\n**Answers:**\nx = {answers[0]}\n**or**\nx = {answers[1]}')
    await ctx.reply(embed = embed)
  else:
    embed = discord.Embed(title = "**Advanced Quadratics**",
       description = "This command can be used to solve difficult quadratic problems using the quadratic formulae.\n\nUsage: `!quadratic 1 3 6`\nHere enter all the values in order of a, b, c as suggested by the image below. if you don't know the value of a, b, or c then enter 0 for that value.")
    file = discord.File("memory/quadimage.png", filename="quadimage.png")
    embed.set_image(url="attachment://quadimage.png")
    await ctx.reply(embed = embed, file = file)


def statistics_plots(data):
  # Calculate percentiles
  percentiles = np.percentile(data, np.arange(0, 100, 5))

  # Plot the percentile graph
  plt.figure(figsize=(8, 6))
  plt.plot(np.arange(0, 100, 5), percentiles, marker='x', linestyle='-')

  plt.title('Percentile Graph')
  plt.xlabel('Percentile')
  plt.ylabel('Value')

  plt.grid(True)
  plt.savefig("memory/quartilegraph.png")

  plt.clf()

  plt.figure(figsize=(8, 2))
  plt.boxplot(data, vert=False)
  plt.title('Box Plot')
  plt.xlabel('Data')
  plt.ylabel('Values')
  plt.savefig("memory/boxplot.png")

  # Open the images
  quartile_img = Image.open("memory/quartilegraph.png")
  boxplot_img = Image.open("memory/boxplot.png")

  # Calculate the size of the combined image
  new_width = max(quartile_img.width, boxplot_img.width)
  new_height = quartile_img.height + boxplot_img.height

  # Create a new blank image with the calculated size
  combined_img = Image.new("RGB", (new_width, new_height))

  # Paste the quartile graph on top
  combined_img.paste(quartile_img, (0, 0))

  # Paste the boxplot below the quartile graph
  combined_img.paste(boxplot_img, (0, quartile_img.height))

  # Save the combined image
  combined_img.save("memory/combined_image.png")



@bot.command(name = "analyse")
async def analyse(ctx, *args):
  if len(args) == 0:
    embed = discord.Embed(title = "**Statistics Analyser**",
       description = "This command lets you easily find out the mean median mode IQR etc with some graphs too.\n\nUsage: `!analyse 2 4 9 4 0 3`\nAfter the !analyse, enter all your numbers.")
    await ctx.reply(embed = embed)
  else:
    await ctx.message.add_reaction("<a:loading:1225144141806178437>")
    try:
      numbers = sorted([int(i) for i in list(args)])
      maximum = max(numbers)
      minimum = min(numbers)
      number_range = maximum - minimum
      quantity = len(numbers)
      mode = max(set(numbers), key=numbers.count)
      mean = sum(numbers)/quantity
      median = (numbers[int(quantity/2)-1]+numbers[int(quantity/2)])/2 if quantity % 2 == 0 else numbers[int((quantity+1)/2)-1]
      # if quantity % 2 == 0:
      #   if quantity/2 % 2 == 0:
      #     LQ = (numbers[quantity/4]+numbers[(quantity/4)+1])/2
      #     UQ = (numbers[quantity*3/4]+numbers[(quantity*3/4)+1])/2
      #   else:
      #     LQ = numbers[((quantity+2)/4)-1]
      #     UQ = numbers[quantity/2+((quantity+2)/4)-1]
      # else:
      #   if ((quantity+1)/2)-1 % 2 == 0:
      #     LQ = (numbers[((((quantity+1)/2)-1)/2) - 1] + numbers[(((quantity+1)/2)-1)/2])/2
      #     UQ
      LQ = np.percentile(numbers, 25)
      UQ = np.percentile(numbers, 75)
      IQR = UQ - LQ
      embed = discord.Embed(title = "**Statistics Analyser**",
                            description = f"""Quantity: {quantity}
  Maximum: {maximum}
  Minimum: {minimum}

  Mean: {mean}
  Median: {median}
  Mode: {mode}
  Range: {number_range}

  Lower Quartile: {LQ}
  Upper Quartile: {UQ}
  Inter Quartile Range: {IQR}""")
      statistics_plots(numbers)
      file = discord.File("memory/combined_image.png", filename="combined_image.png")
      embed.set_image(url="attachment://combined_image.png")
      await ctx.reply(embed = embed, file = file)
      # await ctx.reply(embed = embed)
    except Exception as e:
      await ctx.reply(f"An Error has occured. Please inform a developer: {e}")


subjects_={
  "computing": computing,
  "re": religious_education,
}

@bot.command()
async def test(ctx, subject = None, amount = None, type = None):
  if subject == None:
    embed=discord.Embed(title="Supported Subjects for tests.")
    for i in subjects_.keys():
      embed.add_field(name = i.title(), value = "", inline = False)
    return await ctx.reply(embed = embed)



  if amount == None:
    amount = 5
  subjects=subjects_.copy()
  subject=subject.lower()
  embed=discord.Embed(title="Which topic would you like to cover?")
  for num, i in enumerate(subjects[subject]):
    embed.add_field(name=f"{num+1}) {i}",value="", inline = False)
  embed.set_footer(text="Please use the numbers to respond!")
  await ctx.reply(embed=embed)
  prompt=await discordinput(ctx)
  prompt=int(prompt)-1

  if type != None:
    type = type.lower()
    the_questions = {}
    for i,v in subjects[subject][list(subjects[subject].keys())[prompt]].items():
      if v["type"] == type:
        the_questions[i] = v
  else:
    the_questions=subjects[subject][list(subjects[subject].keys())[prompt]].copy()


  total_marks=0
  current_marks=0
  for i in range(0,int(amount)):
    if len(the_questions) == 0:
      if type != None:
        type = type.lower()
        the_questions = {}
        for i,v in subjects[subject][list(subjects[subject].keys())[prompt]].items():
          if v["type"] == type:
            the_questions[i] = v
      else:
        the_questions=subjects[subject][list(subjects[subject].keys())[prompt]].copy()
    question = random.choice(list(the_questions.keys()))
    if the_questions[question]['type']=="type":
      answer = the_questions[question]["answer"]
      embed=discord.Embed(title=f"Question {i+1}",description=question,color=discord.Color.random())
      await ctx.reply(embed=embed)
      inputed=await discordinput(ctx)
      amount=0
      corrected=[]
      extra=[]
      for b in answer:
        if b.lower() in inputed.lower():
          amount+=1
          corrected.append(b)
        else:
          extra.append(b)
      if amount>the_questions[question]["marks"]:
        amount=the_questions[question]["marks"]

      embed=discord.Embed(title=f"Question {i+1}",description=question)
      if amount == 0:
        embed.color=discord.Color.red()
      elif amount == the_questions[question]["marks"]:
        embed.color=discord.Color.green()
      else:
        embed.color=discord.Color.dark_grey()
      embed.add_field(name="Marks",value=f"{amount}/{the_questions[question]['marks']}", inline=False)
      total_marks+=the_questions[question]['marks']
      current_marks+=amount
      text=""
      for i in corrected:
        text+=f"{i}<:correct:1239254032523067505> "
      embed.add_field(name="What's Correct",value=text, inline=False)
      text=""
      for i in extra:
        text+=f"{i}, "
      embed.add_field(name="What You Could Add",value=text, inline=False)
      await ctx.reply(embed=embed)
    elif the_questions[question]['type']=="multi":
      text = question
      answers = the_questions[question]["answers"]
      random.shuffle(answers)
      alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      for index, v in enumerate(the_questions[question]["answers"]):
        text += f"\n{alphabet[index]}: {v}"
      answer = the_questions[question]["answer"]
      embed=discord.Embed(title=f"Question {i+1}",description=text,color=discord.Color.random())
      await ctx.reply(embed=embed)
      inputed = str(await discordinput(ctx)).capitalize()
      total_marks += 1
      embed=discord.Embed(title=f"Question {i+1}",description=question)
      if alphabet.index(inputed) == answers.index(answer[0]):
        current_marks += 1
        embed.color=discord.Color.green()
        embed.add_field(name="Marks",value=f"1/1 <:correct:1239254032523067505>", inline=False)
      else:
        embed.color=discord.Color.red()
        embed.add_field(name="Marks",value=f"0/1 <:incorrect:1239254030773915708>", inline=False)
      await ctx.reply(embed=embed)
    elif the_questions[question]['type']=="definition":
      answer = the_questions[question]["answer"].lower()
      embed=discord.Embed(title=f"Question {i+1}",description=question,color=discord.Color.random())
      await ctx.reply(embed=embed)
      inputed = str(await discordinput(ctx)).lower()
      total_marks += 1
      embed=discord.Embed(title=f"Question {i+1}",description=question)
      
      choice_list = list(inputed.split(" "))
      answer_list = list(answer.split(" "))
      percent_correct = len(list(set(answer_list).intersection(choice_list)))/len(answer_list)
      if percent_correct > 0.75:
        current_marks += 1
        embed.color=discord.Color.green()
        embed.add_field(name="Marks",value=f"1/1 <:correct:1239254032523067505>", inline=False)
      else:
        embed.color=discord.Color.red()
        embed.add_field(name="Marks",value=f"0/1 <:incorrect:1239254030773915708>", inline=False)
        embed.add_field(name="Correct Answer",value=answer, inline=False)
      embed.set_footer(text = f"{round(percent_correct*100)}% correct")
      await ctx.reply(embed=embed)




    #finished
    del the_questions[question]
  embed=discord.Embed(title=f"{list(subjects[subject].keys())[prompt]} Test",description=f"You achieved {current_marks}/{total_marks}<:correct:1239254032523067505> \n\n👏Well Done!👏",color=discord.Color.random())
  await ctx.reply(embed=embed)

  if str(ctx.author.id) not in db:
    temp_data = {"testsData":{}}
    temp_data["testsData"][subject] = [current_marks, total_marks]
    db[str(ctx.author.id)] = temp_data
  else:
    if "testsData" in db[str(ctx.author.id)].keys() and subject in db[str(ctx.author.id)]["testsData"]:
      db[str(ctx.author.id)]["testsData"][subject][0] += current_marks
      db[str(ctx.author.id)]["testsData"][subject][1] += total_marks
    else:
      db[str(ctx.author.id)]["testsData"][subject] = [current_marks, total_marks]

@bot.command(name = "profile", aliases = ["ich"])
async def profile(ctx, person: discord.User = None):
  if person == None:
    person = ctx.author

  if str(person.id) in db:
    embed = discord.Embed(title = f"{person.name}'s Profile'", description = "")
    text = ""
    if "testsData" in db[str(person.id)].keys() and len(db[str(person.id)]["testsData"]) > 0:
      for i, v in db[str(person.id)]["testsData"].items():
        text += f"**{i.title()}** - {round(v[0]*100/v[1])}% ({v[0]} of {v[1]})\n"
    embed.add_field(name = "Tests Average", value = text)
    await ctx.reply(embed = embed)
  else:
    embed = discord.Embed(title = "That person has never used StudyBot before!", description = "")
    await ctx.reply(embed = embed)

@bot.event
async def on_message(message):
  if message.author.id == bot.user.id:
    return
  if str(message.author.id) not in db:
    db[str(message.author.id)] = {"testsData":{}}
  await bot.process_commands(message)
  if (await bot.get_context(message)).valid:
    update = mongo_link.update_one({"_id": ObjectId("664110ab0baf6ec9ea4e2cc9")}, {"$set": db})

if __name__ == "__main__":


  bot.run(TOKEN)
