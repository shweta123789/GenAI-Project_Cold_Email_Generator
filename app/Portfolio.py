"""
class Portfolio:
    def __init__(self, file_path="resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])

"""

import os
import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path=None):
        if file_path is None:
            # Dynamically build path relative to this file's location
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir, "resource", "my_portfolio.csv")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Portfolio CSV not found at: {file_path}")

        print(f"[DEBUG] Loading portfolio CSV from: {file_path}")
        self.data = pd.read_csv(file_path)

        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=row["Techstack"],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get("metadatas", [])
