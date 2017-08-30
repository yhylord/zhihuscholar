from nltk.tokenize.stanford_segmenter import StanfordSegmenter

chinese_segmenter = StanfordSegmenter()
chinese_segmenter.default_config('zh')