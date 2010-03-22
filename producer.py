#!/usr/bin/env python
# coding: utf-8

import TwistedTwitterStream
from twisted.internet import reactor
from twisted.web import client
import urllib

class consumer(TwistedTwitterStream.TweetReceiver):
    def connectionMade(self):
        print "connected..."

    def connectionFailed(self, why):
        print "cannot connect:", why
        reactor.stop()

    def tweetReceived(self, tweet):
        
        print "new tweet:", repr(tweet)
        form = urllib.urlencode({'value':tweet})
        d=client.getPage("http://localhost:8888/q/twitter", method="POST", 
                postdata=form, headers={'Content-Type':'application/x-www-form-urlencoded'})
        def err(w):
            print 'E: ', w

        d.addErrback(err)
        
if __name__ == "__main__":
    TwistedTwitterStream.filter("username", "pass", consumer(),
            track=["fail",])
    reactor.run()
