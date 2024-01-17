import time
import discord_rpc
from gamestate import GameState
GSInstance = GameState()


class SpaceGameRPC:

    def readyCallback(self, current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(self, codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(self, errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))

    def start(self):
        callbacks = {
            'ready': self.readyCallback,
            'disconnected': self.disconnectedCallback,
            'error': self.errorCallback,
        }
        discord_rpc.initialize('852656088586125315', callbacks=callbacks, log=False)
        start = time.time()
        while True:
            discord_rpc.update_presence(
                **{
                    'details': GSInstance.GAMESTATE,
                    'start_timestamp': start,
                    'large_image_key': 'default'
                }
            )
            discord_rpc.update_connection()
            time.sleep(2)
            discord_rpc.run_callbacks()

    def stop(self):
        discord_rpc.shutdown()