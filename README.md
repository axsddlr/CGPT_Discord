<div id="top"></div>

<br />
<div align="center">

<img src="https://styles.redditmedia.com/t5_7hqomg/styles/communityIcon_yyc98alroh5a1.jpg" alt="Logo" width="80" height="80" style="border-radius: 25%;">

<a href="https://www.reddit.com/r/ChatGPT/">
  <h3 align="center">CGPT-Basic-Discord</h3>
</a>

  <p align="center">
    A Basic ChatGPT script Discord bot using <a href="https://github.com/acheong08/ChatGPT">acheong08's</a> Reverse Engineered ChatGPT API by OpenAI
    <br />
    <br />
    <br />

  </p>
</div>

### Contents
<div id="index"></div>

* <p align="left"><a href="#prereq">Installation</a></p>
* <p align="left"><a href="#config">Config</a></p>
* <p align="left"><a href="#usage">Usage</a></p>
* <p align="left"><a href="#api_key">API Key</a></p>
<p align="right">(<a href="#top">back to top</a>)</p>


### Pre-Requisites
<div id="prereq"></div>

This is an example of how to list things you need to use the software and how to install them.
* python 3.9 +

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/axsddlr/CGPT_Discord.git
   ```
2. python
   ```sh
   python -m pip install -r requirements.txt
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

## Obtaining openAI API Key
<div id="api_key"></div>

1. Create account on [OpenAI](https://platform.openai.com/)
2. Go to https://platform.openai.com/account/api-keys
3. Copy API key

<p align="right">(<a href="#top">back to top</a>)</p>

## Config
<div id="config"></div>
change config.example.json to config.json

**Current working model is "text-chat-davinci-002-20221122"**

```
{
    "DISCORD_TOKEN": "<discord bot token>",
    "discord_id":"<discord_id>",
    "api_key": "<openai_api_key>"
    "model_ver": "<working model name>"
}
```
<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
<div id="usage"></div>

   ```sh
  python bot.py
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



