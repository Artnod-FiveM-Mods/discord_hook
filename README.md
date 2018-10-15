[![GitHub license](https://img.shields.io/github/license/Artnod-FiveM-Mods/discord_hook.svg)](https://github.com/Artnod-FiveM-Mods/discord_hook/blob/master/LICENSE) :small_blue_diamond: 
[![Discord](https://img.shields.io/discord/436197783331012629.svg)](https://discord.gg/u7dj7Ja)  
# discord_hook  
IS NOT A SCRIPT FOR FIVEM. It's a third party script.  

**Features:**
  * Check **IP** and **TCP** port every **X** seconds.
  * Send one or more message with a simple command.

**Requirements:**
   * Python 3
   * requests, lxml
 
# Use  
  * Run the command from the discord_hook folder.  
``python cmd_hook.py TOPHOOK``    
``python tcp_hook.py``  

# Configuration  
## Hook Config  
```python
WEBHOOK_CONF = {
    'webhook_url' : 'changeme',
}
```
Replace **changeme** by your webhook url  

## Fivem Config  
```python
FIVEM_CONF = {
    'server_name' : 'ArtNod test server',
    'server_ip'   : '51.15.244.36',
    'server_port' : 30120,
    'check_delay' : 5
}
```
Replace by your custom settings  

## Custom messages
You can add your custom messages in ``settings.py``
  * webhook_url
  * color
  * msg
  * message
    * author: name and icon
    * desc_text
    * fields: name and value
    * thumbnail
    * footer: text and icon
