# Sorting & Searching Algorithm Simulator  
#### 🎥 Video Demo: https://youtu.be/mvFkVRoqD80?si=ItFz_IlAs5hg9B9E

## 📌 Description

This project is a visual simulator for sorting and searching algorithms. The goal is to help students understand how classic algorithms work in a graphical and interactive way, such as:

- **Bubble Sort**
- **Quick Sort**
- **Merge Sort**
- **Insertion Sort**
- **Selection Sort**
- **Binary Search**
- **Linear Search**

The web interface was built using:

- **HTML** for the page structure  
- **CSS** for styling  
- **JavaScript + D3.js** for data visualization and interactivity  
- **Python (Flask)** for data generation and backend integration

---

## ⚙️ How It Works

The user accesses the website, selects the number of elements and the type of algorithm to be simulated. After clicking "generate" and then "sort", a graph is displayed and the selected algorithm begins executing step-by-step, updating the screen in real-time.

---

## 📁 File Structure

- `app.py` – Python code that manages Flask routes, generates random data, and serves HTML files.
- `templates/index.html` – Home page of the website.
- `templates/layout.html` – Page that contains the header and footer.
- `templates/quick.html`, `bubblesort.html`, `merge.html`, `insertion.html`, `selection.html`, `binary.html`, `linear.html` – Pages with the algorithm logic and D3.js visualizations.
- `static/layout.css`, `index.css` – Visual styling for the site.
- `README.md` – This file you are currently reading.

---

## 💡 Why I Chose This Project

I wanted to build something that applied most of what I learned during CS50 and could also help other students better understand the concepts. I also chose this theme because I'm personally interested in the logic behind algorithms, and I really enjoyed the lecture that covered them.

---

## 🧠 Design Decisions

I chose **D3.js** because it is a powerful library for data visualization in the browser. Integrating it with **Flask** allows for dynamic data generation. The goal was to create a simple, intuitive, and functional experience.

---

## 🧗 Main Challenges Faced

The biggest challenge was implementing the algorithms along with the real-time graph interaction. This live updating required managing data changes and delays using `async/await` in JavaScript, which caused some headaches.

Another major challenge was learning the **D3.js** syntax and logic, which was completely new to me. Figuring out how to generate and manipulate dynamic charts based on data took time and lots of trial and error – but it was very rewarding!

---

## 👨‍💻 My Coding Journey

I started by planning how the site should work, focusing on making it user-friendly with interactive buttons and a clean layout.

Then I implemented the backend with Flask, where I created the routes and generated random data based on the number of elements selected by the user. I had more difficulty with recursive algorithms like **Quick Sort** due to the complexity of function calls and state tracking.

Later, I moved on to the visualization. Initially, I tried to integrate the Flask-generated data directly with D3.js, but that caused a lot of issues. As a solution, I decided to implement the algorithms directly in JavaScript within the HTML pages. This made integration and real-time behavior much easier.

---

## 📈 Algorithm Implementation Process

To understand how each algorithm worked, I watched several explanatory and interactive videos. I then implemented the logic in JavaScript and created buttons on the site to make it interactive. When the user enters the desired quantity and clicks "generate", the data vector is displayed and sorted step-by-step.

---

## 📚 What I Learned

- Practical implementation of sorting and searching algorithms  
- Frontend development with HTML, CSS, and JavaScript  
- How to use D3.js for dynamic data visualization  
- Backend and frontend integration with Flask  

---

## 🔧 What Could Be Improved

- Add controls to adjust the visualization speed  
- Allow pausing and resuming the algorithm execution  
- Make the site responsive for mobile devices  
- Include more algorithms to broaden the learning experience  

---

## ✅ Conclusion

I really enjoyed building this project! I'm grateful to the CS50 team for the amazing content and all the motivation. This project helped me apply everything I’ve learned and I hope it encourages other students to explore algorithms and computer science further.

**Thank you!**
