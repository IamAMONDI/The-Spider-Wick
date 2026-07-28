# MindWell

A youth-led mental health awareness website, built as part of our TechCrush capstone project.

## About

MindWell is a youth-led mental health initiative built by a group of students at ALCHE. It started as part of our Grand Challenges and Grand Opportunities (GCGO) Healthcare track, turning a real problem we saw among our peers into something we could build and act on.

Many young people carry more than they show, pressure from school, family expectations, social media, and an uncertain future often go unspoken, because talking about mental health still feels difficult for many youth. MindWell exists to change that, one honest conversation at a time.

## Features

- Awareness content written in clear, relatable language for youth (not clinical jargon)
- Safe spaces for connection, online and in person
- Simple next steps for finding support, from peer conversation to professional help
- Responsive design across mobile, tablet, and desktop

## Tech Stack

- HTML5
- CSS3 (custom design system with CSS variables)
- JavaScript

## Design System

Shared design tokens are defined in `variables.css` so styling stays consistent across all pages and contributors:

```css
:root {
  --color-primary: #2D5A4A;
  --color-accent: #c9e20e;
  --color-text-light: beige;
  --font-main: 'Quicksand', sans-serif;

  --text-h1: 40px;
  --text-h3: 27px;
  --text-body: 22px;
  --text-button: 18px;
  --text-h2: 20px;
}
```

## Project Structure

```
mindwell/
├── index.html
├── about.html
├── impact.html
├── contact.html
├── assets/
│   └── (images, icons)
├── css/
│   ├── variables.css
│   ├── style.css
│   └── (page-specific stylesheets)
└── js/
    └── (scripts)
```

## Team

Built collaboratively by a team of TechCrush frontend development scholars.

## Getting Started

1. Clone the repository
```bash
git clone <repo-url>
```
2. Open `index.html` in your browser, or use a live server extension for local development.

## Contributing

- Create a feature branch before making changes
- Follow the shared `variables.css` design tokens for consistent styling
- Open a pull request for review before merging into `main`

## Status

In progress — actively being built as part of the TechCrush program.