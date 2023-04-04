# Blizz API Workflow

- Get connected realms
- For connected realm ref, get connected realm
- For each connected realm, get current mplus leaderboard
  - I feel like I could just do this once to get the dungeons and just skip to using the mplus leaderboards

## API Calls

```python
# Get Connected Realms List
# https://us.api.blizzard.com/data/wow/connected-realm/?namespace=dynamic-us

# Get Connected Realm
# https://us.api.blizzard.com/data/wow/connected-realm/{realm_id}?namespace=dynamic-us

# Get Connected Realm Mythic Leaderboard
# https://us.api.blizzard.com/data/wow/connected-realm/{realm_id}/mythic-leaderboard/?namespace=dynamic-us


```

## Notes

- I feel like I don't need to get all the connected realms each time.
  - Should really only need to get that info every now and then to make sure they haven't like added a new realm or something
- Where the real work is going to be is getting the current leaderboard for the periods

Connected Realms Index
/data/wow/connected-realm/index

Connected Realm
/data/wow/connected-realm/{connectedRealmId}
