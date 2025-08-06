<h1>🏥 Hospital Data Cleaning Project</h1>

<p>This project focuses on cleaning and analyzing a real-world hospital dataset, addressing missing values, understanding data quality issues, and uncovering insights related to patient satisfaction, doctor performance, and healthcare trends.</p>

<hr>

<h2>📂 Repository Structure</h2>
<ul>
  <li><strong>Hospital dataset.xlsx</strong> – Original raw dataset (Excel format)</li>
  <li><strong>cleaningH.ipynb</strong> – Jupyter notebook containing full cleaning and analysis process</li>
  <li><strong>imputing_method.py</strong> – Python file for the imputing methods used in the analysis</li>
  <li><strong>README.html</strong> – This README file</li>
</ul>

<hr>

<h2>🧼 Data Cleaning Summary</h2>

<h3>Missing Values Handling:</h3>
<ul>
  <li><strong>Patient Satisfaction Score:</strong> 72.68% missing, imputed using <u>mode per doctor</u></li>
  <li><strong>Department Referral:</strong> 58.60% missing, imputed using <u>grouping on doctor, age, and gender</u> with closest match logic</li>
</ul>

<h3>Duplicates:</h3>
<ul>
  <li><strong>No duplicate records</strong> found in the dataset</li>
</ul>

<h3>Distribution:</h3>
<ul>
  <li><strong>Patient Satisfaction Score</strong> is slightly negatively skewed (Skewness = –0.295)</li>
</ul>

<hr>

<h2>🔍 Key Observations</h2>
<ul>
  <li>Most missing satisfaction scores were in the <strong>General Practice</strong> department</li>
  <li>Potential reasons include <em>staff survey oversight</em> or <em>patient inability to respond</em></li>
  <li><strong>2020</strong> had significantly more patient records than 2019, likely due to a pandemic or major health event</li>
  <li><strong>Dr. Joycelyn Elders</strong> was identified as the most active doctor in terms of patient count</li>
</ul>

<hr>

<h2>📊 Visualizations</h2>
<p>Data visualizations using <strong>Seaborn</strong> and <strong>Matplotlib</strong> include:</p>
<ul>
  <li>Sorted bar chart of patient count per doctor</li>
  <li>Year-over-year patient admission trends</li>
  <li>Distribution plots of satisfaction scores</li>
</ul>

<hr>

<h2>🚀 Getting Started</h2>
<ol>
  <li>Clone the repository</li>
  <li>Open <code>cleaningH.ipynb</code> in Jupyter Notebook</li>
  <li>Ensure required libraries are installed:
    <ul>
      <li><code>pandas</code></li>
      <li><code>matplotlib</code></li>
      <li><code>seaborn</code></li>
      <li><code>numpy</code></li>
      <li><code>scipy</code> (for skewness)</li>
    </ul>
  </li>
</ol>

<hr>

<h2>📌 Goals of the Project</h2>
<ul>
  <li>Practice real-world data cleaning techniques</li>
  <li>Handle severe missingness without distorting distributions</li>
  <li>Use grouped logic for context-aware imputation</li>
  <li>Present insights visually and narratively</li>
</ul>

<hr>

<h2>📄 License</h2>
<p>This project is open-source and available under the <strong>MIT License</strong>.</p>

<hr>

<h2>✍️ Author</h2>
<ul>
  <li>👤 <strong>Ahmed Hambuta</strong></li>
  <li>📧 <em>Data science student passionate about health data and real-world analytics</em></li>
</ul>

<p>Feel free to connect on <a href="https://www.linkedin.com/in/ahmedhambuta" target="_blank">LinkedIn</a></p>
