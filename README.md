# ragbotllamaindexblazor-proje

## Overview

This project, `ragbotllamaindexblazor-proje`, is a sophisticated application that leverages the power of Retrieval Augmented Generation (RAG) to enable users to interact with PDF documents through natural language queries. It comprises a Blazor WebAssembly frontend for user interaction, a Python-based PDF processing service, and a Python-based query service.

The **PDF Assistant Frontend** (built with Blazor WebAssembly) provides a user-friendly interface for uploading PDF files and posing questions about their content. It handles file uploads and displays responses from the backend services.

The **PDF Service** (a Flask application) is responsible for receiving uploaded PDF files, securely storing them, and extracting their text content. It then passes this extracted text to the query service for indexing.

The **Query Service** (another Flask application) utilizes `llama_index` to create a vector store index from the provided document texts. This index allows for efficient semantic searching and retrieval of relevant information. When a user asks a question, this service queries the index and generates a concise answer based on the retrieved context.

This architecture allows for a scalable and robust solution for document-based question answering.

## Features

*   **PDF Upload and Processing:** Securely upload PDF documents for analysis.
*   **Text Extraction:** Extracts text content from uploaded PDF files.
*   **RAG Implementation:** Leverages `llama_index` for efficient document indexing and retrieval.
*   **Natural Language Querying:** Ask questions in plain English and receive contextually relevant answers.
*   **Blazor WebAssembly Frontend:** A modern, client-side web interface for seamless user experience.
*   **Microservice Architecture:** Separated PDF processing and query services for modularity and scalability.
*   **Error Handling:** Robust error reporting for upload and query operations.

## Project Structure

```
.
├── README.md
├── frontend/
│   └── PdfAssistantFrontend/
│       ├── App.razor
│       ├── PdfAssistantFrontend.csproj
│       ├── Program.cs
│       ├── _Imports.razor
│       ├── Layout/
│       │   ├── MainLayout.razor
│       │   ├── MainLayout.razor.css
│       │   ├── NavMenu.razor
│       │   └── NavMenu.razor.css
│       └── Pages/
│           ├── Counter.razor
│           ├── PdfAssistant.razor
│           └── Weather.razor
│       └── Properties/
│           └── launchSettings.json
├── pdfservice/
│   └── pdfservice.py
└── queryservice/
    └── query_service.py
```

## Getting Started

To run this project, you will need to have Python and .NET SDK installed.

1.  **Start the PDF Service:**
    Navigate to the `pdfservice` directory and run the following command:
    ```bash
    python pdfservice.py
    ```
    This service will run on `http://localhost:5001`.

2.  **Start the Query Service:**
    Navigate to the `queryservice` directory and run the following command:
    ```bash
    python query_service.py
    ```
    This service will run on `http://localhost:5002`.

3.  **Build and Run the Blazor Frontend:**
    Navigate to the `frontend/PdfAssistantFrontend` directory and run the following command:
    ```bash
    dotnet run
    ```
    The application will launch in your browser, typically at `http://localhost:5143`.

## License

This project is licensed under the GNU GPL v3.0 license. See the [LICENSE](LICENSE) file for more details.