(() => {
  "use strict";
  document.documentElement.classList.replace("no-js", "js");
  const menu = document.querySelector(".menu-toggle");
  menu?.addEventListener("click", () => {
    const expanded = menu.getAttribute("aria-expanded") !== "true";
    menu.setAttribute("aria-expanded", String(expanded));
    document.querySelector(".site-header").classList.toggle("menu-open", expanded);
  });
  document.querySelectorAll("#primary-nav a").forEach((a) => a.addEventListener("click", () => {
    menu?.setAttribute("aria-expanded", "false");
    document.querySelector(".site-header").classList.remove("menu-open");
  }));
  const lessons = [...document.querySelectorAll("[data-lesson]")];
  const search = document.querySelector("#course-search");
  const phase = document.querySelector("#phase-filter");
  function filterLessons() {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    for (const card of lessons) {
      const show = card.dataset.search.includes(query) && (phase.value === "all" || card.dataset.phase === phase.value);
      card.hidden = !show;
      if (show) count++;
    }
    document.querySelectorAll("[data-phase-group]").forEach((group) => {
      group.hidden = ![...group.querySelectorAll("[data-lesson]")].some((card) => !card.hidden);
    });
    document.querySelector("#filter-count").textContent = `${count} lesson${count === 1 ? "" : "s"} shown`;
    document.querySelector("#no-lessons").hidden = count !== 0;
  }
  search?.addEventListener("input", filterLessons);
  phase?.addEventListener("change", filterLessons);
  document.querySelector("#reset-course")?.addEventListener("click", () => {
    search.value = "";
    phase.value = "all";
    filterLessons();
  });
  const resources = [...document.querySelectorAll("[data-resource]")];
  const resourceSearch = document.querySelector("#library-search");
  const kind = document.querySelector("#kind-filter");
  function filterResources() {
    const query = resourceSearch.value.trim().toLocaleLowerCase();
    let count = 0;
    for (const row of resources) {
      const show = row.dataset.search.includes(query) && (kind.value === "all" || row.dataset.kind === kind.value);
      row.hidden = !show;
      if (show) count++;
    }
    document.querySelector("#resource-count").textContent = `${count} kit${count === 1 ? "" : "s"} shown`;
    document.querySelector("#no-resources").hidden = count !== 0;
  }
  resourceSearch?.addEventListener("input", filterResources);
  kind?.addEventListener("change", filterResources);
  const key = "kh-ai-academy-reviewed-v1";
  const validIds = new Set(Array.from({ length: 24 }, (_, i) => `week-${String(i + 1).padStart(2, "0")}`));
  let reviewed = new Set();
  let storageAvailable = true;
  const notice = document.querySelector("#storage-notice");
  if (location.protocol === "file:" && notice) {
    notice.textContent = "Offline file mode: browsers may keep review marks per page. Mark and export the complete checklist on the course map, or serve this folder locally for shared marks.";
  }
  function storageWarning(message, error) {
    storageAvailable = false;
    if (notice) notice.textContent = message;
    console.warn(message, error);
  }
  if (document.querySelector("[data-review]")) {
    try {
      const raw = localStorage.getItem(key);
      if (raw !== null) {
        const values = JSON.parse(raw);
        if (!Array.isArray(values) || values.some((value) => !validIds.has(value))) {
          storageWarning("Saved review data is invalid. Marks are session-only until you reset this browser’s review marks.");
        } else {
          reviewed = new Set(values);
        }
      }
    } catch (error) {
      if (error instanceof SyntaxError || error instanceof DOMException) {
        storageWarning("Review storage is unavailable or unreadable. Your marks apply to this page session only; use Export on the course map to keep a copy.", error);
      } else {
        throw error;
      }
    }
  }
  function updateReview() {
    document.querySelectorAll("[data-review]").forEach((button) => {
      const active = reviewed.has(button.dataset.review);
      button.setAttribute("aria-pressed", String(active));
      button.textContent = active ? "Reviewed · undo" : "Mark reviewed";
    });
    const count = document.querySelector("#review-count");
    if (count) count.textContent = `${reviewed.size} / 24`;
  }
  function save() {
    if (!storageAvailable) return;
    try {
      localStorage.setItem(key, JSON.stringify([...reviewed]));
    } catch (error) {
      if (error instanceof DOMException) {
        storageWarning("This browser could not save your review marks. They remain session-only; export a checklist to keep a copy.", error);
      } else {
        throw error;
      }
    }
  }
  document.querySelectorAll("[data-review]").forEach((button) => button.addEventListener("click", () => {
    const id = button.dataset.review;
    if (reviewed.has(id)) reviewed.delete(id);
    else reviewed.add(id);
    save();
    updateReview();
  }));
  document.querySelector("#reset-progress")?.addEventListener("click", () => {
    if (!confirm("Remove only this programme’s self-reported review marks from this browser?")) return;
    try {
      localStorage.removeItem(key);
      storageAvailable = true;
      if (notice) notice.textContent = "Local review marks reset. No grades or server records were changed.";
    } catch (error) {
      if (error instanceof DOMException) storageWarning("The browser could not clear stored review marks. This page can still be used without saved progress.", error);
      else throw error;
    }
    reviewed = new Set();
    updateReview();
  });
  document.querySelector("#export-progress")?.addEventListener("click", () => {
    const rows = [["Week", "Title", "Self-reported review", "Not an assessment result"]];
    for (const card of lessons) {
      rows.push([card.dataset.review || card.querySelector("[data-review]").dataset.review,
        card.querySelector("h3").textContent.trim(),
        reviewed.has(card.querySelector("[data-review]").dataset.review) ? "Reviewed" : "Not marked",
        "Instructor assessment and release approval are separate"]);
    }
    const csv = rows.map((row) => row.map((value) => `"${String(value).replaceAll('"', '""')}"`).join(",")).join("\r\n");
    const url = URL.createObjectURL(new Blob(["\ufeff", csv], { type: "text/csv;charset=utf-8" }));
    const link = document.createElement("a");
    link.href = url;
    link.download = "ai-programme-review-checklist.csv";
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
  document.querySelectorAll(".print-button").forEach((button) => button.addEventListener("click", () => window.print()));
  updateReview();
})();
