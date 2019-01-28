from django.db import models

class fb_insight(models.Model):

    fb_page = models.CharField(max_length=200)
    fb_metric = models.CharField(max_length=100)
    fb_value = models.CharField(max_length=100)
    fb_date = models.IntegerField()
    fb_token = models.CharField(max_length=200)

    def __str__(self):

        # 1522501931348511 : 현대건설배구단
        # 740318106321385 : KDB Hi뱅킹
        # 611418572386248 : 삼성화재멤버십
        # 483308331873326 : 맘쏙케어22
        # 1559207541044807 : 세계한인벤처네트워크 - INKE
        # 1680512022212737 : 홈씨씨인테리어

        if self.fb_page == '1522501931348511':
            page_name = '현대건설배구단'

        elif self.fb_page == '740318106321385':
            page_name = 'KDB Hi뱅킹'

        elif self.fb_page == '611418572386248':
            page_name = '삼성화재멤버십'

        elif self.fb_page == '483308331873326':
            page_name = '맘쏙케어22'

        elif self.fb_page == '1559207541044807':
            page_name = '세계한인벤처네트워크 - INKE'

        elif self.fb_page == '1680512022212737':
            page_name = '홈씨씨인테리어'

        # page_total_actions : 페이지 행동
        # page_views_total : 페이지 조회
        # page_fan_adds : 페이지 좋아요
        # page_impressions_organic : 게시물 도달
        # page_post_engagement : 게시물 참여
        # page_video_views : 동영상 조회

        '''
        if self.fb_metric == 'page_total_actions':
            metric_name = '페이지 행동'

        elif self.fb_metric == 'page_views_total':
            metric_name = '페이지 조회'

        elif self.fb_metric == 'page_fan_adds':
            metric_name = '페이지 좋아요'

        elif self.fb_metric == 'page_impressions_organic':
            metric_name = '게시물 도달'

        elif self.fb_metric == 'page_post_engagement':
            metric_name = '게시물 참여'

        elif self.fb_metric == 'page_video_views':
            metric_name = '동영상 조회'

        full_name = page_name
        
        '''
        return page_name
# Create your models here.