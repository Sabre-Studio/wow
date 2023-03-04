import { z } from 'zod'

export const dungeonLeaderBoardSchema = z.object({
  _links: z.object({ self: z.object({ href: z.string() }) }),
  map: z.object({
    name: z.object({
      en_US: z.string(),
      es_MX: z.string(),
      pt_BR: z.string(),
      de_DE: z.string(),
      en_GB: z.string(),
      es_ES: z.string(),
      fr_FR: z.string(),
      it_IT: z.string(),
      ru_RU: z.string(),
      ko_KR: z.string(),
      zh_TW: z.string(),
      zh_CN: z.string(),
    }),
    id: z.number(),
  }),
  period: z.number(),
  period_start_timestamp: z.number(),
  period_end_timestamp: z.number(),
  connected_realm: z.object({ href: z.string() }),
  leading_groups: z.array(
    z.object({
      ranking: z.number(),
      duration: z.number(),
      completed_timestamp: z.number(),
      keystone_level: z.number(),
      members: z.array(
        z.object({
          profile: z.object({
            name: z.string(),
            id: z.number(),
            realm: z.object({
              key: z.object({ href: z.string() }),
              id: z.number(),
              slug: z.string(),
            }),
          }),
          faction: z.object({ type: z.string() }),
          specialization: z.object({
            key: z.object({ href: z.string() }),
            id: z.number(),
          }),
        }),
      ),
      mythic_rating: z.object({
        color: z.object({
          r: z.number(),
          g: z.number(),
          b: z.number(),
          a: z.number(),
        }),
        rating: z.number(),
      }),
    }),
  ),
  keystone_affixes: z.array(
    z.object({
      keystone_affix: z.object({
        key: z.object({ href: z.string() }),
        name: z.object({
          en_US: z.string(),
          es_MX: z.string(),
          pt_BR: z.string(),
          de_DE: z.string(),
          en_GB: z.string(),
          es_ES: z.string(),
          fr_FR: z.string(),
          it_IT: z.string(),
          ru_RU: z.string(),
          ko_KR: z.string(),
          zh_TW: z.string(),
          zh_CN: z.string(),
        }),
        id: z.number(),
      }),
      starting_level: z.number(),
    }),
  ),
  map_challenge_mode_id: z.number(),
  name: z.object({
    en_US: z.string(),
    es_MX: z.string(),
    pt_BR: z.string(),
    de_DE: z.string(),
    en_GB: z.string(),
    es_ES: z.string(),
    fr_FR: z.string(),
    it_IT: z.string(),
    ru_RU: z.string(),
    ko_KR: z.string(),
    zh_TW: z.string(),
    zh_CN: z.string(),
  }),
})

export type DungeonLeaderboardResponse = z.infer<
  typeof dungeonLeaderBoardSchema
>
