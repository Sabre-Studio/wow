import { TypeOf, z } from 'zod'

export const connectedRealmSearchSchema = z.object({
  page: z.number(),
  pageSize: z.number(),
  maxPageSize: z.number(),
  pageCount: z.number(),
  results: z.array(
    z.object({
      key: z.object({ href: z.string() }),
      data: z.object({
        realms: z.array(
          z.object({
            is_tournament: z.boolean(),
            timezone: z.string(),
            name: z.object({
              it_IT: z.string(),
              ru_RU: z.string(),
              en_GB: z.string(),
              zh_TW: z.string(),
              ko_KR: z.string(),
              en_US: z.string(),
              es_MX: z.string(),
              pt_BR: z.string(),
              es_ES: z.string(),
              zh_CN: z.string(),
              fr_FR: z.string(),
              de_DE: z.string(),
            }),
            id: z.number(),
            region: z.object({
              name: z.object({
                it_IT: z.string(),
                ru_RU: z.string(),
                en_GB: z.string(),
                zh_TW: z.string(),
                ko_KR: z.string(),
                en_US: z.string(),
                es_MX: z.string(),
                pt_BR: z.string(),
                es_ES: z.string(),
                zh_CN: z.string(),
                fr_FR: z.string(),
                de_DE: z.string(),
              }),
              id: z.number(),
            }),
            category: z.object({
              it_IT: z.string(),
              ru_RU: z.string(),
              en_GB: z.string(),
              zh_TW: z.string(),
              ko_KR: z.string(),
              en_US: z.string(),
              es_MX: z.string(),
              pt_BR: z.string(),
              es_ES: z.string(),
              zh_CN: z.string(),
              fr_FR: z.string(),
              de_DE: z.string(),
            }),
            locale: z.string(),
            type: z.object({
              name: z.object({
                it_IT: z.string(),
                ru_RU: z.string(),
                en_GB: z.string(),
                zh_TW: z.string(),
                ko_KR: z.string(),
                en_US: z.string(),
                es_MX: z.string(),
                pt_BR: z.string(),
                es_ES: z.string(),
                zh_CN: z.string(),
                fr_FR: z.string(),
                de_DE: z.string(),
              }),
              type: z.string(),
            }),
            slug: z.string(),
          }),
        ),
        id: z.number(),
        has_queue: z.boolean(),
        status: z.object({
          name: z.object({
            it_IT: z.string(),
            ru_RU: z.string(),
            en_GB: z.string(),
            zh_TW: z.string(),
            ko_KR: z.string(),
            en_US: z.string(),
            es_MX: z.string(),
            pt_BR: z.string(),
            es_ES: z.string(),
            zh_CN: z.string(),
            fr_FR: z.string(),
            de_DE: z.string(),
          }),
          type: z.string(),
        }),
        population: z.object({
          name: z.object({
            it_IT: z.string(),
            ru_RU: z.string(),
            en_GB: z.string(),
            zh_TW: z.string(),
            ko_KR: z.string(),
            en_US: z.string(),
            es_MX: z.string(),
            pt_BR: z.string(),
            es_ES: z.string(),
            zh_CN: z.string(),
            fr_FR: z.string(),
            de_DE: z.string(),
          }),
          type: z.string(),
        }),
      }),
    }),
  ),
})

export type ConnectedRealmSearchResponse = z.infer<
  typeof connectedRealmSearchSchema
>