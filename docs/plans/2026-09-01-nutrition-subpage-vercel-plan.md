# Nutrition subpage and Vercel preview plan

## Goal

Keep the public course catalog focused on the 11-course curriculum while giving the NIH nutrition education initiative its own complete, Atlas-styled review page.

## Work

1. Add `nutrition.html` with the proposal, 53-hour pathway, evaluation criteria, team roles, and official sources.
2. Add a Nutrition link to the shared public navigation without mixing nutrition content into the course catalog.
3. Replace the long nutrition section in the root README with links to the public page and working specification.
4. Bump the Commons release to `0.100.0` and the public catalog release to `0.41.0`.
5. Run syntax, route, responsive browser, and accessibility smoke checks.
6. Commit and push the feature branch, then create a fresh Vercel preview for review.

## Acceptance checks

- The home page contains the 11-course catalog and only a navigation link to nutrition.
- `nutrition.html` contains the nutrition initiative and does not appear as a curriculum course.
- The nutrition pathway table remains usable on mobile through horizontal scrolling.
- The home, course, module, atlas, and nutrition links remain reachable.
- The Vercel preview is created from the feature branch, not deployed to production.
