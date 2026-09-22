---
layout: default
title: "Build and improve decision-model systems with AI agents"
permalink: /
page_class: home
---

<section class="opening" aria-labelledby="hero-title">
  <p class="opening-context">An open-source skill for agents</p>
  <h1 id="hero-title">Decision models,<br class="desktop-break"> put to work.</h1>
  <div class="opening-bottom">
    <p class="lede">Give your agent the methods to find a useful judgment,
      build the policy and evals around it, and improve against real outcomes.</p>
    <div class="opening-actions">
      <a class="button" href="#install">Install Augustus <span aria-hidden="true">↓</span></a>
      <a href="{{ '/examples.html' | relative_url }}">Read a worked example</a>
    </div>
  </div>
</section>

{% include comparison.html %}

<section class="working-index" id="recipes" aria-labelledby="recipes-title">
  <div class="index-intro">
    <h2 id="recipes-title">Bring a decision.<br class="wide-break"> Leave with a system.</h2>
    <p>Augustus is a skill and method engine, not a hosted runtime. Agents use it
      across software, business, organizations, and everyday decisions.</p>
    <p>Advice produces a design card. Build requests produce working policy and
      evals. Improvement requests produce a bounded, outcome-tested iteration.</p>
    <a href="{{ '/placements.html' | relative_url }}">Explore six model placements</a>
  </div>
  <dl class="task-index">
    <div>
      <dt>Route, rank, or classify</dt>
      <dd>Put a narrow judgment inside a workflow whose permissions, exact work,
        and fallback remain explicit.</dd>
    </div>
    <div>
      <dt>Build an evaluation</dt>
      <dd>Define the baseline, error costs, held-out cases, and a test that could
        reject the proposed change.</dd>
    </div>
    <div>
      <dt>Improve a Software 3.0 system</dt>
      <dd>Compose decision models, run bounded prompt or program hill climbing,
        and confirm gains on protected evidence.</dd>
    </div>
    <div>
      <dt>Make a human tradeoff legible</dt>
      <dd>Connect uncertain evidence to explicit criteria and constraints.
        Keep values and the final decision with people.</dd>
    </div>
  </dl>
</section>

<aside class="useful-no" aria-labelledby="no-title">
  <h2 id="no-title">Sometimes the right model is no model.</h2>
  <p>If validated dates settle whether an invoice is late, compare dates in code.
    A parser, checklist, or existing human process can be the better design.</p>
</aside>

<section class="installation" id="install" aria-labelledby="install-title">
  <div class="installation-intro">
    <h2 id="install-title">Put it in your agent’s hands.</h2>
    <p>The skill needs no API key. Calling a hosted model is a separate,
      optional integration.</p>
    <p>Current release: <a href="{{ '/release-notes-v0.7.0.html' | relative_url }}">0.7.0</a>.
      These commands follow the default branch; check the installed version
      before relying on it.</p>
  </div>
  <div class="install-options">
    <section aria-labelledby="claude-install">
      <h3 id="claude-install">Claude Code</h3>
<pre tabindex="0" role="region" aria-label="Claude Code installation commands"><code>claude plugin marketplace add 24601/Augustus

claude plugin install augustus@augustus</code></pre>
    </section>
    <section aria-labelledby="skills-install">
      <h3 id="skills-install">Other compatible agents</h3>
<pre tabindex="0" role="region" aria-label="Skills CLI installation command"><code>npx skills add 24601/Augustus --skill augustus</code></pre>
    </section>
    <p class="install-help"><a href="https://github.com/24601/Augustus#install">All installation options and version checks</a></p>
  </div>
</section>

<section class="first-prompt" aria-labelledby="try-title">
  <h2 id="try-title">Start with one real workflow.</h2>
  <blockquote>
    <p>Use Augustus to audit our refund-email workflow. Test whether a classifier
      helps, keep eligibility and payments in code, and build an eval that could
      reject the change. Keep the current baseline if it works better.</p>
  </blockquote>
  <p>Bring your evidence, constraints, and current baseline.
    <a href="{{ '/examples.html' | relative_url }}">See the expected design card</a>
    or <a href="https://github.com/24601/Augustus/issues/new/choose">report a confusing recommendation</a>.</p>
</section>

<section class="reading" aria-labelledby="companions-title">
  <div>
    <h2 id="companions-title">The method stays inspectable.</h2>
    <p>Mathematical and scientific methods provide structure; real outcomes decide
      which compositions survive. Research is evidence to reason from, not a
      catalog to imitate.</p>
    <p>TypeSafe Jev Choice/Score/Noul is the default hosted exemplar, not the whole
      class. Augustus is an independent project, not a TypeSafe product.</p>
  </div>
  <ul class="reading-links">
    <li><a href="https://github.com/24601/Augustus/blob/main/.agents/skills/augustus/SKILL.md">Read the skill</a><span>The agent’s entry point</span></li>
    <li><a href="https://github.com/24601/Augustus/tree/main/.agents/skills/augustus/references">Methods and composition</a><span>Focused implementation guidance</span></li>
    <li><a href="{{ '/ecosystem.html' | relative_url }}">Decision-model ecosystem</a><span>Families, contracts, and evidence</span></li>
    <li><a href="https://github.com/24601/Augustus/tree/main/research">Research archive</a><span>Sources, revisions, and reassessment</span></li>
  </ul>
</section>
