# Part 1: Big Data

Big Data is about collecting, storing, cleaning, and understanding large amounts of information. The challenge is not simply having lots of data. It is making sure that the information is useful, reliable, and manageable.

Imagine the Library of Alexandria, one of the most famous libraries of the ancient world. It aimed to gather knowledge from across the known world. Now imagine that, instead of scrolls, it collected every book, letter, trade record, map, and conversation produced by millions of people every day. It would need an extraordinary system to organize and preserve that knowledge.

That is the kind of challenge Big Data helps us understand. The library is our running example: from collecting information to turning it into knowledge.

## 1.1 Introduction to Big Data

### What is data?

**Data** is information recorded in a form that can be stored, read, or processed.

A number written on a piece of paper is data. So is a word in a book, a picture of a building, or a record showing when a scroll arrived at a library.

For example, a record might say:

- Title: *History of Egypt*
- Arrival year: 250 BCE
- Language: Greek
- Number of pages: 120

Each item provides a small piece of information. Together, the items describe one object in the library.

**Information** is data organized in a way that helps us understand something. If we count all the Greek-language books in a collection, the resulting number tells us something about the collection's contents.

### What is Big Data?

**Big Data** refers to datasets—organized collections of data—that are too large, too fast-changing, or too complicated to handle efficiently using traditional data-processing methods alone.

The important word is *efficiently*. A collection does not need to fill an entire building to create a Big Data problem. Even a smaller dataset can be difficult if it arrives extremely quickly or contains many different kinds of information.

Imagine asking a librarian to count every scroll in Alexandria by hand. Manageable? Perhaps. Now ask the librarian to count them again every second while new scrolls arrive, old records change, and several languages and formats are mixed together.

At some point, the librarian deserves a computer.

Computers help us process information much faster, but Big Data requires more than a powerful machine. We also need suitable storage, reliable methods, and ways to find meaningful patterns.

### Types of data

Data comes in different forms. Knowing which form we have helps us decide how to store and process it.

**1. Structured data**

Structured data follows a clear format, usually with fields arranged in rows and columns. Each field has a defined purpose.

Example: a library catalogue with columns for title, author, language, and arrival date. A computer can search these fields easily because every record follows the same rules.

**2. Semi-structured data**

Semi-structured data has some organization but does not fit neatly into a fixed table. It may use labels, tags, or other markers to identify information.

Example: a digital record containing a scroll's title, language, and date as named fields, alongside optional notes about its condition. Not every record needs to contain every field.

**3. Unstructured data**

Unstructured data does not follow one fixed format that a computer can directly treat as a standard table.

Examples include full book texts, scanned manuscripts, photographs, audio recordings, and handwritten letters. These may contain valuable information, but extracting it can be difficult.

The distinction is about organization, not importance. A carefully organized catalogue can be structured data, while a priceless manuscript scan can be unstructured data. Both matter.

A real collection may contain all three types. The more varied the information becomes, the more carefully we must plan how to process it.

## 1.2 Big Data Collection and Storage

Before we can understand a collection, we must first obtain the data and keep it somewhere safe.

**Data collection** is the process of gathering information from sources. A source is simply where the information comes from, such as a form, a book catalogue, a sensor, a website, or a digital archive.

**Data storage** means keeping that information so it can be accessed and used later.

For the Library of Alexandria, collection might mean receiving scrolls from different regions. Storage might mean recording their locations, preserving copies, and making sure they do not disappear into a pile labelled “Important Things — Probably.”

Collection and storage are connected, but they have different problems. Collecting data can be difficult because of how quickly it arrives and how varied it is. Storing it can be difficult because of how much space it needs, how many formats must be maintained, and how safely it must be protected.

### Collection problems: speed and variety

#### Velocity: how quickly data arrives

**Velocity** means the speed at which data is generated, collected, and needs to be processed.

Imagine that Alexandria receives ten new scrolls a day. A librarian can probably register them without much trouble. Now imagine that thousands of new digital records arrive every second. Waiting until the end of the year to organize them would create a rather impressive administrative disaster.

