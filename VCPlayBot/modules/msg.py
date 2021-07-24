import os
from VCPlayBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Salam 👋 [{}](tg://user?id={})!**\n\n🤖 Telegram Qrupları və Kanallarının səsli söhbətlərində musiqi çalmaq üçün yaradılmış bir botam.\n\n✅ Daha çox məlumat üçün mənə /help göndərin."
      HELP_MSG = [
        ".",
f"""
**Salam 👋 Xoş gəlmisiniz {PROJECT_NAME}

⚪️ {PROJECT_NAME} kanal səsli söhbətləri ilə yanaşı qrupunuzun səsli söhbətində də musiqi səsləndirə bilər

⚪️ Köməkçi ad >> @{ASSISTANT_NAME}\n\nTəlimatlar üçün növbəti klikləyin**
""",

f"""
**Ayarlamaq**

1) Bota qrup ve kanalınızda adminlik yetkisi verin
2) Səsli söhbətə başlayın
3) Bir admin tərəfindən /play [mahnı adı] sınayın
*) Musiqibot qoşulubsa, musiqidən həzz alın, Olmasa @ {ASSISTANT_NAME} adlı qrupu əlavə edin və yenidən cəhd edin



**Əmrlər**

**=>> Mahnı oxutmaq 🎧**

- /play: İstədiyiniz mahnını oxudun
- /play [yt url] : Verilmiş url oxudun
- /play [reply yo audio]: yYanıt verilən səsi oxudun


**=>> İzləmə ⏯**

- /player: Ayarlar menyusunu açır
- /skip: Mövcud parçanı atlayır
- /pause: Musiqini dayandırır
- /resume: Dayandırılmış parçanı davam etdirir
- /end: Oxunan mahnını dayandırır
- /current: Oxunan mahnının adını göstərir
- /playlist: Mahnı siyahısını göstərir

* play, / current və / playlist istisna olmaqla digər bütün əmrlər yalnız qrup adminləri üçündür.
""",
        
f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /gcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
