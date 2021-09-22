import telebot

keyboardEN = telebot.types.ReplyKeyboardMarkup(True,)
keyboardEN.row('Servers', 'Storages')
keyboardEN.row('Russian')

keyboardServerEN = telebot.types.ReplyKeyboardMarkup(True)
keyboardServerEN.row('Rack', 'High-Density')
keyboardServerEN.row('Blade')
keyboardServerEN.row('Back')

keyboardServerRackEN = telebot.types.ReplyKeyboardMarkup(True)
keyboardServerRackEN.row('1288H V5', '2288H V5')
keyboardServerRackEN.row('5288 V5', '2488H V5')
keyboardServerRackEN.row('5885H V5')
keyboardServerRackEN.row('Back')

keyboardHighDensityEN = telebot.types.ReplyKeyboardMarkup(True)
keyboardHighDensityEN.row('X6000', 'X6800')
keyboardHighDensityEN.row('Back')

keyboardX6000EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardX6000EN.row('Data Sheet','Documentations')
keyboardX6000EN.row('3D-model')
keyboardX6000EN.row('Back')

keyboardX6800EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardX6800EN.row('Back')

keyboardBladeEN = telebot.types.ReplyKeyboardMarkup(True)
keyboardBladeEN.row('E9000')
keyboardBladeEN.row('Back')

keyboardE9000EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardE9000EN.row('Data Sheet','Documentations')
keyboardE9000EN.row('3D-model')
keyboardE9000EN.row('Back')

keyboardServer1288EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer1288EN.row('Data Sheet','Documentations')
keyboardServer1288EN.row('3D-model')
keyboardServer1288EN.row('Back')

keyboardServer2288EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer2288EN.row('Data Sheet','Documentations')
keyboardServer2288EN.row('3D-model')
keyboardServer2288EN.row('Back')

keyboardServer5288EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer5288EN.row('Data Sheet','Documentations')
keyboardServer5288EN.row('3D-model')
keyboardServer5288EN.row('Back')

keyboardServer2488EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer2488EN.row('Data Sheet','Documentations')
keyboardServer2488EN.row('3D-model')
keyboardServer2488EN.row('Back')

keyboardServer5885EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer5885EN.row('Data Sheet','Documentations')
keyboardServer5885EN.row('3D-model')
keyboardServer5885EN.row('Back')

keyboardStorageEN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageEN.row('All-Flash', 'Hybrid')
keyboardStorageEN.row('Back')

keyboardStorageAllFlashEN = telebot.types.ReplyKeyboardMarkup(True,)
keyboardStorageAllFlashEN.row('OceanStor Dorado V3','OceanStor Dorado V6')
keyboardStorageAllFlashEN.row('Back')


keyboardStorageDoradoV3EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageDoradoV3EN.row('Data Sheet','Documentations')
keyboardStorageDoradoV3EN.row('Description','Tests')
keyboardStorageDoradoV3EN.row('3D-model')
keyboardStorageDoradoV3EN.row('Back')


keyboardStorageDoradoV6EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageDoradoV6EN.row('Back')


keyboardStorageHybridEN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageHybridEN.row('OceanStor 2200 V3','OceanStor 2600 V3')
keyboardStorageHybridEN.row('OceanStor 5000 V5','OceanStor 6800 V5')
keyboardStorageHybridEN.row('OceanStor 18000 V5')
keyboardStorageHybridEN.row('Back')

keyboardStorage2200EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage2200EN.row('Description','3D-model')
keyboardStorage2200EN.row('Back')

keyboardStorage2600EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage2600EN.row('Description','Data Sheet')
keyboardStorage2600EN.row('3D-model')
keyboardStorage2600EN.row('Back')

keyboardStorage5000EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage5000EN.row('Description','Data Sheet')
keyboardStorage5000EN.row('Documentations','3D-model')
keyboardStorage5000EN.row('Back')

keyboardStorage6800EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage6800EN.row('Description','Data Sheet')
keyboardStorage6800EN.row('Documentations','3D-model')
keyboardStorage6800EN.row('Back')

keyboardStorage18000EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage18000EN.row('Description','Data Sheet')
keyboardStorage18000EN.row('Documentations','3D-model')
keyboardStorage18000EN.row('Back')

