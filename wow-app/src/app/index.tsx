import { Route, Routes } from 'react-router-dom'
import Layout from '@components/Layout'
import Home from './Home'
import NotFound from './NotFound'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
      </Route>

      <Route path="*" element={<NotFound />} />
    </Routes>
  )
}
