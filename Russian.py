import telebot

keyboard1 = telebot.types.ReplyKeyboardMarkup(True,)
keyboard1.row('Сервера', 'Системы хранения данных')
keyboard1.row('Английский')

keyboardServer = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer.row('Стоечные', 'Высокой-плотности')
keyboardServer.row('Блейд сервер')
keyboardServer.row('Назад')

keyboardServerRack = telebot.types.ReplyKeyboardMarkup(True)
keyboardServerRack.row('1288H V5', '2288H V5')
keyboardServerRack.row('5288 V5', '2488H V5')
keyboardServerRack.row('5885H V5')
keyboardServerRack.row('Назад')

keyboardHighDensity = telebot.types.ReplyKeyboardMarkup(True)
keyboardHighDensity.row('X6000', 'X6800')
keyboardHighDensity.row('Назад')

keyboardX6000 = telebot.types.ReplyKeyboardMarkup(True)
keyboardX6000.row('Брошура','Оф-документация')
keyboardX6000.row('3D модель')
keyboardX6000.row('Назад')

keyboardX6800 = telebot.types.ReplyKeyboardMarkup(True)
keyboardX6800.row('Назад')

keyboardBlade = telebot.types.ReplyKeyboardMarkup(True)
keyboardBlade.row('E9000')
keyboardBlade.row('Назад')

keyboardE9000 = telebot.types.ReplyKeyboardMarkup(True)
keyboardE9000.row('Брошура','Оф-документация')
keyboardE9000.row('3D модель')
keyboardE9000.row('Назад')

keyboardServer1288 = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer1288.row('Брошура','Оф-документация')
keyboardServer1288.row('3D модель')
keyboardServer1288.row('Назад')

keyboardServer2288 = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer2288.row('Брошура','Оф-документация')
keyboardServer2288.row('3D модель')
keyboardServer2288.row('Назад')

keyboardServer5288 = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer5288.row('Брошура','Оф-документация')
keyboardServer5288.row('3D модель')
keyboardServer5288.row('Назад')

keyboardServer2488 = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer2488.row('Брошура','Оф-документация')
keyboardServer2488.row('3D модель')
keyboardServer2488.row('Назад')

keyboardServer5885 = telebot.types.ReplyKeyboardMarkup(True)
keyboardServer5885.row('Брошура','Оф-документация')
keyboardServer5885.row('3D модель')
keyboardServer5885.row('Назад')

keyboardStorage = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage.row('All-Flash', 'Гибридные')
keyboardStorage.row('Назад')

keyboardStorageAllFlash = telebot.types.ReplyKeyboardMarkup(True,)
keyboardStorageAllFlash.row('OceanStor Dorado V3','OceanStor Dorado V6')
keyboardStorageAllFlash.row('Назад')

keyboardStorageDoradoV3 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageDoradoV3.row('Брошура','Оф-документация')
keyboardStorageDoradoV3.row('Описание','Тесты')
keyboardStorageDoradoV3.row('3D модель')
keyboardStorageDoradoV3.row('Назад')

keyboardStorageDoradoV6 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageDoradoV6.row('Назад')

keyboardStorageHybrid = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageHybrid.row('OceanStor 2200 V3','OceanStor 2600 V3')
keyboardStorageHybrid.row('OceanStor 5000 V5','OceanStor 6800 V5')
keyboardStorageHybrid.row('OceanStor 18000 V5')
keyboardStorageHybrid.row('Назад')

keyboardStorage2200 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage2200.row('Описание','3D модель')
keyboardStorage2200.row('Назад')

keyboardStorage2600 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage2600.row('Описание','Брошура')
keyboardStorage2600.row('3D модель')
keyboardStorage2600.row('Назад')

keyboardStorage5000 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage5000.row('Описание','Брошура')
keyboardStorage5000.row('Оф-документация','3D модель')
keyboardStorage5000.row('Назад')

keyboardStorage6800 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage6800.row('Описание','Брошура')
keyboardStorage6800.row('Оф-документация','3D модель')
keyboardStorage6800.row('Назад')

keyboardStorage18000 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage18000.row('Описание','Брошура')
keyboardStorage18000.row('Оф-документация','3D модель')
keyboardStorage18000.row('Назад')