Why is velocity a problem?

- New data may arrive faster than a system can process it.
- Delays can make information outdated before it is used.
- If incoming data accumulates, the system may run out of temporary space or fall behind.

How do we deal with it?

**Hardware** is the physical equipment used to operate a computer system, including processors, memory, storage drives, and network equipment. Faster processors can handle more operations, while sufficient memory allows the system to work on incoming data without constantly waiting for slower storage.

**Software** is the set of programs and instructions that tell the hardware what to do. Data-processing software can organize incoming records automatically, while streaming systems can process data continuously as it arrives. *Streaming* means handling data piece by piece instead of waiting for one enormous batch.

For example, a digital library could register each new manuscript record as soon as it arrives. It would not need to wait for the librarian to finish lunch, return from lunch, and discover that three thousand records are waiting.

The best solution depends on how quickly the data arrives and how quickly the result is needed. Some records can wait for a scheduled process; others must be handled almost immediately.

#### Variety: data comes in different forms

**Variety** means the differences in the formats, structures, and sources of data.

Alexandria might receive a Greek poem, an Egyptian trade record, a map, and a spoken account recorded as audio. These are all valuable, but they cannot all be processed in exactly the same way.

Why is variety a problem?

- Different formats require different methods of reading and processing.
- Information from different sources may use different languages, names, dates, or measurement systems.
- The same concept may be represented differently in different records.

Suppose one record identifies a writer by their full name, another uses a shortened name, and a third uses a different spelling. A computer might treat these as three different people even when they refer to the same person.

How do we deal with it?

Software can help identify formats, convert compatible data into shared formats, and extract useful information from documents. **Standardization** means using consistent rules so records can be compared. For example, storing dates in a common format makes it easier to sort records chronologically.

**Metadata** is data that describes other data. A photograph of an ancient manuscript might have metadata describing its language, estimated date, file format, and source. This description makes the photograph easier to find and manage.

Hardware also matters. Different equipment may be needed to scan documents, record audio, or store large image files. However, buying more equipment does not automatically solve a problem caused by inconsistent records. Sometimes the real issue is the way the information has been organized.

The goal is not to force every kind of information into one identical shape. It is to make different kinds of information understandable and usable together where appropriate.

### Storage problems: size, variety, and protection

#### Volume: how much data must be stored?

**Volume** refers to the amount of data a system must manage.

A single text document may occupy very little digital space. A high-quality image, a long audio recording, or a large collection of scanned books can require much more. Multiply that by millions of files, and storage becomes a serious planning problem.

Why is volume a problem?

- Storage devices have limited capacity.
- Large collections take longer to transfer, copy, search, and back up.
- Keeping several copies for safety requires additional space.
- Expanding a system can increase equipment, electricity, and maintenance costs.

Digital storage capacity is commonly measured in bytes. A byte is a unit of digital information, and larger units include kilobytes (KB), megabytes (MB), gigabytes (GB), and terabytes (TB). Each unit represents a larger amount of data than the one before it.

Imagine digitizing the entire Library of Alexandria's collection. Storing a few sample pages would be easy. Storing high-quality images of every page, several copies of each file, and additional catalogue records would require far more capacity.

How do we deal with it?

**1. Choose suitable storage.** Solid-state drives and hard disk drives are physical storage devices. Larger collections may use many drives or dedicated storage systems rather than a single computer.

**2. Compress files.** Compression reduces the amount of space a file occupies. Some compression methods preserve all original information; others discard some information to achieve greater size reductions. The appropriate method depends on the data. Losing details from an important manuscript image may not be an acceptable bargain.

**3. Remove unnecessary duplication carefully.** Duplicate files consume space, but files should not be deleted merely because their names look similar. Two manuscripts may contain different versions of the same text. A system must distinguish genuine duplicates from meaningful differences.

**4. Expand storage when needed.** Storage can be increased by adding drives or using distributed storage, where data is kept across multiple connected machines. This can provide more capacity and allow work to be spread across several systems.

