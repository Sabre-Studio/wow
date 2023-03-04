import clsx from 'clsx'
import { Outlet } from 'react-router-dom'

function Layout() {
  return (
    <div className={clsx('Root', 'dark min-h-full bg-mauve-1 text-mauve-12')}>
      <Outlet />
    </div>
  )
}

export default Layout
