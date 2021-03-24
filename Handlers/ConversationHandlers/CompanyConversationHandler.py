from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
#from Configurations.config import CURRENCY
from Handlers.CommandHandlers.BaseCommandHandler import menuCommandHandler
from Handlers.CommandHandlers.CompanyCommandHandler import companies
from Handlers.CommandHandlers.CompanyCommandHandler import russianCompanies
from Handlers.CommandHandlers.CompanyCommandHandler import foreigncompanies


def companiesConversationHandler()-> ConversationHandler:
    handler = ConversationHandler(
        entry_points = [CommandHandler('companies', companies),
                        MessageHandler(Filters.regex('^(Компании на бирже|компании|Компании|компании на бирже))$')
                                       , companies)],
        fallbacks=[menuCommandHandler()]
    )
    return handler

def russianCompaniesConversationHandler()-> ConversationHandler:
    handler = ConversationHandler(
        entry_points= [MessageHandler(Filters.regex('^Российские компании|российские|Российские))$')
                                      ,russianCompanies)],
        fallbacks=[menuCommandHandler()]
    )
    return handler

def foreighnCompaniesConversationHandler()-> ConversationHandler:
    handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^Международные компании|международные|Международные')
                                                   ,foreigncompanies)],
        fallbacks=[menuCommandHandler()]
    )
    return handler



