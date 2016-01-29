#!/usr/bin/env python
"""
this script runs the pi as a server with the port that is passed to it when calling. else it will run it on port 8080.
- modified
- lmeshoo.net
liniMestar
"""
import web
import time
import RPi.GPIO as GPIO

#dont bug me with warnings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

urls = ('/','root')
app = web.application(urls,globals())

class root:
        def __init__(self):
                self.hello = "Ready for HackPoly?"
        def GET(self):
                getInput = web.input(name="")
                aName = str(getInput.name)
                if aName:
                        # set RPi board pins high
                        GPIO.output(7, GPIO.HIGH)
                        GPIO.output(11, GPIO.HIGH)
                        time.delay(1)
                        # set RPi board pins low
                        GPIO.output(7, GPIO.LOW)
                        GPIO.output(11, GPIO.LOW)
                        return """
                                <html>
                                <head>
                                <script>
                                function loaded()
                                {
                                    window.setTimeout(CloseMe, 5);
                                }

                                function CloseMe()
                                {
                                    window.close();
                                }
                                </script>
                                </head>
                                <body onLoad="loaded()">
                                Thanks """+aName+"""!
                                </body>
                                </html>
                                """
if __name__ == "__main__":
        app.run()

