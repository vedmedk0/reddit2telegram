#encoding:utf-8

subreddit = 'indepthstories+longtext+longreads'
t_channel = '@indepthstories'
submissions_ranking = 'new'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
