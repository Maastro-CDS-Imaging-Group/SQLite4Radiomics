import sys
import os

from pathos import multiprocessing
import src.calculate.calculation_script as calc

calculator: calc.Calculator = calc.Calculator()

import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer



class MessageConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, message):
        data = json.loads(message['text'])
        print(data)

        if data['message'] == 'start':
            calculator.main()
            await self.send({
                'text': json.dumps({'progress': f'{calculator.get_progress()}'})
            }, immediately=True)

        elif data['message'] == 'cancel':
            calculator.set_command()
            await self.send({
                'text': json.dumps({'progress': f'{calculator.get_progress()}'})
            }, immediately=True)

    async def websocket_send(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        await self.send({
            'type': 'websocket.disconnect'
        })
