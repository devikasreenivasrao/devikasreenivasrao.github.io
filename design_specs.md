# Portfolio Website Design Specifications

## Global Theme: Dark Academic Aesthetic
- **Background Color**: `#0B0E14` (Deep obsidian/navy blend)
- **Text Color**: `#E2E8F0` (Off-white/slate for primary readability)
- **Muted Text**: `#94A3B8` (For secondary text and labels)
- **Accent Color**: `#6A998C` (Muted sage green)
- **Typography**: 
  - Display: `Supreme`, `sans-serif`
  - Body: `Supreme`, `sans-serif`
  - Code/Mono: `Fira Code`, `monospace`

## Typography Guidelines
- **Section Labels**: Uppercase, 0.85rem, heavily tracked (`letter-spacing: 3px`), colored with the accent color.
- **Section Headings**: Bold (700 weight), large dynamic sizing (`clamp(2.2rem, 5vw, 4rem)`).
- **Paragraphs**: 1.1rem, 1.6 line height for optimal readability.

## Layout Components

### Work / Projects Section
- **Grid Layout (`.work-grid`)**: A 2-column split layout.
  - **Left Column (`.featured-column`)**: Contains the primary/featured project cards.
  - **Right Column (`.projects-container`)**: A masonry/grid structure for secondary projects.
- **Project Cards (`.work-card`)**: 
  - Background: Solid dark (`#11151C`)
  - Border: Subtle translucent white border (`rgba(255, 255, 255, 0.05)`)
  - Interactivity: Subtle upward translation (`translateY(-5px)`) and border highlight (`rgba(255, 255, 255, 0.15)`) on hover.
  - Structure: Index number (e.g., 01), Badge (e.g., Deployed), Title, Description, and Skill Tags.

### Certifications Section
- **Hybrid Layout (`.cert-hybrid-layout`)**: A flex container (`gap: 3.5rem`, `max-width: 1000px`, `margin: 0 auto;` for constrained centering).
- **Statistic Box (`.cert-stat-box`)**: 
  - Fixed width (240px).
  - Background: Slightly lighter than the page background (`var(--color-bg)`).
  - Content: Large display number (`5.5rem`), followed by an uppercase tracked label.
- **List (`.cert-list`)**: 
  - Clean vertical list separated by subtle bottom borders.
  - Each item includes a small accent-colored dot (`.cert-dot`).
  - The Certification Name is left-aligned, and the Provider is right-aligned (`margin-left: auto;`).

### Contact Section
- **Layout (`.contact-section`)**:
  - Horizontal side-by-side layout using flex `space-between`.
  - Text on the left, social icons on the right.
  - Compact height (`min-height: auto`) with top and bottom padding.
- **Text Elements**: Large, bold heading ("Let's build something secure.") followed by a constrained paragraph (`max-width: 600px`).
- **Social Links (`.social-links`)**: 
  - Horizontally aligned icon buttons in the center of the screen below the text.
  - Circular buttons (`44px x 44px`, `border-radius: 50%`) with standard border.
  - Hover effects: Accent color border and icon fill, with slight upward translation.

## Responsiveness (`@media` rules)
- **`max-width: 1024px` / `900px`**: Transitions complex 2-column grid structures (like the work grid) into stacked single columns (`grid-template-columns: 1fr`).
- **`max-width: 768px` / `640px`**: Reduces padding, adjusts the Certifications hybrid layout from a row to a column, and ensures fonts scale gracefully using `clamp()`.
