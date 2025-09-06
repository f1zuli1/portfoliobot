import discord
from discord.ext import commands
from discord import ui, ButtonStyle, TextStyle
from logic import DB_Manager
from config import DATABASE, TOKEN

manager = DB_Manager(DATABASE)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --------------------- Modal ve Buton ---------------------
class TestModal(ui.Modal, title='Create Profil'):
    field_1 = ui.TextInput(label='Ad')
    field_2 = ui.TextInput(label='Soyad', style=TextStyle.paragraph)
    field_3 = ui.TextInput(label='Dogum Tarihi', placeholder="DD/MM/YY")

    async def on_submit(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        manager.insert_profile(user_id, self.field_1.value, self.field_2.value, self.field_3.value)
        await interaction.response.send_message("Profiliniz kaydedildi!", ephemeral=True)

class TestButton(ui.Button):
    def __init__(self):
        super().__init__(label="Profil", style=ButtonStyle.blurple)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(TestModal())

class TestView(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(TestButton())

# --------------------- Bot Events ---------------------
@bot.event
async def on_ready():
    print(f'Bot hazır! {bot.user} olarak giriş yapıldı.')

# --------------------- Komutlar ---------------------
@bot.command()
async def start(ctx):
    await ctx.send("Merhaba! Ben bir proje yöneticisi botuyum. =) \nKomutlar için !info yazabilirsiniz.")
    # info komutunu bot sistemi üzerinden çağır
    await ctx.invoke(bot.get_command('info'))

@bot.command()
async def info(ctx):
    await ctx.send("""
Kullanabileceğiniz komutlar şunlardır:

!new_project - yeni bir proje eklemek
!projects - tüm projelerinizi listelemek
!update_projects - proje verilerini güncellemek
!skills - belirli bir projeye beceri eklemek
!delete - bir projeyi silmek
!createprofil - profil oluşturmak
!profil - profili görüntülemek
!deleteprofil - profili silmek
""")

@bot.command()
async def createprofil(ctx):
    await ctx.send("Bu düğmeye basarak profil oluşturabilirsiniz:", view=TestView())

@bot.command()
async def profil(ctx):
    user_id = ctx.author.id
    profile = manager.get_profile(user_id)
    if profile:
        ad, soyad, dogum_tarixi = profile
        await ctx.send(f"ID: {user_id}\nAd: {ad}\nSoyad: {soyad}\nDogum Tarihi: {dogum_tarixi}")
    else:
        await ctx.send("Henüz bir profil oluşturmadınız. !createprofil komutunu kullanın.")

@bot.command()
async def deleteprofil(ctx, user_id: int):
    profile = manager.get_profile(user_id)
    if profile:
        manager.delete_profile(user_id)
        await ctx.send(f"{user_id} ID’li profil başarıyla silindi.")
    else:
        await ctx.send(f"{user_id} ID’li profili bulamadım.")

# --------------------- Bot Run ---------------------
bot.run(TOKEN)
