import clsx from 'clsx'
import { Outlet } from 'react-router-dom'

function Layout() {
  return (
    <div className={clsx('Root', 'dark h-full bg-mauve-1 text-mauve-12')}>
      <Outlet />
    </div>
  )
}

export default Layout
