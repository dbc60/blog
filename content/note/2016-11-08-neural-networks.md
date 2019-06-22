---
title: Neural Networks
date: 2016-11-08
draft: true
categories: [software]
tags: [ai, ml]
---

Stuff about neural networks I found on the net that looked interesting
<!--more-->

Fjodor Van Veen posted [a mostly complete chart of neural networks](http://www.asimovinstitute.org/neural-network-zoo/#) (dated 2016.09.14). He lists 13 cell types and a labeled diagram, node map, for each of 27 neural networks. Each node map shows the types of cells it contains and how they are connected. The 13 cell types are:

1. Backfed Input Cell
1. Input Cell
1. Noisy Input Cell
1. Hidden Cell
1. Probablistic Hidden Cell
1. Spiking Hidden Cell
1. Ouput Cell
1. Match Input Output Cell
1. Recurrent Cell
1. Memory Cell
1. Different Memory Cell
1. Kernel
1. Convolution or Pool

The neural networks shown are:

1. Perception (P)
1. Feed Forward (FF)
1. Radial Basis Network (RBF)
1. Deep Feed Forward (DFF)
1. Recurrent Neural Network (RNN)
1. Long/Short Term Memory (LSTM)
1. Gated Recurrent Unit (GRU)
1. Auto Encoder (AE)
1. Variational AE (VAE)
1. Denoising AE (DAE)
1. Sparse AE (SAE)
1. Markov Chain (MC)
1. Hopfield Network (HN)
1. Boltzmann Mahine (BM)
1. Restricted BM (RBM)
1. Deep Belief Network (DBN)
1. Deep Convolutional Network (DCN)
1. Deconvolutional Network (DN)
1. Deep Convolutional Inverse Graphics Network (DCIGN)
1. Generative Adversarial Network (GAN)
1. Liquid State Machine (LSN)
1. Extreme Learning Machine (ELM)
1. Echo State Network (ESN)
1. Deep Residual Network (DRN)
1. Kohonen Network (KN)
1. Support Vector Machine (SVM)
1. Neural Turing Machine (NTM)

The author notes that this list is far from comprehensive, there are variations to the names and he has given no information as to how each of the different nodes work internally. He does go on to provide a very brief description of the different architectures.

The training methods vary among these networks.

1. back-propagation: giving the network paired datasets of "what goes in" and "what we want to have coming out." This is call ed supervised learning.
   - P
   - FF
1. unsupervised learning: provide input and let the network fill in the blanks. The error is being back-propagated is often some variation of the difference between the input and the output (like MSE or just the linear difference).

## References

- [Metacademy](http://metacademy.org) If you just want to check out what ML is about this is the best site.
- [Better Explained](https://betterexplained.com/) if you need to brush up on some of the math
- [Introduction to Probability](https://smile.amazon.com/Introduction-Probability-Chapman-St...)
- Stanford EE263: [Introduction to Linear Dynamical Systems](http://ee263.stanford.edu/)

Beginner:

- [An Introduction to Machine Learning for Developers](http://blog.algorithmia.com/introduction-machine-learning-developers/)
- [Andrew Ng's class](http://cs229.stanford.edu)
- [Python Machine Learning](https://smile.amazon.com/Python-Machine-Learning-Sebastian-R...)
- [An Introduction to Statistical Learning](https://smile.amazon.com/Introduction-Statistical-Learning-A...)

Intermediate:

- [Pattern Recognition and Machine Learning](https://smile.amazon.com/Pattern-Recognition-Learning-Inform...)
- [Machine Learning: A Probabilistic Perspective](https://smile.amazon.com/Machine-Learning-Probabilistic-Pers...)
- [All of Statistics: A Concise Course in Statistical Inference](https://smile.amazon.com/gp/product/0387402721/)
- [Elements of Statistical Learning: Data Mining, Inference, and Prediction](https://smile.amazon.com/gp/product/0387848576)
- [Stanford CS131 Computer vision](http://vision.stanford.edu/teaching/cs131_fall1617/)
- [Stanford CS231n Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/)
- [Convex Optimization](https://smile.amazon.com/Convex-Optimization-Stephen-Boyd/dp...)
- [Deep Learning](http://www.deeplearningbook.org/ or https://smile.amazon.com/Deep-Learning-Adaptive-Computation-...)
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)

Advanced:

- [Probabilistic Graphical Models: Principles and Techniques](https://smile.amazon.com/Probabilistic-Graphical-Models-Prin...)

Looking into probabilistic programming is helpful too. These resources are pretty good:

- [The Design and Implementation of Probabilistic Programming Languages](http://dippl.org)
- [Practical Probabilistic Programming](https://smile.amazon.com/Practical-Probabilistic-Programming...)

Currently (as of 2016.11.08), the most popular ML frameworks are scikit-learn, Tensorflow, Theano and Keras.
