@namespace
class SpriteKind:
    Projectile2 = SpriteKind.create()
    snake = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global falling
    falling = sprites.create(img("""
            . . 2 2 2 2 . . 
                    . 2 2 2 2 2 2 . 
                    2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 
                    . 2 2 2 2 2 2 . 
                    . . 2 2 2 2 . .
        """),
        SpriteKind.projectile)
    falling.set_bounce_on_wall(True)
    falling.set_position(sprite.x, sprite.y - 5)
    falling.set_velocity(sprite.vx, 0 - sprite.vy)
    falling.ay = sprite.ay
    sprite.destroy()
sprites.on_overlap(SpriteKind.Projectile2, SpriteKind.player, on_on_overlap)

def _1():
    global s4Dir, basket, falling, limit
    s4Dir = 1
    info.set_life(3)
    basket = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                    . . 7 1 1 1 1 1 1 1 1 1 7 . . . 
                    . . 7 1 1 1 1 1 1 1 1 1 7 . . . 
                    . . 7 1 1 1 1 1 1 1 1 1 7 . . . 
                    . . 7 1 1 1 1 1 1 1 1 1 7 . . . 
                    . . 7 1 1 1 1 1 1 1 1 1 7 . . . 
                    . . 7 1 1 1 1 1 1 1 1 1 7 . . . 
                    . . 7 1 1 1 1 1 1 1 1 1 7 . . . 
                    . . 7 1 1 1 1 1 1 1 1 1 7 . . . 
                    . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    basket.set_position(80, 100)
    controller.move_sprite(basket, 160, 0)
    tiles.set_tilemap(tilemap("""
        層級1
    """))
    for index in range(20):
        level = 0
        if level == 0:
            if info.score() < 10 or randint(1, min(50, info.score())) < 10:
                falling = sprites.create(img("""
                        . . 2 2 2 2 . . 
                                            . 2 2 2 2 2 2 . 
                                            2 2 2 2 2 2 2 2 
                                            2 2 2 2 2 2 2 2 
                                            2 2 2 2 2 2 2 2 
                                            2 2 2 2 2 2 2 2 
                                            . 2 2 2 2 2 2 . 
                                            . . 2 2 2 2 . .
                    """),
                    SpriteKind.projectile)
            else:
                falling = sprites.create(img("""
                        . . 8 8 8 8 . . 
                                            . 8 8 8 8 8 8 . 
                                            8 8 8 8 8 8 8 8 
                                            8 8 8 8 8 8 8 8 
                                            8 8 8 8 8 8 8 8 
                                            8 8 8 8 8 8 8 8 
                                            . 8 8 8 8 8 8 . 
                                            . . 8 8 8 8 . .
                    """),
                    SpriteKind.Projectile2)
            limit = min(10, info.score())
            falling.set_velocity(randint(-100, 100), randint(0 - limit, 5))
            falling.ay = 20
            falling.set_bounce_on_wall(True)
            pause(1000)
            if info.score() >= 5:
                falling.destroy()
                _2()
                break

def on_on_overlap2(sprite2, otherSprite2):
    info.set_score(info.score() + 1)
    sprite2.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap2)

