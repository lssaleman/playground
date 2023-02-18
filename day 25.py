import tkinter

tkinter.Tk()


def random_number(x):
    import random
    y = random.randint(1, x)
    return y


def loot(x):
    drop = random_number(4)
    armor_drop = 0
    offense_drop = 0
    gold_drop = 0
    no_drop = 0
    if drop == 1:
        armor_drop = armor_drop + random_number(2) * x
    if drop == 2:
        offense_drop = offense_drop + random_number(2) * x
    if drop == 3:
        gold_drop = gold_drop + random_number(5) * x
    if drop == 4:
        no_drop += 1
    return armor_drop, offense_drop, gold_drop, no_drop


def loot_output(x, y):
    total_loot = loot(y)
    if total_loot[0] > 0:
        print("The", "\033[31m", x, "\033[0m", "drops", "\033[34m", "armor", "\033[0m", "increasing your defence by",
              "\033[34m", total_loot[0], "\033[0m", ".", )
    elif total_loot[1] > 0:
        print("The", "\033[31m", x, "\033[0m", "drops a", "\033[31m", "weapon", "\033[0m", "increasing your offence by",
              "\033[31m", total_loot[1], "\033[0m", ".")
    elif total_loot[2] > 0:
        print("The", "\033[31m", x, "\033[0m", "drops", "\033[33m", "gold", "\033[0m", "increasing your gold by",
              "\033[33m", total_loot[2], "\033[0m", ".")
    elif total_loot[3] > 0:
        print("The", "\033[31m", x, "\033[0m", "drops nothing.")
    return total_loot


def game_start():
    start = "THE GAME WILL START NOW GOOD LUCK AND HAVE FUN!!"
    return start


def defense():
    defense_stat = random_number(4)
    return defense_stat


def offense():
    offense_stat = random_number(1)
    return offense_stat


def enemy_attack():
    attack_enemy = random_number(7)
    damage_enemy = attack_enemy
    return damage_enemy


def player_attack():
    attack_player = random_number(5)
    return attack_player


def combat_defence(x):
    block = 100 - 100 * 2.71 ** (-0.1 * x)
    block = round(block)
    return block


counter = 0  # game mode
gold = 0  # amount of gold a player has
kill_count = 0  # total enemies defeated
total_events = 0  # total events
total_traps = 0  # total traps
total_combat_rounds = 0  # total combat rounds
total_pots = 0  # total pots
shop_counter = 0  # counter for the next shop
shop_increase = 10  # counter for total rounds till next shop
xp_counter = 0  # current xp
xp_to_level = 10  # xp you need to reach the next level
level_counter = 0  # how many levels the player has
last_event_one = 0  # event that can't happen within 2 turns
last_event_two = 0  # event that can't happen within 2 turns
last_event_counter = 0  # checks what last event has to be overwritten
guess = "a"  # guess for the scout
maximum_health = 20

# class counters
mage_counter = 0  # checks if the mage has already been revived
fighter_bonus_health = 0  # bonus starting health of the fighter (changes the fighter gets selected as class)
fighter_counter = 0  # ramping offence for the fighter the longer the fight takes
tank_bonus_health = 0  # # bonus starting health of the tank (changes the tank gets selected as class)
ranger_counter = 0  # ranger cooldown for running away
berserk_bonus = 0  # berserk bonus damage (changes in fights)

# enemies counter
orc_pattern = 1  # (checks what the orc is doing currently)
# TODO
print()
print("Welcome to\033[36m Tamadia Dungeons!!\033[0m")
print()
print(
    """     The "Black Death" has infected your entire family, you are the only one who managed to escape the sickness, all you are thinking about is trying to
     save your family. You have spoken to many people but no one can help you. A stranger shows up in your village, a traveller, telling stories and fairy 
     tales. In one of his tales he mentions a way to cure able to save everyone who receives it from any imaginable sickness. After he is done you talk to him,
     asking where to find this cure. He says that the cure is a dragonscale. Whoever gets in touch with it will be cured. "Where can I find a dragonscale?" You
     ask. "There are supposedly only a few dragons left but I heard rumours, that in the "Dungeons of Tamadia" is a deep dark cave with a dragon living in it."
     He warns you, that such a journey is far too dangerous but you're not listening anymore, you are already on your way.""")
