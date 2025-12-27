import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

BOT_TOKEN = "توکن_بات_تلگرامت_از_BotFather"  # مثلاً 7234567890:AAF...
FAL_API_KEY = "e9f920d6-896f-4068-92d3-782df838676a:3fe3ef70848fb7e8eab0e9a96f5aa4dd"  # key خودت

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌌 سلام به XI AI Meme Generator! 🚀\n\n"
        "مم‌های holographic futuristic با تم xAI و Grok می‌سازم!\n"
        "prompt بنویس، مثلاً:\n"
        "• XI logo with neon blue holographic eye in cosmic space\n"
        "• Grok AI robot holding $XI token\n\n"
        "سبک اتوماتیک اضافه می‌شه!\n"
        "#XItoTheMoon"
    )

@dp.message(F.text & ~F.command)
async def generate_meme(message: Message):
    prompt = message.text.strip()
    
    full_prompt = f"{prompt}, highly detailed holographic futuristic AI art, neon blue glowing circuits, xAI Grok inspired, dark space background, ultra sharp, cinematic lighting, maximum truth vibe"
    
    await message.answer("🧠 در حال ساخت meme با Fal.ai (Flux model)... (۱۰-۲۰ ثانیه) 🚀")

    try:
        response = requests.post(
            "https://fal.run/fal-ai/flux/schnell",
            headers={
                "Authorization": f"Key {FAL_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": full_prompt,
                "image_size": "square_hd"
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            image_url = data["images"][0]["url"]
            await message.answer_photo(
                image_url,
                caption=f"ممنون که از XI AI Meme Generator استفاده کردی! 🌌\n"
                        f"Prompt: {prompt}\n\n"
                        f"#XI #xAI #Grok #XItoTheMoon"
            )
        else:
            await message.answer(f"خطا: {response.text} – دوباره امتحان کن.")
    
    except Exception as e:
        await message.answer("مشکل فنی! بعداً امتحان کن 😅")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("XI AI Meme Generator Bot با Fal.ai در حال اجراست 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