**5. Plan backups.** A backup is an additional copy kept so information can be recovered if the original is lost or damaged. Backups must be maintained and tested; a file labelled “backup” is not very reassuring if nobody can restore it.

#### Variety: storing different kinds of data

Variety causes storage problems as well as collection problems. The issue is not only how to read different data formats, but also how to organize and retrieve them efficiently.

A catalogue of book titles fits naturally into a table. Full texts, photographs, maps, and audio recordings need different ways of being stored and searched. A single storage method may not be ideal for every type.

Why is this a problem?

- Some formats require specialized tools to access.
- Files may have different size, performance, and preservation requirements.
- Connecting a file to its description can be difficult if their records are not managed consistently.

How do we deal with it?

**Databases** are organized systems for storing and retrieving information. A relational database stores information in related tables, making it suitable for structured records such as catalogue entries. Other database systems are designed to handle more flexible data structures.

**Object storage** keeps individual items, such as image files or scanned documents, together with identifying information. It is useful when a collection contains many large files that do not fit neatly into rows and columns.

A practical library system could keep titles, authors, and dates in a database while storing manuscript images separately. The catalogue would contain references to the corresponding images, allowing a user to find a manuscript and then open its digital copy.

The key is to choose storage based on the data and how people need to use it. One universal solution sounds convenient until it becomes the digital equivalent of trying to store every scroll, map, and statue in the same filing cabinet.

#### Value: protecting useful information

Having data is not enough. It must also be reliable, accessible to the right people, and protected from misuse.

**Value** here concerns the usefulness of stored data and the ability to preserve that usefulness. Security is a central part of this because stolen, altered, or lost information can become unreliable or unavailable.

Why is security a problem?

- Unauthorized people may access confidential information.
- Someone may alter records, making them inaccurate.
- Hardware failures, accidents, or malicious attacks may destroy data.
- Information may become unreadable when software or file formats become obsolete.

Imagine a record claiming that a rare manuscript is stored in Room A when somebody has secretly changed it to Room B. The data still exists, but its reliability has been damaged. The librarian now has a treasure hunt with no map.

How do we deal with it?

- **Access control:** restrict who can read or change particular information.
- **Authentication:** verify that a user is who they claim to be, for example through a password or another identity check.
- **Encryption:** transform information into a protected form that can be read only with the appropriate key.
- **Backups and recovery:** keep usable copies and practice restoring them.
- **Integrity checks:** use methods such as checksums, which calculate a value from a file so later changes or corruption can be detected.
- **Maintenance:** update software, monitor systems, and preserve files in formats that remain accessible.

Security also requires sensible decisions about people. A librarian may need to view a manuscript catalogue without having permission to alter every record. Access should match the person's responsibilities.

The objective is not to build a system so secure that nobody can use it. A library locked so tightly that even the librarian cannot enter is technically well protected—and practically useless.

## 1.3 Data Filtration

A large collection of data is not automatically a good collection of data. Some records are incomplete, duplicated, irrelevant, or simply wrong.

**Data filtration** is the process of selecting data that meets particular requirements and excluding data that does not. It helps a system focus on the information needed for a task.

Imagine asking the Library of Alexandria to count every manuscript written in Greek. The collection contains Greek manuscripts, Egyptian records, duplicate catalogue entries, damaged scrolls, and shopping lists accidentally filed under “Philosophy.”

Counting everything would not answer the question. We need to filter first.

### Why filter data?

There are four main reasons.

1. **Remove irrelevant information.** If we are studying Greek manuscripts, records about unrelated objects may not be needed.
2. **Identify duplicates.** Repeated records can distort counts and waste storage.
3. **Handle errors.** Missing dates, impossible values, and inconsistent labels can reduce reliability.
4. **Reduce processing costs.** Working with fewer, more relevant records can save time and computing resources.

However, filtering is not the same as deleting everything unusual. A damaged manuscript might be exactly the item a historian wants to study. A missing date might be a genuine historical uncertainty rather than a mistake.

The rules must match the purpose of the analysis.

### Hardware for data filtration

Hardware can help filtration run faster, especially when the collection is large.

