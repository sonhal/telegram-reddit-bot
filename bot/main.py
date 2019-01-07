from bot.reddit import reddit_connector


def main():
    reddit_con = reddit_connector.get_get_configured_connection()

    # assume you have a Reddit instance bound to variable `reddit`
    subreddit = reddit_con.subreddit('redditdev')

    print(subreddit.display_name)  # Output: redditdev
    print(subreddit.title)  # Output: reddit Development
    print(subreddit.description)  # Output: A subreddit for discussion of ...





if __name__ == '__main__':
    main()