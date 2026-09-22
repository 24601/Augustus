---
layout: default
title: "Build and improve decision-model systems with AI agents"
permalink: /
page_class: home
---

<section class="hero" aria-labelledby="hero-title">
  <div>
    <p class="kicker hero-reveal" style="--d: 0ms">Version 0.7.0</p>
    <h1 id="hero-title" class="hero-title">
      <span class="line hero-reveal" style="--d: 50ms">Place judgment.</span>
      <span class="line hero-reveal" style="--d: 110ms">Keep authority explicit.</span>
    </h1>
    <p class="lede hero-reveal" style="--d: 180ms">
      Augustus helps agents find, build, evaluate, and improve systems with decision models.
      TypeSafe Jev Choice/Score/Noul is the default hosted exemplar; code,
      policy, and people keep ownership of exact work and consequential action.
    </p>
    <div class="cta-row hero-reveal" style="--d: 250ms">
      <a class="btn btn-primary" href="https://github.com/24601/Augustus#install">Install the skill</a>
      <a class="btn btn-ghost" href="{{ '/examples.html' | relative_url }}">See an example</a>
      <a class="btn btn-ghost" href="{{ '/ecosystem.html' | relative_url }}">Ecosystem</a>
    </div>
  </div>
  <aside class="hero-card panel hero-reveal" style="--d: 320ms" aria-hidden="true">
    <p class="hero-card-label">Placement</p>
    <div class="skel-row">
      <span class="skel-bar skel-bar-short"></span>
      <span class="skel-bar"></span>
    </div>
    <div class="skel-row skel-row-active">
      <span class="token">Choice</span>
      <span class="skel-bar skel-bar-mid"></span>
    </div>
    <div class="skel-row">
      <span class="token">Score</span>
      <span class="skel-bar skel-bar-short"></span>
    </div>
    <div class="skel-row">
      <span class="token">Noul</span>
      <span class="skel-bar skel-bar-mid"></span>
    </div>
  </aside>
</section>

{% include comparison.html %}
{% include recipes.html %}

<section class="section" aria-labelledby="what-title">
  <div class="section-head">
    <p class="kicker">What it is</p>
    <h2 id="what-title">From decision models to working systems and evals</h2>
    <p>
      Named for Augustus De Morgan, the skill frames decisions across software,
      business, organizations, and everyday life. It connects evidence to a
      narrow judgment, implements a testable composition, and improves it
      against observed outcomes. The model may rank, score, or classify; exact
      computation, permissions, side effects, and final accountability remain
      with code or people.
    </p>
    <p>
      Start with the
      <a href="https://github.com/24601/Augustus/blob/main/.agents/skills/augustus/SKILL.md">primary skill</a>
      and its focused references. The
      <a href="https://github.com/24601/Augustus/tree/main/research">research archive</a>
      preserves broader history and evidence without expanding the runtime
      instructions. Augustus is an independent project, not a TypeSafe product.
    </p>
  </div>
</section>

<section class="section" aria-labelledby="install-title">
  <div class="section-head">
    <p class="kicker">Install</p>
    <h2 id="install-title">Install the skill</h2>
    <p>
      Use the marketplace with Claude Code, or add the skill to any compatible
      agent. The current release is 0.7.0.
      These commands follow the default branch; review the installed version
      before relying on it. The skill itself needs no API key. Calling a hosted
      model is a separate, optional integration.
    </p>
  </div>
  <div class="install-grid">
    <div class="install-card panel">
      <h3>Claude Code</h3>
<pre><code>claude plugin marketplace add 24601/Augustus
claude plugin install augustus@augustus</code></pre>
    </div>
    <div class="install-card panel">
      <h3>skills.sh / npx</h3>
<pre><code>npx skills add 24601/Augustus --skill augustus</code></pre>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="try-title">
  <div class="section-head">
    <p class="kicker">First useful result</p>
    <h2 id="try-title">Bring one real workflow</h2>
    <p>After installation, ask: “Use Augustus to audit our refund-email workflow.
      Find one useful classifier insertion, keep eligibility and payments in
      code, and propose a test that could reject the change.”</p>
    <p>Advice yields a design card; build requests yield working policy and evals;
      improvement requests yield a bounded, outcome-tested iteration loop.
      <a href="{{ '/examples.html' | relative_url }}">Read two worked examples</a>
      or <a href="https://github.com/24601/Augustus/issues/new/choose">report a confusing recommendation</a>.
      A parser, checklist, or no new model can be the right answer.</p>
  </div>
</section>

<section class="section" aria-labelledby="pillars-title">
  <div class="section-head">
    <p class="kicker">Working method</p>
    <h2 id="pillars-title">Four moves from question to outcome</h2>
    <p>
      Keep each move small enough to inspect. Use evidence from the intended
      workflow, including ordinary, ambiguous, and adverse cases.
    </p>
  </div>
  <div class="card-grid">
    <article class="card panel">
      <p class="kicker">Frame</p>
      <h3>Name the decision</h3>
      <p>
        Define the desired behavior, current baseline, available evidence, and
        cost of each kind of error.
      </p>
    </article>
    <article class="card panel">
      <p class="kicker">Place</p>
      <h3>Assign the narrow judgment</h3>
      <p>
        Choose a family whose output semantics fit the action, and keep exact
        rules, calculations, and transformations in deterministic code.
      </p>
    </article>
    <article class="card panel">
      <p class="kicker">Govern</p>
      <h3>Make policy and authority explicit</h3>
      <p>
        Specify thresholds or bands, fallback behavior, permissions, human
        review, and the checks that run before an effect occurs.
      </p>
    </article>
    <article class="card panel">
      <p class="kicker">Validate</p>
      <h3>Measure the workflow outcome</h3>
      <p>
        Test held-out cases, compare with a simpler baseline, inspect failures,
        and record whether the checked action improved the real outcome.
      </p>
    </article>
  </div>
</section>

<section class="section" aria-labelledby="companions-title">
  <div class="section-head">
    <p class="kicker">Resources</p>
    <h2 id="companions-title">Contracts, method, and evidence</h2>
    <p>Use current contracts for implementation and project evidence for design choices.</p>
  </div>
  <ul class="companion-list">
    <li>
      <a class="panel" href="https://github.com/typesafe-ai/skills">
        <strong>TypeSafe skills</strong>
        <span>Current Jev integration contracts and usage guidance.</span>
      </a>
    </li>
    <li>
      <a class="panel" href="https://github.com/24601/Augustus/tree/main/.agents/skills/augustus/references">
        <strong>Augustus references</strong>
        <span>Focused guidance for class selection, boundaries, and validation.</span>
      </a>
    </li>
    <li>
      <a class="panel" href="{{ '/ecosystem.html' | relative_url }}">
        <strong>Ecosystem and archive</strong>
        <span>A navigable family map with evidence labels and historical research.</span>
      </a>
    </li>
  </ul>
  <p class="meta-line">Current release 0.7.0 · <a href="{{ '/release-notes-v0.7.0.html' | relative_url }}">Release notes</a>.</p>
</section>
