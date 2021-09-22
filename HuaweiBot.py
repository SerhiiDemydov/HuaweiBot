import telebot
from English import english
from Russian import russian
from config import service,spreadsheetId,API_TOKEN




def read(ranges):
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                   ranges=ranges,
                                                   valueRenderOption='FORMATTED_VALUE',
                                                   dateTimeRenderOption='FORMATTED_STRING').execute()
    sheet_values = results['valueRanges'][0]['values'][0]
    return (sheet_values[0])

def write(Lang,name,id,type):

    for i in range(len(Lang)):
        service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body = {
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Language users!B"+str(i+2)+":E"+str(i+2),
            #"majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
            "values":[[id[i],name[i],Lang[i],type[i]]]},
                ]
            }).execute()
    print('Write done:')




keyboardLanguage = telebot.types.ReplyKeyboardMarkup(True,)
keyboardLanguage.row('English/Английский')
keyboardLanguage.row('Russian/Русский')



bot = telebot.TeleBot(API_TOKEN)

id = []
name = []
type = []
id = []
Language = []
results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                   ranges= 'Language users',
                                                   valueRenderOption='FORMATTED_VALUE',
                                                   dateTimeRenderOption='FORMATTED_STRING').execute()
Result = results['valueRanges'][0]['values']
for i in range(1,len(Result)):
    Language.append(int(Result[i][3]))
    name.append(Result[i][2])
    id.append(Result[i][1])
    type.append(Result[i][4])
print(Language,name,id,type)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбирете язык / Select language',reply_markup=keyboardLanguage)


@bot.message_handler(content_types=['text'])
def send_text1(message):
    try:
        global type, id, name, i, Language

        for i in range(len(id)):
            user_id = message.from_user.id
            if str(user_id) == id[i]:
                find = True
                break
            else:
                find = False

        if find == False:
            id.append(str(user_id))
            name.append(str(message.from_user.first_name)) #+ " " + message.from_user.last_name))
            type.append(0)
            Language.append(0)

        if message.text.lower() == 'english/английский' or message.text.lower() == 'английский':
            Language[i] = 1
            english(bot,message,type,read,i)

        elif message.text.lower() == 'russian/русский' or message.text.lower() == 'russian':
            Language[i] = 0
            russian(bot,message,type,read,i)

        elif Language[i] == 1:
            english(bot,message,type,read,i)

        elif Language[i] == 0:
            russian(bot,message,type,read,i)

        print('ID=', id, '; Name=', name, '; TYPE=', type, '; i=', i, '; FIND=', find, '; Language=', Language)
        write(Language, name, id, type)

    except Exception:
        if Language[i] == 0:
            bot.send_message(message.chat.id, 'Повторите, пожалуйста')
        else:
            bot.send_message(message.chat.id, 'Repeat please')



# @bot.message_handler(content_types=['text'])
# def send_text2(message):


# @bot.message_handler(content_types=['text'])
# def send_text3(message):
#    if message.text.lower() == 'Флеш-система хранения данных OceanStor Dorado V3':
#        bot.send_message(message.chat.id, "OceanStor Dorado V3 — первая в отрасли система хранения данных на базе"
#                                      "флеш-накопителей"
#                                      "NVMe" "для коммерческой эксплуатации"
#                                      "с поддержкой критически важных приложений."
#                                      "\n Для ссылки на техническую документацию, выберете модель")

bot.polling()