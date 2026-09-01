# Atlas site restyle plan

## Goal

Apply the visual language of the clinical data visualization atlas to every public curriculum page so the home page, course pages, module pages, and working lesson feel like one product.

## Audience

Learners and instructors browsing the curriculum, choosing a course, or opening a weekly module.

## Reference system

The source of truth is `courses/data-visualization/atlas.html`:

- Manrope for interface and learning content, with IBM Plex Mono for short labels and numbers.
- Cool gray canvas (`#f5f7fb`), white surfaces, navy text, restrained blue actions, and pale blue supporting panels.
- A 64px translucent top bar, a 1200px content frame, thin borders, modest shadows, and 8px to 18px corner radii.
- Compact labels, direct headings, clear progress and route cues, and accessible focus states.

## Work

1. Replace the separate editorial theme in `site.css` with the Atlas tokens and component treatment while preserving the existing HTML and curriculum rendering model.
2. Update the shared page shells in `index.html`, `course.html`, and `module.html` to use the Atlas font stack, theme color, navigation labels, and concise supporting copy.
3. Adjust the rendered home, course, and module components in `site.js` only where the Atlas information hierarchy requires different wording or grouping.
4. Keep the data visualization atlas unchanged as the reference implementation.
5. Bump the public catalog and Commons semantic versions for the site-wide release.

## Acceptance checks

- The home page still renders 11 course links and 77 module routes.
- Every valid course still renders seven module links.
- Every valid module still renders its topics, submission, course context, and seven-step route.
- Home, representative course, and representative module pages match the Atlas palette, typography, border, spacing, and interaction style.
- The three page types work at 375px, 768px, and 1440px without horizontal overflow.
- Keyboard focus remains visible, reduced-motion preferences are honored, and browser console checks show no site errors.
- The final branch is committed and pushed for review. A Vercel deployment is separate and requires an explicit deploy request.
