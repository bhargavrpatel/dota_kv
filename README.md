#Dota 2 KV Package
Unlike my [Lua Snippets](https://github.com/bhargavrpatel/Dota-2-Sublime-Packages) project, this is a *Package*. The package consists of custom syntax highlighting and Snippets. The Snippets consist of all the KV pairs, modifiers, and constants. 

### Installation
Chose either of the methods listed below. I suggest everyone use **Method 1**
#### Method 1
I have uploaded the mod as a submission to Sublime Package Control. This means when I update the package, it will update on your system automatically.
The ideal method is as follows:
1. Install [Sublime Package Control ](https://sublime.wbond.net/installation)
2. Open Command Pallet (CNTRL+SHIFT+P), type "Install Package" then press Enter.
3. Once the list of packages has been cached, type "Dota KV" then press Enter.

#### Method 2
If you do not wish to install via Sublime Package Control, your version of the package will not be automatically updated when I update. The steps are as follows.
1. Download repo as a zip file. 
2. Extract all the files into a folder called "Dota KV"
3. In Sublime text, click on Preferences > Browse Packages. Move the "Dota KV" folder in the explorer instance that pops up.

***
## Guide
### Snippets for Functions
![Snippets V1.0.0 Demo](http://fat.gfycat.com/ObedientParallelIbis.gif)
Supported Functions so far. They are all that are listed on [Hex6's website](hex6.se/dota/modifier_functions.txt). The "Triggers" for these is same as their name. When you start typing, **first letter has to be capital.**. I plan on adding the others used in creation of heroes/units in a couple of days.
* Random
* Target
* States
* SpendCharge
* OnProjectileHit
* OnOwnerSpawned
* OnOwnerDied
* OnSpellStart
* OnToggleOn
* OnToggleOff
* OnChannelFinish
* OnAttackStart
* OnDeath
* OnKill
* OnTakeDamage
* OnThinkInterval
* OnCreated
* Properties 	-	Modifiers "Properties" sub-function
* Modifiers   - Used to create new modifiers
* Orb
* MoveUnit
* CleaveAttack
* ReplaceUnit
* SpawnUnit
* TrackingProjectile
* Damage
* CreateThinker
* CreateThinkerWall
* ApplyModifier
* RemoveModifier
* KnockBack
* LifeSteal
* FireSound
* FireEffect
* Heal

### Completions for Constants
There are above 1400 constants that I have added. I will not list them here, you can simply open *constants.sublime-completions* in Sublime Text to see them. Unlike snippets, **constants are case agnostic**. First letter not need be capital.

#### Methods of using Constants
1. You can start typing words which you can think of and press **Cntrl + Space** to see a list. 
2. Type a completion as best you can and simply press TAB. You can then iterate over the completion by pressing TAB. 
![Constants V1.0.0 Demo](http://giant.gfycat.com/AgreeableUnselfishAztecant.gif)

 Here is a list which states them by category. 

| Category  | Trigger*  | Example |
| :------------ |:---------------:| -----:|
| Ability Types | abilityType        |    DOTA_ABILITY_TYPE_BASIC |
| Ability Behaviors | abilityBehavior        |    DOTA_ABILITY_BEHAVIOR_AOE |
| Modifier Names      | modifierName | modifier_slark_essence_shift_debuff |
| Modifier States     | modifierState        |   MODIFIER_STATE_BLIND |
| Modifier Property | modifierState        |    MODIFIER_PROPERTY_ABSOLUTE_NO_DAMAGE_MAGICAL |
| Modifier Events | modifierEvent        |    MODIFIER_EVENT_ON_ABILITY_END_CHANNEL |
| Damage Types | damageType        |    DAMAGE_TYPE_MAGICAL |
| Particle Attach | PATTACHParticleAttach        |    PATTACH_ABSORIGIN |
| Particle Attach | PATTACHParticleAttach        |    PATTACH_ABSORIGIN |
| Item Flags | itemFlag        |    ITEM_FLAG_LIMITINWORLD |
| Item Types | itemType        |    ITEM_CORE |
| Item Sharability | sharable        |    ITEM_FULLY_SHAREABLE |
| Item Declarations | delcare        |    DECLARE_PURCHASES_IN_SPEECH |
| FCVARs | fcvar        |    FCVAR_CHEAT |
| Movement Capabilities | movementCap        |    DOTA_UNIT_CAP_MELEE_ATTACK |
| Team | team        |    DOTA_TEAM_GOODGUYS |
| Random Crit Type | randomType        |    DOTA_PSEUDO_RANDOM_BREWMASTER_CRIT |
| Hull Sizes | hullSize        |    DOTA_HULL_SIZE_BUILDING |
| Attribute Types | attribute        |    DOTA_ATTRIBUTE_INTELLECT |
| Unit Target | unitTarget        |    DOTA_UNIT_TARGET_BUILDING |
| Unit Target Team | unitTargetTeam        |    DOTA_UNIT_TARGET_TEAM_CUSTOM |
| Unit Target Flags | unitTargetFlag        |    DOTA_UNIT_TARGET_FLAG_RANGED_ONLY |
| TARGETKEYs | targetKey        |    POINT |
| Orb Priorities | orbPrio        |    DOTA_ORB_PRIORITY_ITEM_PROC |
| Orb Labels | orbLabel        |    DOTA_ORB_LABEL_EXCEPTION |
* As I said before: Triggers arent as sensitive as Snippets. Type anyword that comes inside the Trigger and you should see a popup.