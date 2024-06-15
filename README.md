# pygdo-chappy

Chappy Implementation in pygdo8. IP of gizmore / ITMB


## What is Chappy?

Chappy is a text based MMORPG. It is a mixture of Tamagochi, Pokemon and Slapwarz.
You control and interact with your Chappy bird, which also is connected to openai chatgpt.
You can breed and fight with other chappies, across different chat platforms.


### How to play Chappy?

Simply send text messages via your favorite chat client.

Supported are:

- IRC ([servers](./DOCS/09_IRC.md))
- Telegram ([@dog_dog_bot](https://t.me/gdo_dog_bot))
- HTTP ([https://pygdo.gizmore.org](https://pygdo.gizmore.org))
- Bash (only for local users on the gameserver)
- WhatsApp ([Chappy](https://wa.me/491788474692)) +49 178 8 47 46 92

Planned are:

- Discord (@Chappy) 
- Twitter (@Chappy)
- E-Mail (chappy@gizmore.org)
- SMS

### How to start

Bot commands start with `$`. Chappy commands start with `$cpy.`.

Your first command should be `$cpy.start`
This will prepare your chappy genome and call `$cpy.reset` to get you a freshly breded chappy.

Those Chappies from reset are at max 50% of a genome.

To get better chappies you need to `$cpy.evolve` or `$cpy.breed`.

Breeding costs life. Fighting gains and loses life. Evolve costs life as well.

You gain life by feeding and playing with your chappy, or by fighting others.

#### Commands

- $cpy.start
- $cpy.reset
- $cpy.breed <other_chappy> <offered_credits>
- $cpy.buy <other_chappy> <offered_credits>

And you can interact with your chappy by sending it a private message.
Example: `Chappy: Let us play a round of blackjack.`
If your chappy is in good shape, chances for a better genome raise.
