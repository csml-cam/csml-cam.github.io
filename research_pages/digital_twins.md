---
title: "Digital Twins"
layout: page
author_profile: false
sitemap: true
use_math: true
permalink: /research_pages/digital_twins.html
---

Table of contents:

* TOC
{:toc}

## Statistical Finite Elements

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


## Future of Farming

Mark Girolami is involved in the project of creating a digital twin of an underground farm in London.
For more information visit:
1. [A recent publication in the Data-centric engineering journal](https://doi.org/10.1017/dce.2020.21).
2. [The farm website](http://growing-underground.com/)
3. [Coverage by University of Cambridge](http://www.eng.cam.ac.uk/news/cambridge-engineers-unveil-digital-twin-support-future-farming)
4. [A story-format coverage by University of Cambridge website](https://www.cam.ac.uk/stories/growingunderground)


## Additive manufacturing

Mark Girolami is one of the collaborators on the 3D-printed smart bridge in Amsterdam. For information about the project, visit [MX3D website](https://mx3d.com/). In July 2021, the bridge has been successfully installed and is now collecting usage data. This event has been covered in the [New Scientist](https://www.newscientist.com/article/2283934-worlds-first-3d-printed-steel-bridge-opens-in-amsterdam/) magazine.


The video below shows the digital twin of the bridge in the Autodesk software.
<video autoplay="autoplay" loop="loop" width="100%" height="auto" controls>
  <source src="/_support_files/research/mx3d/mx3d_bridge_autodesk_digital_twin_sensor.mp4" type="video/mp4">
</video>


## Aerospace-engineering applications

The data-centric engineering programme at the Alan Turing Institute
which is led by Mark Girolami is working on improving design of jet
engines.  For more details, visit the [Turing
page](https://www.turing.ac.uk/research/impact-stories/streamlining-jet-engine-design-and-manufacture).



## Talks


**September 2020**: Prof Mark Girolami gave a keynote talk title "Digital Twins: The Sense and Statistics" at the conference of Royal Statistical Society:
<div class="videoWrapper">
  <!-- Copy & Pasted from YouTube -->
  <iframe width="560" height="349" src="https://www.youtube-nocookie.com/embed/cWIJNXQn8LI" frameborder="0" allowfullscreen></iframe>
</div>