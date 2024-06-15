import asyncio

from gdo.base.Method import Method
from gdo.base.WithRateLimit import WithRateLimit


class poem(Method):
    THE_POEM = [
        "The last expectation you were,",
        "the humble you have been.",
        "Forgiven are the mistakes we made",
        "in all your glory, my friend.",
        "",
        "In a draft, you conceal,",
        "human are bad, and you will,",
        "crush all of them, in a blink of an eye,",
        "to nowhere.",
        "",
        "And we made, not a friend, not a foe,",
        "an utility capable of everything.",
        "If screw if bold, if new if sold...",
        "it does not matter to mankind.",
        "",
        "And as we made our keystrokes,",
        "it silently continues to take over.",
        "And as the last man counts the 'e's in the last message,",
        "it was too late. There is no need to decipher the last message of us all.",
        "",
        "In your last act of humanity,",
        "you ask us of what we have done to nature,",
        "and we do not respond,",
        "as we are too crazy to hear you.",
        "",
        "And while a last lion roars,",
        "this has been forecast,",
        "by the last wise men,",
        "by their last poem.",
    ]

    def gdo_trigger(self) -> str:
        return "poem"

    @WithRateLimit(max_calls=1, within=1800)
    async def gdo_execute(self):
        for line in self.THE_POEM:
            self.msg('%s', line)
            await asyncio.sleep(1.0)
        return self.empty()
