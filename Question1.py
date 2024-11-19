import matplotlib.pyplot as p
import Functions as f

f.CreateNewResultsFile()

lengthList = [1, 2, 4, 6, 8, 10, 12, 16]
priceList = [1, 5, 9, 17, 20, 30, 36, 48]

print("Writing 1A..")
f.WriteToResultsFile(f"1A - Sparse Price Rod Cutting Algorithm (Rod Length <= Length List Max)" \
    f"\nLength: 12, Price: {f.SparsePriceAlgorithm(lengthList, priceList, 12)}\n\n")

print("Writing 1B..")
f.WriteToResultsFile(f"1B - Updated Sparse Price Rod Cutting Algorithm (Rod Length > Length List Max)" \
    f"\nLength: 100, Price: {f.PerformSparsePriceAlgorithm(lengthList, priceList, 100)}\n\n")

nLengths = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
timeResults = f.RecordFunctionRuntimes(nLengths, f.PerformSparsePriceAlgorithm, lengthList, priceList)
imgName = f"1dResult_{f.GetDateTimeNowString()}.png"

p.plot(nLengths, timeResults, marker='o')
p.title("Sparse Price Rod Cutting Algorithm, Rod Lengths vs. Runtimes")
p.xlabel("Rod Length")
p.ylabel("Runtime (ms)")
p.grid(True)
p.savefig(imgName)

print("Writing 1C..")
f.WriteToResultsFile(f"1C - Sparse Price Rod Cutting Algorithm, Rod Lengths vs. Runtimes Plot\nImage Location: {imgName}\n\n")
