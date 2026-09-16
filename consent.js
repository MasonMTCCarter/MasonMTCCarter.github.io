(function () {
  "use strict";

  var CONSENT_KEY = "littlewonder:pinterest-consent:v1";
  var ACCEPTED = "accepted";
  var REJECTED = "rejected";
  var PINTEREST_URL = "https://s.pinimg.com/ct/core.js";
  var PINTEREST_ID = "2613241918623";
  var consent = null;
  var pinterestStarted = false;
  var pageVisitSent = false;
  var trackingEnabled = false;

  function readConsent() {
    try {
      var stored = window.localStorage.getItem(CONSENT_KEY);
      return stored === ACCEPTED || stored === REJECTED ? stored : null;
    } catch (error) {
      console.warn("Pinterest consent storage is unavailable; tracking will remain disabled until a choice is made for this page.", error);
      return null;
    }
  }

  function saveConsent(value) {
    try {
      window.localStorage.setItem(CONSENT_KEY, value);
    } catch (error) {
      console.warn("Pinterest consent could not be saved; this choice applies only to the current page.", error);
    }
  }

  function showNotice() {
    var notice = document.getElementById("pinterest-consent");
    if (notice) {
      notice.hidden = false;
    }
  }

  function hideNotice() {
    var notice = document.getElementById("pinterest-consent");
    if (notice) {
      notice.hidden = true;
    }
  }

  function initializePinterest() {
    if (pinterestStarted || !trackingEnabled) {
      return;
    }

    pinterestStarted = true;
    window.pintrk = window.pintrk || function () {
      window.pintrk.queue.push(Array.prototype.slice.call(arguments));
    };
    window.pintrk.queue = window.pintrk.queue || [];
    window.pintrk.version = "3.0";

    var script = document.createElement("script");
    script.async = true;
    script.src = PINTEREST_URL;
    script.addEventListener("error", function () {
      console.error("Pinterest tracking failed to load.");
    });
    var firstScript = document.getElementsByTagName("script")[0];
    firstScript.parentNode.insertBefore(script, firstScript);

    window.pintrk("load", PINTEREST_ID);
    window.pintrk("page");
    if (!pageVisitSent) {
      window.pintrk("track", "pagevisit", { event_id: "eventId0001" });
      pageVisitSent = true;
    }
  }

  function chooseConsent(value) {
    consent = value;
    trackingEnabled = value === ACCEPTED;
    saveConsent(value);
    hideNotice();
    if (trackingEnabled) {
      initializePinterest();
    }
  }

  function openSettings() {
    showNotice();
    var rejectButton = document.querySelector("[data-consent='rejected']");
    if (rejectButton) {
      rejectButton.focus();
    }
  }

  function setupConsent() {
    var notice = document.getElementById("pinterest-consent");
    var settings = document.querySelector(".privacy-settings");
    var choiceButtons = document.querySelectorAll("[data-consent]");

    if (!notice || !settings) {
      console.error("Pinterest consent controls could not be initialized.");
      return;
    }

    Array.prototype.forEach.call(choiceButtons, function (button) {
      button.addEventListener("click", function () {
        chooseConsent(button.getAttribute("data-consent"));
      });
    });
    settings.addEventListener("click", openSettings);

    consent = readConsent();
    if (consent === ACCEPTED) {
      trackingEnabled = true;
      initializePinterest();
    } else if (consent === REJECTED) {
      trackingEnabled = false;
      hideNotice();
    } else {
      showNotice();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupConsent);
  } else {
    setupConsent();
  }
}());
