# Data Transformation and Manipulation

This directory contains courses and exercises focused on data transformation and manipulation techniques essential for machine learning and artificial intelligence. You will find detailed explanations on various data processing methods, practical implementations, and use cases in ML/AI.

## Chapter 1: Introduction to Data Manipulation and Transformation

1. [Importance of Data Manipulation](./Chapter1_Introduction/01_Introductions.md)
   - Understanding and exploring data
   - Preparing data for analysis
   - Practical applications in various fields (finance, healthcare, marketing)

2. [Overview of Python Libraries](./Chapter1_Introduction/01_Introductions.md)
   - Pandas: handling tabular data, DataFrame, Series
   - NumPy: efficient numerical computations, multidimensional arrays
   - Scipy: advanced mathematical functions, statistics, optimization

3. [Data File Formats](./Chapter1_Introduction/01_Introductions.md)
   - CSV: reading, writing, manipulation
   - Other common formats (Excel, JSON, SQL)

## Chapter 2: Data Preparation and Cleaning

1. Identifying and Handling Missing Data
   - Detecting missing data (isnull, notnull)
   - Techniques for handling (imputation, deletion)
   - Advanced imputation methods (KNN, MICE)

2. Handling Duplicates
   - Detecting and removing duplicates (drop_duplicates)

3. Selecting and Grouping Data
   - Selecting variables and individuals (loc, iloc)
   - Grouping variables (groupby, pivot_table)
   - Conditional filtering (query)

4. Data Transformation and Normalization
   - Normalization and standardization (MinMaxScaler, StandardScaler, RobustScaler)
   - Encoding categorical variables (One-Hot Encoding, Label Encoding)
   - Handling dates and times (datetime)

## Chapter 3: Statistical Analysis and Outlier Management

1. Objectives of Statistical Analysis
   - Predicting behavior of unobserved individuals
   - Explaining variability with other variables
   - Distinguishing groups of individuals

2. Detecting and Managing Outliers
   - Detecting univariate and multivariate outliers
   - Detection methods (hypothesis testing, Z-score, IQR)
   - Impact of outliers on analyses
   - Treating outliers (Winsorization, log transformation)

3. Distributions and Validation
   - Normal (Gaussian) distribution and other common distributions (exponential, uniform)
   - Validating distributions (Shapiro-Wilk test, Kolmogorov-Smirnov, Anderson-Darling)

4. Transformations for Normality
   - PowerTransformer "yeo-johnson"
   - Cox-box
   - Log
   - Sqrt**1/3

## Chapter 4: Data Anonymization

1. Types of Data to Anonymize
   - Personal data (name, address)
   - Sensitive data (age, biometric data)

2. Anonymization Techniques
   - Removing information
   - Transforming information (grouping, less precision, generating random individuals)

3. Anonymization Algorithms
   - K-anonymity via bucketization and generalization
   - Random algorithms (combining real and generated data)

4. Hashing Names with hashlib
   - Hashing techniques (MD5, SHA-256)

## Chapter 5: Natural Language Processing (NLP)

1. Importance and Applications of NLP
   - Sentiment analysis
   - Text classification
   - Information extraction

2. Preparing Unstructured Text Data
   - Corpus cleaning (removing numbers, spelling correction, case harmonization)
   - Removing punctuation, stopwords, numbers, URLs
   - Converting to lowercase

3. Text Preprocessing Techniques
   - Tokenization
   - Stemming
   - Lemmatization
   - Named entity recognition (NER)

4. Text Vectorization
   - TF-IDF method
   - Other vectorization methods (Bag of Words, Word Embeddings: Word2Vec, GloVe)

## Chapter 6: Audio Data Processing

1. Introduction and Audio File Formats
   - MP3, WAV, FLAC formats
   - Differences between compressed and uncompressed formats

2. Audio Data Analysis
   - Time-domain vs frequency-domain analysis
   - Spectrum and Cepstrum
   - Fourier Transform (FFT) analysis

3. Extracting Audio Features
   - Zero Crossing Rate (ZCR)
   - Spectral Centroid
   - Mel-Frequency Cepstral Coefficients (MFCC)
   - Spectral Rolloff
   - Other features (Chroma Features, Tonnetz)

## Chapter 7: Image Data Processing

1. Introduction and Image File Formats
   - JPEG, PNG, TIFF formats
   - Differences between compressed and uncompressed formats

2. Image Preprocessing
   - Resizing and cropping
   - Converting to grayscale
   - Pixel normalization

3. Image Transformation Techniques
   - Data augmentation (rotation, translation, flip, zoom)
   - Filtering and denoising (smoothing filters, edge detection)

4. Extracting Image Features
   - Histogram of Oriented Gradients (HOG)
   - Keypoint descriptors (SIFT, SURF)
   - Convolutional Neural Networks (CNN)

## Chapter 8: Advanced Data Transformation Techniques

1. Feature Engineering
   - Creating new variables
   - Transforming existing variables

2. Dimensionality Reduction
   - Principal Component Analysis (PCA)
   - Linear Discriminant Analysis (LDA)
   - t-Distributed Stochastic Neighbor Embedding (t-SNE)

---

Thank you for visiting this directory and reviewing the educational material. For any questions or suggestions, you can contact me at [ryan.naidji@gmail.com](mailto:ryan.naidji@gmail.com).