def russian(bot,message,type,read,i):

    if message.text.lower() == 'russian/русский' or message.text.lower() == 'russian':
        bot.send_message(message.chat.id,
                         'Привет, ' + message.from_user.first_name + ', вас приветствует HuaweiEBG_Bot ✋. Какое направление вас интересеут?',
                         reply_markup=keyboard1)

    elif message.text.lower() == 'сервера':
        bot.send_message(message.chat.id, 'Выберете интересующий вид серверов',reply_markup=keyboardServer)

    elif message.text.lower() == 'стоечные':
        bot.send_message(message.chat.id, 'Выберете интересующий сервер', reply_markup=keyboardServerRack)

    elif message.text.lower() == '1288h v5':
        type[i] = 8
        bot.send_message(message.chat.id, read("Server!B8") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Server!B3"),
                 reply_markup=keyboardServer1288)
    elif message.text.lower() == 'брошура' and type[i] == 8:
        bot.send_message(message.chat.id, '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Server!B5"),
                 reply_markup=keyboardServer1288)

    elif message.text.lower() == 'оф-документация' and type[i] == 8:
        bot.send_message(message.chat.id, '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Server!B7"),
                 reply_markup=keyboardServer1288)

    elif message.text.lower() == '3d модель' and type[i] == 8:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Server!B4"),
                 reply_markup=keyboardServer1288)

    elif message.text.lower() == '2288h v5':
        type[i] = 9
        bot.send_message(message.chat.id, read("Server!C8") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Server!C3"),
                 reply_markup=keyboardServer2288)

    elif message.text.lower() == 'брошура' and type[i] == 9:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Server!C5"),
                 reply_markup=keyboardServer2288)

    elif message.text.lower() == 'оф-документация' and type[i] == 9:
        bot.send_message(message.chat.id,
                 '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Server!C7"),
                 reply_markup=keyboardServer2288)

    elif message.text.lower() == '3d модель' and type[i] == 9:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Server!C4"),
                 reply_markup=keyboardServer2288)

    elif message.text.lower() == '5288 v5':
        type[i] = 10
        bot.send_message(message.chat.id, read("Server!D8") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Server!D3"),
                 reply_markup=keyboardServer5288)

    elif message.text.lower() == 'брошура' and type[i] == 10:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Server!D5"),
                 reply_markup=keyboardServer5288)

    elif message.text.lower() == 'оф-документация' and type[i] == 10:
        bot.send_message(message.chat.id,
                 '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Server!D7"),
                 reply_markup=keyboardServer5288)

    elif message.text.lower() == '3d модель' and type[i] == 10:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Server!D4"),
                 reply_markup=keyboardServer5288)

    elif message.text.lower() == '2488h v5':
        type[i] = 11
        bot.send_message(message.chat.id, read("Server!E8") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Server!E3"),
                 reply_markup=keyboardServer2488)

    elif message.text.lower() == 'брошура' and type[i] == 11:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Server!E5"),
                 reply_markup=keyboardServer2488)

    elif message.text.lower() == 'оф-документация' and type[i] == 11:
        bot.send_message(message.chat.id,
                 '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Server!E7"),
                 reply_markup=keyboardServer2488)

    elif message.text.lower() == '3d модель' and type[i] == 11:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Server!E4"),
                 reply_markup=keyboardServer2488)

    elif message.text.lower() == '5885h v5':
        type[i] = 12
        bot.send_message(message.chat.id, read("Server!F8") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Server!F3"),
                 reply_markup=keyboardServer5885)

    elif message.text.lower() == 'брошура' and type[i] == 12:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Server!F5"),
                 reply_markup=keyboardServer5885)

    elif message.text.lower() == 'оф-документация' and type[i] == 12:
        bot.send_message(message.chat.id,
                 '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Server!F7"),
                 reply_markup=keyboardServer5885)

    elif message.text.lower() == '3d модель' and type[i] == 12:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Server!F4"),
                 reply_markup=keyboardServer5885)

    elif message.text.lower() == 'высокой-плотности':
        bot.send_message(message.chat.id, 'Выберете интересующую модель', reply_markup=keyboardHighDensity)

    elif message.text.lower() == 'x6000':
        type[i] = 13
        bot.send_message(message.chat.id, read("Server!G8") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Server!G3"),
                 reply_markup=keyboardX6000)

    elif message.text.lower() == 'брошура' and type[i] == 13:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Server!G5"),
                 reply_markup=keyboardX6000)
    elif message.text.lower() == 'оф-документация' and type[i] == 13:
        bot.send_message(message.chat.id,
                 '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Server!G7"),
                 reply_markup=keyboardX6000)

    elif message.text.lower() == '3d модель' and type[i] == 13:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Server!G4"),
                 reply_markup=keyboardX6000)

    elif message.text.lower() == 'x6800':
        type[i] = 14
        bot.send_message(message.chat.id, read("Server!H8") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Server!H3"),
                 reply_markup=keyboardX6800)

    elif message.text.lower() == 'блейд сервер':
        bot.send_message(message.chat.id, 'Выберете интересующую модель', reply_markup=keyboardBlade)

    elif message.text.lower() == 'e9000':
        type[i] = 15
        bot.send_message(message.chat.id, read("Server!I8") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Server!I3"),
                 reply_markup=keyboardE9000)

    elif message.text.lower() == 'брошура' and type[i] == 15:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Server!I5"),
                 reply_markup=keyboardE9000)

    elif message.text.lower() == 'оф-документация' and type[i] == 15:
        bot.send_message(message.chat.id,
                 '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Server!I7"),
                 reply_markup=keyboardE9000)

    elif message.text.lower() == '3d модель' and type[i] == 15:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Server!I4"),
                 reply_markup=keyboardE9000)

    elif message.text.lower() == 'системы хранения данных':
        bot.send_message(message.chat.id, 'Выберете тип системы хранения данных', reply_markup=keyboardStorage)

    elif message.text.lower() == 'all-flash':
        bot.send_message(message.chat.id, 'Выберете интересующий модельный ряд', reply_markup=keyboardStorageAllFlash)

    elif message.text.lower() == 'гибридные':
        bot.send_message(message.chat.id, 'Выберете интересующий модельный ряд', reply_markup=keyboardStorageHybrid)

    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Какое направление вас интересеут?', reply_markup=keyboard1)

    elif message.text.lower() == 'oceanstor dorado v3':
        type[i] = 1
        bot.send_message(message.chat.id, read("Storage!C9") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Storage!C3"),
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'брошура' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Storage!C5"),
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'оф-документация' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Storage!C7"),
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'описание' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + read("Storage!C8"),
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'тесты' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 ТЕСТЫ 👇👇👇 \n' + read("Storage!C6"),
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == '3d модель' and type[i] == 1:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Storage!C4"),
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'oceanstor dorado v6':
        type[i] = 2
        bot.send_message(message.chat.id, read("Storage!B9") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Storage!B3"),
                 reply_markup=keyboardStorageDoradoV6)

    elif message.text.lower() == 'oceanstor 2200 v3':
        type[i] = 3
        bot.send_message(message.chat.id, read("Storage!D9") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Storage!D3"),
                 reply_markup=keyboardStorage2200)

    elif message.text.lower() == 'описание' and type[i] == 3:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + read("Storage!D8"),
                 reply_markup=keyboardStorage2200)

    elif message.text.lower() == '3d модель' and type[i] == 3:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Storage!D4"),
                 reply_markup=keyboardStorage2200)

    elif message.text.lower() == 'oceanstor 2600 v3':
        type[i] = 4
        bot.send_message(message.chat.id, read("Storage!E9") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Storage!E3"),
                 reply_markup=keyboardStorage2600)

    elif message.text.lower() == 'описание' and type[i] == 4:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + read("Storage!E8"),
                 reply_markup=keyboardStorage2600)

    elif message.text.lower() == 'брошура' and type[i] == 4:
        bot.send_message(message.chat.id, '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Storage!E5"),
                 reply_markup=keyboardStorage2600)

    elif message.text.lower() == '3d модель' and type[i] == 4:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Storage!E4"),
                 reply_markup=keyboardStorage2600)

    elif message.text.lower() == 'oceanstor 5000 v5':
        type[i] = 5
        bot.send_message(message.chat.id, read("Storage!F9") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Storage!F3"),
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == 'оф-документация' and type[i] == 5:
        bot.send_message(message.chat.id, '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Storage!F7"),
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == 'описание' and type[i] == 5:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + read("Storage!F8"),
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == 'брошура' and type[i] == 5:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Storage!F5"),
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == '3d модель' and type[i] == 5:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Storage!F4"),
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == 'oceanstor 6800 v5':
        type[i] = 6
        bot.send_message(message.chat.id, read("Storage!G9") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Storage!G3"),
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == 'оф-документация' and type[i] == 6:
        bot.send_message(message.chat.id, '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Storage!G7"),
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == 'описание' and type[i] == 6:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + read("Storage!G8"),
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == 'брошура' and type[i] == 6:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Storage!G5"),
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == '3d модель' and type[i] == 6:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Storage!G4"),
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == 'oceanstor 18000 v5':
        type[i] = 7
        bot.send_message(message.chat.id, read("Storage!H9") +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + read("Storage!H3"),
                 reply_markup=keyboardStorage18000)

    elif message.text.lower() == 'оф-документация' and type[i] == 7:
        bot.send_message(message.chat.id,
                 '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + read("Storage!H7"),
                 reply_markup=keyboardStorage18000)

    elif message.text.lower() == 'описание' and type[i] == 7:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + read("Storage!H8"),
                 reply_markup=keyboardStorage18000)

    elif message.text.lower() == 'брошура' and type[i] == 7:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + read("Storage!H5"),
                 reply_markup=keyboardStorage18000)

    elif message.text.lower() == '3d модель' and type[i] == 7:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + read("Storage!H4"),
                 reply_markup=keyboardStorage18000)



