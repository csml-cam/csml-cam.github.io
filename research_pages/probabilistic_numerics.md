---
title: "Probabilistic Numerics"
layout: page
author_profile: false
sitemap: true
permalink: /research_pages/probabilistic_numerics.html
---

Table of contents:

* TOC
{:toc}

Probabilistic numerical methods are a set of tools to solve numerical analysis
problems from the point of view of statistical inference. Our work mostly
focuses on Bayesian numerical methods, which are motivated by their uncertainty
quantification properties for the output of numerical methods. The group has
significantly advanced the field in research years, with work on the foundations
of probabilistic numerics, on methodology for quadrature, ODE solvers and PDE
solvers, and on applications to complex engineering problems.

An overview of the field can be found on the following website: [probabilistic-numerics.org](http://www.probabilistic-numerics.org/)/

## Foundations

### [Bayesian Probabilistic Numerical Methods](https://epubs.siam.org/doi/pdf/10.1137/17M1139357)
This paper identifies Bayesian probabilistic numerical methods as a particular class of noiseless Bayesian inversion problems. It is shown that, while many PN methods incorporate Bayesian ideas, the resulting posterior distribution is seldom fully Bayesian by this definition. Nevertheless, under remarkably general conditions there always exists an essentially unique Bayesian probabilistic numerical method for a particular problem, although the posterior distribution is often intractable.

Secondly, analogues are drawn with the fields of information-based complexity and average-case analysis, in a discussion of performance analysis for Bayesian PNM. It is shown that, where an average-case optimal numerical method is known for a particular problem, the posterior mean of an equivalent Bayesian PNM will naturally coincide with this point estimate, a result often commented on in other works (see the integration and PDE sections). However, it is also shown that there are situations in which optimal information for Bayesian PNM and average-case optimal information do not coincide.

Thirdly, the numerical disintegration algorithm is constructed to allow exploration of the intractable posterior distributions which often arise from Bayesian PNM. Numerical disintegration is an algorithm which approximates the true Bayesian distribution with samples from a tractable distribution close to the truth in an appropriate probability metric. Theoretical results are presented showing convergence of the numerical disintegration scheme in a limiting sense. This approach is applied to several challenging numerical problems, including Painleve’s first transcendental.

Lastly, the composition of PN methods into pipelines is discussed. Many numerical problems require the solution of multiple interdependent systems. Conditions are established for the output of such pipelines to be Bayesian, when the composite numerical methods are Bayesian PNM. This methodology is then applied to a prototypical pipeline, given by a challenging problem in industrial process monitoring.

- **Reference**: Cockayne, Jon, Chris J. Oates, T. J. Sullivan, and Mark Girolami. 2019. ‘Bayesian Probabilistic Numerical Methods’. SIAM Review 61 (3): 756–789. https://doi.org/10.1137/17m1139357.
- [arXiv reference](https://arxiv.org/abs/1702.03673)




## Integration

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


### [Frank-Wolfe Bayesian Quadrature: Probabilistic Integration with Theoretical Guarantees](https://papers.nips.cc/paper/5749-frank-wolfe-bayesian-quadrature-probabilistic-integration-with-theoretical-guarantees)

This paper provides a method of efficiently choosing design points for Bayesian Quadrature, based on a convex optimisation algorithm called the Frank-Wolfe algorithm. This algorithm can efficiently spread the points around the domain of integration where most of the measure is located. It is also the first probabilistic integration algorithm which has theoretical guarantees in the form of rates of convergence and contraction of the posterior probability distribution of Bayesian Quadrature.

See a nice [blog review by Ingmar Schuster](https://ingmarschuster.wordpress.com/2015/10/26/frank-wolfe-bayesian-quadrature/).

- **Reference**: Briol, F-X., Oates, C. J., Girolami, M., & Osborne, M. A. (2015). Frank-Wolfe Bayesian Quadrature: Probabilistic Integration with Theoretical Guarantees. Advances In Neural Information Processing Systems (NIPS), pages 1162-1170.
- [arXiv link](https://arxiv.org/pdf/1506.02681v2.pdf).


### [Probabilistic Integration: A Role for Statisticians in Numerical Analysis?](https://projecteuclid.org/euclid.ss/1555056025)

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


### [Probabilistic Models for Integration Error in the Assessment of Functional Cardiac Models](https://papers.nips.cc/paper/2017/hash/98dce83da57b0395e163467c9dae521b-Abstract.html)

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


<div class="videoWrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/SrrO4OxydO0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### [On the Sampling Problem for Kernel Quadrature](http://proceedings.mlr.press/v70/briol17a)

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



## Partial Differential Equations

### [Probabilistic Numerical Methods for Partial Differential Equations and Bayesian Inverse Problems](https://arxiv.org/abs/1605.07811)

This paper contributes a Bayesian probabilistic numerical method for linear and nonlinear partial differential equations (PDEs) and studies incorporation of the posterior measure produced into Bayesian inversion problems, in a prototypical pipeline of computation.

The central contribution is a probabilistic numerical method for linear PDEs. It is shown that when the PDE is linear and the prior measure on the solution is Gaussian with an appropriate covariance function, the posterior measure produced is also Gaussian and has a closed form. Furthermore, the posterior mean of this measure is identical to the point estimate of the solution produced by symmetric collocation.  This allows a transfer of convergence results from that work. New results are also developed surrounding the concentration of the posterior measure as the fidelity of the approximation is increased.

The second contribution of the paper is to propagate the uncertainty from the forward solver into the posterior measure over the solution of PDE-constrained Bayesian inverse problems. It is shown that when the posterior uncertainty over the forward solution is marginalised in the likelihood of the Bayesian inverse problem, the resultant posterior measure for the inverse problem rigorously accounts for the uncertainty resulting from an intractable forward solution. This allows for a cheap, approximate solution to the PDE to be used, which can reduce the computational time required for these challenging problems. The approach is applied to Electrical Impedance Tomography, a PDE-constrained inverse problem in medical imaging.

Lastly, posterior measures are constructed for a certain class of semilinear PDEs, such as the steady-state Allen-Cahn equation, a PDE known to exhibit multiple solutions. While the method proposed is heavily dependent on the form of the PDE, it illustrates how PN methods might be applied to other challenging nonlinear problems for which discretisation error is highly significant.

- **Reference 1**: Probabilistic Numerical Methods for PDE-constrained Bayesian Inverse Problems. Cockayne, J., Oates, C. J., Sullivan, T., Girolami, M. Proceedings of the 36th International Workshop on Bayesian Inference and Maximum Entropy Methods in Science and Engineering.
- **Reference 2**: Probabilistic Meshless Methods for Partial Differential Equations and Bayesian Inverse Problems. Cockayne, J., Oates, C. J., Sullivan, T., Girolami, M., arXiv:1605.07811.
- [An introduction to probabilistic meshless methods](https://www.pathlms.com/siam/courses/4150/sections/5835/video_presentations/42666)


## Ordinary Differential Equations

This site accompanies our recent publication, Probability Measures for Numerical Solutions of Differential Equations. It proposes a new strategy for randomising existing solvers for ordinary and partial differential equations, which rigorously models the uncertainty introduced by the numerical methods. This correct handling of uncertainty is crucial when numerical solvers are used for statistical analysis, for example, in Bayesian inference. This work is part of the emerging field of Probabilistic Numerics, which frames numerical methods as statistical inference tasks, allowing the tools of statistics to be combined with classical numerical analysis.

- [arXiv link](http://arxiv.org/abs/1506.04592)
- [presentation](/_support_files/research/monte_carlo/pn/conrad_warwicknumerics_2015.pdf)
- [Code on bitbucket](https://bitbucket.org/prconrad/pints)

## Applications

### [Bayesian Probabilistic Numerical Methods for Industrial Process Monitoring](https://arxiv.org/abs/1707.06107)

Hydrocyclones provide a simple and inexpensive method for removing solids from liquids, as well as separating two liquids according to their relative densities. They have widespread applications, including in areas such as environmental engineering and the petrochemical industry. Continual monitoring is essential in most industrial applications, since the input ﬂow rate is an important control parameter that can be adjusted to maximise the separation eﬃciency of the equipment. In addition, the high pressures that are often involved necessitate careful observation of the internal ﬂuid dynamics to ensure safety. However, direct observation of the internal ﬂow of the ﬂuids is diﬃcult or impossible due to, for example, the reinforced walls of the hydrocyclone and the opacity of the mixed component.

One possible technique for monitoring internal ﬂow in a hydrocyclone is electrical impedance tomography (EIT). This inherently statistical technique relates measurements of electrical potential taken on the exterior of the machine to the internal conductivity field of the liquid, via the repeated solution of a particular partial differential equation (PDE) model. Unfortunately, EIT methods are computationally intensive and are sensitive to numerical error in the solution of the PDE. It is therefore desirable to relax the statistical problem, in such a way that valid statistical inferences can be drawn at decreased computational cost.

This paper explores the role of probabilistic numerical methods in the monitoring of industrial equipment via EIT. As such, it represents one of the first serious industrial applications of probabilistic numerical methods. Results broadly supported the effectiveness of the statistical relaxation of PDE models that is provided by probabilistic numerical methods. On the other hand, this work highlighted a number of important issues that remain open, including the need to develop efficient alternatives to Markov chain Monte Carlo methods for posterior exploration and the need to address prior elicitation for models specified via a PDE.

- **Reference**: Oates CJ, Cockayne J, Robert GA. Bayesian Probabilistic Numerical Methods for Industrial Process Monitoring, arXiv:1707.06107.

