var notification = webkitNotifications.createNotification(
    'icon.png',
    "Hello!',
    'asdf'
);

notification.show()
function saveTabData(tab, data) {
  if (tab.incognito) {
    chrome.runtime.getBackgroundPage(function(bgPage) {
      bgPage[tab.url] = data;      // Persist data ONLY in memory
    });
  } else {
    localStorage[tab.url] = data;  // OK to store data
  }
}
