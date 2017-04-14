import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = []
        self.negatives = []
        with open('positive-words.txt', 'r') as f:
            for line in f:
                if line.startswith(';') == True:
                    pass
                else:
                    self.positives.append(line.strip())
        f.closed
                    
        with open('negative-words.txt', 'r') as f:
            for line in f:
                if line.startswith(';') == True:
                    pass
                else:
                    self.negatives.append(line.strip())
        f.closed
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        score = 0
        for token in tokens:
            
            if token in self.negatives:
                score += -1
            elif token in self.positives:
                score += 1
            
        return score
