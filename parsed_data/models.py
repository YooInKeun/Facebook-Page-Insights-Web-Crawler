from django.db import models

class fb_insight(models.Model):

    fb_page = models.CharField(max_length=200)
    fb_metric = models.CharField(max_length=100)
    fb_value = models.CharField(max_length=100)
    fb_date = models.CharField(max_length=100)
    fb_token = models.CharField(max_length=200)
    fb_page_name = models.CharField(max_length=200)

    def __str__(self):

        # 133755520063453 : 토이 인터랙티브
        # 570813366394251 : TOY interactive
        # 740318106321385 : KDB Hi 뱅킹

        page_name = "none"
        metric_name = "none"

        if self.fb_page == '133755520063453':
            page_name = '토이 인터랙티브'

        elif self.fb_page == '570813366394251':
            page_name = 'TOY interactive'

        elif self.fb_page == '740318106321385':
            page_name = 'KDB Hi 뱅킹'

        # page_fan_adds_unique : 페이지 유기적 좋아요
        # page_fan_removes_unique : 페이지 좋아요 취소
        # page_fan_pure_adds_unique : 페이지 순 좋아요 (page_fan_adds_unique) - (page_fan_removes_unique) 값으로 직접 만들기

        # page_actions_post_reactions_like_total : 페이지 총 게시물 좋아요
        # page_impressions_organic : 게시물 유기적 도달
        # page_post_engagement : 게시물 참여

        if self.fb_metric == 'page_fan_adds_unique':
            metric_name = '페이지 유기적 좋아요'

        elif self.fb_metric == 'page_fan_removes_unique':
            metric_name = '페이지 좋아요 취소'

        elif self.fb_metric == 'page_fan_pure_adds_unique':
            metric_name = '페이지 순 좋아요'

        elif self.fb_metric == 'page_actions_post_reactions_like_total':
            metric_name = '게시물 좋아요'

        elif self.fb_metric == 'page_impressions_organic_unique':
            metric_name = '게시물 유기적 도달'

        elif self.fb_metric == 'page_post_engagements':
            metric_name = '게시물 참여'

        full_name = self.fb_page_name + '(' + self.fb_metric + ')' + ' [ ' + self.fb_date + ' ]'

        return full_name

# Create your models here.