print()
print("Create your character!")
counter += 1
print("What\033[34m name\033[0m do you want to give your character?")
name = input(">")
first_name = name
first_health = 20
first_offense = offense()
first_defense = defense()
first_class = "empty"

while True:
    print("What class do you want to chose?\033[36m (fighter,tank,mage,ranger,scout,berserk,treasure hunter)\033[0m For explanation\033[32m (help)\033[0m")
    class_choice = input(">")

    if class_choice == "help":
        print("\033[36mFighter\033[0m: Increases his attack the longer a fight takes and\033[35m +5\033[0m current and maximum health.")
        print("\033[36mTank\033[0m: Has\033[34m +5\033[0m defence and\033[35m +10\033[0m current and maximum health.")
        print("\033[36mMage\033[0m: Has\033[31m +3\033[0m offence and revives once with\033[35m 20\033[0m health after death.")
        print("\033[36mRanger\033[0m: Can escape fights while still getting the xp (cooldown 3 fights).")
        print("\033[36mScout\033[0m: Has a chance to avoid trap damage by guessing a correct letter.\033[32m (a/b)\033[0m If the guess is correct, the\033[36m "
              "scout\033[0m will receive loot.")
        print("\033[36mBerserk\033[0m: Has no defence but increases his offense based on missing health.\033[31m +2\033[0m bonus offense.")
        print("\033[36mTreasure hunter\033[0m : Will always get loot and bonus gold from defeating\033[31m goblins\033[0m .")
        print()
        continue

    if class_choice.lower() == "fighter":
        first_health = first_health + 5
        first_class = "fighter"
        maximum_health = 25
        fighter_bonus_health = 5
        break
    elif class_choice.lower() == "tank":
        maximum_health = 30
        first_health = first_health + 10
        first_defense = first_defense + 5
        first_class = "tank"
        break
    elif class_choice.lower() == "mage":
        first_offense = first_offense + 3
        first_class = "mage"
        break
    elif class_choice.lower() == "ranger":
        first_class = "ranger"
        break
    elif class_choice.lower() == "scout":
        first_class = "scout"
        break
    elif class_choice.lower() == "berserk":
        first_class = "berserk"
        first_defense = first_defense * 0
        first_offense = first_offense + 2
        break
    elif class_choice.lower() == "treasure hunter":
        first_class = "treasure hunter"
        break
    else:
        continue

