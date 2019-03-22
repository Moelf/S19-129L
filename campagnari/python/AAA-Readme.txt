Contents of this directory
=================

animationExample.py
    An example of a graphical animation

CensusTownAndCityPopulation.csv
    A csv file which will be needed for homework 3

ccHistStuff.py
   Utilities for histogram plotting.  At the moment implemented
   a stat box and putting error bars on a histogram.

checkDecayChain.py
   Needed to check the output of Homework 8, Exercise 2

colorPicture.py
  An example of making an 8 bit color pixel map

compareLogNormal.py
   A comparison of a Gaussian and a "massaged" Lognormal
   which looks very much like a Lognormal distribution
   except that the "massaged" Lognormal can never go
   negative.

dampedOscillator.py
   Use or scipy.integrate.odeint to solve the equation for a
   forced damped oscillator (2nd order linear differential
   equation)

data_fourtop.pkl  data_fourtop.csv
   A pickle or csv file needed for Homework 9

dataSet.npy
    A dataset consisting of a 1D numpy array saved in numpy format.
    This is to be used for Exercise 1 in Homework Set 4.

demoGraph.py
    An example of how to plot points with error bars and lines

demoHist.py
    Lots of example of different types of histogram plottind,
    1D and 2D, also color maps (temperature plots)

demoReadFile.py
    Several ways of reading a text file

demoWriteFile.py
    How to write out stuff to a text file

exampleOfCommandInput.py
    Example of passing parameters and options to a python program
    from the command line

fft.ipynb
    Jupyter notebook for Fast Fourier Transfer example.
    On the rpi you start the jupyter notebook with the
    command
    linux> jupyter-notebook
    On my MAC I sstart with
    mac> jupyter notebook
    (Don't ask me why?)

exampleOfZip.py
   zip is a useful way of aggregating iterables in a loop

genExponential.py
   Example of generating and plotting (on a log scale) an exponential

genPoisson.py
   Example of generating and plotting a Poisson distribution

histForMinuitFit.npz
   Contains some data needed by maxLikFit.py

LVector_specifications.py
   Exercise 1, Homework 6, asks for writing a Lorentz Vector class.
   This python file specifies the methods that are required (including
   their names)

maxLikFit.py
   Example of extended maximum likelihood fit with Minuit
   Described in
   http://hep.ucsb.edu/people/claudio/ph129-w19/ExtendedNLLExample.pdf
   Needs to read data from histForMinuitFit.npz

markovChain.py
   Example of how to generate random numbers using a Markov Chain.
   In this case we have a hardwired Gaussian as our target pdf
   and a flat pdf as our proposal

muonSim.py
   Generated pp -> W -> mu nu decays and plot the transverse
   momentum of the muon.  The ideas behind this were discussed
   in class on Feb 4.  Slides with the discussion can be found on
   the class website

myTriangle.py
   An example of a class that implements a "triangle" object in 2D

plotGaussian.py
   Plots of gaussian, error function, one sided p-value to N(sigma)

RC.py
   Solution of Homework 5 Exercise 6 using prepackaged
   code scipy.integrate.odeint to solve an ordinary 1st order
   differential equation

straightTracks.txt
   A text file needed for Exercises 1 and 3 in Homework 7

simpleFit_v1.py 
   Example code to do a chisq fit using matrix algebra. 
   Fit 6 points to  a+b*x^2

simpleFit_v2.py 
   Same as simpleFit_v1, still 6 points, but now the fitting function
   is a/(1+b*x)

testFit_v1.py
   A test/demo on how to fit a polynomial with np.polyfit

testFit_v2.py
   A test/demo to do the same thing as testFit_V1 but using
   scipy.optimize.curve_fit

testFit_v3.py
   A test/demo to do the same thing as testFit_V1 and testFit_V2
   but using Minuit/iminuit

testOfImportanceSampling.py
   An example of MC integration with and without importance sampling

testFile.txt
  A random text file used by demoReadFile.py

testOfScope.py
  A short program to test the "scope" of variables
