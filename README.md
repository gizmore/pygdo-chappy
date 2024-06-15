# pygdo-chappy

Chappy Implementation in pygdo8. IP of gizmore / ITMB


## What is Chappy?

Chappy is a text based MMORPG. It is a mixture of Tamagochi, Pokemon and Slapwarz.
You control and interact with your Chappy bird, which also is connected to openai chatgpt.
You can breed and fight with other chappies, across different chat platforms.
Images and stats are also generated by your chappy's genomes.


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

Bot commands start with `$`. Chappy commands start with `$cp`, except `$chappy.start`.

Your first command should be `$chappy.start`
This will prepare your chappy genome.
Then issue `$cpr` to reset the game and get you a freshly breded chappy.

Those Chappies from reset are at max 50% power for a genome.

To get better chappies you need to `$cpe` (evolve) or `$cpb` (breed).

Breeding and Evolve costs life.
Fighting wins and loses you life points.

You also get more lives by feeding and playing with your chappy.

You can fight a random chappy, or choose a target yourself.
If you fight a chappy twice within 1 hour you lose a life.

#### Commands

- $chappy.start
- $cpr - Reset the Game
- $cps [<other_chappy>] - Show your or some other chappy details.
- $cpf [<other_chappy>] - Fight a [random] chappy.
- $cpe - Evolve your genome.
- $cpb <other_chappy> - Breed with other chappy.
- $chappy.shop [<item>] - List items or show item. (TODO)
- $chappy.buy <item> - Buy shop item. (TODO)

And you can interact with your chappy by sending it a private message.
Example: `Chappy: Let us play a round of blackjack.`
If your chappy is in good shape, chances for a better genome raise.
