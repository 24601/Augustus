---
layout: default
title: "Augustus: System One decision judgment"
permalink: /
page_class: home
---

<section class="hero" aria-labelledby="hero-title">
  <div>
    <p class="kicker hero-reveal" style="--d: 0ms">v0.4.0, System One</p>
    <h1 id="hero-title" class="hero-title">
      <span class="line hero-reveal" style="--d: 50ms">Place judgment.</span>
      <span class="line hero-reveal" style="--d: 110ms">Keep proof exact.</span>
    </h1>
    <p class="lede hero-reveal" style="--d: 180ms">
      Agent skill for placing TypeSafe Jev Choice/Score/Noul with classical
      decision methods, composition algebra, and a validation gate.
    </p>
    <div class="cta-row hero-reveal" style="--d: 250ms">
      <a class="btn btn-primary" href="https://github.com/24601/Augustus#install">Install the skill</a>
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

<section class="section" aria-labelledby="what-title">
  <div class="section-head">
    <p class="kicker">What it is</p>
    <h2 id="what-title">A gate for where judgment belongs</h2>
    <p>
      Augustus is named for Augustus De Morgan, mentor of William Stanley
      Jevons. TypeSafe Jev is the documented exemplar, not the monopoly.
      Exact work stays in code or policy. The model owns narrow judgment.
      A soft Noul is not a proof. The atlas lives in
      <a href="https://github.com/24601/Augustus/tree/main/.agents/skills/augustus"><code>.agents/skills/augustus/</code></a>
      and <a href="https://github.com/24601/Augustus/blob/main/research/notes.md"><code>research/notes.md</code></a>.
      This page is a gate, not a rewrite of the
      <a href="https://github.com/24601/Augustus">repository README</a>.
    </p>
  </div>
</section>

<section class="section" aria-labelledby="install-title">
  <div class="section-head">
    <p class="kicker">Install</p>
    <h2 id="install-title">Two paths</h2>
    <p>Claude Code via the marketplace, or any skills-compatible agent.</p>
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

<section class="section" aria-labelledby="pillars-title">
  <div class="section-head">
    <p class="kicker">Pillars</p>
    <h2 id="pillars-title">Four placements, then a family</h2>
    <p>
      Pick the pillar from the hole, then the family, then the vendor.
      Ranking is not calibration. A soft Noul is not a hard gate.
    </p>
  </div>
  <div class="card-grid">
    <article class="card panel">
      <p class="kicker">Placement</p>
      <h3>Pillar, family, fail polarity</h3>
      <p>
        Name where judgment sits, which family matches the action, fail-open
        vs fail-closed, and the experiment that could prove the design wrong.
      </p>
    </article>
    <article class="card panel">
      <p class="kicker">Classical methods</p>
      <h3>Mental models, not a vendor how-to</h3>
      <p>
        Expected utility, abstention, VOI, MCDA, signal detection,
        search and control, Leveson-style org and safety. Across AI,
        software, business, knowledge work, and life.
      </p>
    </article>
    <article class="card panel">
      <p class="kicker">Formal methods</p>
      <h3>Proof stays proof</h3>
      <p>
        Alloy, TLA+, contracts, DST (Antithesis, Resonate, PufferLib).
        A Noul is a sensor. Never launder it as a proof.
      </p>
    </article>
    <article class="card panel">
      <p class="kicker">Validation</p>
      <h3>A gate, not a scoreboard</h3>
      <p>
        Harbor and jevals practice: Score is 0..n-1. Noul has no confidence
        field. 0.85 / minProbability is not a hard Harbor gate. VERIFY needs
        discriminating evidence.
      </p>
    </article>
  </div>
</section>

<section class="section" aria-labelledby="companions-title">
  <div class="section-head">
    <p class="kicker">Companions</p>
    <h2 id="companions-title">Contracts, integrity, atlas</h2>
    <p>Not a TypeSafe product. Augustus owns placement. Neighbors own their jobs.</p>
  </div>
  <ul class="companion-list">
    <li>
      <a class="panel" href="https://github.com/typesafe-ai/skills">
        <strong>typesafe-ai skill</strong>
        <span>Official Jev integration contracts. Read live docs before writing API code.</span>
      </a>
    </li>
    <li>
      <a class="panel" href="https://github.com/24601/rh-guard">
        <strong>rh-guard</strong>
        <span>Integrity and reward-hack companion. Soft Noul is not a hard safety bar.</span>
      </a>
    </li>
    <li>
      <a class="panel" href="{{ '/ecosystem.html' | relative_url }}">
        <strong>Ecosystem index</strong>
        <span>Launch-week class snapshot plus neighbors. Jev is the densest public corpus, not the monopoly.</span>
      </a>
    </li>
  </ul>
  <p class="meta-line">Last updated 2026-09-20 (v0.4.0).</p>
</section>
