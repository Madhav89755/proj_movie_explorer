import { ENDPOINTS } from '@/api/endpoints'
import { getJson, postJson } from '@/api/http'

export async function fetchStaffList(params = {}) {
  const page = await getJson(ENDPOINTS.staff, {
    limit: 100,
    ...params,
  })

  return page.results
}

export function fetchStaffById(id) {
  return getJson(ENDPOINTS.staffById(id))
}

export async function fetchGenres(params = {}) {
  const page = await getJson(ENDPOINTS.genres, {
    limit: 100,
    ...params,
  })

  return page.results
}

export function createGenre(payload) {
  return postJson(ENDPOINTS.genres, payload)
}

export function createStaff(payload) {
  return postJson(ENDPOINTS.staff, payload)
}
