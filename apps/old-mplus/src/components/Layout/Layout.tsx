import clsx from 'clsx'
import { Outlet } from 'react-router-dom'

function Layout() {
  return (
    <div className={clsx('Root', 'h-full bg-gray-900 text-white')}>
      <Outlet />
    </div>
  )
}

export default Layout
