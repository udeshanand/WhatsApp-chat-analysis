WhatsApp Chat Analyzer
    <p>A <strong>Streamlit-based data analysis tool</strong> that helps you analyze WhatsApp chat exports. It provides insights into user activity, word usage, media sharing, and more — all visualized interactively.</p>
    <h2> Features</h2>
    <ul>
      <li>Upload and parse WhatsApp chat <code>.txt</code> file (exported from WhatsApp)</li>
      <li>View total messages, words, media, and shared links</li>
      <li>Generate a <strong>WordCloud</strong> for most frequently used words</li>
      <li>See <strong>most common words</strong> with bar charts</li>
      <li>Identify <strong>most active users</strong> in group chats</li>
      <li>Interactive, clean <strong>Streamlit UI</strong></li>
    </ul>
    <h2> Tech Stack</h2>
    <ul>
      <li>Python 3.7</li>
      <li>Streamlit</li>
      <li>Matplotlib</li>
      <li>WordCloud</li>
      <li>Pandas / NumPy</li>
      <li>Custom helper modules (<code>preprocessor.py</code>, <code>functions.py</code>)</li>
    </ul>
    <h2>Project Structure</h2>
    <pre><code>whatsapp-chat-analyzer/
├── app.py                # main Streamlit app
├── preprocessor.py       # parses raw chat data
├── functions.py          # helper functions for analysis
├── requirements.txt      # dependencies
└── sample_chat.txt       # example WhatsApp export file
</code></pre>
    <h2>Installation & Setup</h2>
    <ol>
      <li><strong>Clone the repository</strong>
        <pre><code>git clone https://github.com/udeshanand/WhatsApp-chat-analysis.git
cd whatsapp-chat-analyzer</code></pre>
      </li>
      <li><strong>Create a virtual environment (optional)</strong>
        <pre><code>python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows</code></pre>
      </li>
      <li><strong>Install dependencies</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
      </li>
      <li><strong>Run the Streamlit app</strong>
        <pre><code>streamlit run app.py</code></pre>
      </li>
    </ol>
    <h2> How It Works</h2>
    <h3>1. File Upload</h3>
    <p>Upload a WhatsApp chat text file exported from your phone. The app parses and cleans it.</p>
    <h3>2. Data Preprocessing</h3>
    <p>The file is processed by <code>preprocessor.preprocess(data)</code> to extract users, timestamps, and messages.</p>
    <h3>3. Analysis Includes:</h3>
    <table>
      <tr><th>Metric</th><th>Description</th></tr>
      <tr><td>Total Messages</td><td>Count of all messages sent</td></tr>
      <tr><td>Total Words</td><td>Count of all words used</td></tr>
      <tr><td>Media Shared</td><td>Number of media messages (<code>&lt;Media omitted&gt;</code>)</td></tr>
      <tr><td>Links Shared</td><td>Count of hyperlinks shared</td></tr>
      <tr><td>Most Active Users</td><td>Top users by message count</td></tr>
      <tr><td>WordCloud</td><td>Visualization of most common words</td></tr>
      <tr><td>Most Common Words</td><td>Ranked list with counts</td></tr>
    </table>
    <h2> Example Chat File Format</h2>
    <pre><code>12/05/2023, 9:35 pm - John: Hey, how are you?
12/05/2023, 9:36 pm - Alice: I'm good! You?
12/05/2023, 9:37 pm - John: Doing well, thanks!</code></pre>
    <h2>Key Functions</h2>
    <table>
      <tr><th>Function</th><th>Purpose</th></tr>
      <tr><td><code>preprocessor.preprocess(data)</code></td><td>Converts WhatsApp chat into structured DataFrame</td></tr>
      <tr><td><code>functions.total_message(user, df)</code></td><td>Returns total number of messages</td></tr>
      <tr><td><code>functions.total_words(user, df)</code></td><td>Counts all words sent by a user</td></tr>
      <tr><td><code>functions.total_media_msg(user, df)</code></td><td>Counts total media messages</td></tr>
      <tr><td><code>functions.total_links(user, df)</code></td><td>Counts total shared links</td></tr>
      <tr><td><code>functions.most_active_user(df)</code></td><td>Finds most active users</td></tr>
      <tr><td><code>functions.percent_peruser(df)</code></td><td>Calculates user contribution percentage</td></tr>
      <tr><td><code>functions.create_wordcloud(user, df)</code></td><td>Generates wordcloud visualization</td></tr>
      <tr><td><code>functions.most_common_words(user, df)</code></td><td>Lists top words with counts</td></tr>
    </table>
    <h2> Author</h2>
    <strong>Udesh kumar</strong><br>
       
    
