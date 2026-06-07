import { ENDPOINTS } from '@/api/endpoints'
import { getJson, postJson } from '@/api/http'

export function fetchMovies(filters = {}) {
  return getJson(ENDPOINTS.movies, filters)
}

export function fetchMovieById(id) {
  return getJson(ENDPOINTS.movieById(id))
}

export function createMovie(payload) {
  return postJson(ENDPOINTS.movieManage, payload)
}

export async function fetchMoviesWithDetails(filters = {}) {
  const page = await fetchMovies(filters)
  const detailedResults = await Promise.all(
    page.results.map(async (movie) => {
      try {
        return await fetchMovieById(movie.id)
      } catch {
        return {
          ...movie,
          genre: [],
          actors: [],
          director: null,
        }
      }
    }),
  )

  return {
    ...page,
    results: detailedResults,
  }
}
