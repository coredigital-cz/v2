/* acoperisulsolid.ro — Acoperișuri Perfecte */
(function () {
  'use strict';

  var WA = '40756419558';
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

  function wa(text) {
    return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text);
  }

  /* ---------- calculator ---------- */
  var state = null;
  var calc = document.getElementById('calc');
  if (calc) {
    state = { amprenta: 110, panta: 'medie', material: 'metalica', sarpanta: 'nu' };

    var PANTA = { mica: 1.16, medie: 1.32, mare: 1.50 };
    var MANOPERA = { metalica: [50, 80], ceramica: [75, 120], faltuita: [95, 150] };
    var MATERIAL = { metalica: [65, 110], ceramica: [120, 200], faltuita: [110, 175] };
    var SARPANTA = { da: [130, 210], nu: [0, 0] };
    var ET = {
      mica: 'mică', medie: 'medie', mare: 'mare',
      metalica: 'țiglă metalică', ceramica: 'țiglă ceramică', faltuita: 'tablă fălțuită',
      da: 'da, șarpantă nouă', nu: 'nu, șarpanta existentă'
    };

    function round50(n) { return Math.round(n / 50) * 50; }
    function fmt(n) { return n.toLocaleString('ro-RO'); }

    function render() {
      var mp = Math.round(state.amprenta * PANTA[state.panta]);
      var m = MANOPERA[state.material], mat = MATERIAL[state.material], sr = SARPANTA[state.sarpanta];

      var manLo = round50(mp * m[0]), manHi = round50(mp * m[1]);
      var matLo = round50(mp * mat[0]), matHi = round50(mp * mat[1]);
      var srLo = round50(mp * sr[0]), srHi = round50(mp * sr[1]);

      state.mp = mp;
      state.manopera = fmt(manLo) + ' – ' + fmt(manHi) + ' lei';
      state.materiale = fmt(matLo) + ' – ' + fmt(matHi) + ' lei';
      state.sarpantaCost = srHi ? fmt(srLo) + ' – ' + fmt(srHi) + ' lei' : 'nu e inclusă';
      state.total = fmt(manLo + matLo + srLo) + ' – ' + fmt(manHi + matHi + srHi) + ' lei';

      document.getElementById('c-mp').textContent = fmt(mp) + ' mp';
      document.getElementById('c-man').textContent = state.manopera;
      document.getElementById('c-mat').textContent = state.materiale;
      document.getElementById('c-sar').textContent = state.sarpantaCost;
      document.getElementById('c-tot').innerHTML =
        fmt(manLo + matLo + srLo) + ' <em>–</em> ' + fmt(manHi + matHi + srHi) + ' lei';

      var link = document.getElementById('c-wa');
      if (link) { link.href = wa(calcText()); }
    }

    function calcText() {
      return 'Bună ziua! Am folosit calculatorul de pe acoperisulsolid.ro.\n\n' +
        'Amprenta casei: ' + state.amprenta + ' mp\n' +
        'Panta: ' + ET[state.panta] + '\n' +
        'Învelitoare: ' + ET[state.material] + '\n' +
        'Șarpantă nouă: ' + ET[state.sarpanta] + '\n' +
        'Suprafață estimată: ' + state.mp + ' mp\n' +
        'Estimare totală: ' + state.total + '\n\n' +
        'Aș dori o ofertă exactă.';
    }

    var slider = document.getElementById('c-amprenta');
    if (slider) {
      slider.addEventListener('input', function () {
        state.amprenta = parseInt(slider.value, 10);
        document.getElementById('c-amprenta-v').textContent = state.amprenta + ' mp';
        render();
      });
    }
    calc.querySelectorAll('.seg').forEach(function (seg) {
      var key = seg.getAttribute('data-key');
      seg.querySelectorAll('button').forEach(function (b) {
        b.addEventListener('click', function () {
          seg.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
          b.classList.add('on');
          state[key] = b.getAttribute('data-v');
          render();
        });
      });
    });
    render();
    calc.calcText = calcText;
  }

  /* ---------- formulare → WhatsApp ---------- */
  function val(form, name) {
    var el = form.querySelector('[name="' + name + '"]');
    return el ? el.value.trim() : '';
  }

  document.querySelectorAll('form[data-wa]').forEach(function (form) {
    var msg = form.querySelector('.f-msg');

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();

      var nume = val(form, 'nume');
      var tel = val(form, 'telefon');
      if (!nume || !tel) {
        if (msg) {
          msg.textContent = 'Completați numele și numărul de telefon, apoi trimiteți din nou.';
          msg.className = 'f-msg f-msg-err';
        }
        (form.querySelector('[name="nume"]') || form).focus();
        return;
      }
      if (msg) { msg.textContent = ''; msg.className = 'f-msg'; }

      var linii;
      if (form.hasAttribute('data-calc') && state) {
        linii = [calc.calcText(), '', 'Nume: ' + nume, 'Telefon: ' + tel];
        var o1 = val(form, 'oras');
        if (o1) { linii.push('Localitate: ' + o1); }
      } else {
        linii = ['Bună ziua! Aș dori o ofertă pentru lucrări la acoperiș.', '',
                 'Nume: ' + nume, 'Telefon: ' + tel];
        var oras = val(form, 'oras');
        if (oras) { linii.push('Localitate: ' + oras); }
        var lucrare = val(form, 'lucrare');
        if (lucrare) { linii.push('Lucrare: ' + lucrare); }
        var supraf = val(form, 'suprafata');
        if (supraf) { linii.push('Suprafață aproximativă: ' + supraf + ' mp'); }
        var det = val(form, 'detalii');
        if (det) { linii.push('', 'Detalii: ' + det); }
      }

      window.open(wa(linii.join('\n')), '_blank', 'noopener');
    });
  });

  /* ---------- an curent ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