- **Processors (CPUs):** execute instructions that check records against rules.
- **Memory (RAM):** holds data temporarily while the system works on it.
- **Storage drives:** provide access to the files being checked.
- **Specialized processors:** GPUs, or graphics processing units, can accelerate certain highly parallel calculations—calculations that can be split into many similar operations.

For example, a system checking millions of catalogue records for missing titles may use multiple processor cores to examine records simultaneously.

More powerful hardware can help, but it cannot decide whether a manuscript is historically important. That requires appropriate rules and, in some cases, human judgment.

### Software for data filtration

Software defines what to keep, what to flag for review, and what to exclude.

Common methods include:

- **Rule-based filtering:** keep records that meet specified conditions, such as having a valid date or a particular language label.
- **Deduplication:** identify and handle duplicate records.
- **Validation:** check whether data follows expected rules, such as whether a year falls within a plausible range.
- **Text processing:** search documents for words, phrases, or patterns relevant to a task.

A simple filtering rule might be:

> Keep every catalogue record whose language is Greek and whose title is not missing.

A more advanced system could use optical character recognition (OCR), a technology that converts text in images into machine-readable text. OCR could help extract words from scanned manuscript pages, although ancient handwriting and damaged surfaces can produce mistakes.

Some systems also use machine learning, a method in which computers learn patterns from examples. A trained model might help identify likely duplicate records or classify documents. Its predictions should still be checked when errors matter.

**Important distinction:** filtration does not guarantee that the remaining data is correct. It only applies the chosen criteria. Poor rules can remove useful information while allowing bad records to remain.

## 1.4 Big Data Analysis

After collecting, storing, and filtering data, we can begin asking questions about it.

**Data analysis** is the process of examining data to discover patterns, compare results, test ideas, and answer questions.

For our library, possible questions include:

- Which languages appear most frequently in the catalogue?
- How did the number of recorded manuscripts change over time?
- Which regions contributed the most manuscripts?
- Are certain subjects commonly found together?

Instead of reading every scroll individually, we can use analysis to examine the collection as a whole.

### Why analyse data?

Data analysis helps turn raw records into evidence that people can use to make decisions or understand a situation.

For example, counting manuscripts by language could reveal which languages are most represented in the catalogue. Comparing arrival dates might reveal changes in the collection over time.

But a result must be interpreted carefully. If Greek manuscripts make up 70% of the surviving catalogue records, that does not automatically mean 70% of all manuscripts originally held by the library were Greek. Some records may be missing, and some manuscripts may never have been catalogued.

Analysis can reveal patterns. It cannot magically repair missing historical evidence.

### How does data analysis work?

A typical analysis follows a sequence.

1. **Ask a question.** What do we want to find out?
2. **Prepare the data.** Check, filter, and organize relevant records.
3. **Apply an analysis method.** Count, compare, calculate, or search for patterns.
4. **Interpret the result.** Explain what the result means and what it cannot tell us.

The question comes first because it determines what data we need and which method is appropriate. Without a clear question, we risk performing impressive calculations that answer absolutely nothing.

### Specific data analysis methods

#### 1. Descriptive analysis

**Descriptive analysis** summarizes what the available data contains.

Common techniques include counting, calculating percentages, finding averages, and grouping records into categories.

Suppose a hypothetical catalogue contains 1,000 records, of which 600 are labelled Greek.

The proportion is:

\[
\frac{600}{1000}\times100=60\%
\]

We can report that 60% of the catalogue records are labelled Greek. This is a useful summary, but it does not establish the language distribution of the entire historical collection.

#### 2. Comparative analysis

Comparative analysis examines similarities and differences between groups.

For example, we could compare the number of manuscripts recorded from two historical periods. If the first period has 200 records and the second has 350, the second has 150 more recorded manuscripts.

We would still need to investigate whether this difference reflects actual growth, better record-keeping, or missing information from the earlier period.

#### 3. Trend analysis

**Trend analysis** examines how a measurement changes over time.

Suppose a fictional digital archive records the following number of newly catalogued manuscripts:

