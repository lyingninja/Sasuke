{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Sasuke",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lyingninja/Sasuke/blob/main/Sasuke.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bORj9z1KX8af",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "db1a7669-a297-4674-c0fa-aebaa9c839f2"
      },
      "source": [
        "\n",
        "!pip install python-telegram-bot --upgrade"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: python-telegram-bot in /usr/local/lib/python3.7/dist-packages (13.7)\n",
            "Requirement already satisfied: pytz>=2018.6 in /usr/local/lib/python3.7/dist-packages (from python-telegram-bot) (2018.9)\n",
            "Requirement already satisfied: tornado>=6.1 in /usr/local/lib/python3.7/dist-packages (from python-telegram-bot) (6.1)\n",
            "Requirement already satisfied: cachetools==4.2.2 in /usr/local/lib/python3.7/dist-packages (from python-telegram-bot) (4.2.2)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.7/dist-packages (from python-telegram-bot) (2021.5.30)\n",
            "Requirement already satisfied: APScheduler==3.6.3 in /usr/local/lib/python3.7/dist-packages (from python-telegram-bot) (3.6.3)\n",
            "Requirement already satisfied: tzlocal>=1.2 in /usr/local/lib/python3.7/dist-packages (from APScheduler==3.6.3->python-telegram-bot) (1.5.1)\n",
            "Requirement already satisfied: setuptools>=0.7 in /usr/local/lib/python3.7/dist-packages (from APScheduler==3.6.3->python-telegram-bot) (57.4.0)\n",
            "Requirement already satisfied: six>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from APScheduler==3.6.3->python-telegram-bot) (1.15.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 764
        },
        "id": "1OF_L6hMYpC6",
        "outputId": "03005fa7-1efb-418d-9ab8-513f9f8c232a"
      },
      "source": [
        "from telegram.ext import Updater\n",
        "updater = Updater(token='2097282130:AAGspMjwMnplLdTqCEhq39JH55NZvyNoNPk', use_context=True)\n",
        "dispatcher = updater.dispatcher\n",
        "import logging\n",
        "logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\n",
        "                     level=logging.INFO)\n",
        "def start(update, context):\n",
        "    context.bot.send_message(chat_id=update.effective_chat.id, text=\"I'm a bot, please talk to me!\")\n",
        "from telegram.ext import CommandHandler\n",
        "start_handler = CommandHandler('start', start)\n",
        "dispatcher.add_handler(start_handler)\n",
        "updater.start_polling()\n",
        "def echo(update, context):\n",
        "    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)\n",
        "\n",
        "from telegram.ext import MessageHandler, Filters\n",
        "echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)\n",
        "dispatcher.add_handler(echo_handler)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-5-5e47c2473265>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mtelegram\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mext\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mUpdater\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mupdater\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mUpdater\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtoken\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'2097282130:AAGspMjwMnplLdTqCEhq39JH55NZvyNoNPk'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muse_context\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mdispatcher\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mupdater\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdispatcher\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mlogging\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/telegram/ext/__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     41\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     42\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mjobqueue\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mJobQueue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mJob\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 43\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mupdater\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mUpdater\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     44\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mcallbackqueryhandler\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mCallbackQueryHandler\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     45\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mchoseninlineresulthandler\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mChosenInlineResultHandler\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/telegram/ext/updater.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     47\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtelegram\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mRequest\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     48\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtelegram\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtypes\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mCCT\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mUD\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mCD\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mBD\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 49\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mtelegram\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwebhookhandler\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mWebhookAppClass\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mWebhookServer\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     50\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mTYPE_CHECKING\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/telegram/ext/utils/webhookhandler.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtyping\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mTYPE_CHECKING\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mAny\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mOptional\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     26\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 27\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mtornado\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mweb\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     28\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mhttputil\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhttpserver\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mHTTPServer\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tornado/web.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     85\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mescape\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     86\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mgen\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 87\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhttpserver\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mHTTPServer\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     88\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mhttputil\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     89\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0miostream\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tornado/httpserver.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     30\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     31\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mescape\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnative_str\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 32\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhttp1connection\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mHTTP1ServerConnection\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mHTTP1ConnectionParameters\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     33\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mhttputil\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     34\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0miostream\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tornado/http1connection.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     32\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mgen\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     33\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mhttputil\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 34\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0miostream\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     35\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mgen_log\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mapp_log\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     36\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mtornado\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mutil\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mGzipDecompressor\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tornado/iostream.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m    208\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    209\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 210\u001b[0;31m \u001b[0;32mclass\u001b[0m \u001b[0mBaseIOStream\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mobject\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    211\u001b[0m     \"\"\"A utility class to write to and read from a non-blocking file or socket.\n\u001b[1;32m    212\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/tornado/iostream.py\u001b[0m in \u001b[0;36mBaseIOStream\u001b[0;34m()\u001b[0m\n\u001b[1;32m    284\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_closed\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    285\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 286\u001b[0;31m     \u001b[0;32mdef\u001b[0m \u001b[0mfileno\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mUnion\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mioloop\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_Selectable\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    287\u001b[0m         \u001b[0;34m\"\"\"Returns the file descriptor for this stream.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    288\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0mNotImplementedError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mAttributeError\u001b[0m: module 'tornado.ioloop' has no attribute '_Selectable'"
          ]
        }
      ]
    }
  ]
}