def english(bot,message,type,read,i):

    if message.text.lower() == 'english/английский' or message.text.lower() == 'английский':
        bot.send_message(message.chat.id,
                     'Hello, ' + message.from_user.first_name + ', Welcome to HuaweiEBG_Bot ✋. Which direction are you interested in?',
                     reply_markup=keyboardEN)

    elif message.text.lower() == 'back':
        bot.send_message(message.chat.id, 'Which direction are you interested in?', reply_markup=keyboardEN)

    elif message.text.lower() == 'servers':
        bot.send_message(message.chat.id, 'Choose the type of server you are interested in.',reply_markup=keyboardServerEN)

    elif message.text.lower() == 'rack':
        bot.send_message(message.chat.id, 'Choose the server of interest', reply_markup=keyboardServerRackEN)

    elif message.text.lower() == '1288h v5':
        type[i] = 8
        bot.send_message(message.chat.id, read("Server!B8") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Server!B3"),
                         reply_markup=keyboardServer1288EN)
    elif message.text.lower() == 'data sheet' and type[i] == 8:
        bot.send_message(message.chat.id, '👇👇👇 Data Sheet 👇👇👇 \n' + read("Server!B5"),
                         reply_markup=keyboardServer1288EN)
    elif message.text.lower() == 'documentations' and type[i] == 8:
        bot.send_message(message.chat.id, '👇👇👇 Documentations 👇👇👇 \n' + read("Server!B7"),
                         reply_markup=keyboardServer1288EN)
    elif message.text.lower() == '3d-model' and type[i] == 8:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Server!B4"),
                         reply_markup=keyboardServer1288EN)

    elif message.text.lower() == '2288h v5':
        type[i] = 9
        bot.send_message(message.chat.id, read("Server!C8") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Server!C3"),
                         reply_markup=keyboardServer2288EN)
    elif message.text.lower() == 'data sheet' and type[i] == 9:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + read("Server!C5"),
                         reply_markup=keyboardServer2288EN)
    elif message.text.lower() == 'documentations' and type[i] == 9:
        bot.send_message(message.chat.id,
                         '👇👇👇 Documentations 👇👇👇 \n' + read("Server!C7"),
                         reply_markup=keyboardServer2288EN)
    elif message.text.lower() == '3d-model' and type[i] == 9:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Server!C4"),
                         reply_markup=keyboardServer2288EN)

    elif message.text.lower() == '5288 v5':
        type[i] = 10
        bot.send_message(message.chat.id, read("Server!D8") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Server!D3"),
                         reply_markup=keyboardServer5288EN)
    elif message.text.lower() == 'data sheet' and type[i] == 10:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + read("Server!D5"),
                         reply_markup=keyboardServer5288EN)
    elif message.text.lower() == 'documentations' and type[i] == 10:
        bot.send_message(message.chat.id,
                         '👇👇👇 Documentations 👇👇👇 \n' + read("Server!D7"),
                         reply_markup=keyboardServer5288EN)
    elif message.text.lower() == '3d-model' and type[i] == 10:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Server!D4"),
                         reply_markup=keyboardServer5288EN)

    elif message.text.lower() == '2488h v5':
        type[i] = 11
        bot.send_message(message.chat.id, read("Server!E8") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Server!E3"),
                         reply_markup=keyboardServer2488EN)
    elif message.text.lower() == 'data sheet' and type[i] == 11:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + read("Server!E5"),
                         reply_markup=keyboardServer2488EN)
    elif message.text.lower() == 'documentations' and type[i] == 11:
        bot.send_message(message.chat.id,
                         '👇👇👇 Documentations 👇👇👇 \n' + read("Server!E7"),
                         reply_markup=keyboardServer2488EN)
    elif message.text.lower() == '3d-model' and type[i] == 11:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Server!E4"),
                         reply_markup=keyboardServer2488EN)

    elif message.text.lower() == '5885h v5':
        type[i] = 12
        bot.send_message(message.chat.id, read("Server!F8") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Server!F3"),
                         reply_markup=keyboardServer5885EN)
    elif message.text.lower() == 'data sheet' and type[i] == 12:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data sheet 👇👇👇 \n' + read("Server!F5"),
                         reply_markup=keyboardServer5885EN)
    elif message.text.lower() == 'documentations' and type[i] == 12:
        bot.send_message(message.chat.id,
                         '👇👇👇 Documentations 👇👇👇 \n' + read("Server!F7"),
                         reply_markup=keyboardServer5885EN)
    elif message.text.lower() == '3d-model' and type[i] == 12:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Server!F4"),
                         reply_markup=keyboardServer5885EN)

    elif message.text.lower() == 'high-density':
        bot.send_message(message.chat.id, 'Выберете интересующую модель', reply_markup=keyboardHighDensityEN)

    elif message.text.lower() == 'x6000':
        type[i] = 13
        bot.send_message(message.chat.id, read("Server!G8") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Server!G3"),
                         reply_markup=keyboardX6000EN)
    elif message.text.lower() == 'data sheet' and type[i] == 13:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + read("Server!G5"),
                         reply_markup=keyboardX6000EN)
    elif message.text.lower() == 'documentations' and type[i] == 13:
        bot.send_message(message.chat.id,
                         '👇👇👇 Documentations 👇👇👇 \n' + read("Server!G7"),
                         reply_markup=keyboardX6000EN)
    elif message.text.lower() == '3d-model' and type[i] == 13:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Server!G4"),
                         reply_markup=keyboardX6000EN)

    elif message.text.lower() == 'x6800':
        type[i] = 14
        bot.send_message(message.chat.id, read("Server!H8") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Server!H3"),
                         reply_markup=keyboardX6800EN)

    elif message.text.lower() == 'blade':
        bot.send_message(message.chat.id, 'Выберете интересующую модель', reply_markup=keyboardBladeEN)

    elif message.text.lower() == 'e9000':
        type[i] = 15
        bot.send_message(message.chat.id, read("Server!I8") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Server!I3"),
                         reply_markup=keyboardE9000EN)
    elif message.text.lower() == 'data sheet' and type[i] == 15:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + read("Server!I5"),
                         reply_markup=keyboardE9000EN)
    elif message.text.lower() == 'documentations' and type[i] == 15:
        bot.send_message(message.chat.id,
                         '👇👇👇 Documentations 👇👇👇 \n' + read("Server!I7"),
                         reply_markup=keyboardE9000EN)
    elif message.text.lower() == '3d-model' and type[i] == 15:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Server!I4"),
                         reply_markup=keyboardE9000EN)

    elif message.text.lower() == 'storages':
        bot.send_message(message.chat.id, 'Выберете тип системы хранения данных',reply_markup=keyboardStorageEN)

    elif message.text.lower() == 'all-flash':
        bot.send_message(message.chat.id, 'Выберете интересующий модельный ряд', reply_markup=keyboardStorageAllFlashEN)
    elif message.text.lower() == 'hybrid':
        bot.send_message(message.chat.id, 'Выберете интересующий модельный ряд', reply_markup=keyboardStorageHybridEN)

    elif message.text.lower() == 'oceanstor dorado v3':
        type[i] = 1
        bot.send_message(message.chat.id, read("Storage!C9") +
        """\n\n Для ссылки на документацию, выберете интересующий документ
        \n""" + read("Storage!C3"),
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == 'data sheet' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 Data Sheet 👇👇👇 \n' + read("Storage!C5"),
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == 'documentations' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 Documentations 👇👇👇 \n' + read("Storage!C7"),
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == 'description' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 Description 👇👇👇 \n' + read("Storage!C8"),
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == 'tests' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 Tests 👇👇👇 \n' + read("Storage!C6"),
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == '3d-model' and type[i] == 1:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Storage!C4"),
                         reply_markup=keyboardStorageDoradoV3EN)

    elif message.text.lower() == 'oceanstor dorado v6':
        type[i] = 2
        bot.send_message(message.chat.id, read("Storage!B9") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Storage!B3"),
                         reply_markup=keyboardStorageDoradoV6EN)

    elif message.text.lower() == 'oceanstor 2200 v3':
        type[i] = 3
        bot.send_message(message.chat.id, read("Storage!D9") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Storage!D3"),
                         reply_markup=keyboardStorage2200EN)
    elif message.text.lower() == 'description' and type[i] == 3:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + read("Storage!D8"),
                         reply_markup=keyboardStorage2200EN)
    elif message.text.lower() == '3d-model' and type[i] == 3:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Storage!D4"),
                         reply_markup=keyboardStorage2200EN)

    elif message.text.lower() == 'oceanstor 2600 v3':
        type[i] = 4
        bot.send_message(message.chat.id, read("Storage!E9") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Storage!E3"),
                         reply_markup=keyboardStorage2600EN)
    elif message.text.lower() == 'description' and type[i] == 4:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + read("Storage!E8"),
                         reply_markup=keyboardStorage2600EN)
    elif message.text.lower() == 'data sheet' and type[i] == 4:
        bot.send_message(message.chat.id, '👇👇👇 Data Sheet 👇👇👇 \n' + read("Storage!E5"),
                         reply_markup=keyboardStorage2600EN)
    elif message.text.lower() == '3d-model' and type[i] == 4:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Storage!E4"),
                         reply_markup=keyboardStorage2600EN)

    elif message.text.lower() == 'oceanstor 5000 v5':
        type[i] = 5
        bot.send_message(message.chat.id, read("Storage!F9") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Storage!F3"),
                         reply_markup=keyboardStorage5000EN)
    elif message.text.lower() == 'documentations' and type[i] == 5:
        bot.send_message(message.chat.id, '👇👇👇 Documentations 👇👇👇 \n' + read("Storage!F7"),
                         reply_markup=keyboardStorage5000EN)
    elif message.text.lower() == 'description' and type[i] == 5:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + read("Storage!F8"),
                         reply_markup=keyboardStorage5000EN)
    elif message.text.lower() == 'data sheet' and type[i] == 5:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + read("Storage!F5"),
                         reply_markup=keyboardStorage5000EN)
    elif message.text.lower() == '3d-model' and type[i] == 5:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Storage!F4"),
                         reply_markup=keyboardStorage5000EN)

    elif message.text.lower() == 'oceanstor 6800 v5':
        type[i] = 6
        bot.send_message(message.chat.id, read("Storage!G9") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Storage!G3"),
                         reply_markup=keyboardStorage6800EN)
    elif message.text.lower() == 'documentations' and type[i] == 6:
        bot.send_message(message.chat.id, '👇👇👇 Documentations 👇👇👇 \n' + read("Storage!G7"),
                         reply_markup=keyboardStorage6800EN)
    elif message.text.lower() == 'description' and type[i] == 6:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + read("Storage!G8"),
                         reply_markup=keyboardStorage6800EN)
    elif message.text.lower() == 'data sheet' and type[i] == 6:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + read("Storage!G5"),
                         reply_markup=keyboardStorage6800EN)
    elif message.text.lower() == '3d-model' and type[i] == 6:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Storage!G4"),
                         reply_markup=keyboardStorage6800EN)

    elif message.text.lower() == 'oceanstor 18000 v5':
        type[i] = 7
        bot.send_message(message.chat.id, read("Storage!H9") +
                         """\n\n Для ссылки на документацию, выберете интересующий документ
                         \n""" + read("Storage!H3"),
                         reply_markup=keyboardStorage18000EN)
    elif message.text.lower() == 'documentations' and type[i] == 7:
        bot.send_message(message.chat.id,
                         '👇👇👇 Documentations 👇👇👇 \n' + read("Storage!H7"),
                         reply_markup=keyboardStorage18000EN)
    elif message.text.lower() == 'description' and type[i] == 7:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + read("Storage!H8"),
                         reply_markup=keyboardStorage18000EN)
    elif message.text.lower() == 'data sheet' and type[i] == 7:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + read("Storage!H5"),
                         reply_markup=keyboardStorage18000EN)
    elif message.text.lower() == '3d-model' and type[i] == 7:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + read("Storage!H4"),
                         reply_markup=keyboardStorage18000EN)

    else:
        bot.send_message(message.chat.id,'Sorry, I do not understand you. Please click on the button or write /start')