from django import template

register = template.Library()

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