import clsx from 'clsx'

function Home() {
  return (
    <main className={clsx('HomeRoot', 'flex justify-center')}>
      <h1 className={clsx('Heading', 'mt-5 text-4xl')}>
        Sabre's Weekly M+ Leaderboard
      </h1>
    </main>
  )
}

export default Home
