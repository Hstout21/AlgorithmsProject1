import datetime as dt
import time as t
import os

# Functions for homework problems


# 1A, Original Algorithm
def SparsePriceAlgorithm(lengthList, priceList, maxLengthSold):

    priceHash = CreateDictionary(lengthList, priceList)
    MaxSize = maxLengthSold+1
    Results = [0] * MaxSize

    for i in range(1, MaxSize):
        CurrentMaxPrice = 0
        for j in lengthList:
            if j <= i:
                CurrentMaxPrice = max(CurrentMaxPrice, priceHash[j] + Results[i - j])
        Results[i] = CurrentMaxPrice

    return Results[maxLengthSold]

# 1B, Enhancement For Over Limit n Values.
def PerformSparsePriceAlgorithm(lengthList, priceList, maxLengthSold):

    MaxLength = max(lengthList)

    if maxLengthSold > MaxLength:
        overflowAmount = maxLengthSold - MaxLength
        maxPriceForOverflow = (overflowAmount // MaxLength) * priceList[lengthList.index(MaxLength)]
        return maxPriceForOverflow + SparsePriceAlgorithm(lengthList, priceList, maxLengthSold % MaxLength)
    else:
        return SparsePriceAlgorithm(lengthList, priceList, maxLengthSold)
    
# 2A & B, Original Coin Change Algorithm.
def CoinChangeAlgorithm(coinList, amountToCheck):

    MaxAmount = amountToCheck+1
    Results = [0] * MaxAmount
    Results[0] = 1

    for i in coinList:
        for j in range(i, MaxAmount):
            Results[j] += Results[j-i]
            
    return Results[amountToCheck]

# 2C, Reconstructed Coin Change Algorithm that saves unique combinations.
def ReconstructedCoinChangeAlgorithm(coinList, amountToCheck):

    MaxAmount = amountToCheck+1
    Results = [[] for _ in range(MaxAmount)]
    Results[0] = [[]]

    for i in coinList:
        for j in range(i, MaxAmount):
            for x in Results[j-i]:
                newCombination = x+[i]
                Results[j].append(newCombination)

    return Results[amountToCheck]


# Helpers.
def CreateDictionary(keys, values):
    return {x: y for x, y in zip(keys, values)}

def RecordFunctionRuntimes(valuesList, function, param1, param2=None):
    retVal = []
    for i in valuesList:
        startTime = t.perf_counter()
        function(param1, i) if param2 is None else function(param1, param2, i)
        retVal.append(ConvertSeconds(t.perf_counter()-startTime))
    return retVal
    
def ConvertSeconds(seconds):
    return f"{seconds * 1000:.3f}"

def GetDateTimeNowString():
    return dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def CreateNewResultsFile():
    resultsPath = "Results.txt"
    if os.path.exists(resultsPath):
        print("Clearing Old Results.")
        open(resultsPath, 'w').close()
    with open(resultsPath, 'a') as file:
        file.write("\nHomework 4 Results | Hunter Stout\n\n")

def WriteToResultsFile(msg):
    with open("Results.txt", 'a') as file:
        file.write(msg)

def WriteNewLineToResultsFile():
    with open("Results.txt", 'a') as file:
        file.write("\n")

def PrintCombinations(title, coinList, valuesList, isPrintCombinationExamples=False):
    WriteToResultsFile(f"{title}:\n")
    for i in valuesList:
        if isPrintCombinationExamples:
            combinations = ReconstructedCoinChangeAlgorithm(coinList, i)
            WriteToResultsFile(f"Amount: {i}, Combination Amount: {len(combinations)}\n")
            WriteToResultsFile(f"Unique Combinations: {combinations}\n\n")
        else:
            WriteToResultsFile(f"Amount: {i}, Combination Amount: {CoinChangeAlgorithm(coinList, i)}\n")