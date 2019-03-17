Problem 1:
-----------
Run ex1.py to see the three plots with resulting sum of signal + background on top of the mass histogram. I check an exponential fit, a linear fit, and a quadratic fit. As displayed in the plotsthemselves, the exponential background gave S=22.6 \pm 7.8, the linear background gave S=18.5 \pm 1.4, and the quadratic background gave S=18.8 \pm 7.7.
The exponential fit is the most physically realistic fit as it goes to zero as mass gets very large. Thus, our final result is S = 22.6 \pm 7.8 \pm 5.0, approximating 5.0 as the systematic error from the various calculations.
I've also included a PDF with more data nicely displayed in a semi-report format titled problem_1.pdf.


Problem 2:
-----------
Run ex2.py. Simulates a nuclear decay chain 1000 times and wrotes results to the data.pik file, which may be read by checkDecayChain.py and results in proper consistencies and plots.