if counter == 1:
    print(
        f"The name of your character is\033[34m {first_name}\033[0m, their health is\033[35m {first_health}\033[0m their base offense is\033[31m {first_offense}"
        f"\033[0m and their base defense is\033[34m {first_defense}\033[0m . The class of your character is\033[35m {first_class}\033[0m. Your maximum health "
        f"is\033[35m {maximum_health}\033[0m.")
    print()
    print("\033[36mTHE GAME STARTS NOW GOOD LUCK AND HAVE FUN!\033[0m")
    print()

    while True:
        if level_counter == 5:
            print("\033[36mYou have beaten Tamadia Dungeons, congratulations!!\033[0m")
            print(f"You have killed\033[31m {kill_count}\033[0m enemies, you had\033[33m {gold}\033[0m gold, you fought\033[31m {total_combat_rounds}\033[0m "
                  f"combats in total you went through\033[31m {total_events}\033[0m events, you walked through\033[31m {total_traps}\033[0m total traps and you"
                  f" drunk\033[31m {total_pots}\033[0m pots in total. You had\033[31m {first_offense}\033[0m offense and\033[34m {first_defense}\033[0m defence"
                  f".")
            break
        if first_health <= 0 and first_class == "mage" and mage_counter == 0:
            first_health = 20
            mage_counter = mage_counter + 1
            print(f"You have been revived with\033[35m {first_health}\033[0m health.")
        elif first_health <= 0:
            print(f"Your health is\033[35m {first_health}\033[0m that means you have died. You have killed\033[31m {kill_count}\033[0m enemies, you had\033[33m"
                  f" {gold}\033[0m gold, you fought\033[31m {total_combat_rounds}\033[0m combats in total,")
            print(f"you went through\033[31m {total_events}\033[0m events, you walked through\033[31m {total_traps}\033[0m total traps and you drunk\033[31m"
                  f"{total_pots}\033[0m pots in total. You had\033[31m {first_offense}\033[0m offense and\033[34m {first_defense}\033[0m defence.")
            break
        if xp_counter >= xp_to_level:
            level_counter = level_counter + 1
            xp_counter = xp_counter - xp_to_level
            xp_to_level = xp_to_level + 5
            first_health = first_health + 5
            maximum_health = maximum_health + level_counter * 5 + fighter_bonus_health + tank_bonus_health
            print(f"\033[34m{first_name}\033[0m has reached level\033[32m {level_counter}\033[0m. Congrats! Your maximum health is now\033[35m {maximum_health}"
                  f"\033[0m. Your current health is now\033[35m {first_health}\033[0m.")
            print()
        if shop_counter >= shop_increase:
            event = "shop"
            shop_increase = shop_increase + 5
            shop_counter = 0
        else:
            event = random_number(5)
            shop_counter = shop_counter + 1
            if last_event_one == event or last_event_two == event:
                continue
            if event == 5 and level_counter < 3:
                continue
        if last_event_counter == 1:
            last_event_one = event
            last_event_counter = 0
        elif last_event_counter == 0:
            last_event_two = event
            last_event_counter = 1
        total_events += 1
        if event == 1:
            combat_round = 0
            print()
            print(f"Oh no, a\033[31m goblin\033[0m emerges. Do you want to fight?\033[32m (fight/run)\033[34m {first_name}\033[0m current health is\033[35m "
                  f"{first_health}\033[0m.")
            decision = input(">")
            if decision == "fight":
                goblin_health = random_number(10) + 10
                goblin_defence = random_number(10)
                while True:
                    combat_round += 1
                    total_combat_rounds += 1
                    print()
                    print(f"Combat round\033[31m {combat_round}\033[0m.")
                    goblin_attack = enemy_attack()
                    goblin_damage = goblin_attack - round((goblin_attack / 100) * (combat_defence(first_defense)))
                    if goblin_damage > 0:
                        first_health = first_health - goblin_damage
                        if first_health <= 0:
                            break
                        print(f"The\033[31m goblin\033[0m deals\033[31m {goblin_damage}\033[0m damage. Your health is now\033[35m {first_health}\033[0m.")
                        if first_class == "ranger" and ranger_counter == 0 and first_health > 0:
                            print("Do you want to run away?\033[32m (yes/no)\033[0m")
                            run = input(">")
                            if run == "yes":
                                ranger_counter = 3
                                xp_counter = xp_counter + 5
                                print(f"You received\033[32m 5\033[0m xp. You now have\033[32m {xp_counter}\033[0m out of\033[32m {xp_to_level}\033[0m "
                                      f"xp to level up.")
                                print()
                                break
                    else:
                        print("The enemy deals\033[31m 0\033[0m damage.")
                    if first_health <= 0:
                        break
                    elif first_health > 0:
                        if first_class == "berserk":
                            berserk_bonus = berserk_bonus + (maximum_health - first_health)
                            print(f"You attack with a berserk bonus of\033[31m {berserk_bonus}\033[0m.")
                        first_attack = first_offense + fighter_counter + berserk_bonus + player_attack()
                        attack_against_goblin = first_attack - round(first_attack / 100) * (
                            combat_defence(goblin_defence))
                        if attack_against_goblin > 0:
                            goblin_health = goblin_health - attack_against_goblin
                            print(f"You have dealt\033[31m {attack_against_goblin}\033[0m damage. The health of your enemy is now\033[31m {goblin_health}"
                                  f"\033[0m.")
                            fighter_counter = fighter_counter + 1
                        else:
                            print("You have dealt\033[31m 0\033[0m damage.")
                            fighter_counter = fighter_counter + 1
                        if goblin_health <= 0:
                            kill_count += 1
                            berserk_bonus = 0
                            if ranger_counter > 0:
                                ranger_counter = ranger_counter - 1
                            goblin_loot = loot(1)
                            if goblin_loot[0] > 0:
                                first_defense = first_defense + goblin_loot[0]
                                print()
                                print(
                                    f"\033[36mYou have won!\033[0m The\033[31m goblin\033[0m has dropped\033[34m armor\033[0m increasing your defense to"
                                    f"\033[34m {first_defense}\033[0m.")
                            elif goblin_loot[1] > 0:
                                first_offense = first_offense + goblin_loot[1]
                                print()
                                print(f"\033[36mYou have won!\033[0m The\033[31m goblin\033[0m has dropped a\033[31m weapon\033[0m increasing your offense"
                                      f"\033[31m {first_offense}\033[0m.")
                            elif goblin_loot[2] > 0:
                                gold = gold + goblin_loot[2]
                                print()
                                print(f"\033[36mYou have won!\033[0m The\033[31m goblin\033[0m has dropped\033[33m gold\033[0m increasing your gold to\033[33m "
                                      f"{gold}\033[0m.")
                            elif goblin_loot[3] > 0:
                                print()
                                print("\033[36mYou have won!\033[0m The\033[31m goblin\033[0m has dropped nothing.")
                            xp_counter = xp_counter + 5
                            print(f"\033[34m{first_name}\033[0m has received\033[32m 5\033[0m xp. They now have\033[32m {xp_counter}\033[0m out of\033[32m "
                                  f"{xp_to_level}\033[0m xp to reach the next level up.")
                            print()
                            break

                        else:
                            continue
            else:
                continue
        elif event == 2:
            print(f"\033[34m{first_name}\033[0m has found a pot do you want to drink it?\033[32m (drink/ignore)\033[0m their current health is\033[35m "
                  f"{first_health}\033[0m.")
            take_pot = input(">")
            if take_pot == "drink":
                total_pots += 1
                pot_event = random_number(3)
                if pot_event == 1 or pot_event == 3:
                    pot_good = random_number(9)
                    first_health = first_health + pot_good
                    if first_health > maximum_health:
                        first_health = maximum_health
                    print(f"The pot was healthy increasing\033[34m {first_name}\033[0m health to\033[35m {first_health}\033[0m.")
                    print()
                    continue
                elif pot_event == 2:
                    pot_bad = random_number(5)
                    first_health = first_health - pot_bad
                    print(f"The pot was poisonous decreasing\033[34m {first_name}\033[0m health to\033[35m {first_health}\033[0m.")
                    print()
                    continue

            print()
            continue

        elif event == 3:
            total_traps += 1
            if first_class == "scout":
                a_b = random_number(2)
                if a_b == 1:
                    guess = "a"
                else:
                    guess = "b"
                print("Guess the correct letter to avoid the trap damage!\033[32m (a/b) \033[0m", )
                guess_player = input(">")
                if guess_player == guess:
                    xp_counter = xp_counter + 5
                    print("You have guessed the correct letter, you avoid the trap.", "\033[34m", first_name, "\033[0m",
                          "takes", "\033[31m", "0", "\033[0m", "damage. They have received", "\033[32m", "5", "\033[0m",
                          "xp. They now have", "\033[32m", xp_counter, "\033[0m", "out of", "\033[32m", xp_to_level,
                          "\033[0m", "xp to reach the next level up.")
                    scout_loot = random_number(3)
                    if scout_loot == 1:
                        gold_gain = random_number(5)
                        gold += gold_gain
                        print("Hidden in the trap you have found", "\033[33m", gold_gain, "\033[0m", "gold, congrats!!")
                        print()
                        continue
                    elif scout_loot == 2:
                        first_defense = first_defense + random_number(2)
                        print("Hidden in the trap you have found armor increasing", "\033[34m", first_name, "\033[0m",
                              "defense to", "\033[34m", first_defense, "\033[0m", ".")
                        print()
                        continue
                    elif scout_loot == 3:
                        first_offense = first_offense + random_number(2)
                        print("Hidden in the trap you have found a weapon increasing", "\033[34m", first_name,
                              "\033[0m", "offense to", "\033[31m", first_offense, "\033[0m", ".")
                        print()
                        continue
                else:
                    print("Your guess was wrong.")
            trap_damage = random_number(4)
            first_health = first_health - trap_damage
            print(f"\033[34m{first_name}\033[0m has walked into a trap, they take\033[31m {trap_damage}\033[0m damage. Their health is now\033[35m "
                  f"{first_health}\033[0m.")
            print()
            continue

        elif event == 4:
            gold_gain = random_number(3)
            gold = gold + gold_gain
            print(f"\033[34m{first_name}\033[0m has found\033[33m {gold_gain}\033[0m {gold}. They now have\033[33m {gold}\033[0m gold. Keep it save!")
            print()
            continue

        elif event == 5:
            combat_round = 0
            print("An\033[31m orc\033[0m emerges, do you want to fight?\033[32m (fight/run)\033[0m")
            fight_orc = input(">")
            if fight_orc == "fight":
                orc_health = random_number(15) + 15
                orc_defence = random_number(10) + 10
                orc_attack = random_number(7) + 7
                orc_pattern = 1
                while orc_health > 0:
                    berserk_bonus = 0
                    if first_class == "ranger" and ranger_counter == 0 and first_health > 0:
                        print("Do you want to run away?\033[32m (run/stay)\033[0m")
                        run = input(">")
                        if run.lower == "run":
                            ranger_counter = 3
                            xp_counter = xp_counter + 10
                            print(f"You received\033[32m 10\033[0m xp. You now have\033[32m {xp_counter}\033[0m out of\033[32m {xp_to_level}\033[0m "
                                  f"xp to level up.")
                            print()
                            break
                    if first_class == "berserk":
                        berserk_bonus = maximum_health - first_health
                    fighter_counter = fighter_counter + 1
                    print("Choose your action\033[32m (attack/block)\033[0m")
                    if orc_pattern == 1 or orc_pattern == 2:
                        orc_react = input(">")
                        if orc_react == "attack":
                            orc_damage = orc_attack - round(orc_attack / 100 * combat_defence(first_defense))
                            first_health = first_health - orc_damage
                            print(f"You didn't block the orc attack. You take\033[31m {orc_damage}\033[0m damage. Your health is now\033[35m "
                                  f"{first_health}\033[0m")
                            print()
                            orc_pattern = orc_pattern + 1
                            print()
                            continue
                        elif orc_react == "block":
                            print("The orc attacks but you are prepared and block. You take 0 damage")
                            orc_pattern = orc_pattern + 1
                            print()
                            continue
                    if orc_pattern == 3 or orc_pattern == 4:
                        orc_react = input(">")
                        if orc_react == "attack":
                            first_attack = first_offense + fighter_counter + berserk_bonus + player_attack()
                            first_damage = first_attack - round(first_attack / 100 * combat_defence(orc_defence))
                            orc_health = orc_health - first_damage
                            if first_class == "berserk":
                                print(f"You attack with a berserk bonus of\033[31m {berserk_bonus}\033[0m.")
                            print(
                                f"The orc is recovering from its attack, making it vulnerable to your attack. You deal\033[31m {first_damage}\033[0m damage. "
                                f"The health of the orc is now\033[35m {orc_health}\033[0m")
                            print()
                            if orc_pattern == 3:
                                orc_pattern = orc_pattern + 1
                            elif orc_pattern == 4:
                                orc_pattern = orc_pattern - 3
                        else:
                            print("You stare at the seemingly exhausted monster. Nothing happens")
                            print()
                    if orc_health < 0:
                        kill_count += 1
                        berserk_bonus = 0
                        if ranger_counter > 0:
                            ranger_counter = ranger_counter - 1
                        orc_loot = loot(2)
                        if orc_loot[0] > 0:
                            first_defense = first_defense + orc_loot[0]
                            print()
                            print("\033[36mYou have won!\033[0m The\033[31m orc", "\033[0m",
                                  "has dropped", "\033[34m", "armor", "\033[0m", "increasing your defense to",
                                  "\033[34m", first_defense, "\033[0m", ".")
                        elif orc_loot[1] > 0:
                            first_offense = first_offense + orc_loot[1]
                            print()

                            print("\033[36mYou have won!", "\033[0m", "The", "\033[31m", "orc", "\033[0m",
                                  "has dropped a", "\033[31m", "weapon", "\033[0m", "increasing your offense to",
                                  "\033[31m", first_offense, "\033[0m", ".")
                        elif orc_loot[2] > 0:
                            gold = gold + orc_loot[2]
                            print()
                            print("\033[36mYou have won!", "\033[0m", "The", "\033[31m", "orc", "\033[0m",
                                  "has dropped", "\033[33m", "gold", "\033[0m", "increasing your gold to",
                                  "\033[33m", gold, "\033[0m", ".")
                        elif orc_loot[3] > 0:
                            print()
                            print("\033[36mYou have won!", "\033[0m", "The", "\033[31m", "orc", "\033[0m",
                                  "has dropped nothing.")
                        xp_counter = xp_counter + 10
                        print(f"\033[34m{first_name}\033[0m", "has received", "\033[32m", "10", "\033[0m",
                              "xp. They now have", "\033[32m", xp_counter, "\033[0m", "out of", "\033[32m",
                              xp_to_level, "\033[0m", "xp to reach the next level up.")
                        print()

        elif event == "shop":
            print(f"\033[34m{first_name}\033[0m has encountered a\033[36m SHOP.\033[34m {first_name}\033[0m current gold is\033[33m {gold}\033[0m.")
            reroll_counter = 0
            while True:
                reroll_counter += 1
                if reroll_counter == 4:
                    print("You have reached the maximum amount ot rerolls.")
                    print()
                    break
                what_item = random_number(3)
                while first_class == "berserk" and what_item == 1:
                    what_item = random_number(3)
                if what_item == 1:
                    armor_stats = random_number(5)
                    price_armor = random_number(20)
                    print()
                    print("The shop offers you armor with", "\033[34m", armor_stats, "\033[0m",
                          "defence for the price of", "\033[33m",
                          price_armor, "\033[0m",
                          "gold. Do you want to buy it?", "\033[32m", "(yes/reroll)", "\033[0m")
                    if gold < price_armor:
                        print("You can't afford this armor.")
                        print()
                        continue
                    buy_armor = input(">")
                    if buy_armor == "yes":
                        first_defense = first_defense + armor_stats
                        gold = gold - price_armor
                        print("You have bought the armor. Your defence is now", "\033[34m", first_defense, "\033[0m",
                              ". You have", "\033[33m",
                              gold, "\033[0m",
                              "gold left.")
                        print()
                        break
                    else:
                        continue

                elif what_item == 2:
                    weapon_stats = random_number(5)
                    price_weapon = random_number(20)
                    print()
                    print("The shop offers you a weapon with", "\033[31m", weapon_stats, "\033[0m",
                          "offence for the price of", "\033[33m",
                          price_weapon, "\033[0m",
                          "gold. Do you want to buy it?", "\033[32m", "(yes/reroll)", "\033[0m", )
                    if gold < price_weapon:
                        print("You can't afford this weapon.")
                        print()
                        continue
                    buy_weapon = input(">")
                    if buy_weapon == "yes":
                        first_offense = first_offense + weapon_stats
                        gold = gold - price_weapon
                        print("You have bought the weapon. Your offence is now", "\033[31m", first_offense, "\033[0m",
                              ". You have", "\033[33m",
                              gold, "\033[0m", "left.")
                        print()
                        break
                    else:
                        continue

                elif what_item == 3:
                    pot_stats = random_number(20)
                    price_pot = random_number(15)
                    print("The shop offers you a pot that would increase your health by", "\033[35m", pot_stats,
                          "\033[0m", "for the price of",
                          "\033[33m",
                          price_pot, "\033[0m", "gold. Do you want to buy it?", "\033[32m", "(yes/reroll)", "\033[0m")
                    if gold < price_pot:
                        print("You can't afford this pot.")
                        print()
                        continue
                    buy_pot = input(">")
                    if buy_pot == "yes":
                        first_health = first_health + pot_stats
                        if first_health > maximum_health:
                            first_health = maximum_health
                        gold = gold - price_pot
                        print("You have bought the pot increasing your health to", "\033[35m", first_health, "\033[0m",
                              ". You have",
                              "\033[33m", gold, "\033[0m",
                              "gold left.")
                        print()
                        break
                    else:
                        continue
