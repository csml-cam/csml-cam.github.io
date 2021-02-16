---
title: "CSML@Cam - Research"
layout: textlay
excerpt: "CSML@Cam - Research"
sitemap: false
use_math: true
permalink: /research.html
---

Research
* TOC
{:toc}

## Digital Twins

### Statistical Finite Elements

The Finite Element Method (FEM) is the most popular tool for solving partial differential equations across science and engineering. Yet to this date there has been no coherent statistical methodology to incorporate observed data into FEM simulations. 

The Statistical Finite Element method augments the classical FEM with a coherent statistical construction to provide the framework for updating FEM models in the presence of data. It does this through admitting that the underlying physical model is possibly misspecified with reality, introducing stochastic forcing inside the governing equations. This forms the *prior* for the model. We then take an approach similar to that of [Bayesian calibration](https://doi.org/10.1111/1467-9868.00294), and posit a data-generating process that the observations were possibly generated according to. The FEM model is then updated in the face of this data, resulting in a compromise between reality and prior model specification --- the *posterior* --- with a full uncertainty quantification.

To date we have published two papers on this work. The [first](https://doi.org/10.1016/j.cma.2020.113533) demonstrates the effectiveness of the method in the context of computational mechanics, and studies a variety of examples for the one- and two-dimensional elliptic problems. The [second](https://doi.org/10.1073/pnas.2015006118) studies the methodology in the context of nonlinear internal waves (*solitons*), using the Korteweg-de Vries equation. These works lay the appropriate mathematical and statistical foundation for which the Digital Twin revolution can build upon, and we are very excited to study, develop, and apply these methods further.

**References**: Girolami, M., Febrianto, E., Yin, G., and Cirak, F. (2021). [The statistical finite element method (statFEM) for coherent synthesis of observation data and model predictions](https://doi.org/10.1016/j.cma.2020.113533). Computer Methods in Applied Mechanics and Engineering, 375, 113533.

Duffin, C., Cripps, E., Stemler, T., and Girolami, M. (2021). [Statistical finite elements for misspecified models](https://doi.org/10.1073/pnas.2015006118). Proceedings of the National Academy of Sciences, 118(2).

![girolami-statfem-paper-image](/_support_files/research/statfem/statfem-poisson.png){:height="150px"}
![duffin-statfem-paper-image](/_support_files/research/statfem/cubic-posterior.png){:height="150px"}

{% capture summary %}
Related links
{% endcapture %}
{% capture details %}
- [CMAME paper](https://doi.org/10.1016/j.cma.2020.113533)
- [PNAS paper](https://doi.org/10.1073/pnas.2015006118)
- [Cambridge media release](https://www-smartinfrastructure.eng.cam.ac.uk/news/cambridge-academic-csic-redefines-finite-element-method-data-age)
- [Turing media release](https://www.turing.ac.uk/news/turing-delivers-data-driven-computational-predictive-methods-emerging-complex-engineering)
- [UWA media relase](https://www.uwa.edu.au/news/article/2021/january/new-system-to-advance-predictions-in-engineering)
{% endcapture %}
{% include details.html %}


### Future of Farming

Mark Girolami is involved in the project of creating a digital twin of an underground farm in London.
For more information visit:
1. [A recent publication in the Data-centric engineering journal](https://doi.org/10.1017/dce.2020.21).
2. [The farm website](http://growing-underground.com/)
3. [Coverage by University of Cambridge](http://www.eng.cam.ac.uk/news/cambridge-engineers-unveil-digital-twin-support-future-farming)


### Aerospace-engineering applications

The data-centric engineering programme at the Alan Turing Institute
which is led by Mark Girolami is working on improving design of jet
engines.  For more details, visit the [Turing
page](https://www.turing.ac.uk/research/impact-stories/streamlining-jet-engine-design-and-manufacture).



### Talks


**September 2020**: Prof Mark Girolami gave a keynote talk title "Digital Twins: The Sense and Statistics" at the conference of Royal Statistical Society: 
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/cWIJNXQn8LI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



## Insights into Cities

The main website for the project can be found at [https://iconicmath.org/](https://iconicmath.org/).

## Monte Carlo Methods

### Control Functionals

#### [Control functionals for Monte Carlo Integration](http://onlinelibrary.wiley.com/doi/10.1111/rssb.12185/full)

Monte Carlo integation attempts to estimate an expectation of a function of a random variable, based on a collection of independent realisations.  The most basic solution to this problem is to construct an ''arithmetic mean'' estimator.  Under the central limit theorem, the arithmetic mean converges to its expectation at a rate $$O(n^{-1/2})$$, where n is the number of independent realisations.  However in many modern applications, e.g. involving complex computer models, root-n convergence is simply too slow. In a recent paper, Chris Oates, Mark Girolami and Nicolas Chopin introduced a new class of estimators for Monte Carlo integration that leverage gradient information on the sampling distribution in order to improve performance. The proposed estimators, called ''control functionals'', achieve super-root-n-convergence and often require orders of magnitude fewer simulations, compared with existing approaches, in order to achieve a fixed level of precision.

Our methodology, called ''control functionals'', proceeds on the premise that the score function exists and can, in principle, be evaluated at any given point.  We will leverage the score to construct more efficient estimators the expectation.

1. Begin by splitting samples into two disjoint subsets, where the size of both
   subsets is assumed to increase linearly as n tends to infinity.
2. The first subset is used to estimate a surrogate function, based on the
   gradient information contained in the score, such that the surrogate function
   shares the same expectation as but has a variance that vanishes as the size
   of the subset tends to infinity. This step is discussed in detail in the
   paper and can be easily facilitated using techniques from non-parametric
   regression.
3. The second subset is used to evaluate an arithmetic mean.
4. Any dependence on the split of the samples is then removed by averaging over
   many possible splits.

It is proven in the paper that the estimator that results from applying Steps 1-4 is (under weak regularity conditions) unbiased and achieves super-root-n convergence.

**Results**: Consider the toy example where f(x) = sin(πx) and X~N(0, 1). Here we know from symmetry that the expectation is zero.   Applying the usual arithmetic mean estimator  we obtain root-n convergence.  Now contrast with the control functional estimator.This particular implementation estimates the surrogate function using techniques from Gaussian process (GP).  The performance of control functionals is so strong that we need to use a different scale on the y-axis in order to compare the estimators. Here, on the y-axis we plot the (estimated) estimator standard deviation, multiplied by the square-root of n, so that the familiar root-n convergence is represented by a horizontal line.

You can see here that control functionals achieve super-root-n convergence. Here we also comare against "Riemann Sums" (DOI 10.1023/A:1008926514119) and "ZV Control Variates" (DOI 10.1007/s11222-012-9344-6). The difference between GP Control Functionals and GP Control Functionals (Simplified) is explained in the main text of the paper.

For further details, please refer to the full paper (link above), where you can also find applications of the control functional methodology to Bayes-Hermite quadrature, marginalisation in hierarchical models, and computation of normalising constants for non-linear differential equation models.

**Reference**: Oates, C. J., Girolami, M. and Chopin, N. (2017), Control functionals for Monte Carlo integration. J. R. Stat. Soc. B, 79: 695–718. doi:10.1111/rssb.12185

![oates-cf-paper-image-1](/_support_files/research/monte_carlo/control_functionals/control-functionals-pic-1.jpg){:height="200px"}
![oates-cf-paper-image-2](/_support_files/research/monte_carlo/control_functionals/control-functionals-pic-2.jpg){:height="200px"}
![oates-cf-paper-image-3](/_support_files/research/monte_carlo/control_functionals/control-functionals-pic-3.jpg){:height="200px"}

{% capture summary %}
Related links
{% endcapture %}
{% capture details %}
- [Paper](http://arxiv.org/abs/1410.2392)
- [CF Supplement](/_support_files/research/monte_carlo/control_functionals/supplement.pdf)
- [CF Software](/_support_files/research/monte_carlo/control_functionals/cf_software.zip)
- [Xi'an's Og Blog Discussion](http://xianblog.wordpress.com/2014/10/21/control-functionals-for-monte-carlo-integration/)
{% endcapture %}
{% include details.html %}


#### [Convergence Rates for a Class of Estimators Based on Stein's Method](https://arxiv.org/abs/1603.03220)

This paper extends the paper "Control functionals for Monte Carlo Integration" by providing a detailed analysis of the convergence guarantees of control functionals when the target density and the integrand are both smooth. This helps further clarify scenarios in which the additional computational cost encurred by constructing control functionals will provide gains in statistical efficiency. Our results work both in the case of Monte Carlo i.i.d. samples from the target density, as well as some Markov chains with strong ergodicity properties.

Suppose the target density is a+1 times differentiable and the target integrand f is b+1 times differentiable. Under mild conditions on the integration domain, we show that the integration error of the corresponding control functional estimator converges at rate of $$O(n^{-\frac{1}{2} - min(a,b) / d + \epsilon})$$, where n is the number of integrand evaluations and d is the dimension of the domain of integration. In cases where the target integrand and the target density are smooth, the control functional estimator will provide significant performance gains. The rate also highlights the curse of dimensionality which is common in control variates methods.

The paper concludes with some experiments on a challenging Bayesian inverse problem based on a PDE of steady-state flow in aquifers and other subsurface systems. These experiments demonstrate the potential gains attainable with control functionals.

**Reference**: Oates, C. J., Cockayne, J., Briol, F-X. & Girolami, M. (2016). Convergence Rates for a Class of Estimators Based on Stein's Identity. arXiv:1603.03220.


### Hamiltonian Monte Carlo


#### [Geometry and Dynamics for Markov Chain Monte Carlo](http://www.annualreviews.org/doi/abs/10.1146/annurev-statistics-031017-100141)

Markov Chain Monte Carlo methods have revolutionised mathematical computation and enabled statistical inference within many previously intractable models. In this context, Hamiltonian dynamics have been proposed as an efficient way of building chains which can explore probability densities efficiently. The method emerges from physics and geometry and these links have been extensively studied by a series of authors through the last thirty years. However, there is currently a gap between the intuitions and knowledge of users of the methodology and our deep understanding of these theoretical foundations. 

The aim of this review is to provide a comprehensive introduction to the geometric tools used in Hamiltonian Monte Carlo at a level accessible to statisticians, machine learners and other users of the methodology with only a basic understanding of Monte Carlo methods. This will be complemented with some discussion of the most recent advances in the field which we believe will become increasingly relevant to applied scientists. 

![barp-review-paper-image](/_support_files/research/monte_carlo/hmc/geometry-pic-hmc.jpg){:height="100px"}

**Reference**: Barp, A., Briol, F-X., Kennedy, A. D. & Girolami, M. (2017). Geometry and Dynamics for Markov Chain Monte Carlo. arXiv:1705.02891. Annual Review of Statistics and Its Applications, Vol. 5. 


#### [Riemann manifold Langevin and Hamiltonian Monte Carlo methods](http://onlinelibrary.wiley.com/doi/10.1111/j.1467-9868.2010.00765.x/full)

This paper proposes Metropolis adjusted Langevin and Hamiltonian Monte Carlo sampling methods defined on the Riemann manifold to resolve the shortcomings of existing Monte Carlo algorithms when sampling from target densities that may be high dimensional and exhibit strong correlations. The methods provide fully automated adaptation mechanisms that circumvent the costly pilot runs required to tune proposal densities for Metropolis- Hastings or indeed Hamiltonian Monte Carlo and Metropolis Adjusted Langevin Algorithms. This allows for highly efficient sampling even in very high dimensions where different scalings may be required for the transient and stationary phases of the Markov chain.

The proposed methodology exploits the Riemannian geometry of the parameter space of statistical models and thus automatically adapts to the local structure when simulating paths across this manifold providing highly efficient convergence and exploration of the target density. The performance of these Riemannian Manifold Monte Carlo methods is rigorously assessed by performing inference on logistic regression models, log-Gaussian Cox point processes, stochastic volatility models, and Bayesian estimation of dynamical systems described by nonlinear differential equations. Substantial improvements in the time normalised Effective Sample Size are reported when compared to alternative sampling approaches.

**Reference**: Girolami, M. and Calderhead, B. (2011), Riemann manifold Langevin and Hamiltonian Monte Carlo methods. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 73: 123–214. doi:10.1111/j.1467-9868.2010.00765.x

{% capture summary %}
Extra Material
{% endcapture %}
{% capture details %}
- [RSS-B Paper](http://onlinelibrary.wiley.com/doi/10.1111/rssb.2011.73.issue-2/issuetoc)
- [RMHMC Meeting Slides 1](/_support_files/research/monte_carlo/hmc/RMHMC-Meeting-Slides-1.pdf)
- [RMHMC Meeting Slides 2](/_support_files/research/monte_carlo/hmc/RMHMC-Meeting-Slides-1.pdf)
- [RMHMC Logistic Regression](/_support_files/research/monte_carlo/hmc/RMHMC-Logistic-Regression.zip)
- [RMHMC Stochastic Vol](/_support_files/research/monte_carlo/hmc/RMHMC-Stochastic-Vol.zip)
- [RMHMC ODE Inference](/_support_files/research/monte_carlo/hmc/RMHMC-ODE-Inference.zip)

{% endcapture %}
{% include details.html %}



## Probabilistic Numerics

Probabilistic numerical methods are a set of tools to solve numerical analysis
problems from the point of view of statistical inference. Our work mostly
focuses on Bayesian numerical methods, which are motivated by their uncertainty
quantification properties for the output of numerical methods. The group has
significantly advanced the field in research years, with work on the foundations
of probabilistic numerics, on methodology for quadrature, ODE solvers and PDE
solvers, and on applications to complex engineering problems.

An overview of the field can be found on the following website: [probabilistic-numerics.org](http://www.probabilistic-numerics.org/)/

### Foundations

#### [Bayesian Probabilistic Numerical Methods](https://epubs.siam.org/doi/pdf/10.1137/17M1139357)
This paper identifies Bayesian probabilistic numerical methods as a particular class of noiseless Bayesian inversion problems. It is shown that, while many PN methods incorporate Bayesian ideas, the resulting posterior distribution is seldom fully Bayesian by this definition. Nevertheless, under remarkably general conditions there always exists an essentially unique Bayesian probabilistic numerical method for a particular problem, although the posterior distribution is often intractable.

Secondly, analogues are drawn with the fields of information-based complexity and average-case analysis, in a discussion of performance analysis for Bayesian PNM. It is shown that, where an average-case optimal numerical method is known for a particular problem, the posterior mean of an equivalent Bayesian PNM will naturally coincide with this point estimate, a result often commented on in other works (see the integration and PDE sections). However, it is also shown that there are situations in which optimal information for Bayesian PNM and average-case optimal information do not coincide.

Thirdly, the numerical disintegration algorithm is constructed to allow exploration of the intractable posterior distributions which often arise from Bayesian PNM. Numerical disintegration is an algorithm which approximates the true Bayesian distribution with samples from a tractable distribution close to the truth in an appropriate probability metric. Theoretical results are presented showing convergence of the numerical disintegration scheme in a limiting sense. This approach is applied to several challenging numerical problems, including Painleve’s first transcendental.

Lastly, the composition of PN methods into pipelines is discussed. Many numerical problems require the solution of multiple interdependent systems. Conditions are established for the output of such pipelines to be Bayesian, when the composite numerical methods are Bayesian PNM. This methodology is then applied to a prototypical pipeline, given by a challenging problem in industrial process monitoring.

- **Reference**: Cockayne, Jon, Chris J. Oates, T. J. Sullivan, and Mark Girolami. 2019. ‘Bayesian Probabilistic Numerical Methods’. SIAM Review 61 (3): 756–789. https://doi.org/10.1137/17m1139357.
- [arXiv reference](https://arxiv.org/abs/1702.03673)




### Integration

Probabilistic integration is one of the main sub-branches of probabilistic
numerics. The particular method of numerical integration our group has been
working on is called Bayesian Quadrature (also called Bayesian Monte Carlo, or
Kernel Quadrature). The method consists of approximating the integrand of
interest with a Gaussian process, and then integrating analytically this
approximation of the integrand (this is possible since integrals of Gaussian
variables are themselves Gaussian; see sketch on the right hand side). In this
case the approximation provided by the method will be a univariate (Gaussian)
posterior distribution. The mean of this distribution provides a point estimate
of the integral and its variance represents our uncertainty over the solution of
the numerical procedure. As the number of observations in the underlying
Gaussian process increases, the posterior mass will concentrate on the true
value of the integral. This posterior variance is also an example of a measure
of uncertainty which can be propagated through subsequent computation.

The work discussed on the rest of this webpage focuses on providing efficient
algorithms for probabilistic integration together with strong theoretical
guarantees in both a statistical and numerical analysis sense.


#### [Frank-Wolfe Bayesian Quadrature: Probabilistic Integration with Theoretical Guarantees](https://papers.nips.cc/paper/5749-frank-wolfe-bayesian-quadrature-probabilistic-integration-with-theoretical-guarantees)

This paper provides a method of efficiently choosing design points for Bayesian Quadrature, based on a convex optimisation algorithm called the Frank-Wolfe algorithm. This algorithm can efficiently spread the points around the domain of integration where most of the measure is located. It is also the first probabilistic integration algorithm which has theoretical guarantees in the form of rates of convergence and contraction of the posterior probability distribution of Bayesian Quadrature.

See a nice [blog review by Ingmar Schuster](https://ingmarschuster.wordpress.com/2015/10/26/frank-wolfe-bayesian-quadrature/).

- **Reference**: Briol, F-X., Oates, C. J., Girolami, M., & Osborne, M. A. (2015). Frank-Wolfe Bayesian Quadrature: Probabilistic Integration with Theoretical Guarantees. Advances In Neural Information Processing Systems (NIPS), pages 1162-1170.
- [arXiv link](https://arxiv.org/pdf/1506.02681v2.pdf).


#### [Probabilistic Integration: A Role for Statisticians in Numerical Analysis?](https://projecteuclid.org/euclid.ss/1555056025)

This paper discusses extensively the usefulness of having a probabilistic
numerical approach to numerical integration. It focuses mostly on Bayesian Monte
Carlo and Bayesian Quasi Monte Carlo, the Bayesian Quadrature methods based on
Monte Carlo and Quasi-Monte Carlo states. The paper shows that, under several
assumptions on the regularity of the function to be integrated (e.g. assumptions
on the smoothness of the function), such approaches can provide significant
improvements over standard Monte Carlo methods. More precisely, the convergence
rate (asymptotic rate at which the error decreases with the number of function
evaluations) of these method can significantly outperform that of the
non-probabilistic methods. Finally, The paper also demonstrates some of the
potential advantages of having a probability distribution to summarise our
numerical uncertainty, and shows numerically on several test functions that good
calibration of this distribution is possible. An honest discussion of the
advantages and disadvantages of the method is also provided and is illustrated
on several applications ranging from computer graphics to petroleum engineering.

- **Reference**: Briol, F-X., Oates, C. J., Girolami, M., Osborne, M. A. & Sejdinovic, D. (2015). Probabilistic Integration: A Role for Statisticians in Numerical Analysis?
- [arXiv link](http://arxiv.org/abs/1512.00933)
- [blog post by Andrew Gelma](https://statmodeling.stat.columbia.edu/2015/12/07/28279/)
- [blog post by Christian Rober](https://xianblog.wordpress.com/2015/12/17/je-suis-revenu-de-montreal-nips-2015/)
- The paper was awarded a Best Student Paper 2016 award by the Section for Bayesian Statistical Science of the American Statistical Association!


#### [Probabilistic Models for Integration Error in the Assessment of Functional Cardiac Models](https://papers.nips.cc/paper/2017/hash/98dce83da57b0395e163467c9dae521b-Abstract.html)

This paper extends some of our previous work on Bayesian quadrature to cases
where the probability distribution with respect to which we are integrating is
not available in closed-form. In particular, we assume we have access to
distribution only through samples, which is often the case in areas such as
Bayesian calibration of computer models. We propose a probabilistic numerics
approach to this problem which includes a model for the integrand together with
another model for the kernel mean (also called kernel embedding) obtained using
a Dirichlet process to model the measure with respect to which we are
integrating. The approach is illustrated on a Bayesian forecasting problem for
the Goodwin oscillator, a well known model of complex chemical systems made up
of a system of ODEs. We also have some nice applications to complex cardiac
models.

- **Reference**: Oates, C. J., Niederer, S., Lee, A., Briol, F-X. & Girolami, M. (2016). Probabilistic Models for Integration Error in the Assessment of Functional Cardiac Models.
- [arXiv link](https://arxiv.org/abs/1606.06841)

<iframe width="560" height="315" src="https://www.youtube.com/embed/SrrO4OxydO0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


#### [On the Sampling Problem for Kernel Quadrature](http://proceedings.mlr.press/v70/briol17a)

This paper looks at various importance sampling distribution for use in
probabilistic integration/Bayesian Monte Carlo. Here, the optimal importance
distirbution will be different from the optimal importance distribution in
standard Monte Carlo integration. In particular, this optimal distribution will
be completely intractable, and will depend on the number of samples, the choice
of kernel and the probability measure with respect to which we are
integrating. We propose an adaptive SMC algorithm to automate the choice of a
"good" distribution for importance sampling with Bayesian Quadrature weights.

**Reference**: Briol FX, Oates CJ, Cockayne J, Chen, WY, Girolami M. (2017) On the Sampling Problem for Kernel Quadrature. International Conference on Machine Learning (ICML 2017), 70:586-595.
- [arXiv link](https://arxiv.org/abs/1706.03369)



### Partial Differential Equations

#### [Probabilistic Numerical Methods for Partial Differential Equations and Bayesian Inverse Problems](https://arxiv.org/abs/1605.07811)

This paper contributes a Bayesian probabilistic numerical method for linear and nonlinear partial differential equations (PDEs) and studies incorporation of the posterior measure produced into Bayesian inversion problems, in a prototypical pipeline of computation.

The central contribution is a probabilistic numerical method for linear PDEs. It is shown that when the PDE is linear and the prior measure on the solution is Gaussian with an appropriate covariance function, the posterior measure produced is also Gaussian and has a closed form. Furthermore, the posterior mean of this measure is identical to the point estimate of the solution produced by symmetric collocation.  This allows a transfer of convergence results from that work. New results are also developed surrounding the concentration of the posterior measure as the fidelity of the approximation is increased.

The second contribution of the paper is to propagate the uncertainty from the forward solver into the posterior measure over the solution of PDE-constrained Bayesian inverse problems. It is shown that when the posterior uncertainty over the forward solution is marginalised in the likelihood of the Bayesian inverse problem, the resultant posterior measure for the inverse problem rigorously accounts for the uncertainty resulting from an intractable forward solution. This allows for a cheap, approximate solution to the PDE to be used, which can reduce the computational time required for these challenging problems. The approach is applied to Electrical Impedance Tomography, a PDE-constrained inverse problem in medical imaging.

Lastly, posterior measures are constructed for a certain class of semilinear PDEs, such as the steady-state Allen-Cahn equation, a PDE known to exhibit multiple solutions. While the method proposed is heavily dependent on the form of the PDE, it illustrates how PN methods might be applied to other challenging nonlinear problems for which discretisation error is highly significant.

- **Reference 1**: Probabilistic Numerical Methods for PDE-constrained Bayesian Inverse Problems. Cockayne, J., Oates, C. J., Sullivan, T., Girolami, M. Proceedings of the 36th International Workshop on Bayesian Inference and Maximum Entropy Methods in Science and Engineering.
- **Reference 2**: Probabilistic Meshless Methods for Partial Differential Equations and Bayesian Inverse Problems. Cockayne, J., Oates, C. J., Sullivan, T., Girolami, M., arXiv:1605.07811.
- [An introduction to probabilistic meshless methods](https://www.pathlms.com/siam/courses/4150/sections/5835/video_presentations/42666)


### Ordinary Differential Equations

This site accompanies our recent publication, Probability Measures for Numerical Solutions of Differential Equations. It proposes a new strategy for randomising existing solvers for ordinary and partial differential equations, which rigorously models the uncertainty introduced by the numerical methods. This correct handling of uncertainty is crucial when numerical solvers are used for statistical analysis, for example, in Bayesian inference. This work is part of the emerging field of Probabilistic Numerics, which frames numerical methods as statistical inference tasks, allowing the tools of statistics to be combined with classical numerical analysis.

- [arXiv link](http://arxiv.org/abs/1506.04592)
- [presentation](/_support_files/research/monte_carlo/pn/conrad_warwicknumerics_2015.pdf)
- [Code on bitbucket](https://bitbucket.org/prconrad/pints)

### Applications

#### [Bayesian Probabilistic Numerical Methods for Industrial Process Monitoring](https://arxiv.org/abs/1707.06107)

Hydrocyclones provide a simple and inexpensive method for removing solids from liquids, as well as separating two liquids according to their relative densities. They have widespread applications, including in areas such as environmental engineering and the petrochemical industry. Continual monitoring is essential in most industrial applications, since the input ﬂow rate is an important control parameter that can be adjusted to maximise the separation eﬃciency of the equipment. In addition, the high pressures that are often involved necessitate careful observation of the internal ﬂuid dynamics to ensure safety. However, direct observation of the internal ﬂow of the ﬂuids is diﬃcult or impossible due to, for example, the reinforced walls of the hydrocyclone and the opacity of the mixed component.

One possible technique for monitoring internal ﬂow in a hydrocyclone is electrical impedance tomography (EIT). This inherently statistical technique relates measurements of electrical potential taken on the exterior of the machine to the internal conductivity field of the liquid, via the repeated solution of a particular partial differential equation (PDE) model. Unfortunately, EIT methods are computationally intensive and are sensitive to numerical error in the solution of the PDE. It is therefore desirable to relax the statistical problem, in such a way that valid statistical inferences can be drawn at decreased computational cost.

This paper explores the role of probabilistic numerical methods in the monitoring of industrial equipment via EIT. As such, it represents one of the first serious industrial applications of probabilistic numerical methods. Results broadly supported the effectiveness of the statistical relaxation of PDE models that is provided by probabilistic numerical methods. On the other hand, this work highlighted a number of important issues that remain open, including the need to develop efficient alternatives to Markov chain Monte Carlo methods for posterior exploration and the need to address prior elicitation for models specified via a PDE.

- **Reference**: Oates CJ, Cockayne J, Robert GA. Bayesian Probabilistic Numerical Methods for Industrial Process Monitoring, arXiv:1707.06107.


## Semantic Information Pursuit for Multimodal Data Analysis ([MURI](http://vision.jhu.edu/infopursuit/))

### About
{:.no_toc}

In 1948 Shanon laid the foundations of information theory which
revolutionized statistics, physics, engineering, and computer science. A strong
limitation, however, is that the semantic content of data is not taken into
account. This research will produce a novel framework for characterizing
semantic information content in multimodal data. It will combine non-convex
optimization with advanced statistical methods, leading to new representation
learning algorithms, measures of uncertainty, and sampling methods. Given data
from a scene, the algorithms will be able find the most informative
representations of the data for a specific task. These methods will be applied
to complex datasets from real situations, including text, images, videos, sensor
signals, and cameras, resulting in intelligent decision based algorithms.

### Current work
{:.no_toc}

Our group is working on characertizing uncertainty in multimodal
representations. We will develop a statistical framework for characterizing the
uncertainty of the information representations using both frequentists and
Bayesian approaches. We will also develop efficient statistical sampling
methods, which will be useful for both characterizing uncertainty and performing
inference in the information pursuit framework.





## Other projects
### [EQUIP Project](https://warwick.ac.uk/fac/sci/maths/research/grants/equip/)
### [software populations approach to ubicomp systems design](http://softwarepopulations.com/index.html)

### Bayesian analysis of Raman spectroscopy

This research project aims to develop new methods for modelling and quantification of surface-enhanced Raman spectroscopy (SERS). Spectra are multivariate observations of the interaction between light and matter. Raman spectroscopy can be used to identify molecules such as DNA by the characteristic scattering of light from a laser. It is sensitive at very low concentrations and can accurately quantify the amount of a given molecule in a sample. Metallic nanoparticles are used in SERS to enhance the Raman signal. The presence of a large, nonuniform background presents a major challenge to analysis of these spectra.

This project is funded by an EPSRC programme grant (ref: EP/L014165/1)
 
https://www.slideshare.net/azeari/bayesian-modelling-and-computation-for-raman-spectroscopy


Collaborators on this project;
- Duncan Graham (University of Strathclyde)  - Principal Investigator
- Mark Girolami (Imperial & Turing)
- Karen Faulds (Strathclyde)
- Pasquale Maffia (Glasgow)
- Kirsten Gracie (Strathclyde)
- Matt Moores (Warwick)
- Jake Carson (Imperial)
- Steven Asiala (Strathclyde)
- Jonathan Noonan (Glasgow)


#### [Bayesian methods to detect dye-labelled DNA oligonucleotides in multiplexed Raman spectra](https://doi.org/10.1111/j.1467-9876.2010.00744.x)

Inferential methodologies are required which can deconvolve the observed mixture and infer the composition of distinct DNA sequences in the overall composite. Inferring the component spectra is posed as a model selection problem for a bilinear statistical model, and the Markov chain Monte Carlo inferential methodology required is developed. In particular, a Gibbs sampler and reversible jump Markov chain Monte Carlo (RJ-MCMC) methods are presented along with techniques based on estimation of the marginal likelihood.

- **Reference**: Zhong, M.; Girolami, M.; Faulds, K. & Graham, D. (2011)
Bayesian methods to detect dye-labelled DNA oligonucleotides in multiplexed
Raman spectra J. R. Stat. Soc. Ser. C, 60,
187-206. https://doi.org/10.1111/j.1467-9876.2010.00744.x

#### [Preferential attachment of specific fluorescent dyes and dye labelled DNA sequences in a SERS multiplex](http://pubs.acs.org/doi/abs/10.1021/acs.analchem.5b02776)


Here, the interaction of single stranded DNA labeled with either fluorescein (FAM) or tetramethylrhodamine (TAMRA) with a metal surface, using spermine induced aggregated silver nanoparticles as the SERS substrate, is investigated by analyzing the labels separately and in mixtures. When the two dyes are premixed prior to the addition of nanoparticles, TAMRA exerts a strong masking effect over FAM due to a stronger affinity for the metal surface. By using bootstrap estimation of changes in SERS peak intensity, a greater insight has been achieved into the surface affinity of the two dyes as well as how they interact with each other. It has been shown that the order of addition of the analytes is important and that specific dye related interactions occur, which could greatly affect the observed SERS spectra.

**Reference**: Gracie, K.; Moores, M.; Smith, W. E.; Harding, K.; Girolami, M.; Graham, D. & Faulds, K. (2016)
Preferential attachment of specific fluorescent dyes and dye labelled DNA sequences in a SERS multiplex
Anal. Chem., 88, 1147-1153. https://doi.org/10.1021/acs.analchem.5b02776

#### [Bayesian modelling and quantification of Raman spectroscopy](https://arxiv.org/abs/1604.07299)

We introduce a sequential Monte Carlo (SMC) algorithm to separate the observed spectrum into a series of peaks plus a smoothly-varying baseline, corrupted by additive white noise. The peaks are modelled as Lorentzian, Gaussian, or pseudo-Voigt functions, while the baseline is estimated using a penalised cubic spline. This latent continuous representation accounts for differences in resolution between measurements. The posterior distribution can be incrementally updated as more data becomes available, resulting in a scalable algorithm that is robust to local maxima.

**Preprint**: Moores, M.; Gracie, K.; Carson, J.; Faulds, K.; Graham, D. & Girolami, M.
Bayesian modelling and quantification of Raman spectroscopy
https://arxiv.org/abs/1604.07299

#### [Unbiased local solutions of partial differential equations via the Feynman-Kac Identities](https://arxiv.org/abs/1603.04196)

The Feynman-Kac formulae (FKF) express local solutions of partial differential equations (PDEs) as expectations with respect to some complementary stochastic differential equation (SDE). In this paper we utilize recent developments in two areas to demonstrate that it is now possible to obtain unbiased solutions for a wide range of PDE models via the FKF. The first is the development of algorithms that simulate diffusion paths exactly (without discretization error), and so make it possible to obtain Monte Carlo estimates of the FKF directly. The second is the development of debiasing methods for SDEs, enabling the construction of unbiased estimates from a sequence of biased estimates.

**Preprint**:
Carson, J.; Pollock, M. & Girolami, M.
Unbiased local solutions of partial differential equations via the Feynman-Kac Identities
https://arxiv.org/abs/1603.04196
