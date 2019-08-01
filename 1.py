import telebot
from telebot import types

API_TOKEN = '898028922:AAEQRlJPNEArVANHXFR8sOlBcV2_-zzo_LI'

bot = telebot.TeleBot(API_TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_order= types.KeyboardButton("Оформить заказ \U0001F4E6")
btn_feedback= types.KeyboardButton("Отзывы \U0001F4AC")
btn_payment= types.KeyboardButton("Способы оплаты \U0001F4B3")
btn_about= types.KeyboardButton("Информация о магазине \U0001F4CA")
btn_rules= types.KeyboardButton("Правила магазина\U00002757")
btn_help= types.KeyboardButton("Поддержка 24/24 (анонимно) \U00002611")
markup_menu.add(btn_order, btn_feedback, btn_payment, btn_about, btn_rules, btn_help)

markup_inline_curs = types.InlineKeyboardMarkup()
btn_in_curs = types.InlineKeyboardButton('Конвертер валют', url='https://pokur.su/btc/rub/1/')
markup_inline_curs.add(btn_in_curs)


markup_inline_kalinorder = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinweed = types.InlineKeyboardButton("\U000025B6 Бошки OG Kush, пресс.", callback_data="kalinweed")
btn_in_kalinhush = types.InlineKeyboardButton("\U000025B6 Гашиш Euro HQ", callback_data="kalinhush")
btn_in_kalinamph = types.InlineKeyboardButton("\U000025B6 Белый амфетамин(АКЦИЯ!!! -20%)", callback_data="kalinamph")
btn_in_kalinmefedron = types.InlineKeyboardButton("\U000025B6 Кристаллический игольчатый мефедрон", callback_data="kalinmefedron")
btn_in_kalingero = types.InlineKeyboardButton("\U000025B6 Героин высокого качества (999) ", callback_data="kalingero")
btn_in_kalinordercancel = types.InlineKeyboardButton("\U0001F519", callback_data="kalinordercancel")
markup_inline_kalinorder.add(btn_in_kalinweed, btn_in_kalinhush, btn_in_kalinamph, btn_in_kalinmefedron, btn_in_kalingero, btn_in_kalinordercancel)

markup_inline_krasnorder = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnweed = types.InlineKeyboardButton("\U000025B6 Бошки OG Kush, пресс.", callback_data="krasnweed")
btn_in_krasnhush = types.InlineKeyboardButton("\U000025B6 Гашиш Euro HQ", callback_data="krasnhush")
btn_in_krasnamph = types.InlineKeyboardButton("\U000025B6 Белый амфетамин(АКЦИЯ!!! -20%)", callback_data="krasnamph")
btn_in_krasnmefedron = types.InlineKeyboardButton("\U000025B6 Кристаллический игольчатый мефедрон", callback_data="krasnmefedron")
btn_in_krasngero = types.InlineKeyboardButton("\U000025B6 Героин высокого качества (999) ", callback_data="krasngero")
btn_in_krasnordercancel = types.InlineKeyboardButton("\U0001F519", callback_data="krasnordercancel")
markup_inline_krasnorder.add(btn_in_krasnweed, btn_in_krasnhush, btn_in_krasnamph, btn_in_krasnmefedron, btn_in_krasngero, btn_in_krasnordercancel)

markup_inline_frunzorder = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzweed = types.InlineKeyboardButton("\U000025B6 Бошки OG Kush, пресс.", callback_data="frunzweed")
btn_in_frunzhush = types.InlineKeyboardButton("\U000025B6 Гашиш Euro HQ", callback_data="frunzhush")
btn_in_frunzamph = types.InlineKeyboardButton("\U000025B6 Белый амфетамин(АКЦИЯ!!! -20%)", callback_data="frunzamph")
btn_in_frunzmefedron = types.InlineKeyboardButton("\U000025B6 Кристаллический игольчатый мефедрон", callback_data="frunzmefedron")
btn_in_frunzgero = types.InlineKeyboardButton("\U000025B6 Героин высокого качества (999) ", callback_data="frunzgero")
btn_in_frunzordercancel = types.InlineKeyboardButton("\U0001F519", callback_data="frunzordercancel")
markup_inline_frunzorder.add(btn_in_frunzweed, btn_in_frunzhush, btn_in_frunzamph, btn_in_frunzmefedron, btn_in_frunzgero, btn_in_frunzordercancel)

markup_inline_oplata = types.InlineKeyboardMarkup(row_width=1)
btn_in_oplata = types.InlineKeyboardButton("Я оплатил \U00002714", callback_data="oplata")
markup_inline_oplata.add(btn_in_oplata)

markup_inline_oplata2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_oplata2 = types.InlineKeyboardButton("Я оплатил \U00002714", callback_data="oplata2")
markup_inline_oplata2.add(btn_in_oplata2)

markup_inline_oplata3 = types.InlineKeyboardMarkup(row_width=1)
btn_in_oplata3 = types.InlineKeyboardButton("Я оплатил \U00002714", callback_data="oplata3")
btn_in_new3 = types.InlineKeyboardButton("Оформить новый заказ \U0001F4E6", callback_data="new3")
markup_inline_oplata3.add(btn_in_oplata3, btn_in_new3)

markup_inline_oplata4 = types.InlineKeyboardMarkup(row_width=1)
btn_in_oplata4 = types.InlineKeyboardButton("Я оплатил \U00002714", callback_data="oplata4")
btn_in_new4 = types.InlineKeyboardButton("Оформить новый заказ \U0001F4E6", callback_data="new4")
markup_inline_oplata4.add(btn_in_oplata4, btn_in_new4)


markup_inline_kalinnumberweed = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinweed1 = types.InlineKeyboardButton("1 гр. - 999 рублей", callback_data="kalinweed1")
btn_in_kalinweed2 = types.InlineKeyboardButton("2 гр. - 1899 рублей", callback_data="kalinweed2")
btn_in_kalinweedback = types.InlineKeyboardButton("\U0001F519", callback_data="kalinweedback")
markup_inline_kalinnumberweed.add(btn_in_kalinweed1, btn_in_kalinweed2, btn_in_kalinweedback)

markup_inline_krasnnumberweed = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnweed1 = types.InlineKeyboardButton("1 гр. - 999 рублей", callback_data="krasnweed1")
btn_in_krasnweed2 = types.InlineKeyboardButton("2 гр. - 1899 рублей", callback_data="krasnweed2")
btn_in_krasnweedback = types.InlineKeyboardButton("\U0001F519", callback_data="krasnweedback")
markup_inline_krasnnumberweed.add(btn_in_krasnweed1, btn_in_krasnweed2, btn_in_krasnweedback)

markup_inline_frunznumberweed = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzweed1 = types.InlineKeyboardButton("1 гр. - 999 рублей", callback_data="frunzweed1")
btn_in_frunzweed2 = types.InlineKeyboardButton("2 гр. - 1899 рублей", callback_data="frunzweed2")
btn_in_frunzweedback = types.InlineKeyboardButton("\U0001F519", callback_data="frunzweedback")
markup_inline_frunznumberweed.add(btn_in_frunzweed1, btn_in_frunzweed2, btn_in_frunzweedback)


markup_inline_kalinnumberhush = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinhush1 = types.InlineKeyboardButton("1 гр. - 649 рублей", callback_data="kalinhush1")
btn_in_kalinhush2 = types.InlineKeyboardButton("2 гр. - 1189 рублей", callback_data="kalinhush2")
btn_in_kalinhushback = types.InlineKeyboardButton("\U0001F519", callback_data="kalinhushback")
markup_inline_kalinnumberhush.add(btn_in_kalinhush1, btn_in_kalinhush2, btn_in_kalinhushback)

markup_inline_krasnnumberhush = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnhush1 = types.InlineKeyboardButton("1 гр. - 649 рублей", callback_data="krasnhush1")
btn_in_krasnhush2 = types.InlineKeyboardButton("2 гр. - 1189 рублей", callback_data="krasnhush2")
btn_in_krasnhushback = types.InlineKeyboardButton("\U0001F519", callback_data="krasnhushback")
markup_inline_krasnnumberhush.add(btn_in_krasnhush1, btn_in_krasnhush2, btn_in_krasnhushback)

markup_inline_frunznumberhush = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzhush1 = types.InlineKeyboardButton("1 гр. - 649 рублей", callback_data="frunzhush1")
btn_in_frunzhush2 = types.InlineKeyboardButton("2 гр. - 1189 рублей", callback_data="frunzhush2")
btn_in_frunzhushback = types.InlineKeyboardButton("\U0001F519", callback_data="frunzhushback")
markup_inline_frunznumberhush.add(btn_in_frunzhush1, btn_in_frunzhush2, btn_in_frunzhushback)


markup_inline_kalinnumberamph = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinamph1 = types.InlineKeyboardButton("1 гр. - 899 рублей", callback_data="kalinamph1")
btn_in_kalinamph2 = types.InlineKeyboardButton("2 гр. - 1689 рублей", callback_data="kalinamph2")
btn_in_kalinamphback = types.InlineKeyboardButton("\U0001F519", callback_data="kalinamphback")
markup_inline_kalinnumberamph.add(btn_in_kalinamph1, btn_in_kalinamph2, btn_in_kalinamphback)

markup_inline_krasnnumberamph = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnamph1 = types.InlineKeyboardButton("1 гр. - 899 рублей", callback_data="krasnamph1")
btn_in_krasnamph2 = types.InlineKeyboardButton("2 гр. - 1689 рублей", callback_data="krasnamph2")
btn_in_krasnamphback = types.InlineKeyboardButton("\U0001F519", callback_data="krasnamphback")
markup_inline_krasnnumberamph.add(btn_in_krasnamph1, btn_in_krasnamph2, btn_in_krasnamphback)

markup_inline_frunznumberamph = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzamph1 = types.InlineKeyboardButton("1 гр. - 899 рублей", callback_data="frunzamph1")
btn_in_frunzamph2 = types.InlineKeyboardButton("2 гр. - 1689 рублей", callback_data="frunzamph2")
btn_in_frunzamphback = types.InlineKeyboardButton("\U0001F519", callback_data="frunzamphback")
markup_inline_frunznumberamph.add(btn_in_frunzamph1, btn_in_frunzamph2, btn_in_frunzamphback)


markup_inline_kalinnumbermefedron = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinmefedron1 = types.InlineKeyboardButton("0.5 гр. - 699 рублей", callback_data="kalinmefedron1")
btn_in_kalinmefedron2 = types.InlineKeyboardButton("1 гр. - 1299 рублей", callback_data="kalinmefedron2")
btn_in_kalinmefedronback = types.InlineKeyboardButton("\U0001F519", callback_data="kalinmefedronback")
markup_inline_kalinnumbermefedron.add(btn_in_kalinmefedron1, btn_in_kalinmefedron2, btn_in_kalinmefedronback)

markup_inline_krasnnumbermefedron = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnmefedron1 = types.InlineKeyboardButton("0.5 гр. - 699 рублей", callback_data="krasnmefedron1")
btn_in_krasnmefedron2 = types.InlineKeyboardButton("1 гр. - 1299 рублей", callback_data="krasnmefedron2")
btn_in_krasnmefedronback = types.InlineKeyboardButton("\U0001F519", callback_data="krasnmefedronback")
markup_inline_krasnnumbermefedron.add(btn_in_krasnmefedron1, btn_in_krasnmefedron2, btn_in_krasnmefedronback)

markup_inline_frunznumbermefedron = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzmefedron1 = types.InlineKeyboardButton("0.5 гр. - 699 рублей", callback_data="frunzmefedron1")
btn_in_frunzmefedron2 = types.InlineKeyboardButton("1 гр. - 1299 рублей", callback_data="frunzmefedron2")
btn_in_frunzmefedronback = types.InlineKeyboardButton("\U0001F519", callback_data="frunzmefedronback")
markup_inline_frunznumbermefedron.add(btn_in_frunzmefedron1, btn_in_frunzmefedron2, btn_in_frunzmefedronback)

markup_inline_kalinnumbergero = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalingero1 = types.InlineKeyboardButton("0.5 гр. - 1499 рублей", callback_data="kalingero1")
btn_in_kalingero2 = types.InlineKeyboardButton("1 гр. - 2799 рублей", callback_data="kalingero2")
btn_in_kalingeroback = types.InlineKeyboardButton("\U0001F519", callback_data="kalingeroback")
markup_inline_kalinnumbergero.add(btn_in_kalingero1, btn_in_kalingero2, btn_in_kalingeroback)

markup_inline_krasnnumbergero = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasngero1 = types.InlineKeyboardButton("0.5 гр. - 1499 рублей", callback_data="krasngero1")
btn_in_krasngero2 = types.InlineKeyboardButton("1 гр. - 2799 рублей", callback_data="krasngero2")
btn_in_krasngeroback = types.InlineKeyboardButton("\U0001F519", callback_data="krasngeroback")
markup_inline_krasnnumbergero.add(btn_in_krasngero1, btn_in_krasngero2, btn_in_krasngeroback)

markup_inline_frunznumbergero = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzgero1 = types.InlineKeyboardButton("0.5 гр. - 1499 рублей", callback_data="frunzgero1")
btn_in_frunzgero2 = types.InlineKeyboardButton("1 гр. - 2799 рублей", callback_data="frunzgero2")
btn_in_frunzgeroback = types.InlineKeyboardButton("\U0001F519", callback_data="frunzgeroback")
markup_inline_frunznumbergero.add(btn_in_frunzgero1, btn_in_frunzgero2, btn_in_frunzgeroback)


markup_inline_kalinchoosepayweed1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwiweed1 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwiweed1")
btn_in_kalinyanweed1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyanweed1")
markup_inline_kalinchoosepayweed1.add(btn_in_kalinqiwiweed1, btn_in_kalinyanweed1)

markup_inline_krasnchoosepayweed1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwiweed1 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwiweed1")
btn_in_krasnyanweed1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyanweed1")
markup_inline_krasnchoosepayweed1.add(btn_in_krasnqiwiweed1, btn_in_krasnyanweed1)

markup_inline_frunzchoosepayweed1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwiweed1 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwiweed1")
btn_in_frunzyanweed1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyanweed1")
markup_inline_frunzchoosepayweed1.add(btn_in_frunzqiwiweed1, btn_in_frunzyanweed1)


markup_inline_kalinchoosepayweed2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwiweed2 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwiweed2")
btn_in_kalinyanweed2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyanweed2")
markup_inline_kalinchoosepayweed2.add(btn_in_kalinqiwiweed2, btn_in_kalinyanweed2)

markup_inline_krasnchoosepayweed2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwiweed2 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwiweed2")
btn_in_krasnyanweed2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyanweed2")
markup_inline_krasnchoosepayweed2.add(btn_in_krasnqiwiweed2, btn_in_krasnyanweed2)

markup_inline_frunzchoosepayweed2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwiweed2 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwiweed2")
btn_in_frunzyanweed2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyanweed2")
markup_inline_frunzchoosepayweed2.add(btn_in_frunzqiwiweed2, btn_in_frunzyanweed2)


markup_inline_kalinchoosepayhush1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwihush1 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwihush1")
btn_in_kalinyanhush1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyanhush1")
markup_inline_kalinchoosepayhush1.add(btn_in_kalinqiwihush1, btn_in_kalinyanhush1)

markup_inline_krasnchoosepayhush1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwihush1 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwihush1")
btn_in_krasnyanhush1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyanhush1")
markup_inline_krasnchoosepayhush1.add(btn_in_krasnqiwihush1, btn_in_krasnyanhush1)

markup_inline_frunzchoosepayhush1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwihush1 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwihush1")
btn_in_frunzyanhush1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyanhush1")
markup_inline_frunzchoosepayhush1.add(btn_in_frunzqiwihush1, btn_in_frunzyanhush1)


markup_inline_kalinchoosepayhush2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwihush2 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwihush2")
btn_in_kalinyanhush2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyanhush2")
markup_inline_kalinchoosepayhush2.add(btn_in_kalinqiwihush2, btn_in_kalinyanhush2)

markup_inline_krasnchoosepayhush2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwihush2 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwihush2")
btn_in_krasnyanhush2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyanhush2")
markup_inline_krasnchoosepayhush2.add(btn_in_krasnqiwihush2, btn_in_krasnyanhush2)

markup_inline_frunzchoosepayhush2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwihush2 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwihush2")
btn_in_frunzyanhush2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyanhush2")
markup_inline_frunzchoosepayhush2.add(btn_in_frunzqiwihush2, btn_in_frunzyanhush2)


markup_inline_kalinchoosepayamph1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwiamph1 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwiamph1")
btn_in_kalinyanamph1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyanamph1")
markup_inline_kalinchoosepayamph1.add(btn_in_kalinqiwiamph1, btn_in_kalinyanamph1)

markup_inline_krasnchoosepayamph1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwiamph1 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwiamph1")
btn_in_krasnyanamph1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyanamph1")
markup_inline_krasnchoosepayamph1.add(btn_in_krasnqiwiamph1, btn_in_krasnyanamph1)

markup_inline_frunzchoosepayamph1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwiamph1 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwiamph1")
btn_in_frunzyanamph1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyanamph1")
markup_inline_frunzchoosepayamph1.add(btn_in_frunzqiwiamph1, btn_in_frunzyanamph1)


markup_inline_kalinchoosepayamph2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwiamph2 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwiamph2")
btn_in_kalinyanamph2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyanamph2")
markup_inline_kalinchoosepayamph2.add(btn_in_kalinqiwiamph2, btn_in_kalinyanamph2)

markup_inline_krasnchoosepayamph2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwiamph2 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwiamph2")
btn_in_krasnyanamph2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyanamph2")
markup_inline_krasnchoosepayamph2.add(btn_in_krasnqiwiamph2, btn_in_krasnyanamph2)

markup_inline_frunzchoosepayamph2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwiamph2 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwiamph2")
btn_in_frunzyanamph2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyanamph2")
markup_inline_frunzchoosepayamph2.add(btn_in_frunzqiwiamph2, btn_in_frunzyanamph2)


markup_inline_kalinchoosepaymefedron1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwimefedron1 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwimefedron1")
btn_in_kalinyanmefedron1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyanmefedron1")
markup_inline_kalinchoosepaymefedron1.add(btn_in_kalinqiwimefedron1, btn_in_kalinyanmefedron1)

markup_inline_krasnchoosepaymefedron1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwimefedron1 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwimefedron1")
btn_in_krasnyanmefedron1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyanmefedron1")
markup_inline_krasnchoosepaymefedron1.add(btn_in_krasnqiwimefedron1, btn_in_krasnyanmefedron1)

markup_inline_frunzchoosepaymefedron1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwimefedron1 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwimefedron1")
btn_in_frunzyanmefedron1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyanmefedron1")
markup_inline_frunzchoosepaymefedron1.add(btn_in_frunzqiwimefedron1, btn_in_frunzyanmefedron1)


markup_inline_kalinchoosepaymefedron2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwimefedron2 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwimefedron2")
btn_in_kalinyanmefedron2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyanmefedron2")
markup_inline_kalinchoosepaymefedron2.add(btn_in_kalinqiwimefedron2, btn_in_kalinyanmefedron2)

markup_inline_krasnchoosepaymefedron2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwimefedron2 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwimefedron2")
btn_in_krasnyanmefedron2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyanmefedron2")
markup_inline_krasnchoosepaymefedron2.add(btn_in_krasnqiwimefedron2, btn_in_krasnyanmefedron2)

markup_inline_frunzchoosepaymefedron2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwimefedron2 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwimefedron2")
btn_in_frunzyanmefedron2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyanmefedron2")
markup_inline_frunzchoosepaymefedron2.add(btn_in_frunzqiwimefedron2, btn_in_frunzyanmefedron2)


markup_inline_kalinchoosepaygero1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwigero1 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwigero1")
btn_in_kalinyangero1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyangero1")
markup_inline_kalinchoosepaygero1.add(btn_in_kalinqiwigero1, btn_in_kalinyangero1)

markup_inline_krasnchoosepaygero1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwigero1 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwigero1")
btn_in_krasnyangero1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyangero1")
markup_inline_krasnchoosepaygero1.add(btn_in_krasnqiwigero1, btn_in_krasnyangero1)

markup_inline_frunzchoosepaygero1 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwigero1 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwigero1")
btn_in_frunzyangero1 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyangero1")
markup_inline_frunzchoosepaygero1.add(btn_in_frunzqiwigero1, btn_in_frunzyangero1)


markup_inline_kalinchoosepaygero2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalinqiwigero2 = types.InlineKeyboardButton("Qiwi", callback_data="kalinqiwigero2")
btn_in_kalinyangero2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="kalinyangero2")
markup_inline_kalinchoosepaygero2.add(btn_in_kalinqiwigero2, btn_in_kalinyangero2)

