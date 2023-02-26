# Blizzard API Routes

## Game APIs

### Connected Realm API

- /data/wow/connected-realm/index
- /data/wow/connected-realm/{connectedRealmId}
- /data/wow/search/connected-realm

### Mythic Keystone Affix API

- /data/wow/keystone-affix/index
- /data/wow/keystone-affix/{keyStoneAffixId}
- /data/wow/media/keystone-affix/{keyStoneAffixId}

### Mythic Keystone Dungeon API

- /data/wow/mythic-keystone/dungeon/index
- /data/wow/mythic-keystone/dungeon/{dungeondId}
- /data/wow/mythic-keystone/index
- /data/wow/mythic-keystone/period/index
- /data/wow/mythic-keystone/period/{periodId}
- /data/wow/mythic-keystone/season/index
- /data/wow/mythic-keystone/season/{seasonId}

### Mythic Keystone Leaderboard API

- /data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/index
- /data/wow/connected-realm/{connectedRealmId}/mythic-leaderboard/{dungeondId}/period/{periodId}

### Playable Class API 

- /data/wow/playable-class/index
- /data/wow/playable-class/{classId}
- /data/wow/media/playable-class/{playableClassId}
- /data/wow/playable-class/{classId}/pvp-talent-slots


### Playable Race API 

- /data/wow/playable-race/index
- /data/wow/playable-race/{playableRaceId}

### Playable Specialization API 

- /data/wow/playable-specialization/index
- /data/wow/playable-specialization/{specId}
- /data/wow/media/playable-specialization/{specId}

### Realm API 

- /data/wow/realm/index
- /data/wow/realm/{reamSlug}
- /data/wow/search/realm

### Region API 

- /data/wow/region/index
- /data/wow/region/{regionId}

### Spell API 

- /data/wow/spell/{spellId}
- /data/wow/media/spell/{spellId}
- /data/wow/search/spell

### Talent API 

- /data/wow/talent-tree/index
- /data/wow/talent-tree/{talentTreeId}/playable-specialization/{specId}
- /data/wow/talent-tree/{talentTreeId}
- /data/wow/talent/index
- /data/wow/talent/{talentId}
- /data/wow/pvp-talent/index
- /data/wow/pvp-talent/{pvpTalentId}

### Tech Talent API

- /data/wow/tech-talent-tree/index
- /data/wow/tech-talent-tree/{techTalentTreeId}
- /data/wow/tech-talent/index
- /data/wow/tech-talent/{techTalentId}
- /data/wow/media/tech-talent/{techTalentId}

## Profile API 

### Account Profile API

- /profile/user/wow
  - Don't think I'll use this one bc it requires auth
- /profile/user/wow/protected-character/{realmId}-{characterId}
- /profile/user/wow/collections
- /profile/user/wow/collections/mounts
- /profile/user/wow/collections/pets

### Character Encounters API 

- /profile/wow/character/{realmSlug}/{characterName}/encounters
- /profile/wow/character/{realmSlug}/{characterName}/encounters/dungeons
- /profile/wow/character/{realmSlug}/{characterName}/encounters/raids

### Character Equipment API 

- /profile/wow/character/{realmSlug}/{characterName}/equipment

### Character Mythic Keystone Profile API 

- /profile/wow/character/{realmSlug}/{characterName}/mythic-keystone-profile
- /profile/wow/character/{realmSlug}/{characterName}/mythic-keystone-profile/season/{seasonId}

### Character Profile API 

- /profile/wow/character/{realmSlug}/{characterName}
- /profile/wow/character/{realmSlug}/{characterName}/status

### Character Specialization API 

- /profile/wow/character/{realmSlug}/{characterName}/specializations

### Character Statistics API 

- /profile/wow/character/{realmSlug}/{characterName}/statistics 

