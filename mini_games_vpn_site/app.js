(function() {
  // Настоящая глубокая зацифровка всей технической логики (Hex-массив)
  var _0x2c4e = [
    '\x34\x35\x2E\x39\x31\x2E\x32\x32\x2E\x31\x30\x34', // [0] IP Эстония
    '\x31\x38\x35\x2E\x33\x38\x2E\x31\x34\x39\x2E\x31\x32', // [1] IP Германия
    '\x39\x31\x2E\x32\x33\x34\x2E\x38\x38\x2E\x37\x30', // [2] IP Польша (Исправлен!)
    '\x31\x34\x36\x2E\x37\x30\x2E\x31\x31\x38\x2E\x34\x33', // [3] IP Нидерланды
    '\x31\x37\x32\x2E\x31\x30\x35\x2E\x39\x31\x2E\x31\x38', // [4] IP США
    '\x23\x63\x6F\x6E\x6E\x65\x63\x74\x42\x75\x74\x74\x6F\x6E', // [5] Кнопка старт
    '\x23\x63\x68\x61\x6E\x67\x65\x49\x70\x42\x75\x74\x74\x6F\x6E', // [6] Кнопка смены IP
    '\x23\x73\x74\x61\x74\x75\x73\x52\x69\x6E\x67', // [7] Кольцо статуса
    '\x23\x73\x74\x61\x74\x75\x73\x54\x65\x78\x74', // [8] Текст статуса
    '\x23\x70\x72\x6F\x74\x65\x63\x74\x69\x6F\x6E\x54\x65\x78\x74', // [9] Текст защиты
    '\x23\x70\x72\x6F\x78\x79\x49\x70', // [10] Прокси IP элемент
    '\x23\x6C\x6F\x63\x61\x74\x69\x6F\x6E\x4E\x61\x6D\x65', // [11] Локация элемент
    '\x23\x70\x63\x53\x74\x61\x74\x65', // [12] Статус ПК
    '\x23\x62\x72\x6F\x77\x73\x65\x72\x53\x74\x61\x74\x65', // [13] Статус браузера
    '\x23\x77\x69\x66\x69\x53\x74\x61\x74\x65', // [14] Статус Wi-Fi
    '\x23\x62\x61\x63\x6B\x65\x6E\x64\x4D\x65\x73\x73\x61\x67\x65', // [15] Бекенд сообщение
    '\x68\x74\x74\x70\x3A', // [16] http:
    '\x68\x74\x74\x70\x73\x3A', // [17] https:
    '\x2E\x6E\x65\x74\x77\x6F\x72\x6B\x2D\x72\x6F\x77', // [18] Строка сети
    '\x77\x72\x6F\x74\x65\x63\x74\x65\x64', // [19] Класс "protected"
    '\x61\x63\x74\x69\x76\x65', // [20] Класс "active"
    '\x63\x6F\x6E\x6E\x65\x63\x74\x65\x64', // [21] Класс "connected"
    '\x62\x61\x63\x6B\x65\x6E\x64\x2D\x6D\x65\x73\x73\x61\x67\x65\x20', // [22] Префикс класса
    '\x2F\x61\x70\x69\x2F\x73\x74\x61\x74\x75\x73', // [23] API статус путь
    '\x2F\x61\x70\x69\x2F\x73\x74\x6F\x70', // [24] API стоп путь
    '\x2F\x61\x70\x69\x2F\x73\x74\x61\x72\x74', // [25] API старт путь
    '\x50\x4F\x53\x54', // [26] POST метод
    '\x63\x6C\x69\x63\x6B' // [27] Событие клика
  ];

  const exitNodes = [
    { ip: _0x2c4e[0], location: "Эстония, Таллин" },
    { ip: _0x2c4e[1], location: "Германия, Франкфурт" },
    { ip: _0x2c4e[2], location: "Польша, Варшава" },
    { ip: _0x2c4e[3], location: "Нидерланды, Амстердам" },
    { ip: _0x2c4e[4], location: "США, Нью-Йорк" }
  ];

  const state = { connected: false, currentNode: null };

  const connectButton = document.querySelector(_0x2c4e[5]);
  const changeIpButton = document.querySelector(_0x2c4e[6]);
  const statusRing = document.querySelector(_0x2c4e[7]);
  const statusText = document.querySelector(_0x2c4e[8]);
  const protectionText = document.querySelector(_0x2c4e[9]);
  const proxyIp = document.querySelector(_0x2c4e[10]);
  const locationName = document.querySelector(_0x2c4e[11]);
  const pcState = document.querySelector(_0x2c4e[12]);
  const browserState = document.querySelector(_0x2c4e[13]);
  const wifiState = document.querySelector(_0x2c4e[14]);
  const backendMessage = document.querySelector(_0x2c4e[15]);

  const backendEnabled = location.protocol === _0x2c4e[16] || location.protocol === _0x2c4e[17];

  function randomNode() {
    const availableNodes = exitNodes.filter((node) => node !== state.currentNode);
    return availableNodes[Math.floor(Math.random() * availableNodes.length)];
  }

  function setNetworkState(isConnected) {
    document.querySelectorAll(_0x2c4e[18]).forEach((row) => {
      row.classList.toggle(_0x2c4e[19], isConnected);
    });
    pcState.textContent = isConnected ? "Защищен" : "Ожидает";
    browserState.textContent = isConnected ? "Через прокси" : "Ожидает";
    wifiState.textContent = isConnected ? "Нужен системный VPN-клиент" : "Требуется приложение";
  }

  function render() {
    statusRing.classList.toggle(_0x2c4e[20], state.connected);
    connectButton.classList.toggle(_0x2c4e[21], state.connected);
    changeIpButton.disabled = !state.connected;

    if (state.connected && state.currentNode) {
      statusText.textContent = "VPN включен";
      protectionText.textContent = "Браузер защищен";
      proxyIp.textContent = state.currentNode.ip;
      locationName.textContent = state.currentNode.location;
      connectButton.textContent = "Отключить VPN";
      setNetworkState(true);
      return;
    }

    statusText.textContent = "VPN выключен";
    protectionText.textContent = "Сеть не защищена";
    proxyIp.textContent = "Не выбран";
    locationName.textContent = "Ожидание";
    connectButton.textContent = "Запустить VPN";
    setNetworkState(false);
  }

  function setBackendMessage(text, type = "") {
    backendMessage.textContent = text;
    backendMessage.className = (_0x2c4e[22] + type).trim();
  }

  async function api(path, options = {}) {
    const response = await fetch(path, {
      headers: { "Content-Type": "application/json" },
      ...options
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  }

  function applyBackendStatus(payload) {
    state.connected = Boolean(payload.running);
    if (state.connected && !state.currentNode) {
      state.currentNode = {
        ip: payload.server_host || "Подключен",
        location: `SOCKS5 ${payload.listen_host}:${payload.listen_port}`
      };
    }
    if (!state.connected) state.currentNode = null;

    const message = payload.error || payload.message;
    if (message) {
      setBackendMessage(message, payload.error ? "error" : payload.running ? "ok" : "");
    } else if (payload.configured) {
      setBackendMessage("Python-контроллер подключен", payload.running ? "ok" : "");
    } else {
      setBackendMessage("Заполни vpn_config.json, чтобы включить настоящий туннель", "error");
    }
    render();
  }

  async function refreshBackendStatus() {
    if (!backendEnabled) {
      setBackendMessage("Открыто как файл: работает только визуальный режим");
      return;
    }
    try {
      applyBackendStatus(await api(_0x2c4e[23]));
    } catch {
      setBackendMessage("Локальный Python-контроллер не подключен");
    }
  }

  connectButton.addEventListener(_0x2c4e[27], async () => {
    if (backendEnabled) {
      try {
        const endpoint = state.connected ? _0x2c4e[24] : _0x2c4e[25];
        applyBackendStatus(await api(endpoint, { method: _0x2c4e[26] }));
        return;
      } catch (error) {
        setBackendMessage(`Python API недоступен: ${error.message}`, "error");
      }
    }
    state.connected = !state.connected;
    state.currentNode = state.connected ? randomNode() : null;
    render();
  });

  changeIpButton.addEventListener(_0x2c4e[27], () => {
    state.currentNode = randomNode();
    render();
  });

  render();
  refreshBackendStatus();
})();
