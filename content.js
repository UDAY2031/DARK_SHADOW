chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'getCheckboxInfo') {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const checkboxInfo = Array.from(checkboxes).map(function (checkbox) {
      return checkbox.value;
    }).join(', ');

    sendResponse(checkboxInfo);
  }
});
