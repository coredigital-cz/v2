/* acoperisulsolid.ro — Acoperișul Solid */
(function () {
  'use strict';

  var TEL_DISP = '0756 419 558';

  /* ---------- meniu mobil (listă verticală) ---------- */
  var burger = document.querySelector('.burger');
  var mnav = document.querySelector('.mnav');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      var open = mnav.classList.toggle('on');
      burger.classList.toggle('on', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mnav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mnav.classList.remove('on');
        burger.classList.remove('on');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------- FAQ ---------- */
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.closest('.faq-i');
      var open = item.classList.toggle('on');
      q.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ---------- reveal ---------- */
  var rv = document.querySelectorAll('.rv');
  if (rv.length) {
    if (!('IntersectionObserver' in window) ||
        window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      rv.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
      rv.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---------- formulare → email (Web3Forms) ---------- */
  function val(form, name) {
    var el = form.querySelector('[name="' + name + '"]');
    return el ? el.value.trim() : '';
  }

  document.querySelectorAll('form[data-ef]').forEach(function (form) {
    var msg = form.querySelector('.f-msg');
    var btn = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();

      var nume = val(form, 'nume');
      var tel = val(form, 'telefon');
      var email = val(form, 'email');
      if (!nume || !tel || !email) {
        if (msg) {
          msg.textContent = 'Completați numele, telefonul și emailul, apoi trimiteți din nou.';
          msg.className = 'f-msg f-msg-err';
        }
        var bad = form.querySelector('[name="nume"]:invalid, [name="telefon"]:invalid, [name="email"]:invalid');
        (bad || form).focus();
        return;
      }

      if (msg) { msg.textContent = 'Se trimite…'; msg.className = 'f-msg'; }
      if (btn) { btn.disabled = true; }

      fetch(form.action, {
        method: 'POST',
        headers: { Accept: 'application/json' },
        body: new FormData(form)
      })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (data && data.success) {
            form.reset();
            if (msg) {
              msg.textContent = 'Mulțumim! V-am primit solicitarea și vă răspundem în cel mai scurt timp.';
              msg.className = 'f-msg f-msg-ok';
            }
          } else {
            if (msg) {
              msg.textContent = 'A apărut o problemă la trimitere. Încercați din nou sau sunați la ' + TEL_DISP + '.';
              msg.className = 'f-msg f-msg-err';
            }
          }
        })
        .catch(function () {
          if (msg) {
            msg.textContent = 'A apărut o problemă la trimitere. Încercați din nou sau sunați la ' + TEL_DISP + '.';
            msg.className = 'f-msg f-msg-err';
          }
        })
        .finally(function () {
          if (btn) { btn.disabled = false; }
        });
    });
  });

  /* ---------- an curent ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
