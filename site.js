(function () {
  "use strict";

  const curriculum = window.Curriculum;
  const stageOrder = ["Foundation", "Applied", "Capstone"];
  const stageCopy = {
    Foundation: "Build healthcare data you can trust, then choose and defend analytics that fit the decision.",
    Applied: "Use the same foundation across seven clinical, operational, research, population, and strategy decisions.",
    Capstone: "Approve a feasible proposal, then deliver one complete project for a real decision owner."
  };

  const escapeHtml = value => String(value).replace(/[&<>"']/g, character => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;"
  })[character]);

  const courseHref = course => `course.html?id=${encodeURIComponent(course.id)}`;
  const moduleHref = (course, module) => `module.html?course=${encodeURIComponent(course.id)}&week=${module.week}`;
  const findCourse = id => curriculum.courses.find(course => course.id === String(id || "").toUpperCase());

  function setVersion() {
    document.querySelectorAll("[data-version]").forEach(node => {
      node.textContent = curriculum.version;
    });
  }

  function renderRecovery(root, type) {
    document.title = `${type} not found | Open Clinical Learning Commons`;
    root.innerHTML = `
      <section class="recovery">
        <p class="eyebrow">Open Clinical Learning Commons</p>
        <h1>${escapeHtml(type)} not found</h1>
        <p>The link does not match the current curriculum roadmap. Return to the course list and choose a course or module.</p>
        <a class="primary-button" href="index.html">See all courses</a>
      </section>`;
  }

  function renderHome() {
    const catalog = document.querySelector("#catalog");
    let sequence = 0;
    catalog.innerHTML = stageOrder.map(stage => {
      const courses = curriculum.courses.filter(course => course.stage === stage);
      const cards = courses.map(course => {
        sequence += 1;
        return `
          <a class="course-card" style="--stage-color: ${stage === "Applied" ? "var(--cyan)" : stage === "Capstone" ? "var(--amber)" : "var(--blue)"}" data-sequence="${String(sequence).padStart(2, "0")}" href="${courseHref(course)}">
            <span class="course-code">${escapeHtml(course.id)} / ${escapeHtml(course.stage)}</span>
            <h3>${escapeHtml(course.title)}</h3>
            <p>${escapeHtml(course.summary)}</p>
            <span class="course-card-footer"><span>${course.modules.length} modules · ${course.credits} credits</span><span class="course-arrow" aria-hidden="true">→</span></span>
          </a>`;
      }).join("");

      return `
        <section class="stage-section" data-stage="${escapeHtml(stage)}" aria-labelledby="${stage.toLowerCase()}-heading">
          <div class="stage-heading">
            <div>
              <span class="stage-label">${escapeHtml(stage)} stage</span>
              <h2 id="${stage.toLowerCase()}-heading">${escapeHtml(stage)}</h2>
              <p>${escapeHtml(stageCopy[stage])}</p>
            </div>
            <span class="catalog-count">${courses.length} ${courses.length === 1 ? "course" : "courses"}</span>
          </div>
          <div class="course-grid">${cards}</div>
        </section>`;
    }).join("");

    console.assert(document.querySelectorAll(".course-card").length === 11, "The home page must show 11 courses.");
  }

  function renderCourse() {
    const root = document.querySelector("#course-root");
    const course = findCourse(new URLSearchParams(window.location.search).get("id"));
    if (!course) {
      renderRecovery(root, "Course");
      return;
    }

    document.title = `${course.id}: ${course.title} | Open Clinical Learning Commons`;
    const moduleLinks = course.modules.map(module => `
      <a class="module-link" href="${moduleHref(course, module)}">
        <span class="week-node">${module.week}</span>
        <span>
          <span class="module-kicker">Week ${module.week}</span>
          <h3>${escapeHtml(module.title)}</h3>
          <p>${escapeHtml(module.outcome)}</p>
        </span>
        <span class="module-arrow" aria-hidden="true">→</span>
      </a>`).join("");
    const relatedResource = course.modules.find(module => module.resource)?.resource;

    root.innerHTML = `
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="index.html">All courses</a><span aria-hidden="true">/</span><span>${escapeHtml(course.id)}</span>
      </nav>
      <section class="page-hero" data-code="${escapeHtml(course.id)}">
        <span class="eyebrow">${escapeHtml(course.stage)} course / ${escapeHtml(course.id)}</span>
        <h1>${escapeHtml(course.title)}</h1>
        <p class="page-summary">${escapeHtml(course.summary)}</p>
        <div class="fact-row" aria-label="Course details">
          <span class="fact-chip"><span class="fact-label">Credits</span><strong>${course.credits}</strong></span>
          <span class="fact-chip"><span class="fact-label">Format</span><strong>${escapeHtml(course.format)}</strong></span>
          <span class="fact-chip"><span class="fact-label">Modules</span><strong>${course.modules.length} weekly modules</strong></span>
        </div>
      </section>
      <div class="course-layout">
        <section aria-labelledby="module-list-heading">
          <div class="section-title">
            <span class="eyebrow">Course route</span>
            <h2 id="module-list-heading">Seven modules</h2>
            <p>Open a module to see its learning outcome, topics, required submission, and place in the course.</p>
          </div>
          <div class="module-list">${moduleLinks}</div>
        </section>
        <aside class="course-aside" aria-label="Course requirements">
          <section class="aside-card">
            <span class="fact-label">Prerequisites</span>
            <h2>Before you begin</h2>
            <p>${escapeHtml(course.prerequisites)}</p>
          </section>
          <section class="aside-card final-card">
            <span class="fact-label">Course finish line</span>
            <h2>Final deliverable</h2>
            <p>${escapeHtml(course.finalDeliverable)}</p>
          </section>
          ${relatedResource ? `<section class="aside-card"><span class="fact-label">Working lesson</span><h2>${escapeHtml(relatedResource.title)}</h2><p>${escapeHtml(relatedResource.description)}</p><a href="${escapeHtml(relatedResource.url)}">Open the lesson →</a></section>` : ""}
        </aside>
      </div>`;

    console.assert(root.querySelectorAll(".module-link").length === 7, `${course.id} must show seven modules.`);
  }

  function renderModule() {
    const root = document.querySelector("#module-root");
    const params = new URLSearchParams(window.location.search);
    const course = findCourse(params.get("course"));
    const week = Number(params.get("week"));
    const module = course?.modules.find(item => item.week === week);
    if (!course || !module) {
      renderRecovery(root, "Module");
      return;
    }

    document.title = `${course.id} Week ${module.week}: ${module.title} | Open Clinical Learning Commons`;
    const topics = module.topics.split(/,|;/).map(topic => topic.trim()).filter(Boolean);
    const previous = course.modules[module.week - 2];
    const next = course.modules[module.week];
    const progress = course.modules.map(item => `<span class="${item.week < module.week ? "complete" : item.week === module.week ? "current" : ""}"></span>`).join("");
    const miniRoute = course.modules.map(item => `
      <a href="${moduleHref(course, item)}" ${item.week === module.week ? 'aria-current="step"' : ""}>
        <span>${item.week}</span><span>${escapeHtml(item.title)}</span>
      </a>`).join("");

    root.innerHTML = `
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="index.html">All courses</a><span aria-hidden="true">/</span>
        <a href="${courseHref(course)}">${escapeHtml(course.id)}</a><span aria-hidden="true">/</span>
        <span>Week ${module.week}</span>
      </nav>
      <section class="module-hero" data-code="${escapeHtml(course.id)}">
        <span class="eyebrow">${escapeHtml(course.id)} / Module ${module.week} of 7</span>
        <h1>${escapeHtml(module.title)}</h1>
        <p class="module-outcome">${escapeHtml(module.outcome)}</p>
        <div class="fact-row" aria-label="Module details">
          <span class="fact-chip"><span class="fact-label">Course</span><strong>${escapeHtml(course.title)}</strong></span>
          <span class="fact-chip"><span class="fact-label">Workload</span><strong>${module.hours} hours</strong></span>
          <span class="fact-chip"><span class="fact-label">Status</span><strong>Roadmap ready</strong></span>
        </div>
        <div class="module-progress" aria-label="Module ${module.week} of 7">${progress}</div>
      </section>
      <div class="module-layout">
        <div class="module-main">
          <section class="content-card">
            <span class="fact-label">Learning outcome</span>
            <h2>What you will be able to do</h2>
            <p>${escapeHtml(module.outcome)}</p>
          </section>
          <section class="content-card">
            <span class="fact-label">Module topics</span>
            <h2>What this module covers</h2>
            <ul class="topic-list">${topics.map(topic => `<li>${escapeHtml(topic)}</li>`).join("")}</ul>
          </section>
          <section class="submission-card">
            <span class="fact-label">Required submission</span>
            <h2>What you will turn in</h2>
            <p>${escapeHtml(module.submission)}</p>
          </section>
          ${module.resource ? `<section class="resource-card"><span class="fact-label">Runnable learning asset</span><h2>${escapeHtml(module.resource.title)}</h2><p>${escapeHtml(module.resource.description)}</p><a class="primary-button" href="${escapeHtml(module.resource.url)}">Open the working lesson</a></section>` : `<section class="status-card"><span class="status-label">Build status</span><p>The roadmap, learning outcome, topics, and submission are ready. Readings, datasets, labs, assessments, and instructor materials are the next build layer for this module.</p></section>`}
          <nav class="module-navigation" aria-label="Module navigation">
            ${previous ? `<a href="${moduleHref(course, previous)}"><small>← Previous module</small><strong>${escapeHtml(previous.title)}</strong></a>` : `<span class="empty-nav"><small>Course start</small><strong>This is the first module.</strong></span>`}
            ${next ? `<a href="${moduleHref(course, next)}"><small>Next module →</small><strong>${escapeHtml(next.title)}</strong></a>` : `<span class="empty-nav"><small>Course finish</small><strong>This is the final module.</strong></span>`}
          </nav>
        </div>
        <aside class="module-aside" aria-label="Course context">
          <section class="aside-card">
            <span class="fact-label">Course context</span>
            <h2>${escapeHtml(course.id)}</h2>
            <p>${escapeHtml(course.title)}</p>
            <p><strong>Prerequisites:</strong><br>${escapeHtml(course.prerequisites)}</p>
            <a href="${courseHref(course)}">View the course →</a>
          </section>
          <section class="aside-card">
            <span class="fact-label">All seven modules</span>
            <h2>Course route</h2>
            <nav class="mini-route" aria-label="Modules in ${escapeHtml(course.id)}">${miniRoute}</nav>
          </section>
        </aside>
      </div>`;

    console.assert(root.querySelectorAll(".mini-route a").length === 7, "The module route must show seven modules.");
  }

  function init() {
    if (!curriculum) {
      throw new Error("Curriculum data was not loaded.");
    }
    setVersion();
    const page = document.body.dataset.page;
    if (page === "home") renderHome();
    if (page === "course") renderCourse();
    if (page === "module") renderModule();
    document.documentElement.dataset.ready = "true";
  }

  window.CommonsSite = { courseHref, moduleHref, findCourse };
  init();
})();
