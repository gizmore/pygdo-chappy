# Chappy combat manual

You can fight a random or specified chappy with `$cpf` (chappy.fight).

You can also specify an element to attack with.

Examples:

```
$cpf WolfgangPetry  # Attack with default element (mankind)
$cpf --with fire  # Attack a random Chappy with fire.
$cpf --with wind gizmore  # Attack gizmore with wind.
```

ATK and Defense calculates from attributes and genes.

### Chappy Attack Attributes

There are 4 attributes that affect combat attack values.

- Attack (can be leveled up)
- Strength * 3.0 (can be raised via genes)
- Quickness * 1.5 (can be raised via genes)
- Intelligence * 2.0 (can be raised via genes)


### Chappy Defense Attributes

There are 4 attributes that affect combat defense values.

- Defense (can be leveled up)
- Strength * 1.5 (can be raised via genes)
- Quickness * 3.0 (can be raised via genes)
- Intelligence * 2.0 (can be raised via genes)


### Chappy Elements

There are 6 "elements" coded into the stats affecting the combat.

3 Base elements get the power via your Chappy's colors.
There are 3 colors that affect these base elements by it's rgb values.
Feather-, hair- and eye-color.

- red Fire (red) (Fire) vs (Earth)
- green Earth (Earth) vs. (Water)
- blue Water (Water) vs. (Fire)

3 Composite elements are using 2 base elements,
and a special gene, to compute attack and defense.

- Ice (Earth + Water + Gene: HairLength) vs. (Earth + Fire + Gene: HairLength)
- Wind (Water + Fire + Gene: WingSize) vs. (Earth + Fire + Gene: WingSize)

- Mankind / BirdPersons: (Gene: Size) vs. (Gene: Size)


## Chappy Combat Math

