from telegram.ext import CommandHandler
from Configurations.config import CURRENCY
from Keyboards.CompanyKeyboards import commandMarkup
from Keyboards.CompanyKeyboards import sectorMarkup
from StaticMessages import company_message



def companyCommandHandler()-> CommandHandler:
    handler = CommandHandler(
        command= "companies",
        callback= companies)
    return handler


def companies(bot, update) -> int:
    bot.message.reply_text("Какие компании тебя интересуют?"
                           , reply_markup=commandMarkup())
    return CURRENCY

def russianCompanies(bot,update) -> int:
    bot.message.reply_text(company_message,
                           reply_markup=sectorMarkup(1))
    return CURRENCY

def foreigncompanies(bot, update) -> int:
    bot.message.reply_text(company_message,
                           reply_markup=sectorMarkup(2)) ### Допилить фильтры рынков и сделать клаву
    return CURRENCY                                            ### для МО