def _2():
    global mySprite
    basket.destroy()
    tiles.set_tilemap(tilemap("""
        層級3
    """))
    mySprite = sprites.create(assets.image("""
        myImage17
    """), SpriteKind.player)
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile11
    """))
    controller.move_sprite(mySprite)
    scene.camera_follow_sprite(mySprite)

def on_hit_wall(sprite3, location):
    if tiles.tile_at_location_equals(location, assets.tile("""
        myTile
    """)):
        info.change_life_by(-1)
        sprite3.destroy()
scene.on_hit_wall(SpriteKind.Projectile2, on_hit_wall)

def on_overlap_tile(sprite4, location2):
    game.show_long_text("過關", DialogLayout.BOTTOM)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_hit_wall2(sprite5, location3):
    if tiles.tile_at_location_equals(location3, assets.tile("""
        myTile
    """)):
        info.change_life_by(-1)
        sprite5.destroy()
scene.on_hit_wall(SpriteKind.projectile, on_hit_wall2)

mySprite: Sprite = None
limit = 0
basket: Sprite = None
s4Dir = 0
falling: Sprite = None
scene.set_background_image(img("""
    3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333d133333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333dd33333333333333333333d1133333333333333333333333333333333333333333333333333333333333333333333313333333333
        333333333333333333333333333333333333333333333333333333111133333333333333333333d333333333333333333333333333333333333333333333333333333333333333333333113333333333
        33333333333333333333333333333333333333333333333333333111d1131111333333333993333333333333333333333333333333333333333333333333333333333333333333333333113333333333
        333333333d133333333333333333333333333333333333333111d11bb11111d1133339d99993333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        33333333d111d1d33333333333333333333333333333333311d111dbdd111bb1133339999993333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        333333331111111d333333333333333333333333333333311dbb1111111111bd111339999933333333333333333333333333333d1113111d333333333333333333333333333333333333333333333333
        333333331111111d333333333333333333333333333333311bb111111111111d1111d9999933333333333333333333333333333111111111333333333333333333333333333333333333333333333333
        33333333d1111113333333333333333333333333333333311d11111111111111dbb199999333333333333333333333333333333111111111333333333333333333333333333333333333333333333333
        33333333311111333333333333333333333333333333333111111111111111111db999399333333333333333333333333333333111111111333333333333333333333333333333333333333333333333
        33333333311113333333333333333333333333333333311111111111111111111d9913393333333333333333333333333333333311111113333333333333333333333333333333333333333333333333
        333333333311d333333333333333333333311113d133d1111111111111111111999113333333333333333333333333333333333331111113333333333333333333333333333333333333333333333333
        3333333333dd3333333333333333333333d11111111111b11111111111111119991111333333333333333333333333333333333333111133333333333333333333333333333333333333333333333333
        3333333333333333333333333333333d1111bbd11b1111b11111111111111d99911111133333333333333333333333333333333333311333333333333333333333333333333333333333333333333333
        333333333333333333333333333333111111dd11dbbd11d111111111111199911111bd1d3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333333333311bbd11111111bb11111111111911999111111bb113333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333333333d1bbd1111111111d11111111111999991111111bd113333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333333333d1dd111111111111dd111111111999d11111111b1133333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        333333333333333333333333333d1111111111111111111111111111d9911111111111d33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333331111111111111111111111111111119991111111111d33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333333d1bbb1111111111111111111111111119d1111111db1133333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333311bb1111111111111111111111111111111111111bbb1d3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333333d11b1111111111111111111111111111111111111bb11d3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333331111111111111d11111111111111111111111111111133333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        333333333333333333333333331111111111111199111111111111111111111111111d333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333d1bb11111111111d991111111111111111111111db11d333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        333333333333333333333333311bb11111111111d99d111111111111111111111bbb11333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        333333333333333333333333331db11111111199999911111111111111111111dbbb1133333333333333333333ddd3333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333311d11111119999d1d911111111111111111111111113333333333333333333311111333333333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333333311111119999d111111111111111111111111d111133333333333333d1111111bbd11111d3333333333333333333333333333333333333d13333333333333333333333
        33333333333333333333333333331111d999111111111111111111111111111bb11d3333333333333d11ddd11dbbbd11d111333333333333333333333333333333333333dd3333333333333333333333
        333333333333333333333333333311d999d1111111111111111111111111111bbb11333333333333311bbbbb12222b11bbd1d33333333333333333333333333333333333111333333333333333333333
        33333333333333333333333333331999911111111111111111111111111111dbd113333333333333d11bb222222222222bbd1d33333333333333333333333333333333333d3333333333333333333333
        333333333333333333333333d999999d1111111111111111111111111111111111d33333333333111113222222222222222b1111d3333333333333333333333333333333333333333333333333333333
        33333333333333333333339999999d11111111111111111111111111111111d1133333333333311dbd32222222222222222211d113333333333333333333333333333333333333333333333333333333
        333333333333333333333399b999d331dd1111111111111111111111111111bb11333333333331dbb22222222222222222222bbb113333333d11d3333333333333333333333333333333333333333333
        333333333333333333333333999933311bbd11111111111111111111111111bd113333333333d1bb2222222222222222222222bbd133333311111d33d11d333333333333333333333333333333333333
        333333333333333333333333999933311bbbd1d1111111111111111111111d1113333333333331d22222222222222222222222bbd1d11d311dbb11d11111333333333333333333333333333333333333
        3333333333333d13333333339399333d111111bbbd1bbbd1d111111111111111333333333333d11222222222222222222222222bd1111111dbbbbd11bbb1d33333333333333333333333333333333333
        333333333333d11333333333339d3333d111111bd11bbb11dbbd111111111b11333333393333112222222222222222222222222b111bbddd222222bbbbb1d33333333333333333333333333333333333
        333333333333d1333333333333333333333331111111d1111bb111b11111bb113333333993311b2222222222222222222222222b11bbb222222222222bd111d333333333333333333333333333333333
        33333333333333333333333333333333333333d1131111dd1111111bbbd1b11d3333333993311b2222222222222222222222222211b222222222222222e1111333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333dd331111dd11113333339999931db222222222222222222222222221d222222222222222222bb1d33333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333d111111d33333333999991db22222222222222222222222222222222222222222222222b1133333333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333999999999b2222222222222222222222222222222222222222222222231d33333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333999d33999d222222222222222222222222222222222222222222222231dd3333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333331d999b2222222222222222222222222222222222222222222221111333333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333d1dbb999222222299222222222222222222222222222222222222bd1d33333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333d1bb229999b2222b9b22222222222222222222222222222222222bb1133333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333311b222299999b2b9b222222222222222222222222222222222222b1133333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333d11d22222b999999b222222222222222222222222222222222222d1d33333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333d1122222222b999d22222222222222222222222222222222222b11333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333311b222222222229922222222222222222222222222222222222b1d333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333311b222222222229922222222222222222222222222222222222b11333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333311bb22222222229d22222222222222222222222222222222222bd1333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333d11d22222222222222222222222222222222992222222222222bd1333333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333333d111322222222222222222222222222222299222222222222bb11333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333d1b2222222222222222222222222222229b222222222222b11d333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333311b22222222222222222222222222222b9992222222222d11d3333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333311b22222222222222222222222222222d999992222222311d33333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333311bb2222222222222222222222222222b922999b22222b1d333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333d1db222222222222222222222222222229b22b999b22bb1d333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333311db2222222222222222222222222222b22222b9992bd1d3333333333333333dd333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333331112222222222222222222222222222222222229999113333399333333333111133333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333333d1d2222222222222222222222222222222222223199993333999333333d1d111133333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333333d1bb2222222222222222222222222222222222bd1dd99993d999933331111111133333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333333d1bb22222222222222222222222222222222bbb1133339999999933331111111133333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333333333331dbb22222222222222222222222222222111111d33333999999933331111111d33333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333d11d22222222222222222222222222bbd11111d333333399999933333111111333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333333333333d1112222222222222222222222d1ddd11333333333339999999d3333333111333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333333333d1122222222222222222222bb111111333333333339999999933333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333333333333311b222222222222222223dbb1133333333333333339999999d33333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333d133333333331dbb222222222222222111111d33333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333311133333333331dbb2222222222222bb11ddd3333333333333333333333333333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333d1d333333333311bbb22222222231dd1133333333333333333333333333333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333333333311db22222222b11111d33333333333333333333333333333333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333333333333333111322222bb113333333333333333333333333333333333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333333333333d1322211111d3333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333333333333333331dbbd1d1d333333333333333333333333333333333333333333333333333333333333333
        333333333333333333333333333333333333333333333333333333333333333333333333333333333333333311dd1d333333333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333111d3333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333113333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        33333333333333333333333311d3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333331333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333311333333
        33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333d1333333
        3333333333333333333333333333333333333333333311333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333311333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
