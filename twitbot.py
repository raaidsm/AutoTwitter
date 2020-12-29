from selenium import webdriver
from typing import Any


class Twitter:
    """Object representing the Twitter application."""
    def __init__(self) -> None:
        """Initialize new Twitter object with browser object and Twitter page information."""
        self.tweets = []
        self.liked = 'M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754 2.29 0 ' \
                     '3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 ' \
                     '6.376-7.454 13.11-10.037 13.157H12z'
        self.not_liked = 'M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754 2.29 ' \
                         '0 3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 ' \
                         '6.376-7.454 13.11-10.037 13.157H12zM7.354 4.225c-2.08 0-3.903 1.988-3.903 4.255 0 5.74 ' \
                         '7.034 11.596 8.55 11.658 1.518-.062 8.55-5.917 8.55-11.658 0-2.267-1.823-4.255-3.903-4.255-' \
                         '2.528 0-3.94 2.936-3.952 2.965-.23.562-1.156.562-1.387 0-.014-.03-1.425-2.965-3.954-2.965z'
        self.browser = webdriver.Chrome("C:\\Users\\Raaid Mahboob\\PycharmProjects\\The Twitter Bookmark-Bot Project\\"
                                        "chromedriver.exe")

    def create_tweet(self, tweet_num: int) -> None:
        """Create new Tweet and add it to list of tweets."""
        clickable = self.get_clickable(tweet_num)
        like_val = self.is_liked(tweet_num)
        tweet = Tweet(tweet_num, clickable, like_val)
        self.tweets.append(tweet)

    def get_clickable(self, tweet_num: int) -> Any:
        """Return clickable object from specified tweet in Bookmarks."""
        _clickable = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/'
                                                        f'div[2]/section/div/div/div/div[{tweet_num}]/div/article/'
                                                        'div/div[1]')
        return _clickable

    def is_liked(self, tweet_num: int) -> bool:
        """Check whether specified tweet in Bookmarks has been liked."""
        _like = self.browser.find_element_by_css_selector(f'#react-root > div > div > div > main > div > div > div > '
                                                          f'div > div > div:nth-child(2) > section > div > div > div > '
                                                          f'div:nth-child({tweet_num}) > div > article > div > div.css-'
                                                          f'1dbjc4n.r-18u37iz.r-thb0q2 > div.css-1dbjc4n.r-1iusvr4.'
                                                          f'r-16y2uox.r-1777fci.r-5f2r5o.r-1mi0q7o > div.css-1dbjc4n.'
                                                          f'r-18u37iz.r-1wtj0ep.r-156q2ks.r-1mdbhws > div:nth-'
                                                          f'child(3) > div > div > div:nth-child(1) > svg > g > path')
        _like_val = _like.get_attribute('d')
        return _like_val == self.liked


class Tweet:
    """Object representing an individual tweet."""
    def __init__(self, tweet_num: int, clickable: Any, like_val: bool) -> None:
        """Initialize a new tweet object."""
        self.tweet_num = tweet_num
        self.clickable = clickable
        self.like_val = like_val

    def click_tweet(self) -> None:
        """CLick specified tweet in Bookmarks."""
        self.clickable.click()

    def get_like_val(self) -> bool:
        """Return like_val of tweet."""
        return self.like_val
