document.addEventListener('DOMContentLoaded', function () {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'getCheckboxInfo' }, function (response) {
      displayCheckboxInfo(response);
    });
  });

  function displayCheckboxInfo(checkboxInfo) {
    const checkboxInfoElement = document.getElementById('checkboxInfo');
    checkboxInfoElement.innerHTML = checkboxInfo || 'No checkbox information available.';
  }
});
