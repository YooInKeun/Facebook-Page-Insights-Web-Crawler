from django import template

register = template.Library()

sum = 0
day_count = 0
val = 0
val_cnt = 0
eng_val_cnt = 0
imp = []

metric = 'page_fan_adds_unique'

@register.filter

def get_name(myName):

    page_name = '페이지 이름'

    if myName == '133755520063453':
        page_name = '토이 인터랙티브'

    elif myName == '570813366394251':
        page_name = 'TOY interactive'

    elif myName == '740318106321385':
        page_name = 'KDB Hi 뱅킹'

    return page_name

@register.filter

def get_metric(myMetric):

    if myMetric == 'page_fan_adds_unique':
        metric_name = '페이지 좋아요'

    elif myMetric == 'page_fan_removes_unique':
        metric_name = '페이지 좋아요 취소'

    elif myMetric == 'page_fan_pure_adds_unique':
        metric_name = '페이지 순 좋아요'

    elif myMetric == 'page_actions_post_reactions_like_total':
        metric_name = '게시물 좋아요'

    elif myMetric == 'page_impressions_organic_unique':
        metric_name = '게시물 유기적 도달'

    elif myMetric == 'page_post_engagements':
        metric_name = '게시물 참여'

    return metric_name

@register.filter

def get_int_from_date(myDate):

    global int_from_date
    int_from_date = int(myDate[0:4] + myDate[5:7] + myDate[8:10])

    return int_from_date

@register.filter

def get_int_to_date(myDate):

    global int_to_date
    int_to_date = int(myDate[0:4] + myDate[5:7] + myDate[8:10])

    return int_to_date

@register.filter

def set_sum(myValue):

    global sum
    sum += int(myValue)

    return sum

@register.filter

def get_sum(myValue):

    global sum

    return int(sum)

@register.filter

def set_sum_zero(myMetric):

    global metric
    global sum

    if(metric != myMetric):
        metric = myMetric
        sum = 0

    return ''

@register.filter

def get_diff(myValue):

    global val
    global val_cnt

    diff = int(myValue) - val

    if diff == 0 :
        str_diff = "▪  0"

    elif diff > 0 :
        str_diff = "▲" + str(diff)

    elif diff < 0 :
        str_diff = "▼" + str(abs(diff))

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
    global eng_val_cnt

    val = 0
    val_cnt = 0
    eng_val_cnt = 0

    return ''

@register.filter

def load_val(myValue):

    global imp

    imp.append(myValue)

    return ''

@register.filter

def set_imp_empty(myValue):

    global imp

    imp.clear()

    return ''

@register.filter

def get_eng_percent(myValue):

    global eng_val_cnt
    global imp

    try:
        eng_per = float(myValue) / float(imp[eng_val_cnt])
        eng_per = format(eng_per*100, '.2f')
        eng_per = str(eng_per) + '%'

    except ZeroDivisionError:
        eng_per =''

    eng_val_cnt +=1

    return eng_per

# 문자열 변수 생성 가능

class SetVarNode(template.Node):
    def __init__(self, new_val, var_name):
        self.new_val = new_val
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = self.new_val
        return ''

import re

@register.tag

def setvar(parser,token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
    new_val, var_name = m.groups()
    if not (new_val[0] == new_val[-1] and new_val[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return SetVarNode(new_val[1:-1], var_name)


# 모든 타입 변수 생성 가능

class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value

        return u""

@register.tag(name='set')

def set_var(parser, token):
    """
    {% set some_var = '123' %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form: {% set <var_name> = <var_value> %}")

    return SetVarNode(parts[1], parts[3])

