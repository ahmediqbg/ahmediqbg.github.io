---
layout: page
title: Interests
permalink: /interests/
---

<!--<script src="/static/js/bandcamp.js"> JK, CORS prevents me from working. ;_;_-->

## Recreation

I like to run and swim in my free time, and (rarely) will scuba dive.

I cycle more now than running, as it's more convenient.

Baking treats is another hobby of mine, and I like to give treats to my friends and family when I can.

Nature is something I love, and camping is super relaxing for me.

## Music

- Death Grips
- Venetian Snares
- FFF
- Lauren Bousfield
- Off Me Nut
- Cardopusher
- Spongebob Squarewave
- **Hundreds** of other artists -- see <https://bandcamp.com/henryfbp>.

### 50 Recently bought Bandcamp Albums

<!-- asdf -->
<div style="height: 200px; overflow: scroll;">

{%- for album in site.data.bandcamp_purchased_albums- %}
    
<iframe style="border: 0; width: 100%; height: 42px;" src="https://bandcamp.com/EmbeddedPlayer/album={{ album.id }}/size=small/bgcol=ffffff/linkcol=0687f5/transparent=true/" seamless><a href="{{ album.item_url | escape }}">{{ album.title | escape }}</a></iframe>

{%- endfor -%}

</div>

## Video Games

### Minecraft 

Minecraft is likely my most-played game, with over 1,500 hours.

Factorio, Terraria, and other derivatives are stuff I love.

### FPS

I also adore the Doom (DOS esp.) series and Castlevania (GBA games!).

### Fighting

Super Smash Brothers is great too.