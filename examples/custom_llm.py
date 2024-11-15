"""Example usage of GraphRAG with custom LLM and Embedding services compatible with the OpenAI API."""
from typing import List

from dotenv import load_dotenv

from fast_graphrag import GraphRAG
from fast_graphrag._llm import OpenAIEmbeddingService, OpenAILLMService

load_dotenv()

DOMAIN = ""
QUERIES: List[str] = []
ENTITY_TYPES: List[str] = []

working_dir = "./examples/ignore/hp"
grag = GraphRAG(
    working_dir=working_dir,
    domain=DOMAIN,
    example_queries="\n".join(QUERIES),
    entity_types=ENTITY_TYPES,
    config=GraphRAG.Config(
        llm_service=OpenAILLMService(model="your-llm-model", base_url="api.url.com", api_key="your-api-key"),
        embedding_service=OpenAIEmbeddingService(
            model="your-embedding-model",
            base_url="api.url.com",
            api_key="your-api-key",
            embedding_dim=512,  # the output embedding dim, the embedding dim of vector storage must match this value
        ),
    ),
)