"""))
game.set_dialog_frame(img("""
    ..bbbbbbbbbbbbbbbbbbbb..
        .bd111111111111111111db.
        bd1dbbbbbbbbbbbbbbbbd1db
        b1dbbbbbbbbbbbbbbbbbbd1b
        b1bd1111111111111111db1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1bd1111111111111111db1b
        bd1bbbbbbbbbbbbbbbbbb1db
        bbd111111111111111111dbb
        .bbbbbbbbbbbbbbbbbbbbbb.
        ..bbbbbbbbbbbbbbbbbbbb..
"""))
game.set_dialog_text_color(6)
game.show_long_text("歡迎來到鐘聲響起時", DialogLayout.BOTTOM)
助手 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
scene.set_background_image(assets.image("""
    myImage21
"""))
助手.set_position(141, 39)
game.set_dialog_frame(img("""
    ..bbbbbbbbbbbbbbbbbbbb..
        .bd111111111111111111db.
        bd1dbbbbbbbbbbbbbbbbd1db
        b1dbbbbbbbbbbbbbbbbbbd1b
        b1bd1111111111111111db1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1b111111111111111111b1b
        b1bd1111111111111111db1b
        bd1bbbbbbbbbbbbbbbbbb1db
        bbd111111111111111111dbb
        .bbbbbbbbbbbbbbbbbbbbbb.
        ..bbbbbbbbbbbbbbbbbbbb..
