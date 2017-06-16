#!/usr/local/bin/python
# -*- coding: UTF-8 -*-


import spacy
from spacy.language_data import TOKENIZER_INFIXES
from spacy.tokenizer import Tokenizer
import en_core_web_md

def create_tokenizer(nlp):
    infix_re = spacy.util.compile_infix_regex(TOKENIZER_INFIXES + [  # u'\w*[,-.–_—:;\(\)\[\]\{\}/]{1,3}\S\w*',
        # r'\w*[,\-.\-_:;\(\)\[\]\{\}\/]{1,3}\S\w*',
        r'\w*\S[,.-_:;\(\)\[\]\{\}/]\S*\w',
        r'\w*\S-\S*\w',
        u'\w*\S–\S*\w',
        u'\w*\S—\S*\w',
        # u'\w*[,-.–_—:;\(\)\[\]\{\}/]{1,3}\S\w*'
    ])
    # TODO: prefix and suffix raise TypeError: '_regex.Pattern' object is not callable
    # prefix_boundaries_to_keep = [r'\(', r'\[',  r'\{', r'<']
    # suffix_boundaries_to_keep = [ r'\)', r'\]', r'\}',  r'>']
    # prefixe_re = spacy.util.compile_prefix_regex([i for i in TOKENIZER_PREFIXES if i not in
    # prefix_boundaries_to_keep])
    # suffixe_re = spacy.util.compile_suffix_regex([i for i in TOKENIZER_SUFFIXES if i not in
    # suffix_boundaries_to_keep])

    # return Tokenizer(nlp.vocab, {}, prefixe_re.search, suffixe_re.search,
    #                  infix_re.finditer)
    return Tokenizer(nlp.vocab, {}, nlp.tokenizer.prefix_search, nlp.tokenizer.suffix_search,
                     infix_re.finditer)


def init_spacy_english_language():
    nlp = en_core_web_md.load(create_make_doc=create_tokenizer)
    return nlp


