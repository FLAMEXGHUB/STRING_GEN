from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"ℍ𝔼𝕐 𝕋ℍ𝔼ℝ𝔼🥀 {message.from_user.first_name},\n\n๏ 𝐓ʜɪs 𝐈s {Anony.mention},\nAɴ 𝐎ᴘᴇɴ 𝐒ᴏᴜʀᴄᴇ 𝐒ᴛʀɪɴɢ 𝐒ᴇssɪᴏɴ 𝐆ᴇɴᴇʀᴀᴛᴏʀ 𝐁ᴏᴛ, 𝐖ʀɪᴛᴛᴇɴ 𝐈ɴ 𝐏ʏᴛʜᴏɴ 𝐖ɪᴛʜ 𝐓ʜᴇ 𝐇ᴇʟᴩ 𝐎ғ 𝐏ʏʀᴏɢʀᴀᴍ. 𝐓ʜɪs 𝐁ᴏᴛ 𝐈s 𝐁ᴏᴜɢʜᴛ 𝐓ᴏ 𝐘ᴏᴜ 𝐁ʏ~ @FL4ME_BOTS",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)