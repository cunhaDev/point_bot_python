from datetime import datetime
import bot
import variables

def validateHour():
    hour = datetime.now().strftime("%H:%M")
    if variables.ENTRATA == hour \
            or variables.ALMOCO == hour \
            or variables.RETORNO_ALMOCO == hour \
            or variables.SAIDA == hour:
        bot.init()
    else:
        return