DOMAIN_STOP_WORDS = [
    "'ll",
    "'ve",
    "0",
    "1",
    "10",
    "100",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "2",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "3",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "4",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "5",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "6",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "7",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "8",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "9",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "96",
    "97",
    "98",
    "99",
    "a",
    "able",
    "about",
    "above",
    "abst",
    "accordance",
    "according",
    "accordingly",
    "across",
    "act",
    "actually",
    "added",
    "adj",
    "affected",
    "affecting",
    "affects",
    "after",
    "afterwards",
    "again",
    "against",
    "ah",
    "all",
    "almost",
    "alone",
    "along",
    "already",
    "also",
    "although",
    "always",
    "am",
    "among",
    "amongst",
    "an",
    "and",
    "announce",
    "another",
    "any",
    "anybody",
    "anyhow",
    "anymore",
    "anyone",
    "anything",
    "anyway",
    "anyways",
    "anywhere",
    "apparently",
    "approximately",
    "are",
    "aren",
    "arent",
    "arise",
    "around",
    "as",
    "aside",
    "ask",
    "asking",
    "at",
    "auth",
    "available",
    "away",
    "awfully",
    "b",
    "back",
    "be",
    "became",
    "because",
    "become",
    "becomes",
    "becoming",
    "been",
    "before",
    "beforehand",
    "begin",
    "beginning",
    "beginnings",
    "begins",
    "behind",
    "being",
    "believe",
    "below",
    "beside",
    "besides",
    "between",
    "beyond",
    "biol",
    "both",
    "brief",
    "briefly",
    "but",
    "by",
    "c",
    "ca",
    "came",
    "can",
    "can't",
    "cannot",
    "cause",
    "causes",
    "certain",
    "certainly",
    "co",
    "com",
    "come",
    "comes",
    "contain",
    "containing",
    "contains",
    "could",
    "couldnt",
    "d",
    "date",
    "did",
    "didn't",
    "different",
    "do",
    "does",
    "doesn't",
    "doing",
    "don't",
    "done",
    "down",
    "downwards",
    "due",
    "during",
    "e",
    "each",
    "ed",
    "edu",
    "effect",
    "eg",
    "eight",
    "eighty",
    "either",
    "else",
    "elsewhere",
    "end",
    "ending",
    "enough",
    "especially",
    "et",
    "et-al",
    "etc",
    "even",
    "ever",
    "every",
    "everybody",
    "everyone",
    "everything",
    "everywhere",
    "ex",
    "except",
    "f",
    "far",
    "few",
    "ff",
    "fifth",
    "first",
    "five",
    "fix",
    "followed",
    "following",
    "follows",
    "for",
    "former",
    "formerly",
    "forth",
    "found",
    "four",
    "from",
    "further",
    "furthermore",
    "g",
    "gave",
    "get",
    "gets",
    "getting",
    "give",
    "given",
    "gives",
    "giving",
    "go",
    "goes",
    "gone",
    "got",
    "gotten",
    "h",
    "had",
    "happens",
    "hardly",
    "has",
    "hasn't",
    "have",
    "haven't",
    "having",
    "he",
    "hed",
    "hence",
    "her",
    "here",
    "hereafter",
    "hereby",
    "herein",
    "heres",
    "hereupon",
    "hers",
    "herself",
    "hes",
    "hi",
    "hid",
    "him",
    "himself",
    "his",
    "hither",
    "home",
    "how",
    "howbeit",
    "however",
    "hundred",
    "i",
    "i'll",
    "i've",
    "id",
    "ie",
    "if",
    "im",
    "immediate",
    "immediately",
    "importance",
    "important",
    "in",
    "inc",
    "indeed",
    "index",
    "information",
    "instead",
    "into",
    "invention",
    "inward",
    "is",
    "isn't",
    "it",
    "it'll",
    "itd",
    "its",
    "itself",
    "j",
    "just",
    "k",
    "keep",
    "keeps",
    "kept",
    "kg",
    "km",
    "know",
    "known",
    "knows",
    "l",
    "largely",
    "last",
    "lately",
    "later",
    "latter",
    "latterly",
    "least",
    "less",
    "lest",
    "let",
    "lets",
    "like",
    "liked",
    "likely",
    "line",
    "little",
    "look",
    "looking",
    "looks",
    "ltd",
    "m",
    "made",
    "mainly",
    "make",
    "makes",
    "many",
    "may",
    "maybe",
    "me",
    "mean",
    "means",
    "meantime",
    "meanwhile",
    "merely",
    "mg",
    "might",
    "million",
    "miss",
    "ml",
    "more",
    "moreover",
    "most",
    "mostly",
    "mr",
    "mrs",
    "much",
    "mug",
    "must",
    "my",
    "myself",
    "n",
    "na",
    "name",
    "namely",
    "nay",
    "nd",
    "near",
    "nearly",
    "necessarily",
    "necessary",
    "need",
    "needs",
    "neither",
    "never",
    "nevertheless",
    "new",
    "next",
    "nine",
    "ninety",
    "no",
    "nobody",
    "non",
    "none",
    "nonetheless",
    "noone",
    "nor",
    "normally",
    "nos",
    "not",
    "noted",
    "nothing",
    "now",
    "nowhere",
    "o",
    "obtain",
    "obtained",
    "obviously",
    "of",
    "off",
    "often",
    "oh",
    "ok",
    "okay",
    "old",
    "omitted",
    "on",
    "once",
    "one",
    "ones",
    "only",
    "onto",
    "or",
    "ord",
    "other",
    "others",
    "otherwise",
    "ought",
    "our",
    "ours",
    "ourselves",
    "out",
    "outside",
    "over",
    "overall",
    "owing",
    "own",
    "p",
    "page",
    "pages",
    "part",
    "particular",
    "particularly",
    "past",
    "per",
    "perhaps",
    "placed",
    "please",
    "plus",
    "poorly",
    "possible",
    "possibly",
    "potentially",
    "pp",
    "predominantly",
    "present",
    "previously",
    "primarily",
    "probably",
    "promptly",
    "proud",
    "provides",
    "put",
    "q",
    "que",
    "quickly",
    "quite",
    "qv",
    "r",
    "ran",
    "rather",
    "rd",
    "re",
    "readily",
    "really",
    "recent",
    "recently",
    "ref",
    "refs",
    "regarding",
    "regardless",
    "regards",
    "related",
    "relatively",
    "research",
    "respectively",
    "resulted",
    "resulting",
    "results",
    "right",
    "run",
    "s",
    "said",
    "same",
    "saw",
    "say",
    "saying",
    "says",
    "sec",
    "section",
    "see",
    "seeing",
    "seem",
    "seemed",
    "seeming",
    "seems",
    "seen",
    "self",
    "selves",
    "sent",
    "seven",
    "several",
    "shall",
    "she",
    "she'll",
    "shed",
    "shes",
    "should",
    "shouldn't",
    "show",
    "showed",
    "shown",
    "showns",
    "shows",
    "significant",
    "significantly",
    "similar",
    "similarly",
    "since",
    "six",
    "slightly",
    "so",
    "some",
    "somebody",
    "somehow",
    "someone",
    "somethan",
    "something",
    "sometime",
    "sometimes",
    "somewhat",
    "somewhere",
    "soon",
    "sorry",
    "specifically",
    "specified",
    "specify",
    "specifying",
    "still",
    "stop",
    "strongly",
    "sub",
    "substantially",
    "successfully",
    "such",
    "sufficiently",
    "suggest",
    "sup",
    "sure",
    "t",
    "take",
    "taken",
    "taking",
    "tell",
    "tends",
    "th",
    "than",
    "thank",
    "thanks",
    "thanx",
    "that",
    "that'll",
    "that've",
    "thats",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "thence",
    "there",
    "there'll",
    "there've",
    "thereafter",
    "thereby",
    "thered",
    "therefore",
    "therein",
    "thereof",
    "therere",
    "theres",
    "thereto",
    "thereupon",
    "these",
    "they",
    "they'll",
    "they've",
    "theyd",
    "theyre",
    "think",
    "this",
    "those",
    "thou",
    "though",
    "thoughh",
    "thousand",
    "throug",
    "through",
    "throughout",
    "thru",
    "thus",
    "til",
    "tip",
    "to",
    "together",
    "too",
    "took",
    "toward",
    "towards",
    "tried",
    "tries",
    "truly",
    "try",
    "trying",
    "ts",
    "twice",
    "two",
    "u",
    "un",
    "under",
    "unfortunately",
    "unless",
    "unlike",
    "unlikely",
    "until",
    "unto",
    "up",
    "upon",
    "ups",
    "us",
    "use",
    "used",
    "useful",
    "usefully",
    "usefulness",
    "uses",
    "using",
    "usually",
    "v",
    "value",
    "various",
    "very",
    "via",
    "viz",
    "vol",
    "vols",
    "vs",
    "w",
    "want",
    "wants",
    "was",
    "wasnt",
    "way",
    "we",
    "we'll",
    "we've",
    "wed",
    "welcome",
    "went",
    "were",
    "werent",
    "what",
    "what'll",
    "whatever",
    "whats",
    "when",
    "whence",
    "whenever",
    "where",
    "whereafter",
    "whereas",
    "whereby",
    "wherein",
    "wheres",
    "whereupon",
    "wherever",
    "whether",
    "which",
    "while",
    "whim",
    "whither",
    "who",
    "who'll",
    "whod",
    "whoever",
    "whole",
    "whom",
    "whomever",
    "whos",
    "whose",
    "why",
    "widely",
    "willing",
    "wish",
    "with",
    "within",
    "without",
    "wont",
    "words",
    "world",
    "would",
    "wouldnt",
    "www",
    "x",
    "y",
    "yes",
    "yet",
    "you",
    "you'll",
    "you've",
    "youd",
    "your",
    "youre",
    "yours",
    "yourself",
    "yourselves",
    "z",
    "zero",
    "cell",
    "cells",
    "expression",
    "patient",
    "patients",
    "study",
    "studies",
    "protein",
    "proteins",
    "gene",
    "genes",
    "mRNA",
    "transcript",
    "domain",
    "domains",
    "factor",
    "factors",
    "level",
    "levels",
    "disease",
    "diseases"]