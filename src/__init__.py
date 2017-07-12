import battalion
import troop
import army
import battle

# name, max_health, current_health, level, rng, atk, dfn, spd, sign_nr


def test():
    grunt0 = troop.Grunt("Ranger1", 25, 25, 1, 20, 10, 5, 20)
    grunt1 = troop.Grunt("Ranger2", 25, 25, 1, 20, 10, 5, 20)
    grunt2 = troop.Grunt("Ranger3", 25, 25, 1, 20, 10, 5, 20)
    grunt3 = troop.Grunt("Soldier1", 50, 50, 1, 1, 20, 20, 10)
    grunt4 = troop.Grunt("Soldier2", 50, 50, 1, 1, 20, 20, 10)
    grunt5 = troop.Grunt("Soldier3", 50, 50, 1, 1, 20, 20, 10)
    champion = troop.Grunt("Champion", 1000, 1000, 1, 1, 20, 20, 50)

    test0 = battalion.Battalion("bat1", grunt0, 30)
    test1 = battalion.Battalion("bat2", grunt1, 30)
    test2 = battalion.Battalion("bat3", grunt2, 30)
    test3 = battalion.Battalion("bat4", grunt3, 30)
    test4 = battalion.Battalion("bat5", grunt4, 30)
    test5 = battalion.Battalion("bat6", grunt5, 30)

    army0 = army.Army()
    army0.add_troop(test0)
    army0.add_troop(test1)
    army0.add_troop(test2)
    army0.add_troop(test3)
    army0.add_troop(test4)
    army0.add_troop(test5)
    army0.insert_troop(champion, 2)

    army1 = army.Army()
    army1.add_troop(test0)
    army1.add_troop(test1)
    army1.add_troop(test2)
    army1.add_troop(test3)
    army1.add_troop(test4)
    army1.add_troop(test5)

    battle0 = battle.Battle(army0.army, army1.army)
    print(len(battle0.big_army))
    print(battle0)

test()
