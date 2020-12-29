from selenium.webdriver.common.keys import Keys
from twitbot import Twitter
from passwd import Pass
import time


class Main:
    """Main part of program; runs everything else."""
    def __init__(self) -> None:
        """Initialize core Twitter object and open browser to Twitter Bookmarks."""
        self.twit = Twitter()
        self.twit.browser.get("https://twitter.com/messages")
        username_space = self.twit.browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/'
                                                                 'div[1]/input')
        password_space = self.twit.browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/'
                                                                 'div[2]/input')
        username_space.send_keys("raidthefort")
        p = Pass()
        password_space.send_keys(p.get_passwd())
        password_space.send_keys(Keys.ENTER)
        self.twit.browser.get("https://twitter.com/i/bookmarks")
        time.sleep(1.5)
        self.initial_tweets()

    def initial_tweets(self) -> None:
        """Initialize first 8 tweets."""
        for i in range(1, 9):
            self.twit.create_tweet(i)

    def print_likes(self) -> None:
        """Print the like values of the specified tweets."""
        for tweet in self.twit.tweets:
            print(str(tweet.tweet_num) + ") " + str(tweet.get_like_val()))

    def run(self) -> None:
        """Custom key function for running entire program."""
        self.print_likes()


if __name__ == "__main__":
    main = Main()
    main.run()
