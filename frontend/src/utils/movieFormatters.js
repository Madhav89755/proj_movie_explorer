export function getReleaseYear(dateString) {
  if (!dateString) {
    return 'Unknown'
  }

  return new Date(dateString).getFullYear()
}

export function listNames(items = []) {
  if (!items.length) {
    return 'N/A'
  }

  return items.map((item) => item.name).join(', ')
}

export function personRoleLabel(actorMovies = [], directorMovies = []) {
  const hasActorWork = actorMovies.length > 0
  const hasDirectorWork = directorMovies.length > 0

  if (hasActorWork && hasDirectorWork) {
    return 'Actor and Director'
  }

  if (hasDirectorWork) {
    return 'Director'
  }

  return 'Actor'
}
