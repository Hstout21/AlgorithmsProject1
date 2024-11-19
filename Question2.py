import matplotlib.pyplot as p
import Functions as f

usCoinList = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000]
wizardCoinList = [1, 29, 493]

amountList = [10, 50, 100, 500, 1000, 1500, 2000, 3000, 5000]
smallAmountList = [10, 25, 50, 100]

imgName = f"Result_{f.GetDateTimeNowString()}.png"

f.WriteToResultsFile("2A, B, & C - All Combination Results\n\n")

f.PrintCombinations("US Coin Combinations", usCoinList, amountList)
usCoinResults = f.RecordFunctionRuntimes(amountList, f.CoinChangeAlgorithm, usCoinList)
f.WriteNewLineToResultsFile()

f.PrintCombinations("Wizarding World Coin Combinations", wizardCoinList, amountList)
wizardCoinResults = f.RecordFunctionRuntimes(amountList, f.CoinChangeAlgorithm, wizardCoinList)
f.WriteNewLineToResultsFile()

f.PrintCombinations("Reconstructed US Coin Combinations", usCoinList, smallAmountList, True)
usCoinReconstructedResults = f.RecordFunctionRuntimes(smallAmountList, f.ReconstructedCoinChangeAlgorithm, usCoinList)
f.WriteNewLineToResultsFile()

f.PrintCombinations("Reconstructed Wizarding World Coin Combinations", wizardCoinList, smallAmountList, True)
wizardCoinReconstructedResults = f.RecordFunctionRuntimes(smallAmountList, f.ReconstructedCoinChangeAlgorithm, wizardCoinList)
f.WriteNewLineToResultsFile()

print(f"Writing 2 Combination Data..")

def QuickPostPlot(x, y, title, imgName, questionNum):
    p.xlabel(x)
    p.ylabel(y)
    p.title(title)
    p.legend()
    p.grid(True)
    p.savefig(imgName)
    print(f"Writing {questionNum}..")
    f.WriteToResultsFile(f"{questionNum} - Coin Change Algorithm Runtimes\nImage Location: {imgName}\n\n")
    p.clf()

def QuickPlot2AB():
    p.plot(amountList, usCoinResults, label="US Coins Original (2a)", marker='D')
    p.plot(amountList, wizardCoinResults, label="Wizard Coins Original (2b)", marker='p')

def QuickPlot2C():
    p.plot(smallAmountList, usCoinReconstructedResults, label="US Coins Reconstructed (2c)", marker='h')
    p.plot(smallAmountList, wizardCoinReconstructedResults, label="Wizard Coins Reconstructed (2c)", marker='8')

# 2A & 2B
QuickPlot2AB()
QuickPostPlot("Amount", "Runtime (ms)", "Coin Change Algorithm Runtimes (Only Original)", f"2ab{imgName}", "2A & B Only")

# 2C
QuickPlot2C()
QuickPostPlot("Amount", "Runtime (ms)", "Coin Change Algorithm Runtimes (Only Reconstructed)", f"2c{imgName}", "2C Only")

# All
QuickPlot2AB()
QuickPlot2C()
QuickPostPlot("Amount", "Runtime (ms)", "Coin Change Algorithm Runtimes (All)", f"2all{imgName}", "2 All.")