markup_inline_krasnchoosepaygero2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasnqiwigero2 = types.InlineKeyboardButton("Qiwi", callback_data="krasnqiwigero2")
btn_in_krasnyangero2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="krasnyangero2")
markup_inline_krasnchoosepaygero2.add(btn_in_krasnqiwigero2, btn_in_krasnyangero2)

markup_inline_frunzchoosepaygero2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzqiwigero2 = types.InlineKeyboardButton("Qiwi", callback_data="frunzqiwigero2")
btn_in_frunzyangero2 = types.InlineKeyboardButton("Яндекс.Деньги", callback_data="frunzyangero2")
markup_inline_frunzchoosepaygero2.add(btn_in_frunzqiwigero2, btn_in_frunzyangero2)

markup_inline_cancel = types.InlineKeyboardMarkup(row_width=1)
btn_in_cancel = types.InlineKeyboardButton("Отменить заказ \U0001F6AB", callback_data="cancel")
markup_inline_cancel.add(btn_in_cancel)


markup_inline_kalincancel2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalincancel2 = types.InlineKeyboardButton("\U0001F519", callback_data="kalincancel2")
markup_inline_kalincancel2.add(btn_in_kalincancel2)

markup_inline_krasncancel2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_krasncancel2 = types.InlineKeyboardButton("\U0001F519", callback_data="krasncancel2")
markup_inline_krasncancel2.add(btn_in_krasncancel2)

