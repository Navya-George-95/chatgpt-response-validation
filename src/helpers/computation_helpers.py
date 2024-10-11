import re
from sentence_transformers import SentenceTransformer, util
from word2number import w2n
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(response, expected_answer):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    response_embedding = model.encode(response, convert_to_tensor=True)
    expected_embedding = model.encode(expected_answer, convert_to_tensor=True)
    cosine_sim = util.cos_sim(response_embedding, expected_embedding)
    return cosine_sim.item()

def keyword_matching(response, expected_keywords):
    response = response.lower()
    return all(keyword.lower() in response for keyword in expected_keywords)

def validate_float_range(response, expected_range):
    import re
    match = re.search(r"[-+]?\d*\.\d+|\d+", response)
    return float(match.group()) if match else None

def extract_number(response):
    try:
        numeric_value = w2n.word_to_num(response)
        return numeric_value

    except ValueError:
        return None

def extract_float(response):
    #Extract the first floating point or integer number from response.
    match = re.search(r"[-+]?\d*\.\d+|\d+", response)
    return float(match.group()) if match else None


def calculate_gpt_models_cosine_similarity(response1, response2):
     model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
     embeddings = model.encode([response1, response2])
     return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