"""))
game.set_dialog_text_color(8)
game.show_long_text("我是你的助手", DialogLayout.BOTTOM)
game.show_long_text("這是你的理想男友", DialogLayout.BOTTOM)
男一 = sprites.create(assets.image("""
    myImage4
"""), SpriteKind.player)
男一.set_position(97, 60)
game.show_long_text("你的任務", DialogLayout.BOTTOM)
game.show_long_text("就是成功讓她喜歡上你", DialogLayout.BOTTOM)
mySprite2 = game.ask_for_string("name", 5)
game.show_long_text("Hello" + " " + mySprite2, DialogLayout.BOTTOM)
game.show_long_text("遊戲開始", DialogLayout.BOTTOM)
助手.destroy()
男一.destroy()
game.show_long_text("國二下學期" + mySprite2 + "因為家庭的緣故" + "      " + "轉到了復興國中",
    DialogLayout.BOTTOM)
老師 = sprites.create(assets.image("""
    myImage3
"""), SpriteKind.player)
老師.set_position(141, 59)
game.show_long_text("今天班上來了一個新的轉學生" + "他叫" + mySprite2, DialogLayout.BOTTOM)
老師.destroy()
if game.ask("" + mySprite2 + "要不要上台跟大家自我介紹一下呢?", ""):
    game.show_long_text("好啊", DialogLayout.BOTTOM)
    game.show_long_text("大家好我是" + mySprite2, DialogLayout.BOTTOM)
    if game.ask("興趣是唱歌(A)還是看劇(B)", ""):
        game.show_long_text("我...我平時的興趣是唱歌", DialogLayout.BOTTOM)
        game.show_long_text("喜歡聽R&B抒情搖滾", DialogLayout.BOTTOM)
        game.show_long_text("請大家多多指教", DialogLayout.BOTTOM)
    else:
        game.show_long_text("我...我平時喜歡追星跟看韓劇", DialogLayout.BOTTOM)
        game.show_long_text("喜歡看帥哥的可以來找我", DialogLayout.BOTTOM)
        game.show_long_text("請大家多多指教", DialogLayout.BOTTOM)
else:
    game.show_long_text("不了吧 沒關係", DialogLayout.BOTTOM)
_1()

def on_update_interval():
    global s4Dir
    s4Dir = s4Dir * -1
game.on_update_interval(1000, on_update_interval)