markup_inline_frunzcancel2 = types.InlineKeyboardMarkup(row_width=1)
btn_in_frunzcancel2 = types.InlineKeyboardButton("\U0001F519", callback_data="frunzcancel2")
markup_inline_frunzcancel2.add(btn_in_frunzcancel2)


markup_inline_url = types.InlineKeyboardMarkup()
btn_in_url = types.InlineKeyboardButton('\U0001F4C4 Правила и условия покупки', url='https://note-pad.net/ru/read/7d028ed3c9203ccc87a288d3f617549a')
markup_inline_url.add(btn_in_url)


markup_inline_urldownload = types.InlineKeyboardMarkup()
btn_in_urlqiwi = types.InlineKeyboardButton('Скачать Qiwi', url='https://qiwi.com/applications/main.action')
btn_in_urlyan = types.InlineKeyboardButton('Скачать Яндекс.Деньги', url='https://money.yandex.ru/')
markup_inline_urldownload.add(btn_in_urlqiwi, btn_in_urlyan)


markup_inline_place = types.InlineKeyboardMarkup(row_width=1)
btn_in_kalin = types.InlineKeyboardButton("\U000025B6 Калининский", callback_data="kalin")
btn_in_krasn = types.InlineKeyboardButton("\U000025B6 Красногвардейский", callback_data="krasn")
btn_in_frunz = types.InlineKeyboardButton("\U000025B6 Невский", callback_data="frunz")
markup_inline_place.add(btn_in_kalin, btn_in_krasn, btn_in_frunz)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 print(message)
 bot.send_message(message.chat.id, "Добро пожаловать в магазин *\U0001F538Criminal Russia\U0001F538*                                                                                                                              "    
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                           "
                                   "_Мы - команда профессионалов, которая ежедневно работает над тем, чтобы наш клиент был обслужен максимально эффективно и качественно. Для вас отобран товар высокого качества по самым демократичным ценам. На нас работают только опытные кладмены, знающие своё дело. Все клады исключительно надёжные и безопасные._                                                                   "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                                   "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
 bot.send_message(message.chat.id, "\U00002139 Вся дополнительная информация находится в меню (*соседний значок от смайликов*)                                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                                   "Хочешь открыть собственный магазин?                                                                                          "
                                   "*Поможем на любом этапе!*                                                                                                     "
                                   "\U0001F539Разработка, хостинг и реклама магазина: @ElectronicSupport                                                                                                                                        "
                                   "\U0001F539Оптовые поставки: @CriminalRussiaAdmin                                                                                                                         "
                                   ,
                                   parse_mode="Markdown", reply_markup=markup_menu)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
 print(message)
 if message.text == "Поддержка 24/24 (анонимно) \U00002611":
  bot.send_message(message.chat.id, "Отвечаем на вопросы, связанные с ассортиментом. Решаем любые проблемы с заказом\U00002714                                                                         "
                                    "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                                    "Свой вопрос можно задать администратору магазина: @CriminalRussiaAdmin", reply_markup=markup_menu)
 elif message.text == "Оформить заказ \U0001F4E6":
  bot.send_message(message.chat.id,
                      "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
  bot.send_message(message.chat.id, "\U00002139 Вся дополнительная информация находится в меню (*соседний значок от смайликов*)                                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                                   "Хочешь открыть собственный магазин?                                                                                          "
                                   "*Поможем на любом этапе!*                                                                                                     "
                                   "\U0001F539Разработка, хостинг и реклама магазина: @ElectronicSupport                                                                                                                                        "
                                   "\U0001F539Оптовые поставки: @CriminalRussiaAdmin                                                                                                                                    "
                                   ,
                                   parse_mode="Markdown", reply_markup=markup_menu)
 elif message.text == "Информация о магазине \U0001F4CA":
  bot.send_message(message.chat.id, "Оптово-розничный магазин марихуаны, фена, мефедрона, гарика и хмурого \U0001F3EA                                                                                                                         "
                                    "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                                    "_Ранее магазин работал исключительно в тени занимаясь оптовыми поставками, но пришло время это изменить. Мы здесь, чтобы именно ты смог насладиться качественным товаром без наценок перекупщиков. Всё от начала создания товара и до его конечного пункта в руки потребителя - выполнено по высшему разряду!_                                                                                                                                                           "
                                    "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                 "
                                    "По любым вопросам касательно товара: @CriminalRussiaAdmin                                                                    "
                                    , parse_mode="Markdown", reply_markup=markup_menu)
 elif message.text == "Способы оплаты \U0001F4B3":
  bot.send_message(message.chat.id,
                   "В целях безопасности платежи принимаются при помощи приложений Яндекс.Деньги, Qiwi или биткоин кошелька                                                "
                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                   'Приложения совместимы с любым смартфоном, для установки нажмите на соответствующую кнопку \U00002B07 ',
                   parse_mode="Markdown", reply_markup=markup_inline_urldownload)
  bot.send_message(message.chat.id,
                   "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                           "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot  ",
                   parse_mode="Markdown", reply_markup=markup_menu)
 elif message.text == "Правила магазина\U00002757":
  bot.send_message(message.chat.id, "*Правила магазина обязательны к прочтению перед покупкой!*                                                                                                                 "
                                    "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                           "
                                    "_Оплачивая заказ - Вы автоматически соглашаетесь с правилами и условиями, указанными ниже. Гарантия на клад: 24 часа с момента получения адреса. По истечении этого срока претензии по отсутствию товара не принимаются_",
                   parse_mode="Markdown", reply_markup=markup_inline_url)
 elif message.text == "Оформить заказ \U0001F4E6":
  bot.send_message(message.chat.id,
                      "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
 elif message.text == "Отзывы \U0001F4AC":
  bot.send_message(message.chat.id,
                   "\U0001F525 Каждому оставившему отзыв - *скидка 5% на следующий заказ!*                                                                                                                                                             "
                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                          "
                   "_Мы благодарны за честную обратную связь. Нам важно понимать, что покупатель доволен и ценой и качеством товара и сервисом, а также где есть проблемы и чего не хватает. Политика магазина направлена на постоянное самосовершенствование, именно поэтому каждый отзыв для нас имеет значение!_                                                                                      "
                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                          "
                   "Кликай сюда \U000027A1 @CriminalRussiaAdmin", parse_mode="Markdown", reply_markup=markup_menu)
 else:
  bot.reply_to(message, message.text, reply_markup=markup_menu)


@bot.callback_query_handler(func=lambda call:True)
def call_back_order(call):
 print(call)
 if call.data == "kalinweed":
      bot.send_message(call.message.chat.id,
                       text='Сколько нужно?                                                   ',
                       parse_mode="Markdown", reply_markup=markup_inline_kalinnumberweed)
 elif call.data == "krasnweed":
      bot.send_message(call.message.chat.id,
                       text='Сколько нужно?                                                ',
                       parse_mode="Markdown", reply_markup=markup_inline_krasnnumberweed)
 elif call.data == "frunzweed":
      bot.send_message(call.message.chat.id,
                       text='Сколько нужно?',
                       parse_mode="Markdown", reply_markup=markup_inline_frunznumberweed)
 elif call.data == "kalinhush":
  bot.send_message(call.message.chat.id,
                      text='Сколько нужно?',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinnumberhush)
 elif call.data == "krasnhush":
  bot.send_message(call.message.chat.id,
                      text='Сколько нужно?',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnnumberhush)
 elif call.data == "frunzhush":
  bot.send_message(call.message.chat.id,
                      text='Сколько нужно?',
                      parse_mode="Markdown", reply_markup=markup_inline_frunznumberhush)
 elif call.data == "kalinamph":
  bot.send_message(call.message.chat.id, text='_Действует скидка -20%_\U0001F381                                                                                                 '
                                              '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                           '
                                              'Сколько нужно?',
                   parse_mode="Markdown", reply_markup=markup_inline_kalinnumberamph)
 elif call.data == "krasnamph":
  bot.send_message(call.message.chat.id, text='_Действует скидка -20%_\U0001F381                                                                                                 '
                                              '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                           '
                                              'Сколько нужно?',
                   parse_mode="Markdown", reply_markup=markup_inline_krasnnumberamph)
 elif call.data == "frunzamph":
  bot.send_message(call.message.chat.id, text='_Действует скидка -20%_\U0001F381                                                                                                 '
                                              '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                           '
                                              'Сколько нужно?',
                   parse_mode="Markdown", reply_markup=markup_inline_frunznumberamph)
 elif call.data == "kalinmefedron":
  bot.send_message(call.message.chat.id,
                   text='Сколько нужно?',
                   parse_mode="Markdown", reply_markup=markup_inline_kalinnumbermefedron)
 elif call.data == "krasnmefedron":
  bot.send_message(call.message.chat.id,
                   text='Сколько нужно?',
                   parse_mode="Markdown", reply_markup=markup_inline_krasnnumbermefedron)
 elif call.data == "frunzmefedron":
  bot.send_message(call.message.chat.id,
                   text='Сколько нужно?',
                   parse_mode="Markdown", reply_markup=markup_inline_frunznumbermefedron)
 elif call.data == "kalingero":
  bot.send_message(call.message.chat.id,
                   text='Сколько нужно?',
                   parse_mode="Markdown", reply_markup=markup_inline_kalinnumbergero)
 elif call.data == "krasngero":
     bot.send_message(call.message.chat.id,
                      text='Сколько нужно?',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnnumbergero)
 elif call.data == "frunzgero":
     bot.send_message(call.message.chat.id,
                      text='Сколько нужно? т',
                      parse_mode="Markdown", reply_markup=markup_inline_frunznumbergero)
 elif call.data == "oplata":
  bot.send_message(call.message.chat.id,
                      text="\U0001F538Статус заказа: *не оплачен*", parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   text="Если статус заказа не меняется в течение 5 минут после оплаты, делайте скриншот платежа и отправляйте в этот чат \U00002709                                                                                                                       "
                        "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                "
                        "_Для этого:_                                                                                                                                                     "
                        "_Надо зайти в приложение Qiwi -> история -> нажать на платёж -> сделать скриншот -> отправить скриншот в этот чат_                                                                                                                                               "
                        "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                                                  "
                        "В случае ненахода или недовеса, а также если есть желание оставить отзыв, пишите администратору магазина: @CriminalRussiaAdmin", parse_mode="Markdown", reply_markup=markup_inline_oplata3)
 elif call.data == "oplata2":
  bot.send_message(call.message.chat.id,
                   text="\U0001F538Статус заказа: *не оплачен*", parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   text="Если статус заказа не меняется в течение 5 минут после оплаты, делайте скриншот платежа и отправляйте в этот чат \U00002709                                                                                                                       "
                        "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                        "
                        "_Для этого:_                                                                                                                                                     "
                        "_Надо зайти в приложение Яндекс.Деньги -> история -> нажать на платёж -> сделать скриншот -> отправить скриншот в этот чат_                                                                                                                                                                                   "
                        "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                                                           "
                        "В случае ненахода или недовеса, а также если есть желание оставить отзыв, пишите администратору магазина: @CriminalRussiaAdmin",
                   parse_mode="Markdown", reply_markup=markup_inline_oplata4)
 elif call.data == "oplata3":
  bot.send_message(call.message.chat.id,
                      text="\U0001F538Статус заказа: *не оплачен*", parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   text="Если статус заказа не меняется в течение 5 минут после оплаты, делайте скриншот платежа и отправляйте в этот чат \U00002709                                                                                                                       "
                        "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                              "
                        "_Для этого:_                                                                                                                                                     "
                        "_Надо зайти в приложение Qiwi -> история -> нажать на платёж -> сделать скриншот -> отправить скриншот в этот чат_                                                                                                                                                                                       "
                        "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                                                  "
                        "В случае ненахода или недовеса, а также если есть желание оставить отзыв, пишите администратору магазина: @CriminalRussiaAdmin", parse_mode="Markdown", reply_markup=markup_inline_oplata3)
 elif call.data == "oplata4":
  bot.send_message(call.message.chat.id,
                   text="\U0001F538Статус заказа: *не оплачен*", parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   text="Если статус заказа не меняется в течение 5 минут после оплаты, делайте скриншот платежа и отправляйте в этот чат \U00002709                                                                                                                       "
                        "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                         "
                        "_Для этого:_                                                                                                                                                     "
                        "_Надо зайти в приложение Яндекс.Деньги -> история -> нажать на платёж -> сделать скриншот -> отправить скриншот в этот чат_                                                                                                                                                                    "
                        "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                                                                                        "
                        "В случае ненахода или недовеса, а также если есть желание оставить отзыв, пишите администратору магазина: @CriminalRussiaAdmin",
                   parse_mode="Markdown", reply_markup=markup_inline_oplata4)
 elif call.data == "kalinweed1":
  bot.send_message(call.message.chat.id, "Способы оплаты:",
                  parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepayweed1)
  bot.send_message(call.message.chat.id,
                  "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                         "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                  parse_mode="Markdown" ,reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasnweed1":
  bot.send_message(call.message.chat.id,'Способы оплаты:',
                  parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepayweed1)
  bot.send_message(call.message.chat.id,
                  "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                               "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                  parse_mode="Markdown" ,reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzweed1":
  bot.send_message(call.message.chat.id,'Способы оплаты:',
                  parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepayweed1)
  bot.send_message(call.message.chat.id,
                  "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                          "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                  parse_mode="Markdown" ,reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalinweed2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepayweed2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                          "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasnweed2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepayweed2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzweed2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepayweed2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                       "
                      "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                      "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot "
                      ,
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalinhush1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepayhush1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                        "
                      "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                      "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot "
                      ,
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasnhush1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepayhush1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                       "
                      "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                      "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot "
                      ,
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzhush1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepayhush1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalinhush2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepayhush2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                              "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasnhush2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepayhush2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzhush2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepayhush2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalinamph1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepayamph1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasnamph1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepayamph1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzamph1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepayamph1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalinamph2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepayamph2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasnamph2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepayamph2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                      "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot "
                      ,
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzamph2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepayamph2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalinmefedron1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepaymefedron1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasnmefedron1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepaymefedron1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzmefedron1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepaymefedron1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalinmefedron2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepaymefedron2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasnmefedron2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepaymefedron2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzmefedron2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepaymefedron2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot  ",
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalingero1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepaygero1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasngero1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepaygero1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzgero1":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepaygero1)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalingero2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinchoosepaygero2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_kalincancel2)
 elif call.data == "krasngero2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnchoosepaygero2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_krasncancel2)
 elif call.data == "frunzgero2":
     bot.send_message(call.message.chat.id,
                      'Способы оплаты:',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzchoosepaygero2)
     bot.send_message(call.message.chat.id,
                      "*Обращаем ваше внимание!*                                                                                                       "
                  "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                  "_Если нет электронных кошельков, то заказ можно оплатить банковской картой _\U0001F4B3                                                                                                           "
                  "_Для этого необходимо предварительно поменять рубли на биткоины в нашем обменнике_\U0001F4B1: @VirtualExchangeBot ",
                      parse_mode="Markdown", reply_markup=markup_inline_frunzcancel2)
 elif call.data == "kalinweedback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                               '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "krasnweedback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "frunzweedback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "kalinhushback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "krasnhushback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "frunzhushback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "kalinamphback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "krasnamphback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "frunzamphback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "kalinmefedronback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_kalinorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "krasnmefedronback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_krasnorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "frunzmefedronback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_frunzorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "kalingeroback":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_kalinorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "krasngeroback":
     bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnorder)
     bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "frunzgeroback":
     bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzorder)
     bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "cancel":
  bot.send_message(call.message.chat.id,
                      "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
  bot.send_message(call.message.chat.id, "\U00002139 Вся дополнительная информация находится в меню (*соседний значок от смайликов*)                                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                  "
                                   "Хочешь открыть собственный магазин?                                                                                          "
                                   "*Поможем на любом этапе!*                                                                                                     "
                                   "\U0001F539Разработка, хостинг и реклама магазина: @ElectronicSupport                                                                                                                                        "
                                   "\U0001F539Оптовые поставки: @CriminalRussiaAdmin                                                                                                                               "
                                   ,
                                   parse_mode="Markdown", reply_markup=markup_menu)
 elif call.data == "kalincancel2":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_kalinorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "krasncancel2":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_krasnorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "frunzcancel2":
  bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_frunzorder)
  bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "kalinordercancel":
  bot.send_message(call.message.chat.id, "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
  bot.send_message(call.message.chat.id, "\U00002139 Вся дополнительная информация находится в меню (*соседний значок от смайликов*)                                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                  "
                                   "Хочешь открыть собственный магазин?                                                                                          "
                                   "*Поможем на любом этапе!*                                                                                                     "
                                   "\U0001F539Разработка, хостинг и реклама магазина: @ElectronicSupport                                                                                                                                        "
                                   "\U0001F539Оптовые поставки: @CriminalRussiaAdmin                                                                                                                                  "
                                   ,
                                   parse_mode="Markdown", reply_markup=markup_menu)
 elif call.data == "krasnordercancel":
  bot.send_message(call.message.chat.id, "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
  bot.send_message(call.message.chat.id, "\U00002139 Вся дополнительная информация находится в меню (*соседний значок от смайликов*)                                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                  "
                                   "Хочешь открыть собственный магазин?                                                                                          "
                                   "*Поможем на любом этапе!*                                                                                                     "
                                   "\U0001F539Разработка, хостинг и реклама магазина: @ElectronicSupport                                                                                                                                        "
                                   "\U0001F539Оптовые поставки: @CriminalRussiaAdmin                                                                                                                                        "
                                   ,
                                   parse_mode="Markdown", reply_markup=markup_menu)
 elif call.data == "frunzordercancel":
  bot.send_message(call.message.chat.id, "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
  bot.send_message(call.message.chat.id, "\U00002139 Вся дополнительная информация находится в меню (*соседний значок от смайликов*)                                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                 "
                                   "Хочешь открыть собственный магазин?                                                                                          "
                                   "*Поможем на любом этапе!*                                                                                                     "
                                   "\U0001F539Разработка, хостинг и реклама магазина: @ElectronicSupport                                                                                                                                        "
                                   "\U0001F539Оптовые поставки: @CriminalRussiaAdmin                                                                                                                                              "
                                   ,
                                   parse_mode="Markdown", reply_markup=markup_menu)
 elif call.data == "kalinqiwiweed1":
  bot.send_message(call.message.chat.id,
                   '*Заказ:\U0001F4E6*                                                                                                                             '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                   '\U0001F538Количество *||* *1 грамм*                                                                              '
                   '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                   '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                   '\U0001F538Район *||* *калининский*                                                                                                '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                   '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                   'Итого: *999 руб.*                                                                                                                        '
                   'Номер Qiwi: \U0001F500                                                            ',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   '*+79117848514*',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_oplata)
  bot.send_message(call.message.chat.id, "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                                         "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                                         "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                   parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwiweed1":
  bot.send_message(call.message.chat.id,
                   '*Заказ:\U0001F4E6*                                                                                                                             '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                   '\U0001F538Количество *||* *1 грамм*                                                                              '
                   '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                   '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                   '\U0001F538Район *||* *красногвардейский*                                                                                                '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                   'Итого: *999 руб.*                                                                                                                                 '
                   'Номер Qiwi: \U0001F500                                                            ',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   '*+79117848514*',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_oplata)
  bot.send_message(call.message.chat.id, "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                                         "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                                         "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                   parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzqiwiweed1":
  bot.send_message(call.message.chat.id,
                   '*Заказ:\U0001F4E6*                                                                                                                             '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                   '\U0001F538Количество *||* *1 грамм*                                                                              '
                   '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                   '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                   '\U0001F538Район *||* *невский*                                                                                                '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                   'Итого: *999 руб.*                                                                                                                                               '
                   'Номер Qiwi: \U0001F500                                                            ',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   '*+79117848514*',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_oplata)
  bot.send_message(call.message.chat.id, "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                                         "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                                         "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                   parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinqiwiweed2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1899 руб.*                                                                                                                                             '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwiweed2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1899 руб.*                                                                                                                                               '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzqiwiweed2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1899 руб.*                                                                                                                                 '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinqiwihush1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                           '
                      'Итого: *649 руб.*                                                                                                                                       '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwihush1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *649 руб.*                                                                                                                                        '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzqiwihush1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *649 руб.*                                                                                                                                         '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinqiwihush2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1189 руб.*                                                                                                                                       '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwihush2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1189 руб.*                                                                                                                                  '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzqiwihush2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1189 руб.*                                                                                                                                          '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinqiwiamph1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *719,2 руб.*                                                                                                                                      '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwiamph1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *719,2 руб.*                                                                                                                            '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzqiwiamph1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *719,2 руб.*                                                                                                                              '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinqiwiamph2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1351,2 руб.*                                                                                                                                 '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwiamph2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1351,2 руб.*                                                                                                                                  '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzqiwiamph2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1351,2 руб.*                                                                                                                                                     '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinqiwimefedron1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *699 руб.*                                                                                                                                                 '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwimefedron1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *699 руб.*                                                                                                                                              '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzqiwimefedron1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *699 руб.*                                                                                                                                                  '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinqiwimefedron2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1299 руб.*                                                                                                                                               '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwimefedron2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1299 руб.*                                                                                                                                                   '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzqiwimefedron2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1299 руб.*                                                                                                                                                 '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinqiwigero1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1499 руб.*                                                                                                                                                '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnqiwigero1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1499 руб.*                                                                                                                                                '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
 elif call.data == "frunzqiwigero1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1499 руб.*                                                                                                                                            '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
 elif call.data == "kalinqiwigero2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *2799 руб.*                                                                                                                                              '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
 elif call.data == "krasnqiwigero2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *2799 руб.*                                                                                                                                             '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
 elif call.data == "frunzqiwigero2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *2799 руб.*                                                                                                                                                '
                      'Номер Qiwi: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*+79117848514*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata)
 elif call.data == "kalinyanweed1":
  bot.send_message(call.message.chat.id,
                   '*Заказ:\U0001F4E6*                                                                                                                             '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                   '\U0001F538Количество *||* *1 грамм*                                                                              '
                   '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                   '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                   '\U0001F538Район *||* *калининский*                                                                                                '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                   'Итого: *999 руб.*                                                                                                                                                      '
                   'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   '*4100110029625382*',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_oplata2)
  bot.send_message(call.message.chat.id, "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                                         "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                                         "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                   parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanweed1":
  bot.send_message(call.message.chat.id,
                   '*Заказ:\U0001F4E6*                                                                                                                             '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                   '\U0001F538Количество *||* *1 грамм*                                                                              '
                   '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                   '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                   '\U0001F538Район *||* *красногвардейский*                                                                                                '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                   'Итого: *999 руб.*                                                                                                                                                      '
                   'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   '*4100110029625382*',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_oplata2)
  bot.send_message(call.message.chat.id, "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                                         "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                                         "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                   parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyanweed1":
  bot.send_message(call.message.chat.id,
                   '*Заказ:\U0001F4E6*                                                                                                                             '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                   '\U0001F538Количество *||* *1 грамм*                                                                              '
                   '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                   '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                   '\U0001F538Район *||* *невский*                                                                                                '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                   '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                   '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                   'Итого: *999 руб.*                                                                                                                                                                    '
                   'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   '*4100110029625382*',
                   parse_mode="Markdown", reply_markup=markup_menu)
  bot.send_message(call.message.chat.id,
                   'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_oplata2)
  bot.send_message(call.message.chat.id, "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                                         "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                                         "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                   parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyanweed2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1899 руб.*                                                                                                                                                       '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanweed2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1899 руб.*                                                                                                                                                      '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyanweed2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *бошки OG Kush, пресс.*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1899 руб.*                                                                                                                                                       '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyanhush1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *649 руб.*                                                                                                                                                           '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanhush1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *649 руб.*                                                                                                                                                                    '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyanhush1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *649 руб.*                                                                                                                                                                   '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyanhush2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1189 руб.*                                                                                                                                                                '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanhush2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1189 руб.*                                                                                                                                                                '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyanhush2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *гашиш Euro HQ*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1189 руб.*                                                                                                                                                         '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyanamph1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *719,2 руб.*                                                                                                                                                     '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanamph1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *719,2 руб.*                                                                                                                                                             '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyanamph1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *719,2 руб.*                                                                                                                                                             '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyanamph2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1351,2 руб.*                                                                                                                                                     '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanamph2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1351,2 руб.*                                                                                                                                                       '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyanamph2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *белый амфетамин*                                                                                                                          '
                      '\U0001F538Количество *||* *2 грамма*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1351,2 руб.*                                                                                                                                                           '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyanmefedron1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                          '
                      'Итого: *699 руб.*                                                                                                                                                                       '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanmefedron1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *699 руб.*                                                                                                                                                                       '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyanmefedron1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *699 руб.*                                                                                                                                                                '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyanmefedron2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1299 руб.*                                                                                                                                                                        '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanmefedron2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1299 руб.*                                                                                                                                                              '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyanmefedron2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *кристаллический игольчатый мефедрон*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                              '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                    '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1299 руб.*                                                                                                                                                                           '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyangero1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1499 руб.*                                                                                                                                                                         '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyangero1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1499 руб.*                                                                                                                                           '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyangero1":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *0,5 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *1499 руб.*                                                                                                                                                            '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalinyangero2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *калининский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *2799 руб.*                                                                                                                                                       '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "krasnyanigero2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *красногвардейский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *2799 руб.*                                                                                                                                                           '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "frunzyangero2":
     bot.send_message(call.message.chat.id,
                      '*Заказ:\U0001F4E6*                                                                                                                             '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '\U0001F538Позиция *||* *героин (999)*                                                                                                                          '
                      '\U0001F538Количество *||* *1 грамм*                                                                             '
                      '\U0001F538Тип заказа *||* *моментальный*                                                                                                   '
                      '\U0001F538Тип клада *||* *магнит*                                                                                                              '
                      '\U0001F538Район *||* *невский*                                                                                                '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             '
                      '_Заказ успешно зарезервирован. Бронь автоматически снимется через 20 минут, если нужная сумма не будет начислена в полном объёме_\U000023F3                                                                                    '
                      '\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                            '
                      'Итого: *2799 руб.*                                                                                                                                                           '
                      'Номер счёта Яндекс.Деньги: \U0001F500                                                            ',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      '*4100110029625382*',
                      parse_mode="Markdown", reply_markup=markup_menu)
     bot.send_message(call.message.chat.id,
                      'В случае успешного перевода необходимо немного подождать (*от 1 до 5 минут*), затем нажать на кнопку \U00002B07',
                      parse_mode="Markdown", reply_markup=markup_inline_oplata2)
     bot.send_message(call.message.chat.id,
                      "Прилагаются 3 картинки. 1 и 2 - фото клада, 3 - точные координаты и подробное описание места                                             "
                      "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                             "
                      "_После покупки рекомендуем удалить все фотографии, чаты и переписки, связанные с магазином_\U00002716",
                      parse_mode="Markdown", reply_markup=markup_inline_cancel)
 elif call.data == "kalin":
     bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_kalinorder)
     bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "krasn":
     bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_krasnorder)
     bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "frunz":
     bot.send_message(call.message.chat.id, text='Что будешь брать?                                                                                '
                                                 'Выбери товар из списка \U00002B07',
                   parse_mode="Markdown", reply_markup=markup_inline_frunzorder)
     bot.send_message(call.message.chat.id, text='За качество ручаемся \U0001F44D', reply_markup=markup_menu)
 elif call.data == "new3":
     bot.send_message(call.message.chat.id,
                      "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
     bot.send_message(call.message.chat.id, "\U00002139 Вся дополнительная информация находится в меню (*соседний значок от смайликов*)                                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                  "
                                   "Хочешь открыть собственный магазин?                                                                                          "
                                   "*Поможем на любом этапе!*                                                                                                     "
                                   "\U0001F539Разработка, хостинг и реклама магазина: @ElectronicSupport                                                                                                                                        "
                                   "\U0001F539Оптовые поставки: @CriminalRussiaAdmin                                                                                                                                             "
                                   ,
                                   parse_mode="Markdown", reply_markup=markup_menu)
 elif call.data == "new4":
     bot.send_message(call.message.chat.id,
                      "Укажи доступный район \U00002B07", parse_mode="Markdown", reply_markup=markup_inline_place)
     bot.send_message(call.message.chat.id, "\U00002139 Вся дополнительная информация находится в меню (*соседний значок от смайликов*)                                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                                  "
                                   "Хочешь открыть собственный магазин?                                                                                          "
                                   "*Поможем на любом этапе!*                                                                                                     "
                                   "\U0001F539Разработка, хостинг и реклама магазина: @ElectronicSupport                                                                                                                                        "
                                   "\U0001F539Оптовые поставки: @CriminalRussiaAdmin                                                                                                                                                     "
                                   ,
                                   parse_mode="Markdown", reply_markup=markup_menu)

bot.polling(none_stop=True, interval=0)

