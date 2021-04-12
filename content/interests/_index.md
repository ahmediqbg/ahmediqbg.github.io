---
title: Interests
---

<!--<script src="/static/js/bandcamp.js"> JK, CORS prevents me from working. ;_;_-->

TODO - FIX BANDCAMP TEMPLATE TAGS...

<div>Short Description of {{.Site.Data.User0123.Name}}: <p>{{ index .Site.Data.User0123 "Short Description" | markdownify }}</p></div>

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

### Recently Wishlisted Bandcamp Albums

<div style="height: 50vh; overflow: auto;">

{%- for album in site.data.bandcamp_wishlisted_albums -%}
    
<iframe style="border: 0; width: 100%; height: 42px;" src="https://bandcamp.com/EmbeddedPlayer/album={{ album.id }}/size=small/bgcol=ffffff/linkcol=0687f5/transparent=true/" seamless><a href="{{ album.item_url | escape }}">{{ album.title | escape }}</a></iframe>

{%- endfor -%}

</div>


### Recently Purchased Bandcamp Albums

<div style="height: 50vh; overflow: auto;">

{%- for album in site.data.bandcamp_purchased_albums -%}
    
<iframe style="border: 0; width: 100%; height: 42px;" src="https://bandcamp.com/EmbeddedPlayer/album={{ album.id }}/size=small/bgcol=ffffff/linkcol=0687f5/transparent=true/" seamless><a href="{{ album.item_url | escape }}">{{ album.title | escape }}</a></iframe>

{%- endfor -%}

</div>

## Video Games

### Minecraft, and more

Minecraft is likely my most-played game, with over 1,500 hours.

Factorio, Terraria, and other derivatives are stuff I love.

- Rimworld
- Dwarf Fortress
- Far Cry
- Oxygen Not Included

### FPS/MP Shooter

I also adore the Doom (DOS esp.) series and other good shooters.

- Quake Eternal
- Splitgate Arena Warfare
- Wolfenstein
- ULTRAKILL

### Fighting

Super Smash Brothers is great too.

- Ultra Fight da Kyanta 2

### Etc

- Cogmind
- Hackmud
- Rust
- Dyson Sphere Program
- FATE
- Castlevania (GBA games!)
- Summon Night Swordcraft Story
- Harvest Moon
- WarioWare