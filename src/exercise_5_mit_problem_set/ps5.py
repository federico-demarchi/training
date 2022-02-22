# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:
import re
from abc import ABC

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import collections
from collections import abc
collections.Callable = collections.abc.Callable

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================


def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory


class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================


class Trigger(object):  # interfaz implementada de forma distinta que en HERO
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger


class PhraseTrigger(Trigger):
    def __init__(self, trig_phrase):
        self.trig_phrase = trig_phrase

    def get_phrase(self):
        return self.trig_phrase

    def is_phrase_in(self, text):
        trig_phrase = self.get_phrase()
        punc = string.punctuation
        for char in text:
            if char in punc:
                text = text.replace(char, " ")
        for char in trig_phrase:
            if char in punc:
                trig_phrase = trig_phrase.replace(char, " ")
        text_list = text.lower().split()
        trig_phrase_list = trig_phrase.lower().split()
        for word in text_list:
            if word == trig_phrase_list[0]:
                flag = True
                for n in range(len(trig_phrase_list)):
                    try:
                        flag = flag and trig_phrase_list[n] == text_list[text_list.index(word) + n]
                    except IndexError:
                        flag = flag and False
                if flag:
                    return True
        return False

# Problem 3
# TODO: TitleTrigger


class TitleTrigger(PhraseTrigger):
    def __init__(self, trig_phrase):
        PhraseTrigger.__init__(self, trig_phrase)   #CHEQUEAR LLAMADO AL CONSTRUCTIOR (super?)

    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
# TODO: DescriptionTrigger


class DescriptionTrigger(PhraseTrigger):
    def __init__(self, trig_phrase):
        PhraseTrigger.__init__(self, trig_phrase)

    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.


class TimeTrigger(Trigger):
    def __init__(self, trig_time):
        self.trig_time = trig_time

    def get_trig_time_as_str(self):
        return self.trig_time

    def get_trig_time_as_datetime(self):
        return datetime.strptime(self.get_trig_time_as_str(), "%d %b %Y %H:%M:%S")

    def get_trig_time_as_datetime_est(self):
        return self.get_trig_time_as_datetime().replace(tzinfo=pytz.timezone('EST'))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger


class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate().tzinfo is not None:
            trig_datetime = self.get_trig_time_as_datetime_est()
        else:
            trig_datetime = self.get_trig_time_as_datetime()

        if story.get_pubdate() < trig_datetime:
            return True
        else:
            return False


class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate().tzinfo is not None:
            trig_datetime = self.get_trig_time_as_datetime_est()
        else:
            trig_datetime = self.get_trig_time_as_datetime()

        if story.get_pubdate() > trig_datetime:
            return True
        else:
            return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger


class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger


class AndTrigger(Trigger):
    def __init__(self, first_trig, second_trig):
        self.first_trig = first_trig
        self.second_trig = second_trig

    def get_first_trig(self):
        return self.first_trig

    def get_second_trig(self):
        return self.second_trig

    def evaluate(self, story):
        first_trig = self.get_first_trig()
        second_trig = self.get_second_trig()
        if first_trig.evaluate(story) and second_trig.evaluate(story):
            return True

# Problem 9
# TODO: OrTrigger


class OrTrigger(Trigger):
    def __init__(self, first_trig, second_trig):
        self.first_trig = first_trig
        self.second_trig = second_trig

    def get_first_trig(self):
        return self.first_trig

    def get_second_trig(self):
        return self.second_trig

    def evaluate(self, story):
        first_trig = self.get_first_trig()
        second_trig = self.get_second_trig()
        if first_trig.evaluate(story) or second_trig.evaluate(story):
            return True

#======================
# Filtering
#======================

# Problem 10


def filter_stories(stories, triggers):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in trigger_list fires.
    """
    # TODO: Problem 10

    result = []
    for story in stories:
        for trigger in triggers:
            if trigger.evaluate(story):
                result.append(story)
    return result


#======================
# User-Specified Triggers
#======================
# Problem 11

def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file
    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # 'lines' is the list of lines that you need to parse and for which you need
    # to build triggers

    # Initialize trigger mapping dictionary
    t_map = {"TITLE": TitleTrigger,
             "DESCRIPTION": DescriptionTrigger,
             "AFTER": AfterTrigger,
             "BEFORE": BeforeTrigger,
             "NOT": NotTrigger,
             "AND": AndTrigger,
             "OR": OrTrigger
             }

    # Initialize trigger dictionary, trigger list
    trigger_dict = {}
    trigger_list = []

    # Helper function to parse each line, create instances of Trigger objects,
    # and execute 'ADD'
    def line_reader(line):
        data = line.split(',')
        if data[0] != "ADD":
            if data[1] == "OR" or data[1] == "AND":
                trigger_dict[data[0]] = t_map[data[1]](trigger_dict[data[2]], trigger_dict[data[3]])
            else:
                trigger_dict[data[0]] = t_map[data[1]](data[2])
        else:
            trigger_list[:] += [trigger_dict[t] for t in data[1:]]

    for line in lines:
        line_reader(line)

    return trigger_list


SLEEPTIME = 120 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Biden")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

