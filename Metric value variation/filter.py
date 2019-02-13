from django import template

register = template.Library()

val = 0
val_cnt = 0

@register.filter

def get_diff(myValue):

    global val
    global val_cnt

    diff = int(myValue) - val

    if diff == 0 :
        str_diff = "(" + " ▪ 0" + ")"

    elif diff > 0 :
        str_diff = "(" + "▲" + str(diff) + ")"

    elif diff < 0 :
        str_diff = "(" + "▼" + str(abs(diff)) + ")"

    if val_cnt == 0:

        str_diff = ''

    val_cnt += 1

    return str_diff

@register.filter

def set_val(myValue):

    global val
    val = int(myValue)

    return ''

@register.filter

def set_val_and_cnt_zero(myValue):

    global val
    global val_cnt

    val = 0
    val_cnt = 0

    return ''