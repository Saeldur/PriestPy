from twitch import TwitchClient

class TwitchHandler:

    async def validateStream(url, twitch_id):
        client = TwitchClient(client_id=twitch_id)
        channelName = url.split('/')[-1]
        channels = client.search.channels(channelName)
        
        if channels:
            channel = channels[0]
            return 'World of Warcraft' in channel.game
        
        return False
        
    async def fetchStreamInfo(url, twitch_id):
        client = TwitchClient(client_id=twitch_id)
        channelName = url.split('/')[-1]
        channels = client.search.channels(channelName)
        
        title = None
        description = None
        avatar = None
        views = None
        followers = None
                
        if channels:
            channel = channels[0]
            
            for ch in channels:
                if ch.display_name == channelName:
                    channel = ch
                    break

            avatar = channel.logo
            title = channel.status
            description = channel.description
            views = channel.views
            followers = channel.followers
        
        return title, description, avatar, views, followers
