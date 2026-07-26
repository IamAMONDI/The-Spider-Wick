# How the Impact Page Works (A Beginner's Guide)

Welcome! If you are new to web development, looking at code can feel like staring at a foreign language. Don't worry! This guide will explain exactly how your new **Impact Page** works using simple, everyday concepts.

We built this page using the three core languages of the web: **HTML**, **CSS**, and **JavaScript**. Think of them like building a house.

---

## 1. HTML (The Structure)
*Think of HTML as the bricks, wooden frames, and walls of a house.*

HTML (HyperText Markup Language) tells the browser what content should exist on the page. In your `impact.html` file, we used tags to build the structure:
*   `<header>` and `<footer>` are the roof and the foundation of your website. They hold the navigation menu and contact links.
*   `<section>` tags are like different rooms in the house. We have one room for the Hero title, one room for the Stats Grid, and another for the Testimonials.
*   `<img>` tags hang pictures on the walls.

---

## 2. CSS (The Interior Design)
*Think of CSS as the paint, the furniture arrangement, and the lighting.*

Without CSS, your HTML would just be a boring black-and-white list of text. In `impact.css`, we added styles to make it look beautiful and modern (the "Open UI" look). We did two very important things to make the page **Responsive** (meaning it looks good on a massive desktop monitor OR a tiny mobile phone screen).

### The Bento Grid (CSS Grid)
We put your statistics inside a CSS Grid. We gave the browser a special instruction: 
`grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));`
This is a magic rule! It tells the browser: *"Try to fit as many columns as you can on the screen, but if the screen is so small that a column shrinks below 300 pixels, just stack them on top of each other instead!"* This is why it automatically turns into a single column on your phone.

### Shrinking Text (Media Queries)
The main title "Changing Lives." is massive—100 pixels tall! That looks great on a laptop, but on a phone, a 100-pixel word would run right off the edge of the screen. 
To fix this, we used a **Media Query**, which looks like this: `@media (max-width: 600px)`.
This rule acts like a light switch. It says: *"If the screen gets smaller than 600 pixels, flip the switch and change the font size to 60 pixels."*

---

## 3. JavaScript (The Electricity & Animation)
*Think of JavaScript as the electricity in your house. It makes things move, turn on, and react to you.*

In `impact.js`, we used JavaScript to make the page feel premium and smooth. Instead of the text and images just sitting there, they gently fade into view as you scroll down.

Here is how the JavaScript works in plain English:
1.  **The Watcher:** We created an `IntersectionObserver`. Think of this as a security camera that watches the screen.
2.  **The Target:** We told the camera to watch everything on the page that has the class `.fade-in`.
3.  **The Trigger:** As you scroll down with your mouse, the camera notices when a target enters the bottom of your screen. 
4.  **The Action:** The moment the camera sees it, it says, "Aha!" and adds a new class called `.visible` to the target. In our CSS, `.visible` tells the element to smoothly slide up and become fully visible.

---

### Summary
That is the entire secret to modern web design! HTML builds the rooms, CSS paints the walls and rearranges the furniture when the house shrinks, and JavaScript turns on the lights when you walk into a new room.
