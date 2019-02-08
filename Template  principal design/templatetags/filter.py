from django import template

register = template.Library()

sum = 0
day_count = 0
metric = 'page_total_actions'

@register.filter

def get_name(myName):

    page_name = 'Page Name'

    if myName == '1522501931348511':
        page_name = '현대건설배구단'

    elif myName == '740318106321385':
        page_name = 'KDB Hi뱅킹'

    elif myName == '611418572386248':
        page_name = '삼성화재멤버십'

    elif myName == '483308331873326':
        page_name = '맘쏙케어22'

    elif myName == '1559207541044807':
        page_name = '세계한인벤처네트워크 - INKE'

    elif myName == '1680512022212737':
        page_name = '홈씨씨인테리어'

    return page_name

@register.filter

def get_metric(myMetric):

    if myMetric == 'page_total_actions':
        metric_name = '페이지 행동'

    elif myMetric == 'page_views_total':
        metric_name = '페이지 조회'

    elif myMetric == 'page_fan_adds':
        metric_name = '페이지 좋아요'

    elif myMetric == 'page_impressions_organic':
        metric_name = '게시물 도달'

    elif myMetric == 'page_post_engagements':
        metric_name = '게시물 참여'

    elif myMetric == 'page_video_views':
        metric_name = '동영상 조회'

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

    return sum

@register.filter

def set_sum_zero(myMetric):

    global metric
    global sum

    if(metric != myMetric):
        metric = myMetric
        sum = 0

    return ''

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

