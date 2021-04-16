import asyncio
import httpx

from django.http import HttpResponse
from django.core.mail import EmailMessage


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

    email = EmailMessage('Subject here',
                         'Here is the message.',
                         'venkates@soulpageit.com',
                         ['venkatesh.marreboyina@soulpageit.com', 'raviteja.marum@soulpageit.com'])
    email.content_subtype = "html"
    email.send()


async def index(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")
