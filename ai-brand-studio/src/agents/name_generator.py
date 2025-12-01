import random
def generate_names(brief, n=20):
    base_words = ['Nova','Nutr','Meal','Muse','Craft','Lead','Pulse','Spark','Flow','Nest','Sync','Loop','Mate','Hive']
    names = []
    for i in range(n):
        a = random.choice(base_words)
        b = random.choice(base_words)
        candidate = f"{a}{b}" if random.random() > 0.5 else f"{a}{random.choice(['ly','io','ify','hub'])}"
        names.append(candidate)
    return list(dict.fromkeys(names))[:n]
