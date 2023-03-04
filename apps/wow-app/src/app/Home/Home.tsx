import clsx from 'clsx'
import { atom, useAtomValue } from 'jotai'
import {
  DungeonLeaderboardResponse,
  dungeonLeaderBoardSchema,
} from 'src/api/dungeon-leaderboard-schema'
import leaderboard from '../../api/data/connected-realm-leaderboard.json'

const leaderboardAtom = atom<DungeonLeaderboardResponse>(
  dungeonLeaderBoardSchema.parse(leaderboard),
)

function Home() {
  const leaderboard = useAtomValue(leaderboardAtom)

  return (
    <main className={clsx('HomeRoot', 'flex flex-col items-center')}>
      <h1 className={clsx('Heading', 'mt-5 text-4xl')}>
        Sabre's Weekly M+ Leaderboard
      </h1>

      <div>
        <div>{leaderboard.map.name.en_US}</div>
        <div>
          {leaderboard.leading_groups.map((group) => (
            <div>
              <p>
                {`${group.ranking} - ${group.keystone_level} - ${group.duration} - ${group.mythic_rating.rating}`}
              </p>

              <ul>
                {group.members.map((member) => (
                  <li>{member.profile.name}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </main>
  )
}

export default Home