| Year | New records |
|---|---:|
| Year 1 | 100 |
| Year 2 | 150 |
| Year 3 | 210 |
| Year 4 | 280 |

The numbers rise each year. A line chart would make that pattern easier to see.

However, the trend describes new catalogue records, not necessarily new manuscripts entering the historical library. The difference matters because analysis must follow what the data actually measures.

#### 4. Predictive analysis

**Predictive analysis** uses existing data to estimate what may happen in the future.

A statistical model, which is a mathematical description of a pattern in data, might estimate how many records a digital archive will need to store next year.

A prediction is not a promise. Unexpected changes, incomplete data, and incorrect assumptions can make predictions inaccurate.

More advanced analysis may use machine learning to identify complex patterns in large datasets. For example, a model trained on labelled manuscript images could estimate the likely language of a new image. Its performance would depend on the quality and representativeness of its training examples.

### Hardware for data analysis

The equipment needed depends on the size of the dataset and the complexity of the calculations.

- **CPU:** a central processing unit that handles general instructions and calculations.
- **RAM:** temporary working memory used while processing data.
- **Storage:** keeps the source records and analysis results.
- **GPU:** a processor suited to many parallel calculations, often useful for large numerical workloads and machine learning.
- **Multiple connected computers:** can divide suitable tasks across machines when one computer is insufficient.

For a small catalogue, an ordinary laptop may be enough. For billions of records or computationally demanding models, a larger system may be needed.

Buying the most powerful computer available is not automatically the best choice. If the task is simply counting 100 records, a supercomputer is a very expensive way to avoid using a spreadsheet.

### Software for data analysis

Software provides the tools needed to organize data, perform calculations, and build models.

| Tool or type | Main purpose |
|---|---|
| Spreadsheets | Organize records, calculate totals, and create simple charts. |
| SQL | A language used to retrieve and analyze data stored in relational databases. |
| Python and R | Programming languages commonly used for data analysis, statistics, and visualization. |
| Distributed processing tools | Divide suitable workloads across multiple computers. |
| Machine learning libraries | Build and evaluate models that learn patterns from data. |

The right choice depends on the task. A spreadsheet may be sufficient for a small catalogue, while a large collection may require a database and distributed processing.

### Data interpretation: making results understandable to humans

Calculations are useful, but people need to understand what those calculations mean.

**Data interpretation** is the process of explaining the meaning, importance, and limitations of analytical results in context.

Suppose an analysis produces the result “60% Greek.” This number is short and precise, but a reader needs to know what it refers to.

Does it mean 60% of all manuscripts? Sixty percent of surviving records? Sixty percent of the records that passed filtration? Without that context, the number is easy to misunderstand.

Several techniques help make results easier to understand.

**Tables** organize exact values so readers can compare them.

**Charts** represent information visually. A bar chart can compare categories, while a line chart can show changes over time.

**Plain-language explanations** describe the result without requiring readers to understand the underlying code or calculations.

**Context and limitations** explain how the data was collected, what the analysis measured, and what conclusions are justified.

Consider these two explanations:

- Technical: “Greek-language records constitute 0.60 of the retained observations.”
- Plain language: “Six out of every ten records remaining after filtering are labelled Greek.”

The second explanation is easier to understand. It also preserves the important qualification that the result concerns records remaining after filtering.

Good interpretation avoids exaggeration. A relationship between two measurements does not automatically mean one caused the other. A chart can display a pattern, but it cannot by itself explain why that pattern exists.

Ultimately, the purpose of analysis is not to produce the largest number of charts or the most intimidating equation. It is to help people understand what the available evidence supports.

---

## Chapter summary

Big Data involves managing information that becomes difficult to handle using traditional methods alone. Its challenges begin when data is collected and stored, continue when irrelevant or unreliable records must be filtered, and become especially important when analysis is used to draw conclusions.

The Library of Alexandria illustrates the whole process: gather records, organize and protect them, select relevant information, examine patterns, and explain the findings clearly.

The central principle is simple: **data becomes useful when it is managed carefully and interpreted responsibly.**
